#!/usr/bin/env python3
"""Attach 'orientation' explainer boxes (ES default + EN) to lesson files.
Grammar/foundational boxes are authored here for precision; topical boxes are
loaded from scratchpad_readers/orient/topical_raw.json (already real HTML)."""
import json, os, glob

base = os.path.join(os.path.dirname(__file__), "..", "data", "curriculum")
G = {}  # id -> {title_es,title_en,es,en}

def add(lid, title_es, title_en, es, en):
    G[lid] = {"title_es": title_es, "title_en": title_en, "es": es.strip(), "en": en.strip()}

# ---------------------------------------------------------------- L00 sons
add("L00", "Cómo suena el francés", "How French sounds",
'''
<p>El francés <b>se escribe con muchas letras y se pronuncia con pocas</b>. La regla de oro: casi todas las <b>consonantes finales son mudas</b>. <span class="fx">Paris</span> suena «parí», <span class="fx">petit</span> suena «petí», y la <b>-e final</b> tampoco se pronuncia (<span class="fx">France</span> = «frans»). La <b>-s del plural</b> también es muda: lo oyes por el artículo, no por la palabra.</p>
<div class="opat">consonante final muda · <span class="fx">-e</span> final muda · nasales <span class="fx">on/an/in</span> por la nariz</div>
<p>Sonidos nuevos que tu español no tiene: las <b>vocales nasales</b> (<span class="fx">bon, blanc, vin</span>) salen por la nariz sin pronunciar la «n»; la <b>u francesa</b> (<span class="fx">tu, rue</span>) se dice poniendo boca de «u» pero diciendo «i»; y la <b>r</b> es gutural, del fondo de la garganta, no la «rr» española.</p>
<p>Buenas noticias: <span class="fx">ch</span> = «sh», <span class="fx">gn</span> = «ñ» (¡como en español!), <span class="fx">qu</span> = «k», y la <b>h siempre es muda</b>. Y la <b>liaison</b>: una consonante final muda «despierta» cuando la siguiente palabra empieza por vocal — <span class="fx">les amis</span> se dice «lez-amí». Por eso el francés suena todo pegado.</p>
''',
'''
<p>French is <b>written with lots of letters and pronounced with few</b>. The golden rule: almost all <b>final consonants are silent</b>. <span class="fx">Paris</span> sounds like «paree», <span class="fx">petit</span> like «ptee», and the <b>final -e</b> is silent too (<span class="fx">France</span> = «frahns»). The <b>plural -s</b> is also silent — you hear the plural from the article, not the word.</p>
<div class="opat">silent final consonant · silent final <span class="fx">-e</span> · nasal <span class="fx">on/an/in</span> through the nose</div>
<p>Sounds Spanish doesn't have: <b>nasal vowels</b> (<span class="fx">bon, blanc, vin</span>) come out through the nose with no real «n»; the <b>French u</b> (<span class="fx">tu, rue</span>) is made with «oo» lips while saying «ee»; and the <b>r</b> is guttural, from the back of the throat, not the Spanish rolled «rr».</p>
<p>Good news: <span class="fx">ch</span> = «sh», <span class="fx">gn</span> = «ny» (just like Spanish ñ!), <span class="fx">qu</span> = «k», and <b>h is always silent</b>. And <b>liaison</b>: a silent final consonant «wakes up» when the next word starts with a vowel — <span class="fx">les amis</span> becomes «lez-amee». That's why French sounds all linked together.</p>
''')

# ---------------------------------------------------------------- L01 être
add("L01", "Être: un solo verbo para ser Y estar", "Être: one verb for both ser AND estar",
'''
<p><span class="fx">être</span> significa <b>ser</b> y <b>estar</b> a la vez: el francés <b>no separa</b> los dos como el español. <span class="fx">Je suis américaine</span> (soy americana) y <span class="fx">je suis fatiguée</span> (estoy cansada) usan el mismo verbo. Una preocupación menos.</p>
<p>Es <b>irregular</b> — como <b>ser</b> en español — así que se memoriza. En presente:</p>
<table class="oform">
<tr><td class="k">je suis</td><td>yo soy / estoy</td></tr>
<tr><td class="k">tu es</td><td>tú eres / estás</td></tr>
<tr><td class="k">il / elle / on est</td><td>él/ella es · «on» = se/nosotros</td></tr>
<tr><td class="k">vous êtes</td><td>usted es / ustedes son</td></tr>
<tr><td class="k">ils / elles sont</td><td>ellos/ellas son</td></tr>
</table>
<div class="opat"><span class="fx">être</span> = ser + estar · <span class="fx">c'est</span> = es / esto es</div>
<p>Ojo: <span class="fx">nous sommes</span> existe, pero al hablar se dice <span class="fx">on est</span>. Y <span class="fx">c'est</span> (es/esto es) es la frase más útil del idioma: <span class="fx">c'est beau, c'est bon, c'est ça</span>.</p>
''',
'''
<p><span class="fx">être</span> means both <b>ser</b> and <b>estar</b> at once: French <b>doesn't split</b> them the way Spanish does. <span class="fx">Je suis américaine</span> (I'm American) and <span class="fx">je suis fatiguée</span> (I'm tired) use the very same verb. One less thing to worry about.</p>
<p>It's <b>irregular</b> — like Spanish <b>ser</b> — so you memorize it. In the present:</p>
<table class="oform">
<tr><td class="k">je suis</td><td>I am</td></tr>
<tr><td class="k">tu es</td><td>you are (informal)</td></tr>
<tr><td class="k">il / elle / on est</td><td>he/she is · «on» = we/one</td></tr>
<tr><td class="k">vous êtes</td><td>you are (formal/plural)</td></tr>
<tr><td class="k">ils / elles sont</td><td>they are</td></tr>
</table>
<div class="opat"><span class="fx">être</span> = ser + estar · <span class="fx">c'est</span> = it is / this is</div>
<p>Note: <span class="fx">nous sommes</span> exists, but in speech people say <span class="fx">on est</span>. And <span class="fx">c'est</span> (it is / this is) is the single most useful phrase in the language: <span class="fx">c'est beau, c'est bon, c'est ça</span>.</p>
''')

# ---------------------------------------------------------------- L02 avoir
add("L02", "Avoir: « tener » y « haber » en un solo verbo", "Avoir: both « to have » and the past-tense « haber »",
'''
<p><span class="fx">avoir</span> hace <b>dos trabajos</b>, igual que en español. Primero, <b>posesión</b> como <b>tener</b>: <span class="fx">j'ai un sac</span> (tengo una bolsa). Segundo, es el <b>auxiliar</b> para construir el pasado, como <b>haber</b>: <span class="fx">j'ai mangé</span> = he comido. Si ya dices «he comido», ya entiendes el mecanismo francés.</p>
<table class="oform">
<tr><td class="k">j'ai</td><td>(yo) tengo / he</td></tr>
<tr><td class="k">tu as</td><td>tienes / has</td></tr>
<tr><td class="k">il / elle / on a</td><td>tiene / ha</td></tr>
<tr><td class="k">vous avez</td><td>tiene(n) / ha(n)</td></tr>
<tr><td class="k">ils / elles ont</td><td>tienen / han</td></tr>
</table>
<div class="opat"><span class="fx">j'ai quinze ans</span> = tengo quince años · <span class="fx">il y a</span> = hay</div>
<p>Y como en español, muchas expresiones usan <b>tener/avoir</b> donde el inglés usa «to be»: <span class="fx">avoir faim</span> (tener hambre), <span class="fx">avoir soif</span>, <span class="fx">avoir chaud / froid</span>, y sobre todo la <b>edad</b>: <span class="fx">j'ai quinze ans</span> = tengo quince años (nunca «soy quince»). De <span class="fx">avoir</span> también sale <span class="fx">il y a</span> = <b>hay</b>.</p>
''',
'''
<p><span class="fx">avoir</span> does <b>two jobs</b>, exactly like Spanish. First, <b>possession</b>, like <b>tener</b>: <span class="fx">j'ai un sac</span> (I have a bag). Second, it's the <b>auxiliary</b> that builds the past, like <b>haber</b>: <span class="fx">j'ai mangé</span> = I have eaten / I ate. If you already say «he comido» in Spanish, you already get the French machinery.</p>
<table class="oform">
<tr><td class="k">j'ai</td><td>I have</td></tr>
<tr><td class="k">tu as</td><td>you have</td></tr>
<tr><td class="k">il / elle / on a</td><td>he/she has</td></tr>
<tr><td class="k">vous avez</td><td>you have (formal/pl.)</td></tr>
<tr><td class="k">ils / elles ont</td><td>they have</td></tr>
</table>
<div class="opat"><span class="fx">j'ai quinze ans</span> = I'm fifteen · <span class="fx">il y a</span> = there is/are</div>
<p>And like Spanish, many expressions use <b>tener/avoir</b> where English uses «to be»: <span class="fx">avoir faim</span> (to be hungry — lit. «have hunger»), <span class="fx">avoir soif</span>, <span class="fx">avoir chaud / froid</span>, and above all <b>age</b>: <span class="fx">j'ai quinze ans</span> = I'm fifteen (literally «I have fifteen years», just like «tengo quince años»). From <span class="fx">avoir</span> also comes <span class="fx">il y a</span> = <b>there is / there are</b>.</p>
''')

# ---------------------------------------------------------------- L06 couleurs
add("L06", "Los adjetivos: concuerdan y van DETRÁS", "Adjectives: they agree and go AFTER the noun",
'''
<p>Aquí tu español es una <b>ventaja enorme</b>. Como en español, los adjetivos de color <b>concuerdan</b> en género y número con el nombre, y van <b>después</b> del nombre: <span class="fx">un sac vert</span> (una bolsa verde), <span class="fx">une valise verte</span>, <span class="fx">des sacs verts</span>. El inglés los pone antes («a green bag»); tú, piensa en español.</p>
<table class="oform">
<tr><td class="k">masculino</td><td><span class="fx">un pull bleu</span> — un suéter azul</td></tr>
<tr><td class="k">femenino (+e)</td><td><span class="fx">une robe bleue</span> — un vestido azul</td></tr>
<tr><td class="k">plural (+s)</td><td><span class="fx">des yeux bleus</span> — ojos azules</td></tr>
</table>
<div class="opat">un sac <span class="fx">vert</span> · une valise <span class="fx">verte</span> (concuerda + va detrás)</div>
<p>El <b>femenino</b> normalmente añade <b>-e</b> (<span class="fx">vert → verte</span>), y el plural una <b>-s</b> — muda al oído, igual que en español la ves más que la oyes. Algunos colores son <b>invariables</b>: <span class="fx">orange</span> y <span class="fx">marron</span> no cambian. Y ojo: unos pocos adjetivos cortos y muy comunes (<span class="fx">grand, petit, beau, joli</span>) sí van <b>antes</b> del nombre — pero los colores, siempre detrás.</p>
''',
'''
<p>Here your Spanish is a <b>huge advantage</b>. Just like Spanish, color adjectives <b>agree</b> in gender and number with the noun, and they go <b>after</b> it: <span class="fx">un sac vert</span> (a green bag), <span class="fx">une valise verte</span>, <span class="fx">des sacs verts</span>. English puts them before («a green bag»); you, think in Spanish.</p>
<table class="oform">
<tr><td class="k">masculine</td><td><span class="fx">un pull bleu</span> — a blue sweater</td></tr>
<tr><td class="k">feminine (+e)</td><td><span class="fx">une robe bleue</span> — a blue dress</td></tr>
<tr><td class="k">plural (+s)</td><td><span class="fx">des yeux bleus</span> — blue eyes</td></tr>
</table>
<div class="opat">un sac <span class="fx">vert</span> · une valise <span class="fx">verte</span> (agrees + comes after)</div>
<p>The <b>feminine</b> usually adds <b>-e</b> (<span class="fx">vert → verte</span>), and the plural adds an <b>-s</b> — silent to the ear, just like in Spanish where you see it more than you hear it. Some colors are <b>invariable</b>: <span class="fx">orange</span> and <span class="fx">marron</span> never change. And note: a few short, very common adjectives (<span class="fx">grand, petit, beau, joli</span>) do go <b>before</b> the noun — but colors always come after.</p>
''')

# ---------------------------------------------------------------- L07 verbes -er
add("L07", "Verbes en -er: el motor regular (y silencioso)", "-er verbs: the regular (and silent) engine",
'''
<p>Es la clase de verbos <b>más grande y más fácil</b>, y casi todos los <b>-ar</b> del español son <b>-er</b> en francés: <span class="fx">parler</span> (hablar), <span class="fx">chanter</span> (cantar), <span class="fx">manger</span> (comer→ aquí «comer»). Para conjugar en presente: quita <b>-er</b> y añade las terminaciones.</p>
<table class="oform">
<tr><td class="k">je parl<b>e</b></td><td>tu parl<b>es</b></td></tr>
<tr><td class="k">il/elle parl<b>e</b></td><td>ils parl<b>ent</b></td></tr>
<tr><td class="k">nous parl<b>ons</b></td><td>vous parl<b>ez</b></td></tr>
</table>
<div class="opat"><span class="fx">je parle · tu parles · il parle · ils parlent</span> → todas suenan «parl»</div>
<p><b>El secreto que lo cambia todo:</b> las terminaciones <span class="fx">-e, -es, -e, -ent</span> son <b>mudas</b>. Así que <span class="fx">je parle</span>, <span class="fx">tu parles</span>, <span class="fx">il parle</span> y <span class="fx">ils parlent</span> suenan <b>idénticas</b> («parl»). Solo <span class="fx">nous</span> y <span class="fx">vous</span> se oyen distintas. Al hablar solo necesitas la raíz + el pronombre — mucho más fácil de lo que parece escrito.</p>
''',
'''
<p>This is the <b>biggest and easiest</b> verb class, and almost every Spanish <b>-ar</b> verb is an <b>-er</b> verb in French: <span class="fx">parler</span> (hablar/to speak), <span class="fx">chanter</span> (to sing), <span class="fx">manger</span> (to eat). To conjugate the present: drop <b>-er</b> and add the endings.</p>
<table class="oform">
<tr><td class="k">je parl<b>e</b></td><td>tu parl<b>es</b></td></tr>
<tr><td class="k">il/elle parl<b>e</b></td><td>ils parl<b>ent</b></td></tr>
<tr><td class="k">nous parl<b>ons</b></td><td>vous parl<b>ez</b></td></tr>
</table>
<div class="opat"><span class="fx">je parle · tu parles · il parle · ils parlent</span> → all sound like «parl»</div>
<p><b>The secret that changes everything:</b> the endings <span class="fx">-e, -es, -e, -ent</span> are <b>silent</b>. So <span class="fx">je parle</span>, <span class="fx">tu parles</span>, <span class="fx">il parle</span>, and <span class="fx">ils parlent</span> sound <b>identical</b> («parl»). Only <span class="fx">nous</span> and <span class="fx">vous</span> sound different. When speaking, you really only need the stem + the pronoun — far easier than it looks on paper.</p>
''')

# ---------------------------------------------------------------- L08 passé composé
add("L08", "El passé composé: cómo se arma el pasado", "The passé composé: how to build the past",
'''
<p>Es el pasado de todos los días, y se arma como tu <b>«he comido»</b>: un <b>auxiliar en presente</b> + el <b>participio</b>. La fórmula:</p>
<div class="opat"><span class="fx">avoir</span> (o <span class="fx">être</span>) en presente + <b>participio pasado</b><br><span class="fx">j'ai mangé</span> = he comido / comí</div>
<p>El participio se forma así: verbos <span class="fx">-er</span> → <b>-é</b> (<span class="fx">parlé</span>), verbos <span class="fx">-ir</span> → <b>-i</b> (<span class="fx">fini</span>), y varios irregulares que se memorizan (<span class="fx">fait, pris, vu, eu</span>). La mayoría usan <span class="fx">avoir</span>: <span class="fx">j'ai vu, tu as pris</span>.</p>
<p><b>Un grupo especial usa <span class="fx">être</span></b> (verbos de movimiento/cambio: aller, venir, partir, rester… y los reflexivos). Y aquí va la diferencia con el español: con <span class="fx">être</span>, el <b>participio concuerda</b> con el sujeto, como un adjetivo. Tú, chica, dices <span class="fx">je suis allée</span> (con -e), <span class="fx">je suis partie</span>. Ojo: el francés usa este tiempo también donde el español usa el pretérito simple («comí»), no solo «he comido».</p>
''',
'''
<p>This is the everyday past, and it's built just like Spanish <b>«he comido»</b>: an <b>auxiliary in the present</b> + the <b>past participle</b>. The formula:</p>
<div class="opat"><span class="fx">avoir</span> (or <span class="fx">être</span>) in the present + <b>past participle</b><br><span class="fx">j'ai mangé</span> = I have eaten / I ate</div>
<p>Form the participle like this: <span class="fx">-er</span> verbs → <b>-é</b> (<span class="fx">parlé</span>), <span class="fx">-ir</span> verbs → <b>-i</b> (<span class="fx">fini</span>), plus several irregulars to memorize (<span class="fx">fait, pris, vu, eu</span>). Most verbs use <span class="fx">avoir</span>: <span class="fx">j'ai vu, tu as pris</span>.</p>
<p><b>A special group uses <span class="fx">être</span></b> (verbs of motion/change: aller, venir, partir, rester… and all reflexives). Here's the twist vs. Spanish: with <span class="fx">être</span>, the <b>participle agrees</b> with the subject, like an adjective. As a girl you say <span class="fx">je suis allée</span> (with -e), <span class="fx">je suis partie</span>. Note: French also uses this tense where Spanish uses the simple preterite («I ate»), not only «I have eaten».</p>
''')

# ---------------------------------------------------------------- L09 imparfait
add("L09", "El imparfait: el « imperfecto » gemelo", "The imparfait: the twin of the Spanish imperfect",
'''
<p>Buenísima noticia: el <span class="fx">imparfait</span> es <b>casi idéntico</b> a tu <b>imperfecto</b> (hablaba, comía). Mismo uso: el <b>fondo</b> de la escena, las <b>costumbres</b>, el clima, cómo <b>eran</b> las cosas. Y se forma con una receta fija y sin excepciones.</p>
<div class="opat">forma <span class="fx">nous</span> del presente − <span class="fx">-ons</span> + <span class="fx">-ais, -ais, -ait, -ions, -iez, -aient</span></div>
<p>Ejemplo: <span class="fx">parler</span> → <span class="fx">nous parlons</span> → raíz <span class="fx">parl-</span> → <span class="fx">je parlais</span> (yo hablaba). Otro: <span class="fx">faire</span> → <span class="fx">nous faisons</span> → <span class="fx">je faisais</span>.</p>
<table class="oform">
<tr><td class="k">je parlais</td><td>yo hablaba</td></tr>
<tr><td class="k">tu parlais</td><td>tú hablabas</td></tr>
<tr><td class="k">il/elle/on parlait</td><td>hablaba</td></tr>
<tr><td class="k">ils parlaient</td><td>hablaban</td></tr>
</table>
<p>Al oído, <span class="fx">-ais, -ait, -aient</span> suenan <b>igual</b> («-è»). Y la gran pareja: <b>imparfait</b> (fondo, «era/estaba») vs <b>passé composé</b> (acción puntual, «pasó») — exactamente la misma división que imperfecto vs pretérito en español.</p>
''',
'''
<p>Great news: the <span class="fx">imparfait</span> is <b>almost identical</b> to your Spanish <b>imperfecto</b> (hablaba, comía). Same job: the <b>background</b> of a scene, <b>habits</b>, weather, how things <b>used to be</b>. And it's built with a fixed recipe — no exceptions.</p>
<div class="opat">present <span class="fx">nous</span> form − <span class="fx">-ons</span> + <span class="fx">-ais, -ais, -ait, -ions, -iez, -aient</span></div>
<p>Example: <span class="fx">parler</span> → <span class="fx">nous parlons</span> → stem <span class="fx">parl-</span> → <span class="fx">je parlais</span> (I was speaking / used to speak). Another: <span class="fx">faire</span> → <span class="fx">nous faisons</span> → <span class="fx">je faisais</span>.</p>
<table class="oform">
<tr><td class="k">je parlais</td><td>I was speaking / used to speak</td></tr>
<tr><td class="k">tu parlais</td><td>you were speaking</td></tr>
<tr><td class="k">il/elle/on parlait</td><td>he/she was speaking</td></tr>
<tr><td class="k">ils parlaient</td><td>they were speaking</td></tr>
</table>
<p>To the ear, <span class="fx">-ais, -ait, -aient</span> all sound the <b>same</b> («-eh»). And the big pairing: <b>imparfait</b> (background, «was/used to») vs <b>passé composé</b> (one finished action, «happened») — exactly the same split as imperfecto vs preterite in Spanish.</p>
''')

# ---------------------------------------------------------------- L16 verbes -ir / -oir
add("L16", "Verbes en -ir / -oir: finir, y los tres imprescindibles", "-ir / -oir verbs: finir, plus the three essentials",
'''
<p>Después de los <span class="fx">-er</span>, estas son las otras familias. Los <span class="fx">-ir</span> tipo <span class="fx">finir</span> (terminar) meten un <b>-iss-</b> en el plural: <span class="fx">je finis, tu finis, il finit, nous finissons, vous finissez, ils finissent</span>.</p>
<p>Pero lo <b>más rentable</b> son tres verbos <span class="fx">-oir</span> irregulares y utilísimos, que además calcan el español:</p>
<table class="oform">
<tr><td class="k">pouvoir</td><td><span class="fx">je peux</span> = puedo</td></tr>
<tr><td class="k">vouloir</td><td><span class="fx">je veux</span> = quiero</td></tr>
<tr><td class="k">devoir</td><td><span class="fx">je dois</span> = debo</td></tr>
</table>
<div class="opat"><span class="fx">je peux</span> = puedo · <span class="fx">je veux</span> = quiero · <span class="fx">je dois</span> = debo</div>
<p>Se usan como en español: verbo conjugado + <b>infinitivo</b>. <span class="fx">Je peux entrer ?</span> (¿puedo entrar?), <span class="fx">je dois partir</span> (debo irme). Y la joya de la cortesía: <span class="fx">je voudrais</span> (quisiera), la forma amable de <span class="fx">vouloir</span> — apréndela como bloque para pedir todo.</p>
''',
'''
<p>After the <span class="fx">-er</span> verbs, these are the other families. <span class="fx">-ir</span> verbs of the <span class="fx">finir</span> (to finish) type slip an <b>-iss-</b> into the plural: <span class="fx">je finis, tu finis, il finit, nous finissons, vous finissez, ils finissent</span>.</p>
<p>But the <b>biggest payoff</b> is three irregular, super-useful <span class="fx">-oir</span> verbs that mirror Spanish:</p>
<table class="oform">
<tr><td class="k">pouvoir</td><td><span class="fx">je peux</span> = I can</td></tr>
<tr><td class="k">vouloir</td><td><span class="fx">je veux</span> = I want</td></tr>
<tr><td class="k">devoir</td><td><span class="fx">je dois</span> = I must</td></tr>
</table>
<div class="opat"><span class="fx">je peux</span> = puedo · <span class="fx">je veux</span> = quiero · <span class="fx">je dois</span> = debo</div>
<p>Use them like Spanish: conjugated verb + <b>infinitive</b>. <span class="fx">Je peux entrer ?</span> (can I come in?), <span class="fx">je dois partir</span> (I have to go). And the politeness gem: <span class="fx">je voudrais</span> (I'd like), the polite form of <span class="fx">vouloir</span> — learn it as a chunk for ordering anything.</p>
''')

# ---------------------------------------------------------------- L21 prépositions y/en
add("L21", "Preposiciones + los pronombres y / en", "Prepositions + the pronouns y / en",
'''
<p>Cuatro preposiciones cargan casi todo: <span class="fx">à</span> (a/en), <span class="fx">de</span> (de/desde), <span class="fx">pour</span> (para) y <span class="fx">par</span> (por). El francés las <b>contrae</b> con el artículo, y esto hay que automatizarlo:</p>
<div class="opat">à + le → <span class="fx">au</span> · à + les → <span class="fx">aux</span> · de + le → <span class="fx">du</span> · de + les → <span class="fx">des</span></div>
<p><b>pour vs par</b> (tu «para» vs «por»): <span class="fx">pour</span> = meta o destino (<span class="fx">pour toi</span>, <span class="fx">pour aller à Nice</span>); <span class="fx">par</span> = a través de o frecuencia (<span class="fx">par ici</span>, <span class="fx">deux fois par jour</span>).</p>
<p>Y dos pronombres que el español resuelve con «ahí» o «de eso»: <span class="fx">y</span> reemplaza <b>à + lugar/cosa</b> — <span class="fx">j'y vais</span> (voy ahí/allá), <span class="fx">on y va !</span> (¡vámonos!). <span class="fx">en</span> reemplaza <b>de + cosa</b> o una cantidad — <span class="fx">j'en veux</span> (quiero de eso), <span class="fx">j'en ai deux</span> (tengo dos). Van <b>antes del verbo</b>, como todos los pronombres.</p>
''',
'''
<p>Four prepositions carry almost everything: <span class="fx">à</span> (to/at), <span class="fx">de</span> (of/from), <span class="fx">pour</span> (for) and <span class="fx">par</span> (by/through). French <b>contracts</b> them with the article, and this needs to become automatic:</p>
<div class="opat">à + le → <span class="fx">au</span> · à + les → <span class="fx">aux</span> · de + le → <span class="fx">du</span> · de + les → <span class="fx">des</span></div>
<p><b>pour vs par</b> (Spanish «para» vs «por»): <span class="fx">pour</span> = goal or destination (<span class="fx">pour toi</span>, <span class="fx">pour aller à Nice</span>); <span class="fx">par</span> = through or frequency (<span class="fx">par ici</span> = this way, <span class="fx">deux fois par jour</span> = twice a day).</p>
<p>And two pronouns Spanish handles with «ahí» or «de eso»: <span class="fx">y</span> replaces <b>à + place/thing</b> — <span class="fx">j'y vais</span> (I'm going there), <span class="fx">on y va !</span> (let's go!). <span class="fx">en</span> replaces <b>de + thing</b> or a quantity — <span class="fx">j'en veux</span> (I want some), <span class="fx">j'en ai deux</span> (I have two). Both go <b>before the verb</b>, like all pronouns.</p>
''')

# ---------------------------------------------------------------- L27 questions
add("L27", "Preguntar: tres maneras, de la calle al libro", "Asking questions: three ways, from street to book",
'''
<p>El francés tiene <b>tres formas</b> de preguntar. Apréndelas de la más hablada a la más formal:</p>
<table class="oform">
<tr><td class="k">1 · entonación</td><td><span class="fx">Tu viens ?</span> — dices la frase y subes la voz (lo más común al hablar)</td></tr>
<tr><td class="k">2 · est-ce que</td><td><span class="fx">Est-ce que tu viens ?</span> — pones <span class="fx">est-ce que</span> delante (neutro, seguro)</td></tr>
<tr><td class="k">3 · inversión</td><td><span class="fx">Viens-tu ?</span> — verbo antes del sujeto (formal/escrito)</td></tr>
</table>
<div class="opat"><span class="fx">Tu viens ?</span> · <span class="fx">Est-ce que tu viens ?</span> · <span class="fx">Viens-tu ?</span></div>
<p>Con palabra interrogativa (<span class="fx">qui, où, quand, comment, pourquoi, combien, quel</span>), al hablar los franceses la ponen muchas veces <b>al final</b>: <span class="fx">Tu t'appelles comment ?</span> (¿cómo te llamas?), <span class="fx">Tu viens quand ?</span>, <span class="fx">Ça coûte combien ?</span>. Suena rarísimo para tu oído español, pero es lo natural. Y no confundas <span class="fx">pourquoi</span> (¿por qué?, pregunta) con <span class="fx">parce que</span> (porque, respuesta).</p>
''',
'''
<p>French has <b>three ways</b> to ask a question. Learn them from most spoken to most formal:</p>
<table class="oform">
<tr><td class="k">1 · intonation</td><td><span class="fx">Tu viens ?</span> — say the statement and raise your voice (most common in speech)</td></tr>
<tr><td class="k">2 · est-ce que</td><td><span class="fx">Est-ce que tu viens ?</span> — stick <span class="fx">est-ce que</span> on the front (neutral, safe)</td></tr>
<tr><td class="k">3 · inversion</td><td><span class="fx">Viens-tu ?</span> — verb before subject (formal/written)</td></tr>
</table>
<div class="opat"><span class="fx">Tu viens ?</span> · <span class="fx">Est-ce que tu viens ?</span> · <span class="fx">Viens-tu ?</span></div>
<p>With a question word (<span class="fx">qui, où, quand, comment, pourquoi, combien, quel</span>), spoken French often puts it <b>at the end</b>: <span class="fx">Tu t'appelles comment ?</span> (what's your name?), <span class="fx">Tu viens quand ?</span>, <span class="fx">Ça coûte combien ?</span>. It sounds wild to a Spanish ear, but it's the natural version. And don't mix up <span class="fx">pourquoi</span> (why?, the question) with <span class="fx">parce que</span> (because, the answer).</p>
''')

# ---------------------------------------------------------------- L28 négation
add("L28", "La negación: el « no » francés viene en dos piezas", "Negation: the French « no » comes in two pieces",
'''
<p>Donde el español pone un solo <b>«no»</b>, el francés <b>abraza el verbo con dos piezas</b>: <span class="fx">ne</span> + verbo + <span class="fx">pas</span>. <span class="fx">Je ne comprends pas</span> = no entiendo. El verbo queda en el sándwich.</p>
<div class="opat"><span class="fx">ne</span> + [verbo] + <span class="fx">pas</span> → <span class="fx">je ne sais pas</span> (no sé)</div>
<p>Cambiando la segunda pieza obtienes otras negaciones — y estas <b>ya son negativas</b>, así que no les añadas <span class="fx">pas</span>:</p>
<table class="oform">
<tr><td class="k">ne … jamais</td><td>nunca</td></tr>
<tr><td class="k">ne … rien</td><td>nada</td></tr>
<tr><td class="k">ne … plus</td><td>ya no</td></tr>
<tr><td class="k">ne … personne</td><td>nadie</td></tr>
</table>
<p><b>La verdad de la calle:</b> al hablar, el <span class="fx">ne</span> <b>casi siempre se cae</b>. Vas a oír <span class="fx">je sais pas</span>, <span class="fx">c'est pas grave</span>, <span class="fx">j'ai rien fait</span>. En pasado, el sándwich envuelve el auxiliar: <span class="fx">je n'ai pas mangé</span> (no he comido).</p>
''',
'''
<p>Where Spanish uses a single <b>«no»</b>, French <b>wraps the verb in two pieces</b>: <span class="fx">ne</span> + verb + <span class="fx">pas</span>. <span class="fx">Je ne comprends pas</span> = I don't understand. The verb sits in the sandwich.</p>
<div class="opat"><span class="fx">ne</span> + [verb] + <span class="fx">pas</span> → <span class="fx">je ne sais pas</span> (I don't know)</div>
<p>Swap the second piece for other negatives — and these <b>are already negative</b>, so never add <span class="fx">pas</span> to them:</p>
<table class="oform">
<tr><td class="k">ne … jamais</td><td>never</td></tr>
<tr><td class="k">ne … rien</td><td>nothing</td></tr>
<tr><td class="k">ne … plus</td><td>no more / no longer</td></tr>
<tr><td class="k">ne … personne</td><td>nobody</td></tr>
</table>
<p><b>The street truth:</b> in speech the <span class="fx">ne</span> <b>almost always drops</b>. You'll hear <span class="fx">je sais pas</span>, <span class="fx">c'est pas grave</span>, <span class="fx">j'ai rien fait</span>. In the past, the sandwich wraps the auxiliary: <span class="fx">je n'ai pas mangé</span> (I didn't eat).</p>
''')

# ---------------------------------------------------------------- L29 reflexives
add("L29", "Verbos reflexivos: idénticos al español (me, te, se)", "Reflexive verbs: identical to Spanish (me, te, se)",
'''
<p>Regalo puro: los reflexivos franceses funcionan <b>igual que en español</b>. Llevan un pronombre (<span class="fx">me, te, se…</span>) que va <b>antes del verbo</b> y concuerda con el sujeto. <span class="fx">Je me lève</span> = me levanto. Punto por punto:</p>
<table class="oform">
<tr><td class="k">je me lève</td><td>me levanto</td></tr>
<tr><td class="k">tu te lèves</td><td>te levantas</td></tr>
<tr><td class="k">il/elle/on se lève</td><td>se levanta</td></tr>
<tr><td class="k">vous vous levez</td><td>se levanta(n)</td></tr>
<tr><td class="k">ils/elles se lèvent</td><td>se levantan</td></tr>
</table>
<div class="opat"><span class="fx">je me lève</span> = me levanto · el pronombre va <b>antes</b> del verbo</div>
<p>Dos detalles: en <b>pasado</b>, los reflexivos usan <span class="fx">être</span> y el participio concuerda — tú dices <span class="fx">je me suis levée</span> (con -e). En <b>imperativo</b> afirmativo el pronombre salta detrás con guion: <span class="fx">lève-toi !</span> (¡levántate!), <span class="fx">dépêche-toi !</span> (¡date prisa!) — igual que el español pega el pronombre.</p>
''',
'''
<p>Pure gift: French reflexives work <b>just like Spanish</b>. They carry a pronoun (<span class="fx">me, te, se…</span>) that goes <b>before the verb</b> and agrees with the subject. <span class="fx">Je me lève</span> = I get up. Point for point:</p>
<table class="oform">
<tr><td class="k">je me lève</td><td>I get up</td></tr>
<tr><td class="k">tu te lèves</td><td>you get up</td></tr>
<tr><td class="k">il/elle/on se lève</td><td>he/she gets up</td></tr>
<tr><td class="k">vous vous levez</td><td>you get up (formal/pl.)</td></tr>
<tr><td class="k">ils/elles se lèvent</td><td>they get up</td></tr>
</table>
<div class="opat"><span class="fx">je me lève</span> = me levanto · pronoun goes <b>before</b> the verb</div>
<p>Two details: in the <b>past</b>, reflexives use <span class="fx">être</span> and the participle agrees — you say <span class="fx">je me suis levée</span> (with -e). In the affirmative <b>imperative</b> the pronoun jumps behind with a hyphen: <span class="fx">lève-toi !</span> (get up!), <span class="fx">dépêche-toi !</span> (hurry up!) — exactly like Spanish attaching the pronoun.</p>
''')

# ---------------------------------------------------------------- L30 object pronouns
add("L30", "Pronombres de objeto: antes del verbo, como en español", "Object pronouns: before the verb, like Spanish",
'''
<p>Reemplazan al nombre para no repetirlo, y — como en español — van <b>antes del verbo</b> (no después, como en inglés «I see him»). Hay dos series:</p>
<table class="oform">
<tr><td class="k">directo</td><td>me, te, <b>le / la</b>, nous, vous, <b>les</b> — <span class="fx">je le vois</span> = lo veo</td></tr>
<tr><td class="k">indirecto</td><td>me, te, <b>lui</b>, nous, vous, <b>leur</b> — <span class="fx">je lui parle</span> = le hablo</td></tr>
</table>
<div class="opat"><span class="fx">je le vois</span> = lo veo · <span class="fx">je lui parle</span> = le hablo</div>
<p>La diferencia clave: <b>directo</b> (a quién veo: lo/la) usa <span class="fx">le/la/les</span>; <b>indirecto</b> (a quién le hablo/doy) usa <span class="fx">lui/leur</span>. En <b>pasado</b> van antes del auxiliar: <span class="fx">je l'ai vu</span> (lo vi). Si juntas dos, el orden es <span class="fx">me/te/se</span> → <span class="fx">le/la/les</span> → <span class="fx">lui/leur</span>: <span class="fx">je te le donne</span> (te lo doy). En imperativo afirmativo saltan detrás: <span class="fx">donne-le-moi</span> (dámelo).</p>
''',
'''
<p>They replace a noun so you don't repeat it, and — like Spanish — they go <b>before the verb</b> (not after, like English «I see him»). There are two sets:</p>
<table class="oform">
<tr><td class="k">direct</td><td>me, te, <b>le / la</b>, nous, vous, <b>les</b> — <span class="fx">je le vois</span> = I see him/it</td></tr>
<tr><td class="k">indirect</td><td>me, te, <b>lui</b>, nous, vous, <b>leur</b> — <span class="fx">je lui parle</span> = I talk to him/her</td></tr>
</table>
<div class="opat"><span class="fx">je le vois</span> = lo veo · <span class="fx">je lui parle</span> = le hablo</div>
<p>The key split: <b>direct</b> (whom I see: him/her) uses <span class="fx">le/la/les</span>; <b>indirect</b> (to whom I speak/give) uses <span class="fx">lui/leur</span>. In the <b>past</b> they sit before the auxiliary: <span class="fx">je l'ai vu</span> (I saw him). Stack two and the order is <span class="fx">me/te/se</span> → <span class="fx">le/la/les</span> → <span class="fx">lui/leur</span>: <span class="fx">je te le donne</span> (I give it to you). In the affirmative imperative they jump behind: <span class="fx">donne-le-moi</span> (give it to me).</p>
''')

# ---------------------------------------------------------------- L31 comparer
add("L31", "Comparar: plus / moins / aussi … que", "Comparing: plus / moins / aussi … que",
'''
<p>Se construye igual que en español, con un molde de dos partes:</p>
<table class="oform">
<tr><td class="k">plus … que</td><td>más … que — <span class="fx">plus grand que</span></td></tr>
<tr><td class="k">moins … que</td><td>menos … que — <span class="fx">moins cher que</span></td></tr>
<tr><td class="k">aussi … que</td><td>tan … como — <span class="fx">aussi grand que</span></td></tr>
</table>
<p>El <b>superlativo</b> añade el artículo: <span class="fx">le / la / les plus</span> + adjetivo = el/la más… <span class="fx">le plus grand</span> (el más grande), <span class="fx">la plus belle plage</span>.</p>
<div class="opat">bon → <span class="fx">meilleur</span> (adjetivo) · bien → <span class="fx">mieux</span> (adverbio)</div>
<p><b>El único tropiezo:</b> el español usa «mejor» para todo, pero el francés parte en dos. <span class="fx">meilleur</span> es adjetivo (acompaña a un nombre: <span class="fx">un meilleur café</span> = un mejor café). <span class="fx">mieux</span> es adverbio (acompaña a un verbo: <span class="fx">on mange mieux</span> = se come mejor). Nunca digas «plus bon».</p>
''',
'''
<p>Built just like Spanish, with a two-part frame:</p>
<table class="oform">
<tr><td class="k">plus … que</td><td>more … than — <span class="fx">plus grand que</span></td></tr>
<tr><td class="k">moins … que</td><td>less … than — <span class="fx">moins cher que</span></td></tr>
<tr><td class="k">aussi … que</td><td>as … as — <span class="fx">aussi grand que</span></td></tr>
</table>
<p>The <b>superlative</b> adds the article: <span class="fx">le / la / les plus</span> + adjective = the most… <span class="fx">le plus grand</span> (the biggest), <span class="fx">la plus belle plage</span>.</p>
<div class="opat">bon → <span class="fx">meilleur</span> (adjective) · bien → <span class="fx">mieux</span> (adverb)</div>
<p><b>The one stumble:</b> Spanish uses «mejor» for everything, but French splits it in two. <span class="fx">meilleur</span> is the adjective (with a noun: <span class="fx">un meilleur café</span> = a better coffee). <span class="fx">mieux</span> is the adverb (with a verb: <span class="fx">on mange mieux</span> = we eat better). Never say «plus bon».</p>
''')

# ---------------------------------------------------------------- L32 possessives/demonstratives
add("L32", "Mon, ce…: posesivos y demostrativos", "Mon, ce…: possessives and demonstratives",
'''
<p><b>Posesivos.</b> Concuerdan con el <b>género de la cosa</b>, no del dueño — igual que tu «mi/mis». El francés tiene tres formas donde el español tiene dos:</p>
<table class="oform">
<tr><td class="k">mon (m)</td><td><span class="fx">mon sac</span> — mi bolsa</td></tr>
<tr><td class="k">ma (f)</td><td><span class="fx">ma valise</span> — mi maleta</td></tr>
<tr><td class="k">mes (pl)</td><td><span class="fx">mes amis</span> — mis amigos</td></tr>
</table>
<p>Igual: <span class="fx">ton/ta/tes</span> (tu/tus) y <span class="fx">son/sa/ses</span> (su/sus). Y como tu <b>«su»</b>, <span class="fx">son/sa</span> vale para <b>él o ella</b>: <span class="fx">son sac</span> = su bolsa, de quien sea. Trampa: ante vocal, el femenino cambia a <span class="fx">mon/ton/son</span> — <span class="fx">mon amie</span>, no «ma amie».</p>
<div class="opat"><span class="fx">ce / cet</span> (m) · <span class="fx">cette</span> (f) · <span class="fx">ces</span> (pl) = este/esta/estos</div>
<p><b>Demostrativos.</b> Aquí el francés es <b>más fácil</b> que el español: no hay este/ese/aquel. Un solo juego — <span class="fx">ce, cette, ces</span> — cubre «this/that». <span class="fx">cet</span> es solo <span class="fx">ce</span> ante vocal (<span class="fx">cet été</span> = este verano).</p>
''',
'''
<p><b>Possessives.</b> They agree with the <b>gender of the thing</b>, not the owner — just like Spanish «mi/mis». French has three forms where Spanish has two:</p>
<table class="oform">
<tr><td class="k">mon (m)</td><td><span class="fx">mon sac</span> — my bag</td></tr>
<tr><td class="k">ma (f)</td><td><span class="fx">ma valise</span> — my suitcase</td></tr>
<tr><td class="k">mes (pl)</td><td><span class="fx">mes amis</span> — my friends</td></tr>
</table>
<p>Same for <span class="fx">ton/ta/tes</span> (your) and <span class="fx">son/sa/ses</span> (his/her). And like Spanish <b>«su»</b>, <span class="fx">son/sa</span> works for <b>his OR her</b>: <span class="fx">son sac</span> = his/her bag. Trap: before a vowel, the feminine switches to <span class="fx">mon/ton/son</span> — <span class="fx">mon amie</span>, never «ma amie».</p>
<div class="opat"><span class="fx">ce / cet</span> (m) · <span class="fx">cette</span> (f) · <span class="fx">ces</span> (pl) = this/that/these</div>
<p><b>Demonstratives.</b> Here French is <b>easier</b> than Spanish: no este/ese/aquel. One set — <span class="fx">ce, cette, ces</span> — covers «this/that». <span class="fx">cet</span> is just <span class="fx">ce</span> before a vowel (<span class="fx">cet été</span> = this summer).</p>
''')

# ---------------------------------------------------------------- L33 impératif
add("L33", "El imperativo: cómo se forma (y sus irregulares)", "The imperative: how it's formed (and its irregulars)",
'''
<p>Para dar órdenes o sugerencias, el francés parte del <b>presente</b> y <b>quita el pronombre sujeto</b> — igual que el español dice «¡mira!», no «¡tú miras!». Hay tres formas:</p>
<table class="oform">
<tr><td class="k">tú (-er): quita la -s</td><td><span class="fx">tu manges</span> → <span class="fx">Mange !</span> · <span class="fx">tu vas</span> → <span class="fx">Va !</span></td></tr>
<tr><td class="k">tú (otros verbos)</td><td><span class="fx">tu finis</span> → <span class="fx">Finis !</span> · <span class="fx">tu viens</span> → <span class="fx">Viens !</span></td></tr>
<tr><td class="k">vous (usted/ustedes)</td><td><span class="fx">vous regardez</span> → <span class="fx">Regardez !</span></td></tr>
<tr><td class="k">nous («vamos»)</td><td><span class="fx">nous allons</span> → <span class="fx">Allons ! / Allons-y !</span> = ¡vámonos!</td></tr>
</table>
<p><b>La regla que casi todos olvidan:</b> en la forma «tú» de los verbos en <span class="fx">-er</span> (y de <span class="fx">aller</span>) se <b>quita la -s</b> final: <span class="fx">Mange !</span>, <span class="fx">Écoute !</span>, <span class="fx">Va !</span>. En los demás verbos, se queda: <span class="fx">Viens !</span>, <span class="fx">Fais !</span>.</p>
<p><b>Irregulares</b> (como tus «ten», «ven», «sé») — memorízalos:</p>
<ul class="oul">
<li><span class="fx">être</span> → <span class="fx">sois / soyez</span> — <span class="fx">Sois sage !</span> (pórtate bien)</li>
<li><span class="fx">avoir</span> → <span class="fx">aie / ayez</span> — <span class="fx">Ayez de la patience</span> (tengan paciencia)</li>
<li><span class="fx">savoir</span> → <span class="fx">sache / sachez</span> — <span class="fx">Sache que…</span> (que sepas que…)</li>
<li><span class="fx">aller</span> → <span class="fx">va / allez</span> — <span class="fx">Vas-y !</span> (¡dale!)</li>
</ul>
<div class="opat">afirmativo: el pronombre va <b>detrás</b> — <span class="fx">Donne-moi</span> (dame), <span class="fx">Lève-toi</span> (levántate)</div>
<p><b>Pronombres:</b> en afirmativo se pegan detrás con guion, y <span class="fx">me/te</span> se vuelven <span class="fx">moi/toi</span>: <span class="fx">Donne-moi ton insta</span>, <span class="fx">Dis-moi</span> (dime), <span class="fx">Allons-y</span>. En <b>negativo</b>, vuelven a su sitio normal delante: <span class="fx">Ne me dis pas ça</span>, <span class="fx">Ne bouge pas !</span> (no te muevas).</p>
''',
'''
<p>To give commands or suggestions, French starts from the <b>present tense</b> and <b>drops the subject pronoun</b> — just like Spanish says «¡mira!», not «¡tú miras!». There are three forms:</p>
<table class="oform">
<tr><td class="k">tu (-er): drop the -s</td><td><span class="fx">tu manges</span> → <span class="fx">Mange !</span> · <span class="fx">tu vas</span> → <span class="fx">Va !</span></td></tr>
<tr><td class="k">tu (other verbs)</td><td><span class="fx">tu finis</span> → <span class="fx">Finis !</span> · <span class="fx">tu viens</span> → <span class="fx">Viens !</span></td></tr>
<tr><td class="k">vous (formal/plural)</td><td><span class="fx">vous regardez</span> → <span class="fx">Regardez !</span></td></tr>
<tr><td class="k">nous («let's»)</td><td><span class="fx">nous allons</span> → <span class="fx">Allons ! / Allons-y !</span> = let's go!</td></tr>
</table>
<p><b>The rule almost everyone forgets:</b> in the «tu» form of <span class="fx">-er</span> verbs (and of <span class="fx">aller</span>) you <b>drop the final -s</b>: <span class="fx">Mange !</span>, <span class="fx">Écoute !</span>, <span class="fx">Va !</span>. For all other verbs it stays: <span class="fx">Viens !</span>, <span class="fx">Fais !</span>.</p>
<p><b>Irregulars</b> (like Spanish «ten», «ven», «sé») — memorize these:</p>
<ul class="oul">
<li><span class="fx">être</span> → <span class="fx">sois / soyez</span> — <span class="fx">Sois sage !</span> (be good)</li>
<li><span class="fx">avoir</span> → <span class="fx">aie / ayez</span> — <span class="fx">Ayez de la patience</span> (have patience)</li>
<li><span class="fx">savoir</span> → <span class="fx">sache / sachez</span> — <span class="fx">Sache que…</span> (know that…)</li>
<li><span class="fx">aller</span> → <span class="fx">va / allez</span> — <span class="fx">Vas-y !</span> (go on!)</li>
</ul>
<div class="opat">affirmative: the pronoun goes <b>after</b> — <span class="fx">Donne-moi</span> (give me), <span class="fx">Lève-toi</span> (get up)</div>
<p><b>Pronouns:</b> in the affirmative they attach behind with a hyphen, and <span class="fx">me/te</span> become <span class="fx">moi/toi</span>: <span class="fx">Donne-moi ton insta</span>, <span class="fx">Dis-moi</span> (tell me), <span class="fx">Allons-y</span>. In the <b>negative</b>, they return to their normal spot in front: <span class="fx">Ne me dis pas ça</span>, <span class="fx">Ne bouge pas !</span> (don't move).</p>
''')

# ---------------------------------------------------------------- merge
odir = os.path.join(os.path.dirname(__file__), "..", "scratchpad_readers", "orient")
topical = json.load(open(os.path.join(odir, "topical_raw.json")))
topical2 = json.load(open(os.path.join(odir, "topical_raw2.json")))
ALL = {}
ALL.update(G)
ALL.update(topical)
ALL.update(topical2)

fmap = {}
for p in glob.glob(os.path.join(base, "lesson_*.json")):
    L = json.load(open(p))
    fmap[L["id"]] = p

applied = []
for lid, o in ALL.items():
    if lid not in fmap:
        print("!! no lesson file for", lid); continue
    L = json.load(open(fmap[lid]))
    L["orientation"] = o
    json.dump(L, open(fmap[lid], "w"), ensure_ascii=False, indent=2)
    applied.append(lid)
print("orientation applied to", len(applied), "lessons:", " ".join(sorted(applied)))
missing = [i for i in sorted(fmap) if i not in ALL]
print("lessons WITHOUT orientation:", " ".join(missing) or "(none)")
