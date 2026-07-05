#!/usr/bin/env python3
"""Assemble batch-2 grammar-gap modules L27-L33 (reader + vocab + sentences + drills)."""
import json, os

READERS = {}  # filled below
LESS = {}

# ---------------- READERS (from Fable agents) ----------------
READERS["L27"] = [
  {"t":"h3","text":"C'est où, c'est quand ?"},
  {"t":"pair","fr":"Ce matin, j'ai demandé à une dame : « Pardon, la plage, c'est où ? Et le marché, c'est quand ? » Pas de grammaire compliquée — tu montes la voix à la fin, et voilà, c'est une question.","es":"Esta mañana, le he preguntado a una señora: «Perdón, la playa, ¿es dónde? ¿Y el mercado, es cuándo?» Nada de gramática complicada — subes la voz al final, y ya está, es una pregunta.","en":"This morning I asked a lady, 'Excuse me, the beach — where is it? And the market, when is it?' No complicated grammar — you just raise your voice at the end, and boom, it's a question."},
  {"t":"h3","text":"Est-ce que : la formule magique"},
  {"t":"pair","fr":"Dans les livres, on écrit « Où vas-tu ? », mais franchement, personne parle comme ça dans la rue. Nous, on colle « est-ce que » devant : « Est-ce que le bus 12 va au port ? » — et le chauffeur comprend tout de suite.","es":"En los libros, se escribe «Où vas-tu?», pero francamente, nadie habla así en la calle. Nosotros, pegamos «es que» delante: «¿Es que el bus 12 va al puerto?» — y el chofer comprende enseguida.","en":"In books they write 'Où vas-tu?', but honestly, nobody talks like that on the street. Us, we just glue 'est-ce que' on the front: 'Does the number 12 bus go to the port?' — and the driver gets it right away."},
  {"t":"h3","text":"Qui, que, quoi ?!"},
  {"t":"pair","fr":"Mon frère est entré sans frapper et m'a demandé : « Tu regardes quoi ? » Moi : « Et toi, qui t'a invité dans ma chambre ? Comment tu oses ? »","es":"Mi hermano ha entrado sin tocar y me ha preguntado: «¿Tú miras qué?» Yo: «Y tú, ¿quién te ha invitado a mi cuarto? ¿Cómo tú osas?»","en":"My brother walked in without knocking and asked, 'What are you watching?' Me: 'And you — who invited you into my room? How dare you?'"},
  {"t":"h3","text":"Pourquoi ? Parce que."},
  {"t":"pair","fr":"Maman demande toujours pourquoi : pourquoi tu rentres tard, pourquoi la glace coûte quatre euros, pourquoi on marche encore. Moi, je réponds avec la logique de Nice : parce que c'est beau, voilà pourquoi.","es":"Mamá pregunta siempre por qué: por qué tú vuelves tarde, por qué el helado cuesta cuatro euros, por qué caminamos todavía. Yo, respondo con la lógica de Niza: porque es bello, he ahí por qué.","en":"Mom is always asking why: why are you home late, why does ice cream cost four euros, why are we still walking. Me, I answer with Nice logic: because it's beautiful, that's why."},
  {"t":"h3","text":"Combien, quel — les questions du marché"},
  {"t":"pair","fr":"Au marché, la question essentielle : « C'est combien, les fraises ? » Et puis « il est quelle heure ? », « on prend quel bus ? » — avec « quel », tu accordes, mais bon, personne t'arrête dans la rue pour vérifier.","es":"En el mercado, la pregunta esencial: «¿Es cuánto, las fresas?» Y luego «¿es qué hora?», «¿tomamos qué bus?» — con «quel» (qué/cuál), tú concuerdas, pero bueno, nadie te para en la calle para verificar.","en":"At the market, the essential question: 'How much are the strawberries?' And then 'what time is it?', 'which bus are we taking?' — with 'quel' you have to make it agree, but hey, nobody stops you on the street to check."}
]
READERS["L28"] = json.load(open(os.path.join(os.path.dirname(__file__),"..","scratchpad_readers","reader_L28.json")))
READERS["L29"] = [
  {"t":"h3","text":"Je me réveille"},
  {"t":"pair","fr":"Le matin, je me réveille à huit heures parce que les mouettes de Nice crient comme des folles. Je me lève tout de suite — le soleil ici, ça ne pardonne pas.","es":"Por la mañana, me despierto a las ocho porque las gaviotas de Niza gritan como locas. Me levanto en seguida — el sol aquí, eso no perdona.","en":"In the morning I wake up at eight because the Nice seagulls scream like maniacs. I get up right away — the sun here does not mess around."},
  {"t":"h3","text":"Je me prépare"},
  {"t":"pair","fr":"Je me lave, je m'habille, je me coiffe — et je réalise un truc : c'est exactement comme en espagnol. Me levanto, je me lève ; le petit pronom se place avant le verbe, cadeau total.","es":"Me lavo, me visto, me peino — y me doy cuenta de una cosa: es exactamente como en español. Me levanto, je me lève; el pequeño pronombre se coloca antes del verbo, regalo total.","en":"I wash up, get dressed, do my hair — and I realize something: it's exactly like Spanish. Me levanto is je me lève; the little pronoun goes right before the verb. Total gift."},
  {"t":"h3","text":"On se dépêche !"},
  {"t":"pair","fr":"Mon amie sonne en bas, alors je me dépêche comme jamais. On descend vite vers la plage avec les serviettes et un pain au chocolat encore chaud.","es":"Mi amiga toca el timbre abajo, así que me doy prisa como nunca. Bajamos rápido hacia la playa con las toallas y un pan de chocolate todavía caliente.","en":"My friend rings the bell downstairs, so I hurry like never before. We rush down to the beach with our towels and a still-warm pain au chocolat."},
  {"t":"h3","text":"La plage"},
  {"t":"pair","fr":"À la plage, on se baigne et on se détend sur les galets — oui, des galets, pas du sable. Le chien d'à côté s'appelle Kiki et sa maîtresse le répète toutes les cinq minutes.","es":"En la playa, nos bañamos y nos relajamos sobre los guijarros — sí, guijarros, no arena. El perro de al lado se llama Kiki y su dueña lo repite cada cinco minutos.","en":"At the beach we swim and relax on the pebbles — yes, pebbles, not sand. The dog next to us is named Kiki, and his owner repeats it every five minutes."},
  {"t":"h3","text":"Je me couche"},
  {"t":"pair","fr":"Le soir, je rentre, je me douche et je me couche vers onze heures. Je m'endors avec le bruit des vagues et une certitude : le français, avec l'espagnol dans la poche, c'est presque de la triche.","es":"Por la noche, vuelvo, me ducho y me acuesto hacia las once. Me duermo con el ruido de las olas y una certeza: el francés, con el español en el bolsillo, es casi trampa.","en":"At night I head home, shower, and go to bed around eleven. I fall asleep to the sound of the waves with one certainty: French, with Spanish in your pocket, is almost cheating."}
]
READERS["L30"] = [
  {"t":"h3","text":"Le pronom avant le verbe, comme chez nous"},
  {"t":"pair","fr":"Bonne nouvelle : en français, le pronom se place avant le verbe, exactement comme en espagnol. Je le vois, je lui parle — mon cerveau connaît déjà cette musique.","es":"Buena noticia: en francés, el pronombre se coloca antes del verbo, exactamente como en español. Lo veo, le hablo — mi cerebro ya conoce esta música.","en":"Good news: in French, the pronoun goes before the verb, exactly like in Spanish. Je le vois, je lui parle — my brain already knows this tune."},
  {"t":"h3","text":"Le garçon du Cours Saleya"},
  {"t":"pair","fr":"Il y a un garçon qui vend des fleurs au marché, et franchement, je le trouve mignon. Je le regarde discrètement pendant que ma mère achète des tomates.","es":"Hay un chico que vende flores en el mercado, y francamente, lo encuentro lindo. Lo miro discretamente mientras mi madre compra tomates.","en":"There's a boy who sells flowers at the market, and honestly, I think he's cute. I sneak looks at him while my mom buys tomatoes."},
  {"t":"h3","text":"Je lui envoie tout"},
  {"t":"pair","fr":"Ma meilleure amie est restée à la maison, alors je lui envoie un message toutes les dix minutes. Hier, je lui ai raconté l'histoire du garçon, et elle m'a répondu avec quinze émojis.","es":"Mi mejor amiga se quedó en casa, así que le envío un mensaje cada diez minutos. Ayer, le conté la historia del chico, y ella me respondió con quince emojis.","en":"My best friend stayed back home, so I text her every ten minutes. Yesterday I told her the story about the boy, and she replied with fifteen emojis."},
  {"t":"h3","text":"Mes parents, je les appelle (parfois)"},
  {"t":"pair","fr":"Quand je me promène seule sur la Promenade des Anglais, je les appelle pour dire que tout va bien. Bon, d'accord : parfois je les ignore un peu, mais je leur réponds toujours avant le dîner.","es":"Cuando paseo sola por la Promenade des Anglais, los llamo para decir que todo va bien. Bueno, de acuerdo: a veces los ignoro un poco, pero les respondo siempre antes de la cena.","en":"When I walk alone on the Promenade des Anglais, I call them to say everything's fine. Okay, fine: sometimes I ignore them a little, but I always answer them before dinner."},
  {"t":"h3","text":"Lui ou le ? Petit truc"},
  {"t":"pair","fr":"Si en espagnol tu dis « lo » ou « la », en français tu dis « le » ou « la » ; et si tu dis « le », en français c'est « lui ». Le garçon aux fleurs, je le trouve adorable, et un jour, promis, je lui parle.","es":"Si en español dices « lo » o « la », en francés dices « le » o « la »; y si dices « le », en francés es « lui ». Al chico de las flores, lo encuentro adorable, y un día, prometido, le hablo.","en":"If in Spanish you say lo or la, in French you say le or la; and if you say le, in French it's lui. The flower boy — I think he's adorable, and one day, I promise, I'm talking to him."}
]
READERS["L31"] = [
  {"t":"h3","text":"La plage ou la montagne ?"},
  {"t":"pair","fr":"La plage est plus proche que la montagne, et franchement, elle est moins compliquée aussi. Mais la montagne est plus tranquille — ici, il y a plus de touristes que de pigeons, et ça, c'est beaucoup.","es":"La playa está más próxima que la montaña, y francamente, es menos complicada también. Pero la montaña es más tranquila — aquí, hay más turistas que palomas, y eso, es mucho.","en":"The beach is closer than the mountains, and honestly, it's less complicated too. But the mountains are quieter — here there are more tourists than pigeons, and that's saying a lot."},
  {"t":"h3","text":"Socca contre pizza"},
  {"t":"pair","fr":"La socca est aussi populaire que la pizza ici, mais elle est moins connue en Amérique. Pour moi, la socca est meilleure que la pizza — oui, j'ai vraiment dit ça.","es":"La socca es tan popular como la pizza aquí, pero es menos conocida en América. Para mí, la socca es mejor que la pizza — sí, verdaderamente dije eso.","en":"Socca is as popular as pizza here, but it's less well known in America. For me, socca is better than pizza — yes, I really said that."},
  {"t":"h3","text":"Nice contre Paris"},
  {"t":"pair","fr":"Paris est plus grand que Nice, c'est évident, mais Nice est plus ensoleillée et moins stressée. Et honnêtement, on mange mieux ici — désolée, Paris.","es":"París es más grande que Niza, es evidente, pero Niza es más soleada y menos estresada. Y honestamente, comemos mejor aquí — perdón, París.","en":"Paris is bigger than Nice, obviously, but Nice is sunnier and less stressed out. And honestly, the food's better here — sorry, Paris."},
  {"t":"h3","text":"Meilleur ou mieux ? Le piège"},
  {"t":"pair","fr":"Ce croissant est meilleur que celui d'hier, et je dors mieux depuis qu'on est arrivés. Attention : « bon » devient « meilleur » et « bien » devient « mieux » — en espagnol c'est « mejor » les deux fois, ici non.","es":"Este croissant es mejor que el de ayer, y duermo mejor desde que llegamos. Cuidado: « bon » se vuelve « meilleur » y « bien » se vuelve « mieux » — en español es « mejor » las dos veces, aquí no.","en":"This croissant is better than yesterday's, and I've been sleeping better since we arrived. Watch out: \"bon\" becomes \"meilleur\" and \"bien\" becomes \"mieux\" — in Spanish it's \"mejor\" both times, here it's not."},
  {"t":"h3","text":"Le plus beau moment"},
  {"t":"pair","fr":"Le coucher de soleil sur la Promenade, c'était le plus beau moment de la semaine, sans discussion. Et le meilleur dans tout ça ? Demain, on recommence.","es":"La puesta de sol en la Promenade, fue el más bello momento de la semana, sin discusión. ¿Y lo mejor de todo eso? Mañana, empezamos de nuevo.","en":"The sunset over the Promenade was the most beautiful moment of the week, no debate. And the best part of it all? Tomorrow we get to do it again."}
]
READERS["L32"] = [
  {"t":"h3","text":"Ma valise, mes problèmes"},
  {"t":"pair","fr":"Ma valise est énorme et mon sac est plein de crème solaire. Mes parents disent que j'exagère, mais bon, c'est ma première semaine à Nice.","es":"Mi maleta es enorme y mi bolso está lleno de crema solar. Mis padres dicen que exagero, pero bueno, es mi primera semana en Niza.","en":"My suitcase is enormous and my bag is stuffed with sunscreen. My parents say I'm overdoing it, but hey, it's my first week in Nice."},
  {"t":"h3","text":"Son sac… à lui ou à elle ?"},
  {"t":"pair","fr":"Sur la plage, quelqu'un a oublié son sac et sa serviette — un garçon ou une fille, mystère total. En français, « son » et « sa » suivent l'objet, pas la personne, exactement comme votre « su ».","es":"En la playa, alguien olvidó su bolso y su toalla — ¿un chico o una chica?, misterio total. En francés, « son » y « sa » siguen al objeto, no a la persona, exactamente como su « su ».","en":"On the beach, somebody left behind their bag and their towel — a boy or a girl, total mystery. In French, 'son' and 'sa' go with the thing, not the owner, exactly like your 'su'."},
  {"t":"h3","text":"Mon amie (oui, mon)"},
  {"t":"pair","fr":"Mon amie Chloé habite près du port et son école donne sur la mer, quelle chance. On dit « mon amie » et pas « ma amie » — devant une voyelle, le français refuse deux voyelles qui se cognent.","es":"Mi amiga Chloé vive cerca del puerto y su escuela da al mar, qué suerte. Se dice « mon amie » y no « ma amie » — delante de una vocal, el francés rechaza dos vocales que chocan.","en":"My friend Chloé lives near the port and her school looks out on the sea — lucky her. You say 'mon amie,' never 'ma amie' — before a vowel, French refuses to let two vowels crash into each other."},
  {"t":"h3","text":"Cette glace, ce bonheur"},
  {"t":"pair","fr":"Cette glace à la lavande est la meilleure de ma vie, et ce vendeur le sait très bien. En français, zéro drame entre « este », « ese » et « aquel » : « ce » et « cette » font tout le travail.","es":"Este helado de lavanda es el mejor de mi vida, y este vendedor lo sabe muy bien. En francés, cero drama entre « este », « ese » y « aquel »: « ce » y « cette » hacen todo el trabajo.","en":"This lavender ice cream is the best of my life, and the guy selling it knows it. In French there's zero drama between 'este,' 'ese,' and 'aquel' — 'ce' and 'cette' do all the work."},
  {"t":"h3","text":"Cet été, ces vacances"},
  {"t":"pair","fr":"Ce soir, on va regarder le coucher de soleil sur la Promenade avec ces touristes et leurs mille photos. Cet été est déjà mon préféré, et ces vacances viennent à peine de commencer.","es":"Esta noche, vamos a mirar la puesta de sol en el Paseo con estos turistas y sus mil fotos. Este verano ya es mi favorito, y estas vacaciones apenas acaban de comenzar.","en":"Tonight we're going to watch the sunset on the Promenade with all these tourists and their thousand photos. This summer is already my favorite, and this vacation has barely even started."}
]
READERS["L33"] = [
  {"t":"h3","text":"Regarde-moi ça !"},
  {"t":"pair","fr":"Regarde cette mer, elle est complètement turquoise ! Écoute les vagues et arrête de regarder ton téléphone deux secondes.","es":"¡Mira este mar, está completamente turquesa! Escucha las olas y para de mirar tu teléfono dos segundos.","en":"Look at this sea, it's completely turquoise! Listen to the waves and stop staring at your phone for two seconds."},
  {"t":"h3","text":"Donne-moi, dis-moi"},
  {"t":"pair","fr":"Donne-moi la crème solaire, je grille déjà. Et dis-moi où tu as caché les chips, s'il te plaît !","es":"Dame la crema solar, ya me quemo. ¡Y dime dónde escondiste las papas, por favor!","en":"Hand me the sunscreen, I'm already frying. And tell me where you hid the chips, please!"},
  {"t":"h3","text":"Allons-y !"},
  {"t":"pair","fr":"L'eau est parfaite, allons-y ! Vas-y en premier, moi je surveille les serviettes… bon, d'accord, on y va ensemble.","es":"El agua está perfecta, ¡vamos! Ve tú primero, yo vigilo las toallas… bueno, de acuerdo, vamos juntas.","en":"The water is perfect, let's go! You go first, I'll guard the towels... okay, fine, we'll go in together."},
  {"t":"h3","text":"Venez voir !"},
  {"t":"pair","fr":"Les filles, venez voir cette méduse, elle est énorme ! Madame, excusez-moi, regardez… c'est dangereux, ça ?","es":"¡Chicas, vengan a ver esta medusa, es enorme! Señora, discúlpeme, mire… ¿es peligroso, eso?","en":"Girls, come see this jellyfish, it's huge! Ma'am, excuse me, look... is that thing dangerous?"},
  {"t":"h3","text":"Ne bouge pas !"},
  {"t":"pair","fr":"Ne bouge pas, il y a une guêpe sur ta glace ! Ne panique pas non plus… trop tard, elle a couru dans la mer avec son cône.","es":"¡No te muevas, hay una avispa en tu helado! Tampoco entres en pánico… demasiado tarde, corrió al mar con su cono.","en":"Don't move, there's a wasp on your ice cream! And don't panic either... too late, she sprinted into the sea, cone and all."}
]

def V(id,fr,es,en,ipa,pos,ct,ex,voice,gender=None,star=False):
    d={"id":id,"fr":fr,"es":es,"en":en,"ipa":ipa,"pos":pos,"cognate_type":ct,"ex":ex,"voice":voice,"audio":id}
    if gender: d["gender"]=gender
    if star: d["star"]=True
    return d
def S(id,fr,es,en,voice,gloss=None):
    d={"id":id,"register":"parle","fr":fr,"es":es,"en":en,"voice":voice,"audio":id}
    if gloss: d["gloss"]=gloss
    return d
def D(q,sub,ans,opts,aud=None):
    d={"q":q,"sub":sub,"ans":ans,"opts":opts}
    if aud: d["aud"]=aud
    return d

# ---------------- L27 Les questions ----------------
LESS["L27"]=dict(order=27,slug="questions",title="Les questions",es_title="Cómo preguntar (qui, où, pourquoi…)",
  focus="Preguntar en francés hablado: las palabras clave (qui, où, quand, comment, pourquoi, combien, quel) y « est-ce que » — sin la inversión de los libros.",
  objectives=["Usar las palabras interrogativas.","Preguntar con « est-ce que » o solo con la entonación.","« quel/quelle » concuerda con el nombre."],
  vocab=[
    V("L27-qui","qui ?","¿quién?","who?","ki","interro","non_cognate","Qui est là ?","emilie",star=True),
    V("L27-quoi","quoi ? / que ?","¿qué?","what?","kwa","interro","non_cognate","Tu fais quoi ?","oris",star=True),
    V("L27-ou","où ?","¿dónde?","where?","u","interro","non_cognate","Où est la plage ?","emilie",star=True),
    V("L27-quand","quand ?","¿cuándo?","when?","kɑ̃","interro","non_cognate","Tu arrives quand ?","oris",star=True),
    V("L27-comment","comment ?","¿cómo?","how?","kɔmɑ̃","interro","non_cognate","Comment tu t'appelles ?","emilie",star=True),
    V("L27-pourquoi","pourquoi ?","¿por qué?","why?","puʁkwa","interro","non_cognate","Pourquoi tu ris ?","oris",star=True),
    V("L27-parceque","parce que","porque","because","paʁs kə","conj","non_cognate","Parce que c'est beau.","emilie"),
    V("L27-combien","combien ?","¿cuánto?","how much?","kɔ̃bjɛ̃","interro","non_cognate","Ça coûte combien ?","oris",star=True),
    V("L27-quel","quel / quelle ?","¿qué? / ¿cuál?","which? / what?","kɛl","interro","non_cognate","Quelle heure est-il ?","emilie",star=True),
    V("L27-estce","est-ce que… ?","(marca de pregunta)","(question marker)","ɛs kə","interro","non_cognate","Est-ce que tu viens ?","oris",star=True),
  ],
  sentences=[
    S("L27-s01","Comment tu t'appelles ? — Moi, c'est Emma.","¿Cómo te llamas? — Yo, soy Emma.","What's your name? — I'm Emma.","emilie"),
    S("L27-s02","Pardon, ça coûte combien, les fraises ?","Perdón, ¿cuánto cuestan las fresas?","Excuse me, how much are the strawberries?","oris"),
    S("L27-s03","Est-ce que le bus 12 va au port ?","¿El bus 12 va al puerto?","Does the number 12 bus go to the port?","emilie",gloss="« est-ce que » = pregunta sí/no, sin inversión"),
    S("L27-s04","On mange quoi ce soir ?","¿Qué comemos esta noche?","What are we eating tonight?","oris"),
  ],
  drills=[
    D("« ¿Qué hora es? »","français correct :","Quelle heure est-il ?",["Quelle heure est-il ?","Quel heure est-il ?","Comment heure est-il ?","Où heure est-il ?"]),
    D("« ¿Cuánto cuesta? » → Ça coûte ___ ?","le bon mot :","combien",["combien","comment","quel","pourquoi"]),
    D("« ¿Por qué ríes? »","attention pourquoi ≠ parce que :","Pourquoi tu ris ?",["Pourquoi tu ris ?","Parce que tu ris ?","Pour quoi tu ris ?","Comment tu ris ?"]),
    D("Question oui/non polie : « ___ tu viens ? »","(es que…) :","Est-ce que",["Est-ce que","Qu'est-ce qui","Est-ce qui","C'est que"]),
    D("« ¿Dónde está la playa? » → « ___ est la plage ? »","où (dónde), pas ou (o) :","Où",["Où","Ou","D'où","Quand"]),
    D("« ¿Quién es? » → « ___ c'est ? »","le bon mot :","Qui",["Qui","Que","Quoi","Quel"]),
  ])

# ---------------- L28 La négation ----------------
LESS["L28"]=dict(order=28,slug="negation",title="La négation",es_title="Decir no (ne… pas, jamais, rien)",
  focus="El « no » francés viene en DOS piezas (ne … pas) alrededor del verbo — pero al hablar, casi siempre se cae el « ne ». Y las variantes: jamais, rien, plus, personne.",
  objectives=["Construir ne … pas alrededor del verbo.","Usar jamais, rien, plus, personne.","Entender que en la calle el « ne » desaparece: « je sais pas »."],
  vocab=[
    V("L28-nepas","ne … pas","no","not","nə pa","neg","non_cognate","Je ne sais pas.","emilie",star=True),
    V("L28-pas","pas (parlé)","no (hablado)","not (spoken)","pa","neg","non_cognate","C'est pas grave.","oris",star=True),
    V("L28-jamais","ne … jamais","nunca","never","nə ʒamɛ","neg","non_cognate","Je ne bois jamais de café.","emilie",star=True),
    V("L28-rien","ne … rien","nada","nothing","nə ʁjɛ̃","neg","non_cognate","Je ne vois rien.","oris",star=True),
    V("L28-plus","ne … plus","ya no","no more / no longer","nə ply","neg","non_cognate","Il n'y a plus de pain.","emilie",star=True),
    V("L28-personne","ne … personne","nadie","nobody","nə pɛʁsɔn","neg","non_cognate","Il n'y a personne.","oris",star=True),
    V("L28-neque","ne … que","solo / solamente","only","nə kə","neg","non_cognate","Je n'ai qu'un euro.","emilie"),
    V("L28-rienmot","rien","nada","nothing","ʁjɛ̃","pron","non_cognate","Rien à déclarer.","oris"),
    V("L28-jamaismot","jamais","nunca / jamás","never","ʒamɛ","adv","transparent","Jamais de la vie !","emilie"),
  ],
  sentences=[
    S("L28-s01","Je ne sais pas où est le tram.","No sé dónde está el tranvía.","I don't know where the tram is.","emilie"),
    S("L28-s02","C'est pas grave, on prend le bus.","No pasa nada, tomamos el bus.","No worries, we'll take the bus.","oris",gloss="parlé: el « ne » desaparece"),
    S("L28-s03","Il n'y a plus de socca ? Dommage !","¿Ya no hay socca? ¡Qué lástima!","No more socca? What a shame!","emilie"),
    S("L28-s04","Je ne mange jamais de viande le matin.","Nunca como carne por la mañana.","I never eat meat in the morning.","oris"),
  ],
  drills=[
    D("« Nunca » = ne … ___","le bon mot :","jamais",["jamais","rien","plus","personne"]),
    D("« Ya no hay pan » → « Il n'y a ___ de pain. »","le bon mot :","plus",["plus","pas","jamais","rien"]),
    D("« No veo nada » → « Je ne vois ___. »","le bon mot :","rien",["rien","personne","jamais","pas"]),
    D("« No hay nadie » → « Il n'y a ___. »","le bon mot :","personne",["personne","rien","plus","aucun"]),
    D("En français parlé « je sais pas », le mot souvent oublié c'est…","(les deux pièces) :","ne",["ne","pas","je","sais"]),
    D("« No lo sé. »","phrase complète :","Je ne sais pas.",["Je ne sais pas.","Je ne sais pas rien.","Je sais no.","Je no sais pas."]),
  ])

# ---------------- L29 Le quotidien (reflexives) ----------------
LESS["L29"]=dict(order=29,slug="quotidien",title="Le quotidien",es_title="La rutina (verbos reflexivos: me levanto…)",
  focus="Los verbos reflexivos funcionan IGUAL que en español (me/te/se + verbo, pronombre antes del verbo). « je me lève » = « me levanto ». Un regalo enorme.",
  objectives=["Conjugar reflexivos (je me lève, tu te lèves).","Colocar el pronombre reflexivo ANTES del verbo, como en español.","Contar tu rutina: lever, laver, habiller, coucher."],
  vocab=[
    V("L29-lever","se lever","levantarse","to get up","sə ləve","verb","non_cognate","Je me lève à sept heures.","emilie",star=True),
    V("L29-reveiller","se réveiller","despertarse","to wake up","sə ʁevɛje","verb","semi","Je me réveille tôt.","oris",star=True),
    V("L29-laver","se laver","lavarse","to wash up","sə lave","verb","transparent","Je me lave les mains.","emilie",star=True),
    V("L29-habiller","s'habiller","vestirse","to get dressed","sabije","verb","non_cognate","Je m'habille vite.","oris",star=True),
    V("L29-coucher","se coucher","acostarse","to go to bed","sə kuʃe","verb","non_cognate","Je me couche tard.","emilie",star=True),
    V("L29-appeler","s'appeler","llamarse","to be called","saple","verb","non_cognate","Je m'appelle Emma.","oris",star=True),
    V("L29-depecher","se dépêcher","darse prisa","to hurry","sə depeʃe","verb","non_cognate","Dépêche-toi !","emilie",star=True),
    V("L29-reposer","se reposer","descansar","to rest","sə ʁəpoze","verb","semi","Je me repose sur la plage.","oris"),
    V("L29-doucher","se doucher","ducharse","to shower","sə duʃe","verb","semi","Je me douche le soir.","emilie"),
  ],
  sentences=[
    S("L29-s01","Le matin, je me lève et je me lave.","Por la mañana, me levanto y me lavo.","In the morning, I get up and wash up.","emilie"),
    S("L29-s02","Dépêche-toi, on va rater le bus !","¡Date prisa, vamos a perder el bus!","Hurry up, we're going to miss the bus!","oris"),
    S("L29-s03","Le soir, je me couche tard à Nice.","Por la noche, me acuesto tarde en Niza.","At night, I go to bed late in Nice.","emilie"),
    S("L29-s04","Comment tu t'appelles ? — Je m'appelle Léa.","¿Cómo te llamas? — Me llamo Léa.","What's your name? — My name is Léa.","oris"),
  ],
  drills=[
    D("« Me levanto » = ___","français correct :","je me lève",["je me lève","je lève","je se lève","me levo"]),
    D("El pronombre reflexivo va ___ el verbo (como en español).","position :","avant",["avant","après","à la fin","on l'oublie"]),
    D("« Se llama Léa » → « Elle ___ Léa. »","le bon mot :","s'appelle",["s'appelle","se appelle","appelle","se llama"]),
    D("« Acostarse » = ___","le bon verbe :","se coucher",["se coucher","se lever","se laver","se reposer"]),
    D("« Me visto rápido » → « Je ___ vite. »","le bon mot :","m'habille",["m'habille","habille","me habille","s'habille"]),
    D("« ¡Date prisa! » (à un ami) → « ___ ! »","impératif réfléchi :","Dépêche-toi",["Dépêche-toi","Te dépêche","Dépêche-te","Se dépêche"]),
  ])

# ---------------- L30 Les pronoms (object) ----------------
LESS["L30"]=dict(order=30,slug="pronoms",title="Les pronoms",es_title="Pronombres de objeto (lo veo, le hablo)",
  focus="Los pronombres de objeto van ANTES del verbo, igual que en español: « je le vois » = « lo veo », « je lui parle » = « le hablo ». Directo (le/la/les) vs indirecto (lui/leur).",
  objectives=["Directo: me, te, le/la, nous, vous, les.","Indirecto: me, te, lui, nous, vous, leur.","Colocar el pronombre antes del verbo (reflejo del español)."],
  vocab=[
    V("L30-me","me / m'","me","me","mə","pron","non_cognate","Il me parle.","emilie",star=True),
    V("L30-te","te / t'","te","you","tə","pron","transparent","Je te vois.","oris",star=True),
    V("L30-le","le","lo","him / it","lə","pron","non_cognate","Je le connais.","emilie",star=True),
    V("L30-la","la","la","her / it","la","pron","transparent","Je la connais.","oris",star=True),
    V("L30-les","les","los / las","them","le","pron","non_cognate","Je les appelle.","emilie",star=True),
    V("L30-lui","lui","le (a él/ella)","(to) him/her","lɥi","pron","non_cognate","Je lui parle.","oris",star=True),
    V("L30-leur","leur","les (a ellos)","(to) them","lœʁ","pron","non_cognate","Je leur parle.","emilie",star=True),
    V("L30-nous","nous","nos","us","nu","pron","non_cognate","Il nous attend.","oris"),
    V("L30-vous","vous","os / les","you (pl.)","vu","pron","non_cognate","Je vous remercie.","emilie"),
  ],
  sentences=[
    S("L30-s01","Ce garçon ? Je le trouve trop mignon.","¿Ese chico? Lo encuentro súper lindo.","That boy? I think he's really cute.","emilie",gloss="le = lo (objeto directo, antes del verbo)"),
    S("L30-s02","Je lui envoie un message tout de suite.","Le envío un mensaje ahora mismo.","I'll send him/her a message right away.","oris"),
    S("L30-s03","Mes parents ? Je les appelle ce soir.","¿Mis padres? Los llamo esta noche.","My parents? I'll call them tonight.","emilie"),
    S("L30-s04","Tu me vois ? Coucou, je suis là !","¿Me ves? ¡Hola, aquí estoy!","Can you see me? Hey, I'm here!","oris"),
  ],
  drills=[
    D("« Lo veo » → « Je ___ vois. »","objet direct :","le",["le","lui","la","les"]),
    D("El pronombre de objeto va ___ el verbo conjugado.","position :","avant",["avant","après","à la fin","n'importe où"]),
    D("« Le hablo (a él) » → « Je ___ parle. »","objet indirect :","lui",["lui","le","leur","il"]),
    D("« Los llamo » → « Je ___ appelle. »","le bon mot :","les",["les","leur","le","la"]),
    D("« Les hablo (a ellos) » → « Je ___ parle. »","objet indirect pluriel :","leur",["leur","les","lui","ils"]),
    D("« Te veo » → « Je ___ vois. »","le bon mot :","te",["te","toi","tu","lui"]),
  ])

# ---------------- L31 Comparer ----------------
LESS["L31"]=dict(order=31,slug="comparer",title="Comparer",es_title="Comparar (plus… que, meilleur, mieux)",
  focus="Comparar como en español: plus… que (más… que), moins… que, aussi… que (tan… como). Cuidado con los irregulares: bon → meilleur (adj), bien → mieux (adv).",
  objectives=["plus/moins/aussi … que.","Superlativo: le/la plus.","Irregulares: meilleur (adj) vs mieux (adv)."],
  vocab=[
    V("L31-plus","plus … que","más … que","more … than","ply kə","comp","non_cognate","Nice est plus belle que Paris.","emilie",star=True),
    V("L31-moins","moins … que","menos … que","less … than","mwɛ̃ kə","comp","non_cognate","Il fait moins froid ici.","oris",star=True),
    V("L31-aussi","aussi … que","tan … como","as … as","osi kə","comp","non_cognate","Elle est aussi grande que moi.","emilie",star=True),
    V("L31-leplus","le plus / la plus","el/la más","the most","lə ply","comp","non_cognate","C'est la plage la plus jolie.","oris",star=True),
    V("L31-meilleur","meilleur / meilleure","mejor (adjetivo)","better (adj.)","mɛjœʁ","adj","non_cognate","Ce croissant est meilleur.","emilie",star=True),
    V("L31-mieux","mieux","mejor (adverbio)","better (adv.)","mjø","adv","non_cognate","On mange mieux à Nice.","oris",star=True),
    V("L31-lemeilleur","le meilleur","el mejor","the best","lə mɛjœʁ","adj","non_cognate","C'est le meilleur glacier.","emilie",star=True),
    V("L31-plusgrand","plus grand","más grande","bigger","ply ɡʁɑ̃","comp","non_cognate","Paris est plus grand que Nice.","oris"),
    V("L31-moinscher","moins cher","más barato","cheaper","mwɛ̃ ʃɛʁ","comp","non_cognate","C'est moins cher au marché.","emilie"),
  ],
  sentences=[
    S("L31-s01","Nice est plus belle que Paris, promis !","¡Niza es más bella que París, lo prometo!","Nice is more beautiful than Paris, I promise!","emilie"),
    S("L31-s02","La socca, c'est meilleur que la pizza !","¡La socca es mejor que la pizza!","Socca is better than pizza!","oris"),
    S("L31-s03","On mange mieux ici qu'à Paris.","Se come mejor aquí que en París.","The food's better here than in Paris.","emilie",gloss="mieux = mejor (adverbio, con un verbo)"),
    S("L31-s04","C'est le meilleur glacier de la ville.","Es la mejor heladería de la ciudad.","It's the best ice cream shop in town.","oris"),
  ],
  drills=[
    D("« más … que » = ___ … que","comparatif :","plus",["plus","moins","aussi","très"]),
    D("« tan … como » = ___ … que","comparatif d'égalité :","aussi",["aussi","plus","moins","tant"]),
    D("Irrégulier : « bon » au comparatif =","(pas « plus bon ») :","meilleur",["meilleur","plus bon","mieux","bien"]),
    D("« se come mejor » (avec un verbe) → « on mange ___ »","adverbe :","mieux",["mieux","meilleur","plus bon","bon"]),
    D("« el mejor helado » → « le ___ glacier »","superlatif :","meilleur",["meilleur","mieux","plus bon","meilleure"]),
    D("« menos caro » → « ___ cher »","le bon mot :","moins",["moins","plus","aussi","très"]),
  ])

# ---------------- L32 Mon, ce ----------------
LESS["L32"]=dict(order=32,slug="possessifs",title="Mon, ce…",es_title="Posesivos y demostrativos (mi, este)",
  focus="Posesivos: mon/ma/mes (mi/mis). Concuerdan con el GÉNERO DE LA COSA, no del dueño (« son sac » = su bolso, de él o de ella) — igual que « su ». Demostrativos: ce/cette/ces (este/esta/estos), ¡sin drama este/ese/aquel!",
  objectives=["mon/ma/mes, ton/ta/tes, son/sa/ses.","son/sa concuerdan con el objeto, no con el dueño (como « su »).","Antes de vocal femenina: mon amie. Demostrativos ce/cette/ces."],
  vocab=[
    V("L32-mon","mon / ma / mes","mi / mis","my","mɔ̃","poss","non_cognate","C'est mon sac.","emilie",star=True),
    V("L32-ton","ton / ta / tes","tu / tus","your","tɔ̃","poss","non_cognate","Où est ton téléphone ?","oris",star=True),
    V("L32-son","son / sa / ses","su / sus","his / her","sɔ̃","poss","non_cognate","C'est son sac.","emilie",star=True),
    V("L32-notre","notre / nos","nuestro / nuestros","our","nɔtʁ","poss","transparent","C'est notre hôtel.","oris"),
    V("L32-votre","votre / vos","su / vuestro","your (pl.)","vɔtʁ","poss","non_cognate","Voici votre chambre.","emilie"),
    V("L32-monamie","mon amie","mi amiga","my friend (f.)","mɔ̃ n‿ami","poss","non_cognate","Mon amie Chloé.","oris",star=True),
    V("L32-ce","ce / cet","este","this / that (m.)","sə","dem","non_cognate","Ce garçon, cet ami.","emilie",star=True),
    V("L32-cette","cette","esta","this / that (f.)","sɛt","dem","non_cognate","Cette plage est belle.","oris",star=True),
    V("L32-ces","ces","estos / estas","these / those","se","dem","non_cognate","Ces glaces sont énormes.","emilie",star=True),
  ],
  sentences=[
    S("L32-s01","C'est mon sac, pas ton sac !","¡Es mi bolso, no tu bolso!","This is my bag, not your bag!","emilie"),
    S("L32-s02","Son frère et sa sœur habitent à Nice.","Su hermano y su hermana viven en Niza.","His/her brother and sister live in Nice.","oris",gloss="son/sa = del objeto, no del dueño"),
    S("L32-s03","Cette plage est ma préférée.","Esta playa es mi preferida.","This beach is my favorite.","emilie"),
    S("L32-s04","Regarde ces glaces, elles sont énormes !","¡Mira estos helados, son enormes!","Look at these ice creams, they're huge!","oris"),
  ],
  drills=[
    D("« mi maleta » (valise = fém.) → « ___ valise »","accord avec l'objet :","ma",["ma","mon","mes","ta"]),
    D("Piège : « mi amiga » (fém. + voyelle) → « ___ amie »","devant une voyelle :","mon",["mon","ma","mes","une"]),
    D("« su coche » (de él o de ella) → « ___ voiture »","voiture = fém., neutre au propriétaire :","sa",["sa","son","ses","leur"]),
    D("« esta playa » → « ___ plage »","démonstratif fém. :","cette",["cette","ce","cet","ces"]),
    D("« este chico » → « ___ garçon »","démonstratif masc. :","ce",["ce","cette","cet","ces"]),
    D("« estos helados » → « ___ glaces »","(pas « ses ») :","ces",["ces","ses","cette","ce"]),
  ])

# ---------------- L33 L'impératif ----------------
LESS["L33"]=dict(order=33,slug="imperatif",title="L'impératif",es_title="Dar órdenes (Regarde ! Allons-y !)",
  focus="Dar órdenes y sugerencias. Se cae el sujeto, como en español (« mira » → « regarde »). Con pronombre: « donne-moi » = « dame ». « Allons-y ! » = « ¡vámonos! ». Negativo: « ne bouge pas ! ».",
  objectives=["Imperativo tú/usted/nosotros (regarde / regardez / allons-y).","Pronombre después en afirmativo: donne-moi (como « dame »).","Imperativo negativo: ne bouge pas."],
  vocab=[
    V("L33-regarde","Regarde !","¡Mira!","Look!","ʁəɡaʁd","imper","non_cognate","Regarde la mer !","emilie",star=True),
    V("L33-ecoute","Écoute !","¡Escucha!","Listen!","ekut","imper","non_cognate","Écoute ça !","oris",star=True),
    V("L33-viens","Viens !","¡Ven!","Come!","vjɛ̃","imper","non_cognate","Viens avec moi !","emilie",star=True),
    V("L33-attends","Attends !","¡Espera!","Wait!","atɑ̃","imper","semi","Attends une seconde !","oris",star=True),
    V("L33-allonsy","Allons-y !","¡Vámonos!","Let's go!","alɔ̃zi","imper","non_cognate","Allons-y, on est en retard !","emilie",star=True),
    V("L33-vasy","Vas-y !","¡Dale! / ¡Ve!","Go on!","vazi","imper","non_cognate","Vas-y, n'aie pas peur !","oris",star=True),
    V("L33-donnemoi","Donne-moi…","Dame…","Give me…","dɔn mwa","imper","non_cognate","Donne-moi ton insta.","emilie",star=True),
    V("L33-dismoi","Dis-moi","Dime","Tell me","di mwa","imper","non_cognate","Dis-moi la vérité.","oris",star=True),
    V("L33-nebougepas","Ne bouge pas !","¡No te muevas!","Don't move!","nə buʒ pa","imper","non_cognate","Ne bouge pas, je prends une photo !","emilie",star=True),
    V("L33-regardez","Regardez ! (vous)","¡Miren! / ¡Mire!","Look! (formal/pl.)","ʁəɡaʁde","imper","non_cognate","Regardez ici, s'il vous plaît.","oris"),
  ],
  sentences=[
    S("L33-s01","Regarde la mer, elle est magnifique !","¡Mira el mar, está magnífico!","Look at the sea, it's magnificent!","emilie"),
    S("L33-s02","Allons-y ! On va rater le bus.","¡Vámonos! Vamos a perder el bus.","Let's go! We're going to miss the bus.","oris"),
    S("L33-s03","Donne-moi ton numéro, je t'appelle.","Dame tu número, te llamo.","Give me your number, I'll call you.","emilie",gloss="pronombre DESPUÉS en afirmativo: donne-moi = dame"),
    S("L33-s04","Ne bouge pas, je prends une photo !","¡No te muevas, saco una foto!","Don't move, I'm taking a photo!","oris"),
  ],
  drills=[
    D("« ¡Mira! » (à un ami) =","impératif tu (verbe -er, pas de -s) :","Regarde !",["Regarde !","Regardes !","Regarder !","Regardez !"]),
    D("« ¡Vámonos! » =","impératif « nous » :","Allons-y !",["Allons-y !","Allez !","On va","Vas-y !"]),
    D("« Dame tu insta » → « ___ ton insta »","pronom après, moi (pas me) :","Donne-moi",["Donne-moi","Me donne","Donnes-moi","Moi donne"]),
    D("« ¡No te muevas! » =","impératif négatif :","Ne bouge pas !",["Ne bouge pas !","Ne pas bouge !","Bouge pas non !","No bouge pas !"]),
    D("« ¡Escucha! » =","impératif tu :","Écoute !",["Écoute !","Écoutes !","Écouter !","Écoutez !"]),
    D("« Dime la verdad » → « ___ la vérité »","le bon mot :","Dis-moi",["Dis-moi","Me dis","Dis-me","Moi dis"]),
  ])

# ---------------- assemble & write ----------------
FN={"L27":"lesson_27_questions.json","L28":"lesson_28_negation.json","L29":"lesson_29_quotidien.json",
    "L30":"lesson_30_pronoms.json","L31":"lesson_31_comparer.json","L32":"lesson_32_possessifs.json",
    "L33":"lesson_33_imperatif.json"}
base=os.path.join(os.path.dirname(__file__),"..","data","curriculum")
for lid,meta in LESS.items():
    obj={"id":lid,"order":meta["order"],"slug":meta["slug"],"title":meta["title"],"es_title":meta["es_title"],
         "focus":meta["focus"],"objectives":meta["objectives"],"reader":READERS[lid],
         "vocab":meta["vocab"],"sentences":meta["sentences"],"drills":meta["drills"]}
    json.dump(obj,open(os.path.join(base,FN[lid]),"w"),ensure_ascii=False,indent=2)
    print("wrote",FN[lid],"| vocab",len(meta["vocab"]),"sent",len(meta["sentences"]),"drills",len(meta["drills"]))
print("done")
