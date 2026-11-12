# Páginas en español (ejecutado por build.py con L = 'es')
# Traducción fiel de la versión francesa: no añadir datos que no estén en el francés.

def migas(nombre, clave):
    return [{'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Inicio', 'item': SITE['url'] + u('accueil')},
        {'@type': 'ListItem', 'position': 2, 'name': nombre, 'item': SITE['url'] + u(clave)}]}]

# ---------- INICIO ----------
pages.append(page(u('accueil'),
 'Danza y yoga en Saint-Joseph, La Reunión | Danzarina',
 'Clases de danza y de yoga, talleres, sesiones personalizadas y experiencias para hoteles en Saint-Joseph y el sur de La Reunión.',
f'''<section class="hero-t" aria-labelledby="h1-accueil">
<figure class="hero-t__media">{picture('accueil-julieta-voile-terracotta', 'Julieta en equilibrio sobre una pierna, con el brazo en alto, sosteniendo un velo terracota y oliva; a su lado se despliega una gran tela de seda terracota.', '100vw', eager=True, mobile=('accueil-julieta-voile-terracotta-4x5', '(max-width: 47.99rem)'))}<figcaption>Imagen artística</figcaption></figure>
<div class="wrap hero-t__grille"><div class="hero-t__texte">
<h1 id="h1-accueil"><span class="hero-t__l1">Danza y Yoga</span></h1>
<p class="lead">Clases de danza y de yoga, talleres y sesiones personalizadas. Un ritmo armonioso entre danza y yoga, para habitar el cuerpo con elegancia y fluidez.</p>
<div class="actions"><a class="btn btn--clair" href="{u('yoga')}">Descubrir el yoga</a><a class="btn btn--ligne" href="{u('danse')}">Descubrir la danza</a></div>
</div></div></section>''',
 f'''<section class="manifeste" aria-label="Nuestra intención"><div class="wrap">
<p class="manifeste__mots"><span>Respirar</span> <span>Recentrarse</span> <span>Conectar</span></p>
<p class="manifeste__texte">Propuestas para todas las edades y todos los niveles, respetando el ritmo de cada persona.</p>
</div></section>

<section class="section section--sable" aria-labelledby="offre-titre"><div class="wrap">
<div class="entete-section"><p class="eyebrow">Lo que ofrecemos</p><h2 id="offre-titre">Moverse, respirar, conectar</h2></div>
<ol class="offres">
<li class="offre"><span class="offre__num" aria-hidden="true">01</span><h3>Danza</h3><p>Tango, salsa y danza para niños: bailar por el placer del movimiento y del encuentro.</p><a class="lien-fleche" href="{u('danse')}">Las clases de danza</a></li>
<li class="offre"><span class="offre__num" aria-hidden="true">02</span><h3>Yoga</h3><p>El Shantyoga, un yoga que se ajusta a cada alumno y pone el acento en las alineaciones.</p><a class="lien-fleche" href="{u('yoga')}">Las clases de yoga</a></li>
<li class="offre"><span class="offre__num" aria-hidden="true">03</span><h3>Clases personalizadas</h3><p>Una sesión construida en torno a tu objetivo, a tu ritmo.</p><a class="lien-fleche" href="{u('perso')}">Cómo funciona</a></li>
</ol>
</div></section>

<section class="section section--olive" aria-labelledby="plage-titre"><div class="wrap duo">
<div>
<p class="eyebrow">Cita de la semana</p>
<h2 id="plage-titre">Yoga en la playa, el martes por la mañana</h2>
<p class="lead">El Shantyoga se ajusta a cada alumno y pone mucho el acento en las alineaciones: escucha del cuerpo, respiración, alineación, presencia y bienestar.</p>
<a class="lien-fleche" href="{u('yoga')}">Todo sobre el yoga</a>
</div>
{yoga_plage()}
</div></section>

<figure class="bandeau bandeau--x">
{picture('danse-canape-ciel-2x1', 'Un bailarín sostiene a una bailarina en extensión sobre un sofá antiguo colocado en un prado, delante de una bala de paja y de montañas al atardecer.', '100vw', mobile=('danse-canape-ciel-4x5', '(max-width: 35.99rem)'))}
<figcaption class="bandeau__phrase">«El cuerpo abre un espacio»</figcaption>
</figure>

<section class="section" aria-labelledby="parcours-titre"><div class="wrap duo duo--inverse">
<figure class="cadre-decale">{picture('parcours-noir-et-blanc', 'Foto en blanco y negro: una bailarina de pie sobre un sofá antiguo en un campo, un hombre sentado a su lado, montañas al fondo.', '(min-width: 56rem) 50vw, 100vw')}<figcaption>Archivo Danzarina.</figcaption></figure>
<div>
<p class="eyebrow">Un recorrido en movimiento</p>
<h2 id="parcours-titre">Una vida bailando, transmitiendo</h2>
<p>Danzarina nace del recorrido de Julieta, artista del movimiento de origen argentino: más de 20 años de formación en ballet, jazz, danza contemporánea, tango, folklore argentino, salsa, zouk y kizomba. Hoy une la danza y el yoga en su propio sistema de enseñanza.</p>
<p>Hoy, Danzarina continúa su camino en La Reunión.</p>
<a class="lien-fleche" href="{u('apropos')}">Descubrir nuestra historia</a>
</div>
</div></section>

<section class="section section--sable" aria-label="Para ir más allá"><div class="wrap tuiles">
<article class="tuile tuile--terre"><p class="eyebrow">Profesionales</p><h2 class="tuile__titre">Hoteles y colaboradores</h2><p>Sesiones de danza o de yoga en tu establecimiento, adaptadas a tu espacio y a tus huéspedes.</p><a class="btn btn--clair" href="{u('hotels')}">Hablar de tu proyecto</a></article>
<article class="tuile tuile--olive"><p class="eyebrow">Citas puntuales</p><h2 class="tuile__titre">Talleres</h2><p>Talleres para profundizar en una práctica. Las próximas fechas se anunciarán aquí y en Instagram.</p><a class="btn btn--clair" href="{u('ateliers')}">Ver los talleres</a></article>
</div></section>
{contact_cta(sur_sable=True)}''',
 schema=[{'@context': 'https://schema.org', '@type': 'WebSite', 'name': 'Danzarina', 'url': SITE['url'] + u('accueil'), 'inLanguage': 'es'}]))

# ---------- DANZA ----------
pages.append(page(u('danse'),
 'Clases de danza en Saint-Joseph, La Reunión: tango, salsa, niños | Danzarina',
 'Clases de danza con Danzarina en el sur de La Reunión: tango y salsa para adultos, danza para niños. Una práctica a tu ritmo, sin presión.',
 titre('Danza', 'Clases de danza', 'Bailar por el placer del movimiento, de la música y del encuentro, a tu ritmo y sin espíritu de competición.'),
 f'''<section class="section" style="padding-top:0"><div class="wrap">
{picture('hero-danse-a-deux-16x9', 'Una pareja baila en un prado, con camisetas naranjas, al sol del final del día.', '(min-width: 72rem) 68rem, 100vw', cls='', mobile=('hero-danse-a-deux-4x5', '(max-width: 35.99rem)'))}
</div></section>
<section class="section" style="padding-top:0" aria-labelledby="styles-titre"><div class="wrap">
<h2 id="styles-titre">Las danzas que ofrecemos</h2>
<div class="grille grille--3">
<article class="carte"><h3>Tango</h3><p>Para adultos. Una danza de escucha y conexión, en la que se aprende a caminar juntos.</p></article>
<article class="carte"><h3>Salsa</h3><p>Para adultos. Una danza alegre y rítmica, para soltarse y compartir.</p></article>
<article class="carte"><h3>Danza para niños</h3><p>Despertar y descubrimiento del movimiento, la música y la expresión.</p></article>
</div>
</div></section>
{vague()}
<section class="section section--sable" aria-labelledby="methode-titre"><div class="wrap duo">
<div>
<h2 id="methode-titre">Nuestra forma de enseñar</h2>
<ul class="liste-points">
<li>Abierto a todo el mundo, principiantes y practicantes.</li>
<li>Cada cual avanza a su ritmo: no hay rendimiento que alcanzar.</li>
<li>Solo o en pareja: no hace falta venir con pareja.</li>
<li>Atención a la escucha del cuerpo y a la conexión.</li>
</ul>
<h3 id="horaires">Horarios, lugares y tarifas</h3>
<p>Los horarios y lugares de las clases de danza de la nueva temporada se publicarán aquí próximamente. Mientras tanto, <a href="{u('contact')}">contáctanos</a> para estar al tanto.</p>
</div>
<figure>{picture('danse-fleurs-violettes', 'Dos bailarines frente a frente en plena figura de baile en pareja, entre flores violetas, bajo un cielo azul.', '(min-width: 56rem) 50vw, 100vw')}</figure>
</div></section>
{vague(' vague--haut')}
<section class="section" aria-labelledby="galerie-titre"><div class="wrap">
<h2 id="galerie-titre">En movimiento</h2>
<ul class="galerie">
<li>{picture('danse-canape-paysage', 'Un bailarín sostiene a una bailarina en extensión sobre un sofá antiguo colocado en la hierba, con montañas al fondo.', '(min-width: 60rem) 33vw, 100vw')}</li>
<li>{picture('mouvement-sous-le-ciel-4x5', 'Dos bailarines en pleno impulso en un campo, bajo un cielo nublado.', '(min-width: 60rem) 33vw, 100vw')}</li>
<li>{picture('parcours-noir-et-blanc', 'Foto en blanco y negro de dos bailarines junto a un sofá antiguo en un campo.', '(min-width: 60rem) 33vw, 100vw')}</li>
</ul>
</div></section>
{contact_cta('¿Ganas de bailar?', 'Cuéntanos qué te atrae y te orientamos hacia la propuesta que te corresponde.')}''',
 schema=migas('Danza', 'danse')))

# ---------- YOGA ----------
pages.append(page(u('yoga'),
 'Clases de yoga en Saint-Joseph: Shantyoga en la playa de Grand Anse | Danzarina',
 'Clases de Shantyoga en Saint-Joseph, La Reunión: yoga en la playa de Grand Anse los martes de 9:30 a 11:00. Un yoga que se ajusta a cada alumno.',
 titre('Yoga', 'Clases de yoga en Saint-Joseph', 'El Shantyoga: un estilo de yoga que se ajusta a cada alumno y que pone mucho el acento en las alineaciones.'),
 f'''<section class="section" style="padding-top:0"><div class="wrap duo">
<div>
<h2>Nuestro enfoque</h2>
<p>Cada sesión deja tiempo para llegar, respirar y escuchar el cuerpo. Las posturas se adaptan a cada persona: lo importante no es ir lejos, sino estar en el lugar justo.</p>
<ul class="liste-points">
<li>Escucha del cuerpo</li><li>Respiración</li><li>Alineación</li><li>Presencia</li><li>Bienestar</li>
</ul>
</div>
{yoga_plage()}
</div></section>
<figure class="bandeau bandeau--doux">{picture('ambiance-yoga-tapis', '', '100vw')}</figure>
{vague()}
<section class="section section--sable" aria-labelledby="pratique-titre"><div class="wrap">
<h2 id="pratique-titre">Información práctica</h2>
<div class="grille grille--3">
<article class="carte"><h3>Nivel</h3><p>Abierto a todo el mundo, sea cual sea tu edad o tu nivel.</p></article>
<article class="carte"><h3>Material</h3><p>Ropa cómoda. Para la esterilla y lo demás, <a href="{u('contact')}">pregúntanos</a> antes de tu primera sesión.</p></article>
<article class="carte"><h3>Salud</h3><p>El yoga no sustituye una opinión médica. En caso de embarazo, lesión o problema de salud, consúltalo con tu médico y avísanos antes de la sesión.</p></article>
</div>
</div></section>
{vague(' vague--haut')}
<section class="section" aria-labelledby="enseignante-titre"><div class="wrap">
<h2 id="enseignante-titre">La profesora</h2>
<p>Julieta tiene la certificación de Shantyoga de 200 horas (2019, formación reconocida por Yoga Alliance) y se está formando en yoga Iyengar.</p>
<a class="lien-fleche" href="{u('apropos')}">Más sobre Julieta</a>
</div></section>
{contact_cta('¿Quieres probar?', 'Escríbenos para conocer las próximas sesiones y reservar tu plaza.')}''',
 schema=migas('Yoga', 'yoga')))

# ---------- CLASES PERSONALIZADAS ----------
pages.append(page(u('perso'),
 'Clases particulares de danza y de yoga en Saint-Joseph | Danzarina',
 'Sesiones personalizadas de danza o de yoga en el sur de La Reunión: un intercambio, un objetivo, un formato adaptado y un seguimiento.',
 titre('Clases personalizadas', 'Clases personalizadas de danza y de yoga', 'Una sesión pensada para ti: solo/a, en pareja o en grupo pequeño, en torno a un objetivo que se te parezca.'),
 f'''<section class="section" style="padding-top:0" aria-labelledby="etapes-titre"><div class="wrap">
<h2 id="etapes-titre">Cómo funciona</h2>
<ol class="etapes">
<li><h3>Un primer intercambio</h3><p>Nos hablas de ti, de lo que quieres y de tus posibles limitaciones.</p></li>
<li><h3>Tu objetivo</h3><p>Abrir el baile de una boda, retomar el movimiento, profundizar en una práctica…</p></li>
<li><h3>Una propuesta</h3><p>Te proponemos un formato: duración, número de sesiones, danza o yoga.</p></li>
<li><h3>La sesión</h3><p>Un momento a tu ritmo, centrado en ti.</p></li>
<li><h3>El seguimiento</h3><p>Hacemos balance juntos y ajustamos lo siguiente.</p></li>
</ol>
</div></section>
{vague()}
<section class="section section--sable"><div class="wrap">
<h2>Lugar y modalidades</h2>
<p>Los lugares posibles, las tarifas y las condiciones de desplazamiento se concretan en el primer intercambio.</p>
</div></section>
{contact_cta('Hablemos de tu proyecto', 'Cuéntanos en unas líneas lo que te apetece: te contestamos para hablarlo.', 'Pedir una sesión', sur_sable=True)}'''))

# ---------- TALLERES ----------
pages.append(page(u('ateliers'),
 'Talleres de danza y de yoga en Saint-Joseph, La Reunión | Danzarina',
 'Los talleres de danza y de yoga de Danzarina en el sur de La Reunión: fechas, lugares y reservas.',
 titre('Talleres', 'Talleres de danza y de yoga', 'Citas puntuales para profundizar en una práctica, descubrir una danza o tomarse un tiempo para uno mismo.'),
 f'''<section class="section" style="padding-top:0"><div class="wrap">
<div class="encart">
<h2 style="font-size:1.4rem">Próximos talleres</h2>
<p>No hay ningún taller programado por ahora. Las próximas fechas se anunciarán en esta página y en <a href="{SITE['instagram']}" rel="noopener">Instagram</a>.</p>
<p style="margin:0">¿Quieres que te avisemos? <a href="{u('contact')}">Escríbenos</a>.</p>
</div>
</div></section>
{contact_cta()}'''))

# ---------- HOTELES ----------
pages.append(page(u('hotels'),
 'Danza y yoga para hoteles y alojamientos en La Reunión | Danzarina',
 'Sesiones de yoga y de danza para hoteles, casas rurales y alojamientos del sur de La Reunión: formatos adaptables, intervención in situ, presupuesto según tu proyecto.',
 titre('Hoteles y colaboradores', 'Danza y yoga para hoteles y alojamientos', 'Una propuesta de bienestar y movimiento para tus huéspedes, construida contigo según tu establecimiento.'),
 f'''<section class="section" style="padding-top:0" aria-labelledby="formats-titre"><div class="wrap">
<h2 id="formats-titre">Lo que podemos construir juntos</h2>
<div class="grille grille--2">
<article class="carte"><h3>Formatos adaptables</h3><p>Yoga, danza o iniciación, en sesión puntual o regular, según el ritmo de tu establecimiento.</p></article>
<article class="carte"><h3>Vamos a tu establecimiento</h3><p>Nos desplazamos a tu establecimiento, en interior o en exterior según los espacios disponibles.</p></article>
<article class="carte"><h3>Según tu público</h3><p>Una propuesta pensada según el número de participantes, sus expectativas y el contexto del lugar.</p></article>
<article class="carte"><h3>Un presupuesto claro</h3><p>Tras un primer intercambio, te enviamos una propuesta detallada.</p></article>
</div>
</div></section>
<figure class="bandeau bandeau--doux">{picture('ambiance-frangipanier', '', '100vw')}</figure>
{vague()}
<section class="section section--sable" aria-labelledby="infos-titre"><div class="wrap">
<h2 id="infos-titre">Para preparar tu solicitud</h2>
<ul class="liste-points">
<li>El nombre y la ubicación de tu establecimiento</li>
<li>El tipo de sesión que te interesa (yoga, danza, ambas)</li>
<li>El número de participantes previsto</li>
<li>Los espacios disponibles y las fechas deseadas</li>
</ul>
</div></section>
{contact_cta('Hablar de tu proyecto', 'Preséntanos tu establecimiento y lo que te gustaría: te respondemos enseguida.', 'Hablar de tu proyecto', sur_sable=True)}'''))

# ---------- SOBRE NOSOTROS ----------
pages.append(page(u('apropos'),
 'Sobre Danzarina: Julieta, danza y yoga en La Reunión | Danzarina',
 'La historia de Danzarina y de Julieta, artista del movimiento de origen argentino: danza, Shantyoga y una nueva etapa en La Reunión.',
 titre('Sobre nosotros', 'Sobre Danzarina', 'Un ritmo armonioso entre danza y yoga, para enriquecer la vida con elegancia y fluidez.'),
 f'''<section class="section" style="padding-top:0" aria-labelledby="julieta-titre"><div class="wrap duo">
<figure>{picture('portrait-editorial-julieta', 'Retrato artístico de Julieta caminando descalza por un sendero, con falda larga y velos superpuestos, al atardecer.', '(min-width: 56rem) 50vw, 100vw')}<figcaption>Retrato artístico.</figcaption></figure>
<div>
<p class="eyebrow">La fundadora</p>
<h2 id="julieta-titre">Julieta</h2>
<h3>Su historia</h3>
<p>Artista del movimiento de origen argentino, Julieta lleva más de 20 años formándose en danza. Es bailarina de ballet, jazz, danza contemporánea, tango, folklore argentino, salsa, zouk y kizomba, y se ha especializado en cada uno de estos estilos.</p>
<p>Ha tenido un gran recorrido por la danza y por el mundo, compartiendo sus conocimientos en diferentes ciudades y escuelas de danza de Rusia, España y Francia.</p>
<h3>Su formación</h3>
<ul class="liste-points">
<li>Más de 20 años de formación en danza: ballet, jazz, danza contemporánea, tango, folklore argentino, salsa, zouk y kizomba, entre otras</li>
<li>Formación con artistas y maestros de renombre en Rusia, Argentina (Córdoba, Buenos Aires), España y Francia</li>
<li>Certificación Shantyoga de 200 horas (2019), formación reconocida por Yoga Alliance</li>
<li>Actualmente, formación en cursos de yoga Iyengar</li>
</ul>
<h3>Su camino en el yoga</h3>
<p>Hoy continúa su camino en el yoga y crea su propio sistema de enseñanza, en el que aplica todo lo que ha aprendido en una vida dedicada al movimiento. Enseña danza a niños, tango y salsa a adultos, y yoga.</p>
</div>
</div></section>
{vague()}
<section class="section section--sable" aria-labelledby="parcours-titre"><div class="wrap duo duo--inverse">
<figure>{picture('danse-canape-paysage', 'Un bailarín sostiene a una bailarina en extensión sobre un sofá antiguo colocado en la hierba, con montañas al fondo.', '(min-width: 56rem) 50vw, 100vw')}<figcaption>Archivo Danzarina.</figcaption></figure>
<div>
<p class="eyebrow">Un recorrido en movimiento</p>
<h2 id="parcours-titre">Bailar en pareja</h2>
<p>Julieta comparte la danza con Christian, pedagogo y bailarín, con quien baila tango y salsa. Christian aprendió danza africana con Hamed.</p>
</div>
</div></section>
{vague(' vague--haut')}
<section class="section" aria-labelledby="vision-titre"><div class="wrap">
<p class="eyebrow">La visión de Danzarina</p>
<h2 id="vision-titre">Una tierra, el mismo movimiento</h2>
<p>Sencillez, naturaleza, paz y fraternidad: Danzarina quiere ofrecer un espacio donde cada persona pueda moverse, respirar y conectar, sea cual sea su edad o su nivel. Tras un camino en movimiento, Danzarina continúa hoy su actividad en Saint-Joseph, en el sur de La Reunión.</p>
</div></section>
{contact_cta()}''',
 schema=[{'@context': 'https://schema.org', '@type': 'Person', 'name': 'Julieta', 'jobTitle': 'Profesora de danza y de yoga', 'worksFor': {'@id': SITE['url'] + '/#organisation'}}]))

# ---------- CONTACTO ----------
pages.append(page(u('contact'),
 'Contacto | Danzarina, danza y yoga en Saint-Joseph',
 'Contacta con Danzarina para las clases de danza y de yoga en Saint-Joseph y el sur de La Reunión: teléfono, email, formulario.',
 titre('Contacto', 'Contacto', f'¿Una pregunta sobre las clases, un proyecto para tu establecimiento? Trabajamos en {T("zone")}.'),
 f'''<section class="section" style="padding-top:0"><div class="wrap duo" style="align-items:start">
<div>
<h2>Contactarnos</h2>
<ul class="coord">
<li>Teléfono: <a href="tel:{SITE['tel_lien']}">&nbsp;{SITE['tel_affiche']}</a></li>
<li>Email: <a href="mailto:{SITE['email']}">&nbsp;{SITE['email']}</a></li>
<li>Instagram: <a href="{SITE['instagram']}" rel="noopener">&nbsp;{SITE['instagram_nom']}</a></li>
<li>Facebook: <a href="{SITE['facebook']}" rel="noopener">&nbsp;Danzarina France</a></li>
</ul>
<h2 style="margin-top:2.5rem">Preguntas frecuentes</h2>
<div class="faq">
<details><summary>¿Hace falta haber practicado antes?</summary><p>No. Las clases están abiertas a todo el mundo, sea cual sea el nivel.</p></details>
<details><summary>¿Hace falta venir con pareja para bailar?</summary><p>No, puedes venir solo/a.</p></details>
<details><summary>¿Dónde son las clases de yoga?</summary><p>El yoga en la playa es en Grand Anse, en Saint-Joseph, los martes de 9:30 a 11:00.</p></details>
</div>
</div>
<div>
<h2>Escribir un mensaje</h2>
<form class="form" name="contact" method="POST" action="{u('merci')}" data-netlify="true" netlify-honeypot="site-web" data-valider data-email="{T('email_inv')}" data-requis="{T('requis')}">
<input type="hidden" name="form-name" value="contact">
<input type="hidden" name="langue" value="es">
<p class="cache"><label>No rellenar: <input name="site-web" tabindex="-1" autocomplete="off"></label></p>
<p class="mention" style="margin:0">Los campos marcados con asterisco (*) son obligatorios.</p>
<div class="champ"><label for="nom">Nombre y apellidos *</label><input id="nom" name="nom" type="text" autocomplete="name" required aria-describedby="nom-erreur" data-vide="Escribe tu nombre."><span class="erreur" id="nom-erreur" aria-live="polite"></span></div>
<div class="champ"><label for="email">Email *</label><input id="email" name="email" type="email" autocomplete="email" required aria-describedby="email-erreur" data-vide="Escribe tu email."><span class="erreur" id="email-erreur" aria-live="polite"></span></div>
<div class="champ"><label for="tel">Teléfono</label><span class="aide" id="tel-aide">Opcional, si prefieres que te llamemos.</span><input id="tel" name="telephone" type="tel" autocomplete="tel" aria-describedby="tel-aide"></div>
<div class="champ"><label for="sujet">Tu consulta es sobre</label><select id="sujet" name="sujet"><option>Danza</option><option>Yoga</option><option>Clases personalizadas</option><option>Talleres</option><option>Hoteles y colaboradores</option><option>Otro</option></select></div>
<div class="champ"><label for="message">Mensaje *</label><textarea id="message" name="message" required aria-describedby="message-erreur" data-vide="Escribe tu mensaje."></textarea><span class="erreur" id="message-erreur" aria-live="polite"></span></div>
<p class="mention">Tus datos solo sirven para responder a tu solicitud. Consulta nuestra <a href="{u('confidentialite')}">política de privacidad</a>.</p>
<button class="btn btn--plein" type="submit">Enviar el mensaje</button>
</form>
</div>
</div></section>''',
 schema=[{'@context': 'https://schema.org', '@type': 'ContactPage', 'name': 'Contacto Danzarina', 'url': SITE['url'] + u('contact')}]))

# ---------- GRACIAS ----------
pages.append(page(u('merci'), 'Mensaje enviado | Danzarina', 'Tu mensaje se ha enviado a Danzarina.',
 titre('Gracias', 'Mensaje enviado', 'Gracias por tu mensaje. Te responderemos lo antes posible.'),
 f'<section class="section" style="padding-top:0"><div class="wrap"><a class="btn btn--plein" href="{u("accueil")}">Volver al inicio</a></div></section>', robots='noindex, follow'))

# ---------- LEGAL ----------
AV = '<p class="mention">Traducción informativa. En caso de diferencia, prevalece la versión francesa.</p>'
pages.append(page(u('mentions'), 'Aviso legal | Danzarina', 'Aviso legal del sitio danzarina.fr.',
 titre('Información legal', 'Aviso legal', 'Conforme a la ley francesa n.º 2004-575 de 21 de junio de 2004 para la confianza en la economía digital (LCEN).'),
 f'''<section class="section contenu-legal" style="padding-top:0"><div class="wrap">
{AV}
<h2>Editor del sitio</h2>
<p>{SITE['nom_long']}, asociación {AC}<br>Sede social: {AC}<br>Número RNA: {AC} · SIRET (si procede): {AC}<br>Teléfono: {SITE['tel_affiche']} · Email: <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
<h2>Director/a de la publicación</h2>
<p>{AC}</p>
<h2>Alojamiento</h2>
<p>Netlify, Inc., 512 2nd Street, Suite 200, San Francisco, CA 94107, Estados Unidos · <a href="https://www.netlify.com" rel="noopener">www.netlify.com</a></p>
<h2>Propiedad intelectual</h2>
<p>Todos los contenidos de este sitio (textos, fotografías, logotipo) son propiedad de Danzarina o de sus autores. Queda prohibida cualquier reproducción sin autorización. Las personas fotografiadas han dado su consentimiento para la difusión de su imagen.</p>
<h2>Créditos</h2>
<p>Fotografías: {AC}. El retrato de la página Sobre nosotros es una imagen artística.</p>
</div></section>''', robots='noindex, follow'))

pages.append(page(u('confidentialite'), 'Política de privacidad | Danzarina', 'Política de privacidad y de protección de datos personales del sitio danzarina.fr.',
 titre('Datos personales', 'Política de privacidad', 'Cómo tratamos los datos que nos confías, conforme al RGPD y a la ley francesa «Informatique et Libertés».'),
 f'''<section class="section contenu-legal" style="padding-top:0"><div class="wrap">
{AV}
<h2>Responsable del tratamiento</h2>
<p>{SITE['nom_long']}, {AC} · <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
<h2>Datos recogidos</h2>
<p>A través del formulario de contacto: nombre, email, teléfono (opcional), asunto y contenido de tu mensaje. No se recoge ningún otro dato.</p>
<h2>Finalidad y base legal</h2>
<p>Responder a tu solicitud (interés legítimo, o medidas precontractuales si pides un presupuesto).</p>
<h2>Destinatarios</h2>
<p>Solo el equipo de Danzarina. Los mensajes pasan por nuestro proveedor de alojamiento, Netlify (servicio Netlify Forms), situado en Estados Unidos y sujeto a las cláusulas contractuales tipo de la Comisión Europea.</p>
<h2>Plazo de conservación</h2>
<p>Tres años desde nuestro último intercambio; después se eliminan.</p>
<h2>Cookies y medición de audiencia</h2>
<p>Este sitio no utiliza cookies de medición de audiencia ni de publicidad, y no recurre a ningún servicio de seguimiento de terceros. Las tipografías están alojadas en nuestro propio servidor.</p>
<h2>Tus derechos</h2>
<p>Tienes derecho de acceso, rectificación, supresión, limitación, oposición y portabilidad. Para ejercerlos: <a href="mailto:{SITE['email']}">{SITE['email']}</a>. También puedes presentar una reclamación ante la CNIL (<a href="https://www.cnil.fr" rel="noopener">www.cnil.fr</a>).</p>
<p class="mention">Última actualización: {AC}</p>
</div></section>''', robots='noindex, follow'))
