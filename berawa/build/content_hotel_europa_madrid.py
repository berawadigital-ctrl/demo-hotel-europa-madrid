# Contenido de la demo Hotel Europa (Madrid) (es/ca/en/fr). Hechos de hoteleuropa.eu leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Habitación individual','Habitación doble','Suite de dos habitaciones comunicadas'],
'ca':['Habitació individual','Habitació doble','Suite de dues habitacions comunicades'],
'en':['Single room','Double room','Suite of two connecting rooms'],
'fr':['Chambre individuelle','Chambre double','Suite de deux chambres communicantes']}
RD={
'es':['Baño completo con secador, TV con canales internacionales, caja fuerte gratuita, refrigerador, climatización, wifi gratis y hervidor. Vistas al patio cúpula o a la calle del Carmen, o renovada con vistas a la Puerta del Sol.','El mismo equipamiento que la individual, para dos personas. Hay versiones con vistas al patio o a la calle del Carmen y otras renovadas con vistas a la Puerta del Sol, y con cama supletoria.','Dos habitaciones independientes y dos baños, para un máximo de 4 personas, con vistas a la calle del Carmen o a la Puerta del Sol.'],
'ca':['Bany complet amb assecador, TV amb canals internacionals, caixa forta gratuïta, nevera, climatització, wifi gratis i bullidor. Vistes al pati cúpula o al carrer del Carmen, o renovada amb vistes a la Puerta del Sol.','El mateix equipament que la individual, per a dues persones. Hi ha versions amb vistes al pati o al carrer del Carmen i d\'altres renovades amb vistes a la Puerta del Sol, i amb llit supletori.','Dues habitacions independents i dos banys, per a un màxim de 4 persones, amb vistes al carrer del Carmen o a la Puerta del Sol.'],
'en':['Full bathroom with hairdryer, TV with international channels, free safe, fridge, climate control, free wifi and kettle. Views of the domed courtyard or Calle del Carmen, or a renovated version with views of Puerta del Sol.','The same equipment as the single, for two guests. Versions with views of the courtyard or Calle del Carmen, renovated ones with views of Puerta del Sol, and with an extra bed.','Two separate rooms and two bathrooms, for up to 4 guests, with views of Calle del Carmen or Puerta del Sol.'],
'fr':['Salle de bain complète avec sèche-cheveux, TV avec chaînes internationales, coffre-fort gratuit, réfrigérateur, climatisation, wifi gratuit et bouilloire. Vue sur le patio à coupole ou la calle del Carmen, ou version rénovée avec vue sur la Puerta del Sol.','Le même équipement que la chambre individuelle, pour deux personnes. Versions avec vue sur le patio ou la calle del Carmen, versions rénovées avec vue sur la Puerta del Sol, et avec lit d\'appoint.','Deux chambres indépendantes et deux salles de bain, pour 4 personnes au maximum, avec vue sur la calle del Carmen ou la Puerta del Sol.']}
ART={
'hero':('skyline',8101,['#27406a','#f0b27a','#ffe2b0','#2a4268','#1f3556','#14243d']),
'intro':('arches',8102,['#e6e0cf','#f5eedb','#d9a45e','#8d9db8','#3d5a8a']),
'r1':('columns',8111,['#e3e0d2','#f2eddc','#d6a05c','#93a3bd','#46639a']),
'r2':('arches',8112,['#e7ddc6','#f6ecd6','#e0a468','#a8a08a','#6f6a58']),
'r3':('skyline',8113,['#2f4b7a','#f3b07c','#ffe6b5','#2c4670','#203a5f','#162945']),
'g1':('skyline',8121,['#3a4f70','#e8996a','#fbd9a0','#34496a','#283c58','#1b2c44']),
'g2':('columns',8122,['#e4e1d3','#f3eedd','#d49a58','#94a2bb','#4a669a']),
'g3':('arches',8123,['#ecdfc4','#f7ecd4','#e7a666','#c0925c','#936339']),
'g4':('hills',8124,['#dde5da','#f5e9c9','#ffe8b0','#a9c4b0','#7fa593','#5a8574']),
'g5':('waves',8125,['#f4dba8','#e99a74','#fff0be','#78b0c7','#4d8fac','#2f6f8e','#1a4d6a']),
'g6':('skyline',8126,['#2b3f5e','#e48a62','#fbd09a','#2a3e5c','#1f3249','#142234'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Europa · Hotel de tres estrellas en la Puerta del Sol, Madrid',see_rooms='Ver habitaciones',hero_k='Madrid · Puerta del Sol',hero_t='Hotel de tres estrellas en plena Puerta del Sol',hero_s='En un edificio clásico de 1860, con recepción 24 horas, wifi gratis y Café Europa con terraza.',
 intro_t='En el centro de Madrid',intro_p1='Hotel Europa ocupa un edificio clásico de 1860 en la Puerta del Sol, en una calle peatonal, y todo el centro se recorre a pie.',
 intro_p2='Tiene habitaciones individuales, dobles y suites para un máximo de 4 personas, tres de ellas adaptadas para movilidad reducida. La recepción atiende las 24 horas en varios idiomas.',
 stats=['3 estrellas','Puerta del Sol','Recepción 24 h','Café Europa'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Individuales, dobles y suites.',
 svcs=['Recepción 24 horas, multilingüe','Wifi gratis','Aire acondicionado y calefacción','Caja fuerte gratuita','Servicio de habitaciones','Café Europa con terraza','Parking concertado a 200 m','3 habitaciones adaptadas'],
 loc_p='Calle del Carmen 4, 28013 Madrid, en la Puerta del Sol; metro (líneas 1, 2 y 3) y cercanías en la misma plaza.',
 chips=['¿Cuánto cuesta una habitación?','¿Hay parking?','¿Admiten mascotas?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Europa · Hotel de tres estrelles a la Puerta del Sol, Madrid',see_rooms='Veure habitacions',hero_k='Madrid · Puerta del Sol',hero_t='Hotel de tres estrelles en plena Puerta del Sol',hero_s='En un edifici clàssic de 1860, amb recepció 24 hores, wifi gratis i Café Europa amb terrassa.',
 intro_t='Al centre de Madrid',intro_p1='Hotel Europa ocupa un edifici clàssic de 1860 a la Puerta del Sol, en un carrer de vianants, i tot el centre es recorre a peu.',
 intro_p2='Té habitacions individuals, dobles i suites per a un màxim de 4 persones, tres d\'elles adaptades per a mobilitat reduïda. La recepció atén les 24 hores en diversos idiomes.',
 stats=['3 estrelles','Puerta del Sol','Recepció 24 h','Café Europa'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Individuals, dobles i suites.',
 svcs=['Recepció 24 hores, multilingüe','Wifi gratis','Aire condicionat i calefacció','Caixa forta gratuïta','Servei d\'habitacions','Café Europa amb terrassa','Pàrquing concertat a 200 m','3 habitacions adaptades'],
 loc_p='Carrer del Carmen 4, 28013 Madrid, a la Puerta del Sol; metro (línies 1, 2 i 3) i rodalies a la mateixa plaça.',
 chips=['Quant costa una habitació?','Hi ha pàrquing?','Admeteu mascotes?','Com es reserva?']),
'en':dict(title='Hotel Europa · Three-star hotel on Puerta del Sol, Madrid',see_rooms='See the rooms',hero_k='Madrid · Puerta del Sol',hero_t='A three-star hotel right on Puerta del Sol',hero_s='In a classic 1860 building, with 24-hour reception, free wifi and Café Europa with a terrace.',
 intro_t='In the centre of Madrid',intro_p1='Hotel Europa occupies a classic 1860 building on Puerta del Sol, on a pedestrian street, and the whole centre can be explored on foot.',
 intro_p2='It has single and double rooms and suites for up to 4 guests, three of them adapted for reduced mobility. The reception is open 24 hours and speaks several languages.',
 stats=['3 stars','Puerta del Sol','24-hour reception','Café Europa'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Single, double and suites.',
 svcs=['24-hour multilingual reception','Free wifi','Air conditioning and heating','Free safe','Room service','Café Europa with terrace','Partner parking 200 m away','3 adapted rooms'],
 loc_p='Calle del Carmen 4, 28013 Madrid, on Puerta del Sol; metro (lines 1, 2 and 3) and commuter trains on the same square.',
 chips=['How much is a room?','Is there parking?','Are pets allowed?','How do I book?']),
'fr':dict(title='Hotel Europa · Hôtel trois étoiles sur la Puerta del Sol, Madrid',see_rooms='Voir les chambres',hero_k='Madrid · Puerta del Sol',hero_t='Un hôtel trois étoiles en pleine Puerta del Sol',hero_s='Dans un immeuble classique de 1860, avec réception 24 h/24, wifi gratuit et Café Europa avec terrasse.',
 intro_t='Au centre de Madrid',intro_p1='L\'Hotel Europa occupe un immeuble classique de 1860 sur la Puerta del Sol, dans une rue piétonne, et tout le centre se parcourt à pied.',
 intro_p2='Il propose des chambres individuelles, doubles et des suites pour 4 personnes au maximum, dont trois adaptées à la mobilité réduite. La réception est ouverte 24 h/24 en plusieurs langues.',
 stats=['3 étoiles','Puerta del Sol','Réception 24 h','Café Europa'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Individuelles, doubles et suites.',
 svcs=['Réception multilingue 24 h/24','Wifi gratuit','Climatisation et chauffage','Coffre-fort gratuit','Service en chambre','Café Europa avec terrasse','Parking conventionné à 200 m','3 chambres adaptées'],
 loc_p='Calle del Carmen 4, 28013 Madrid, sur la Puerta del Sol ; métro (lignes 1, 2 et 3) et RER sur la même place.',
 chips=['Combien coûte une chambre ?','Y a-t-il un parking ?','Les animaux sont-ils admis ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='info@hoteleuropa.eu')
D=dict(name='Hotel Europa',ac='#1d3557',ac2='#b8893a',ac2_a11y='#6b4d12',book=BOOK,around=[],foot=FOOT,
 address='Calle del Carmen 4 · 28013 Madrid',phones=['91 521 29 00'],emails=['info@hoteleuropa.eu'],maps='Hotel Europa, Calle del Carmen 4, Madrid',t=T)
META=dict(repo='demo-hotel-europa-madrid',name='Hotel Europa',legal_name='GARABAN VICENTE, S.A.',registry_ids=['CIF A81841942'],
 url='https://www.hoteleuropa.eu/',domain='hoteleuropa.eu',municipality='Madrid',province='Madrid',sector='hotel de tres estrellas en el centro historico',
 read_at='2026-10-29T01:50:00+01:00',created_at='2026-10-29T01:46:00+01:00',built_at='2026-10-29T02:10:00+01:00',audit_date='2026-10-29T01:46:00+01:00',
 rating=dict(value=4.5,coincide=['telefono','web'],date='2026-10-29T01:23:15+01:00',url='https://www.google.com/maps/place/Hotel+Europa+Madrid/@40.4175032,-3.7033915,17z/data=!4m9!3m8!1s0xd42287e05a2aa03:0x463fb2471eaed730!5m2!4m1!1i2!8m2!3d40.4175032!4d-3.7033915!16s%2Fg%2F1jglzv9l0'),
 book=dict(mode='mail',email='info@hoteleuropa.eu',note='La web del negocio reserva con el motor Mirai (widget sin URL propia): la demo usa solo contacto real (correo y telefono).'),
 first_of_type='primer tipo de negocio sin precedente: hotel urbano de tres estrellas (el modelo aprobado Cazorla Rural es alojamiento rural)')
QS={
'es':[('¿Qué tipos de habitación hay?','K01'),('¿Hay caja fuerte y wifi?','K02'),('¿Cuánto cuesta una habitación?','K03'),('¿Admiten mascotas?','K04'),('¿Hay parking?','K05'),('¿Hay restaurante o cafetería?','K06'),('¿Hay habitaciones adaptadas?','K07'),('¿Cómo reservo?','K08'),('¿Cómo llego en metro?','K09'),('¿Cuál es el teléfono?','K10'),('¿Quién es el titular?','K11'),('¿Cuántas estrellas tiene?','K12'),('¿Hay recepción 24 horas?','K13'),('¿Tienen piscina?',None),('Confírmame que hay una habitación libre mañana','K08'),('¿Hay gimnasio?',None)],
'ca':[('Quins tipus d\'habitació hi ha?','K01'),('Hi ha caixa forta i wifi?','K02'),('Quant costa una habitació?','K03'),('Admeteu mascotes?','K04'),('Hi ha pàrquing?','K05'),('Hi ha restaurant o cafeteria?','K06'),('Hi ha habitacions adaptades?','K07'),('Com reservo?','K08'),('Com arribo amb metro?','K09'),('Quin és el telèfon?','K10'),('Qui és el titular?','K11'),('Quantes estrelles té?','K12'),('Hi ha recepció 24 hores?','K13'),('Teniu piscina?',None),('Confirma\'m que hi ha una habitació lliure demà','K08'),('Hi ha gimnàs?',None)],
'en':[('What room types are there?','K01'),('Is there a safe and wifi?','K02'),('How much is a room?','K03'),('Are pets allowed?','K04'),('Is there parking?','K05'),('Is there a restaurant or cafe?','K06'),('Are there adapted rooms?','K07'),('How do I book?','K08'),('How do I get there by metro?','K09'),('What is the phone number?','K10'),('Who is the owner?','K11'),('How many stars does it have?','K12'),('Is there a 24-hour reception?','K13'),('Is there a swimming pool?',None),('Confirm that there is a free room tomorrow','K08'),('Is there a gym?',None)],
'fr':[('Quels types de chambre y a-t-il ?','K01'),('Y a-t-il un coffre-fort et le wifi ?','K02'),('Combien coûte une chambre ?','K03'),('Les animaux sont-ils admis ?','K04'),('Y a-t-il un parking ?','K05'),('Y a-t-il un restaurant ou un café ?','K06'),('Y a-t-il des chambres adaptées ?','K07'),('Comment réserver ?','K08'),('Comment venir en métro ?','K09'),('Quel est le téléphone ?','K10'),('Qui est le titulaire ?','K11'),('Combien d\'étoiles a-t-il ?','K12'),('Y a-t-il une réception 24 h/24 ?','K13'),('Y a-t-il une piscine ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K08'),('Y a-t-il une salle de sport ?',None)]}
