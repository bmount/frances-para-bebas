/* Français pour bébas — service worker (offline for the trip) */
const VER = 'fpb-v12';
const SHELL = VER + '-shell';
const AUDIO = 'fpb-audio';   // audio is versioned via ?v= query, so keep across releases
const CORE = [
  './', 'index.html', 'app.html', 'manifest.json', 'icon.svg',
  'data/audio_manifest.json', 'data/spoken_grammar.json', 'data/spoken_essentials.json',
  'data/curriculum/lesson_00_sons.json',
  'data/curriculum/lesson_01_etre.json',
  'data/curriculum/lesson_02_avoir.json',
  'data/curriculum/lesson_03_salut.json',
  'data/curriculum/lesson_04_chiffres.json',
  'data/curriculum/lesson_05_cafe.json',
  'data/curriculum/lesson_06_couleurs.json',
  'data/curriculum/lesson_07_verbes_er.json',
  'data/curriculum/lesson_08_passe_compose.json',
  'data/curriculum/lesson_09_imparfait.json',
  'data/curriculum/lesson_10_metiers.json',
  'data/curriculum/lesson_11_ecole.json',
  'data/curriculum/lesson_12_dehors.json',
  'data/curriculum/lesson_13_survie.json',
  'data/curriculum/lesson_14_small_talk.json',
  'data/curriculum/lesson_15_vulgarite.json',
  'data/curriculum/lesson_16_verbes_ir_oir.json',
  'data/curriculum/lesson_17_histoire.json',
  'data/curriculum/lesson_18_mode.json',
  'data/curriculum/lesson_19_cuisine.json',
  'data/curriculum/lesson_20_mythes_religions.json',
  'data/curriculum/lesson_21_prepositions.json',
  'data/quiz_culture.json',
  'data/stories.json'
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
