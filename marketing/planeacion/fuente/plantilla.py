"""Plantilla CapCut, ganchos y videos con voz IA (VESTA BAGS).

Uso:  python3 plantilla.py  -> plantilla.html ;  node plantilla.cjs -> ../VESTA-plantilla-capcut-y-ganchos.pdf
"""
from pathlib import Path

from gen import CSS, IMG, e, phone

HERE = Path(__file__).parent

EXTRA = r"""
.lay { display:grid; grid-template-columns: 70mm 1fr; gap:10mm; align-items:start; }
.big9 { width:70mm; height:124.4mm; border-radius:7mm; background:var(--deep); padding:2mm; position:relative; }
.big9 .s { position:absolute; inset:2mm; border-radius:5.5mm; overflow:hidden; background:#F4EEE6; }
.big9 .s img.prod { position:absolute; left:12%; top:17%; width:72%; mix-blend-mode:multiply; }
.zone { position:absolute; left:0; right:0; background:repeating-linear-gradient(135deg, rgba(78,58,48,.12) 0 2mm, rgba(78,58,48,.03) 2mm 4mm);
        display:flex; align-items:center; justify-content:center; font-size:6.4pt; color:var(--deep); font-weight:700; letter-spacing:.06em; }
.zone.t { top:0; height:13%; }
.zone.b { bottom:0; height:17.7%; }
.zone.r { top:13%; bottom:17.7%; right:0; left:auto; width:13%; writing-mode:vertical-rl; }
.g-hook { position:absolute; left:10%; right:17%; top:16%; background:rgba(255,255,255,.92); border-radius:3mm; text-align:center;
          font-weight:700; font-size:10pt; padding:2mm 2mm; color:var(--ink); }
.g-price { position:absolute; left:16%; right:23%; top:74%; background:var(--deep); color:#FBF6F1; border-radius:99px; text-align:center;
           font-weight:700; font-size:7.6pt; padding:1.4mm 2mm; }
.g-sub { position:absolute; left:10%; right:17%; top:67.5%; text-align:center; font-size:6.6pt; color:var(--ink);
         background:rgba(255,255,255,.75); border-radius:2mm; padding:1mm; }
.callouts { display:grid; grid-template-columns: repeat(3,1fr); gap:4.5mm; }
.co { border-radius:5mm; padding:4mm 4.5mm; background:var(--nude); }
.co h3 { font-size:10pt; font-weight:700; margin-bottom:2mm; display:flex; gap:2mm; align-items:center; }
.co .k { display:inline-flex; width:6mm; height:6mm; border-radius:99px; background:var(--cacao); color:#fff; font-size:7.5pt; align-items:center; justify-content:center; flex:none; }
.co p, .co li { font-size:9pt; line-height:1.5; }
.co ul { list-style:none; } .co li { margin-bottom:1mm; }
.kv { display:grid; grid-template-columns: 1fr auto; gap:1.2mm 4mm; font-size:8.6pt; }
.kv b { color:var(--cacao); text-align:right; }
.sw { display:inline-block; width:3.6mm; height:3.6mm; border-radius:99px; vertical-align:-.8mm; margin-right:1mm; box-shadow:0 0 0 .3mm rgba(0,0,0,.12); }
.tl { display:flex; height:13mm; border-radius:4mm; overflow:hidden; margin-top:2mm; }
.tl div { display:flex; flex-direction:column; justify-content:center; padding:0 2.5mm; font-size:7.6pt; line-height:1.25; }
.tl div b { font-size:8.4pt; }
.tlx { display:flex; justify-content:space-between; font-size:6.6pt; color:var(--mut); margin-top:1mm; }
.steps2 { display:grid; grid-template-columns: 1.25fr 1fr; gap:8mm; }
.stp { display:grid; grid-template-columns: 8mm 1fr; gap:3mm; margin-bottom:3.4mm; align-items:start; }
.stp .n { width:8mm; height:8mm; border-radius:99px; background:var(--cacao); color:#fff; display:flex; align-items:center; justify-content:center; font-size:9pt; font-weight:700; }
.stp p { font-size:9.2pt; line-height:1.5; }
.stp p b { display:block; font-size:10pt; }
.path { display:inline-block; font-size:7.6pt; background:var(--nude); border-radius:99px; padding:.5mm 2.4mm; margin-top:.8mm; color:var(--deep); }
.hooks { display:grid; grid-template-columns: repeat(4,1fr); gap:4mm; }
.hk { border-radius:5mm; padding:4.5mm; background:var(--nude); min-height:53mm; display:flex; flex-direction:column; }
.hk small { font-size:6.6pt; letter-spacing:.1em; text-transform:uppercase; color:var(--cacao); font-weight:700; }
.hk .f { font-size:9.2pt; font-weight:700; margin:1.6mm 0 2.4mm; line-height:1.35; }
.hk .ex { margin-top:auto; display:flex; flex-direction:column; gap:1.4mm; }
.hk .ex span { font-size:8.2pt; background:#fff; border-radius:99px; padding:1.2mm 2.6mm; }
.hk.d { background:var(--deep); color:#fff; } .hk.d small { color:#E6D0BE; }
.beats { display:grid; grid-template-columns: repeat(4,1fr); gap:3mm; margin:3mm 0 5mm; }
.beat { border-radius:5mm; padding:3.6mm 4mm; }
.beat .t { font-size:7pt; letter-spacing:.1em; text-transform:uppercase; font-weight:700; color:var(--cacao); }
.beat b { display:block; font-size:10.5pt; margin:1mm 0 1.6mm; }
.beat p { font-size:9.2pt; line-height:1.5; }
.beat q { display:block; margin-top:2.5mm; font-size:9pt; font-style:normal; background:#fff; border-radius:3mm; padding:2mm 2.4mm; line-height:1.45; }
.scripts { display:grid; grid-template-columns: repeat(4,1fr); gap:5mm; }
.sc { display:flex; flex-direction:column; align-items:center; }
.sc .phone { width:34mm; height:65mm; }
.sc h4 { font-size:9.6pt; font-weight:700; margin:3mm 0 1.5mm; text-align:center; }
.sc .vo { font-size:8.2pt; line-height:1.55; background:var(--nude); border-radius:4mm; padding:3mm 3.4mm; }
.sc .vo i { font-style:normal; color:var(--cacao); font-weight:700; }
.cap2 { display:grid; grid-template-columns: repeat(3,1fr); gap:5mm; }
.capx { background:#fff; border:1px solid var(--line); border-radius:5mm; padding:4mm 4.5mm; font-size:8.8pt; line-height:1.6; }
.capx small { display:block; font-size:6.6pt; letter-spacing:.1em; text-transform:uppercase; color:var(--cacao); font-weight:700; margin-bottom:1.5mm; }
.capx .h { color:var(--mut); }
"""


def top(label):
    return f'<div class="top"><span>VESTA BAGS · {label}</span><img src="{IMG}logo-dark.png"></div>'


def foot(n):
    return f'<div class="foot"><span>Plantilla CapCut y ganchos · VESTA BAGS · noviembre 2026</span><span>{n}</span></div>'


def p_template():
    return f"""
<section class="page">{top("La plantilla")}
  <h2>La plantilla de CapCut</h2>
  <p class="lead" style="margin-bottom:5mm">Se arma una sola vez. Todos los videos usan el mismo color, la misma letra y el mismo orden: así se ven de una misma marca sin necesidad de ser creativos.</p>
  <div class="lay">
    <div class="big9"><div class="s">
      <img class="prod" src="{IMG}2056-2.jpg">
      <div class="zone t">ZONA DE LA APP · VACÍA</div>
      <div class="zone r">BOTONES</div>
      <div class="zone b">ZONA DE LA APP · VACÍA</div>
      <div class="g-hook">Hello Kitty original en La Paz</div>
      <div class="g-sub">subtítulos de la voz, aquí</div>
      <div class="g-price">My Melody · [precio] Bs</div>
    </div></div>
    <div>
      <div class="callouts">
        <div class="co"><h3><span class="k">1</span>Gancho</h3>
          <ul><li>Arriba, debajo de la zona de la app</li><li>6 palabras como máximo, 2 líneas</li><li>Comfortaa negrita, espresso <span class="sw" style="background:#221B18"></span></li>
          <li>Sobre una etiqueta blanca al 90 %, con esquinas redondeadas</li><li>Desde 0 hasta 1,5 s</li></ul></div>
        <div class="co"><h3><span class="k">2</span>Precio o llamado</h3>
          <ul><li>Abajo, por encima de la zona de la app</li><li>Más chico que el gancho, la mitad más o menos</li>
          <li>Letras marfil <span class="sw" style="background:#FBF6F1"></span> sobre una píldora cacao <span class="sw" style="background:#4E3A30"></span></li>
          <li>Solo el precio real o «Escríbenos por WhatsApp»</li></ul></div>
        <div class="co"><h3><span class="k">3</span>Color (Ajustar)</h3>
          <div class="kv"><span>Temperatura</span><b>+8</b><span>Contraste</span><b>−6</b><span>Saturación</span><b>−8</b>
          <span>Exposición</span><b>−3</b><span>Luces</span><b>−10</b><span>Sombras</span><b>+6</b><span>Nitidez</span><b>+4</b></div>
          <p style="margin-top:1.6mm;font-size:7.4pt;color:var(--mut)">Son un punto de partida: ajústalos una vez a tu ojo y no los cambies más.</p></div>
      </div>
      <div class="co" style="margin-top:5mm;background:#fff;border:1px solid var(--line)"><h3>El orden de cada video (unos 12 s)</h3>
        <div class="tl">
          <div style="width:12.5%;background:#7A4B3A;color:#fff"><b>Gancho</b>0–1,5 s</div>
          <div style="width:50%;background:#F3E9E1"><b>4 tomas de 1,5 s</b>una por movimiento: abrir, detalle, girar, al hombro</div>
          <div style="width:16.5%;background:#E6D0BE"><b>Precio</b>o WhatsApp</div>
          <div style="width:21%;background:#4E3A30;color:#fff"><b>Cierre</b>«Compra en Vesta Bags»</div>
        </div>
        <div class="tlx"><span>0 s</span><span>1,5</span><span>7,5</span><span>9,5</span><span>12 s</span></div>
      </div>
      <div class="grid3" style="margin-top:5mm;gap:4.5mm">
        <div class="co"><h3>Animación del texto</h3><p>Entrada: «Fundido», 0,3 s. Sin rebotes, sin máquina de escribir y sin brillos.</p></div>
        <div class="co"><h3>Cortes</h3><p>Cortes secos, sin transiciones. La cámara lenta, solo en los detalles.</p></div>
        <div class="co"><h3>Exportar</h3><p>1080p · 30 fps · tasa de bits recomendada o alta. Sin el final de CapCut.</p></div>
      </div>
    </div>
  </div>
  {foot(1)}
</section>"""


def p_howto():
    once = [
        ("Proyecto nuevo en 9:16", "Importa 4 clips de prueba y elige el formato vertical.", "Formato › 9:16"),
        ("Color para todo", "Toca un clip, pon los valores de la página anterior y aplícalos a todos.", "Ajustar › Aplicar a todo"),
        ("La letra Comfortaa", "Descárgala gratis de Google Fonts e impórtala. Si tu versión no deja importar letras, usa la redondeada más parecida.", "Texto › Fuente › Importar"),
        ("El texto del gancho", "Escribe un gancho de prueba y dale el estilo: color, etiqueta y animación de entrada «Fundido».", "Texto › Añadir texto › Estilo · Animación"),
        ("El texto del precio", "Lo mismo, con la píldora cacao. Colócalo encima de la zona de abajo.", "Texto › Añadir texto"),
        ("La animación de cierre", "Agrega al final tu clip «Compra en Vesta Bags».", "+ › Añadir clip"),
        ("Guarda el proyecto", "Llámalo «PLANTILLA VESTA – NO BORRAR».", ""),
        ("Quita el final de CapCut", "Desactívalo una sola vez, para que no salga la marca de agua.", "Ajustes › Añadir final predeterminado: no"),
    ]
    each = [
        ("Duplica la plantilla", "Mantén presionado el proyecto y elige «Duplicar».", "Mantener presionado › Duplicar"),
        ("Cambia los clips", "Toca cada clip y reemplázalo por tus tomas. El color y los textos se quedan.", "Clip › Reemplazar"),
        ("Cambia los textos", "Escribe el gancho y el precio del video.", ""),
        ("Exporta y sube", "1080p a 30 fps. La música agrégala dentro de TikTok o Instagram.", "Exportar"),
    ]
    def block(lst):
        return "".join(f'<div class="stp"><span class="n">{i+1}</span><p><b>{a}</b>{e(b)}'
                       + (f'<br><span class="path">{e(c)}</span>' if c else "") + '</p></div>' for i, (a, b, c) in enumerate(lst))
    return f"""
<section class="page">{top("Paso a paso")}
  <h2>Cómo armarla y cómo usarla</h2>
  <p class="lead" style="margin-bottom:5mm">Los nombres de los menús pueden cambiar un poco según tu versión de CapCut.</p>
  <div class="steps2">
    <div class="card w"><h3 style="font-size:12pt;margin-bottom:3mm">Una sola vez · 20 minutos</h3><div style="columns:2;column-gap:6mm">{block(once)}</div></div>
    <div class="card"><h3 style="font-size:12pt;margin-bottom:3mm">Cada video · 5 minutos</h3>{block(each)}
      <div class="card d" style="margin-top:4mm;padding:4mm"><p style="font-size:9pt"><b>La regla:</b> nunca empieces un video desde cero. Siempre duplica la plantilla. Eso es lo que hace que todos se vean iguales de bien.</p></div></div>
  </div>
  {foot(2)}
</section>"""


def p_hooks():
    H = [
        ("1 · Personaje + original + dónde", "Lo que la gente ya busca, al principio.", ["Hello Kitty original en La Paz", "Stitch llegó a VESTA", "Garfield, pero elegante"]),
        ("2 · La pregunta que te hacen", "Lo que te escriben por WhatsApp.", ["¿Le entra una tablet?", "¿Pagas al recibir? Sí", "¿Envían a todo Bolivia?"]),
        ("3 · Regalo", "Para quién es, no qué es.", ["¿Qué le regalo a mi mamá?", "Para tu mejor amiga", "Amigo secreto, resuelto"]),
        ("4 · Identidad", "Que se reconozca en la frase.", ["Si eres más Mafalda que Susanita…", "Para las que aman a Stitch", "POV: tu cartera combina contigo"]),
        ("5 · Novedad", "Algo nuevo, que es real.", ["Llegó la Mafalda rosada", "Abre conmigo", "Lo nuevo para Navidad"]),
        ("6 · Elige", "Que comente su opción.", ["¿Rosado o celeste?", "Mafalda o Garfield", "Elige: 1, 2 o 3"]),
        ("7 · Precio directo", "Claro y sin rodeos (solo el precio real).", ["My Melody · [precio] Bs", "Mochila Stitch · [precio] Bs"]),
    ]
    cards = "".join(f'<div class="hk"><small>{a}</small><div class="f">{b}</div><div class="ex">'
                    + "".join(f"<span>«{e(x)}»</span>" for x in ex) + '</div></div>' for a, b, ex in H)
    cards += ('<div class="hk d"><small>Reglas</small><ul style="list-style:none;font-size:8.4pt;line-height:1.55;margin-top:2mm">'
              '<li>6 palabras como máximo</li><li>El personaje en las 2 primeras palabras</li><li>Lo que dice = lo que se ve</li>'
              '<li>Sin «barato», «remate» ni «oferta»</li><li>Sin nombrar a Tizza</li><li>1 emoji como máximo: 🤍</li></ul></div>')
    return f"""
<section class="page">{top("Ganchos")}
  <h2>Cómo escribir los ganchos</h2>
  <p class="lead" style="margin-bottom:5mm">El gancho es lo primero que se lee, en el segundo 0. Hay 7 fórmulas: elige una por video.
  La prueba: si alguien que no te conoce entiende en 1 segundo qué es y si es para ella, funciona.</p>
  <div class="hooks">{cards}</div>
  {foot(3)}
</section>"""


def p_voice():
    beats = [
        ("0–3 s", "Lo presentas", "Nombre del personaje y qué es. Aquí la voz dice el gancho.", "«Te presento la My Melody, de Hello Kitty and Friends.»", "#F8E2E8"),
        ("3–10 s", "2 o 3 detalles", "Solo lo que se ve en la toma. Una frase por toma.", "«Es rosada, con herrajes dorados y un dije de corazón.»", "#F3E9E1"),
        ("10–14 s", "Para quién", "Uso o regalo, sin exagerar.", "«Para ti o para regalar esta Navidad.»", "#E4EEE5"),
        ("14–18 s", "Dónde y cómo", "Siempre el mismo cierre.", "«La encuentras en VESTA, en La Paz. Escríbenos por WhatsApp.»", "#E2EDF6"),
    ]
    bh = "".join(f'<div class="beat" style="background:{bg}"><span class="t">{t}</span><b>{a}</b><p>{e(b)}</p><q>{e(q)}</q></div>'
                 for t, a, b, q, bg in beats)
    return f"""
<section class="page">{top("Voz IA")}
  <h2>Videos con voz de IA: «Te la presento»</h2>
  <p class="lead" style="margin-bottom:2mm">Es lo que hace la cuenta que vende: una voz que describe la cartera mientras se ve. Es fácil de grabar porque son
  las mismas tomas de siempre, y además repite el nombre y el precio. Puede ser 1 de cada 3 videos.</p>
  <div class="beats">{bh}</div>
  <div class="grid3" style="gap:5mm">
    <div class="co"><h3>La voz en CapCut</h3><ul><li>Escribe el guion como texto y conviértelo con «Texto a voz»</li>
      <li>Elige una voz femenina y <b>usa siempre la misma</b>: la voz también es marca</li><li>Velocidad entre 1,0 y 1,1</li>
      <li>Después, «Subtítulos automáticos», con el estilo de la plantilla</li></ul></div>
    <div class="co"><h3>Cómo escribir para la voz</h3><ul><li>Frases cortas: 8 a 10 palabras</li><li>Una frase por toma</li>
      <li>Solo detalles que se ven y medidas confirmadas</li><li>El precio solo si es real</li><li>Música de fondo al 15–20 %</li></ul></div>
    <div class="co" style="background:var(--deep);color:#fff"><h3>Etiqueta de IA (obligatoria)</h3><ul>
      <li>TikTok: al publicar, en «Más opciones», activa «Contenido generado por IA»</li>
      <li>Instagram: activa la etiqueta de IA al publicar</li>
      <li>En el caption: «voz generada con IA»</li></ul></div>
  </div>
  {foot(4)}
</section>"""


def p_scripts():
    S = [
        ("2056-1.jpg", "My Melody", "Hello Kitty and Friends",
         "Te presento la <i>My Melody</i>, de Hello Kitty and Friends. Es rosada, con herrajes dorados y un dije de corazón. "
         "Se lleva al hombro. Para ti o para regalar esta Navidad. <i>La encuentras en VESTA, en La Paz.</i> Escríbenos por WhatsApp.", "#F8E2E8"),
        ("2128-1.jpg", "Mafalda rosada", "Mafalda",
         "Si eres más <i>Mafalda</i> que Susanita, mira esta. Tiene el borde en ondas, a Mafalda con su flor y una borla que se mueve. "
         "También viene en celeste. <i>La encuentras en VESTA, en La Paz.</i> Escríbenos por WhatsApp.", "#F7E3E8"),
        ("2141-1.jpg", "Garfield", "Garfield",
         "<i>Garfield</i>, pero elegante. Tiene a Garfield con su taza, herrajes dorados y un dije de Garfield colgando. "
         "Viene en negro y en verde. <i>La encuentras en VESTA, en La Paz.</i> Escríbenos por WhatsApp.", "#FFFFFF"),
        ("2100-1.jpg", "Mochila Stitch", "Stitch",
         "Para las que aman a <i>Stitch</i>. Una mochila celeste con una ventana de corazón con brillos, y adentro, Stitch y Ángel. "
         "<i>La encuentras en VESTA, en La Paz.</i> Escríbenos por WhatsApp.", "#E2EDF6"),
    ]
    cols = ""
    for img, name, char, vo, bg in S:
        ph = phone(dict(img=img, zoom=0.95, text=f"{char} original en La Paz" if char != "Hello Kitty and Friends" else "Hello Kitty original en La Paz",
                        small=f"{name} · [precio] Bs", bg=bg))
        cols += f'<div class="sc">{ph}<h4>{name}</h4><div class="vo">{vo}</div></div>'
    return f"""
<section class="page">{top("Guiones listos")}
  <h2>4 guiones listos para la voz</h2>
  <p class="lead" style="margin-bottom:4mm">Copia el texto en «Texto a voz». Describen solo lo que se ve en las fotos. Si tu cartera tiene otro color o
  la correa es distinta, cámbialo. Pon el precio real donde dice [precio].</p>
  <div class="scripts">{cols}</div>
  {foot(5)}
</section>"""


def p_captions():
    C = [
        ("Video con gancho de personaje",
         "Hello Kitty original, en La Paz 🤍<br>La My Melody, rosada y con herrajes dorados.<br>"
         "Escríbenos por WhatsApp · En La Paz pagas al recibir.<br><span class='h'>#hellokitty #mymelody #carteras #lapaz #bolivia</span>"),
        ("Video de regalo",
         "¿Ya tienes el regalo de mamá?<br>Esta Mafalda llega lista para regalar.<br>"
         "Escríbenos por WhatsApp · Delivery en La Paz y envíos a toda Bolivia.<br><span class='h'>#regalos #mafalda #carteras #lapaz #navidad</span>"),
        ("Video con voz IA",
         "Garfield, pero elegante 🤍<br>En negro y en verde.<br>Escríbenos por WhatsApp · En La Paz pagas al recibir.<br>"
         "Voz generada con IA.<br><span class='h'>#garfield #carteras #lapaz #bolivia</span>"),
    ]
    ch = "".join(f'<div class="capx"><small>{a}</small>{b}</div>' for a, b in C)
    return f"""
<section class="page">{top("Captions")}
  <h2>El texto de abajo (caption)</h2>
  <p class="lead" style="margin-bottom:5mm">Siempre 4 líneas, en el mismo orden. En TikTok lo importante va en la pantalla; el caption acompaña.</p>
  <div class="beats" style="grid-template-columns:repeat(4,1fr);margin-top:0">
    <div class="beat" style="background:#F8E2E8"><span class="t">Línea 1</span><b>El gancho</b><p>Lo mismo que dice la pantalla, o casi.</p></div>
    <div class="beat" style="background:#F3E9E1"><span class="t">Línea 2</span><b>Un detalle</b><p>Color, personaje o para quién es.</p></div>
    <div class="beat" style="background:#E4EEE5"><span class="t">Línea 3</span><b>Cómo comprar</b><p>WhatsApp + «En La Paz pagas al recibir».</p></div>
    <div class="beat" style="background:#E2EDF6"><span class="t">Línea 4</span><b>3 a 5 hashtags</b><p>El personaje + carteras + lapaz + bolivia.</p></div>
  </div>
  <div class="cap2">{ch}</div>
  {foot(6)}
</section>"""


def build():
    pages = [p_template(), p_howto(), p_hooks(), p_voice(), p_scripts(), p_captions()]
    head = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Plantilla CapCut VESTA</title>'
            '<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@400;500;600;700&display=swap" rel="stylesheet">'
            f'<style>{CSS}{EXTRA}</style></head><body>')
    (HERE / "plantilla.html").write_text(head + "".join(pages) + "</body></html>", encoding="utf-8")
    print("ok", len(pages), "páginas")


if __name__ == "__main__":
    build()
