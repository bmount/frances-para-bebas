/* Français pour bébas — service worker (offline for the trip) */
const VER = 'fpb-v4';
const SHELL = VER + '-shell';
const AUDIO = 'fpb-audio';   // audio is versioned via ?v= query, so keep across releases
const CORE = [
  './', 'index.html', 'app.html', 'manifest.json', 'icon.svg',
  'data/audio_manifest.json', 'data/spoken_grammar.json', 'data/spoken_essentials.json',
  'data/curriculum/lesson_00_sons.json',
  'data/curriculum/lesson_01_etre.json',
  'data/curriculum/lesson_02_avoir.json'
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(SHELL).then(c => c.addAll(CORE)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.filter(k => k !== SHELL && k !== AUDIO).map(k => caches.delete(k))
    )).then(() => self.clients.claim())
  );
});
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);

  // GCS audio: cache-first (big, immutable per ?v=)
  if (url.hostname === 'storage.googleapis.com') {
    e.respondWith(
      caches.open(AUDIO).then(c => c.match(req).then(hit =>
        hit || fetch(req).then(res => { if (res.ok) c.put(req, res.clone()); return res; })
      ))
    );
    return;
  }

  // same-origin app shell + data: stale-while-revalidate
  if (url.origin === location.origin) {
    e.respondWith(
      caches.open(SHELL).then(c => c.match(req).then(hit => {
        const net = fetch(req).then(res => { if (res.ok) c.put(req, res.clone()); return res; }).catch(() => hit);
        return hit || net;
      }))
    );
  }
});
