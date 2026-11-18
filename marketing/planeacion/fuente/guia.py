"""Guía de grabación VESTA: una página por tipo de video (formatos A a J).

Uso:  python3 guia.py  -> guia.html ;  node guia.cjs -> ../VESTA-guia-de-grabacion.pdf
Reutiliza estilos, formatos y el teléfono de gen.py.
"""
import collections
from pathlib import Path

import gen
from gen import CSS, FORMATS, IMG, PLAN, chip, e, phone

HERE = Path(__file__).parent
USES = collections.Counter()
for r in PLAN:
    USES[r[1][0]] += 1
    USES[r[2][0]] += 1

# ---------------------------------------------------------------- ángulos (íconos)
def angle_svg(kind):
    bag = '<rect x="22" y="40" width="20" height="16" rx="3" fill="#E6D0BE"/><path d="M26 40 q6 -9 12 0" stroke="#7A4B3A" stroke-width="1.6" fill="none"/>'
    table = '<line x1="6" y1="56" x2="58" y2="56" stroke="#C9B3A3" stroke-width="1.4"/>'
    ph = lambda x, y, r=0: (f'<g transform="rotate({r} {x+4} {y+7})"><rect x="{x}" y="{y}" width="8" height="14" rx="1.8" fill="#4E3A30"/></g>')
    dash = lambda x1, y1, x2, y2: f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#7A4B3A" stroke-width="1" stroke-dasharray="2 2"/>'
    if kind == "cenital":
        flat = '<rect x="20" y="50" width="24" height="6" rx="2" fill="#E6D0BE"/>'
        body = table + flat + ph(28, 6, 90) + dash(32, 18, 32, 48)
    elif kind == "frontal":
        body = table + bag + ph(4, 36) + dash(13, 44, 21, 46)
    elif kind == "45":
        body = table + bag + ph(6, 14, -40) + dash(14, 26, 24, 40)
    elif kind == "macro":
        body = table + bag + ph(40, 30, 30) + dash(42, 40, 38, 46) + '<circle cx="36" cy="48" r="5" fill="none" stroke="#7A4B3A" stroke-width="1"/>'
    else:  # pantalla
        body = ('<rect x="20" y="8" width="24" height="44" rx="4" fill="#4E3A30"/><rect x="23" y="12" width="18" height="36" rx="2" fill="#F3E9E1"/>'
                '<rect x="26" y="18" width="12" height="4" rx="2" fill="#fff"/><rect x="28" y="26" width="10" height="4" rx="2" fill="#E3EFD9"/>'
                '<circle cx="44" cy="42" r="4" fill="#E6D0BE"/>')
    return f'<svg viewBox="0 0 64 64" class="ang">{body}</svg>'


ANG_LABEL = {"cenital": "Desde arriba", "frontal": "De frente", "45": "En diagonal (45°)",
             "macro": "Muy de cerca", "pantalla": "Grabación de pantalla"}

# ---------------------------------------------------------------- contenido por formato
G = {
 "A": dict(goal="Que se imagine usándola: «yo también llevo eso».", dur="10–15 s", ang="cenital", speed="Normal",
    need=["La cartera", "5 o 6 cosas bonitas y reales: billetera, labial, llaves con llavero, lentes, celular", "Mesa o cartulina blanca"],
    shots=[("Cartera cerrada al centro. Texto del gancho", dict(img="2128-1.jpg", zoom=0.7, text="Lo que llevo a la U", bg="#FFFFFF")),
           ("Abres el cierre: deja que se oiga", dict(img="2128-1.jpg", zoom=1.9, x=50, y=30, small="abre el cierre", bg="#FFFFFF")),
           ("Sacas una cosa por corte y la alineas al costado", dict(img="2133-1.jpg", zoom=0.85, small="1 cosa = 1 corte", bg="#FFFFFF")),
           ("Todo alineado + la cartera", dict(kind="end"))],
    text=["Lo que llevo a la U", "Lo que lleva mi mamá", "Lo que llevo un domingo", "Lo que llevo a la oficina"],
    ojo=["Cables enredados o cosas gastadas", "La sombra de tu brazo encima: la luz tiene que entrar de costado", "Mover el celular: va fijo en el trípode"]),
 "B": dict(goal="Responder antes de que pregunte: «¿me entra?».", dur="10–15 s", ang="45", speed="Normal",
    need=["La cartera, abierta y parada", "Lo que la gente duda que entre: tablet, botella, cuaderno, cosmetiquera, billetera"],
    shots=[("Cartera vacía y abierta", dict(img="2144-1.jpg", zoom=0.85, text="¿Le entra todo?", bg="#F4EEE6")),
           ("Metes cada cosa con el ritmo de la música", dict(img="2144-1.jpg", zoom=1.0, small="tablet ✓ botella ✓", bg="#F4EEE6")),
           ("La cierras sin esfuerzo, bien de cerca", dict(img="2144-1.jpg", zoom=2.0, x=50, y=35, small="cierra fácil", bg="#F4EEE6")),
           ("La levantas por las asas", dict(kind="end"))],
    text=["¿Le entra todo?", "¿Entra mi tablet? Mira", "¿Mini o grande?", "Todo para la fiesta"],
    ojo=["Forzar el cierre: mete solo lo que entra de verdad", "Si no tienes las medidas: «te las pasamos por WhatsApp»", "Una cartera arrugada o caída"]),
 "C": dict(goal="Que se note la calidad que en una foto no se ve.", dur="8–12 s", ang="macro", speed="Cámara lenta",
    need=["La cartera limpia, con un paño seco a mano", "Luz de ventana bien de costado: marca la textura"],
    shots=[("La cartera completa", dict(img="2141-1.jpg", zoom=0.9, text="Esto no se ve en fotos", bg="#FFFFFF")),
           ("El cierre se abre en cámara lenta", dict(img="2141-1.jpg", zoom=2.6, x=50, y=22, bg="#FFFFFF")),
           ("El forro y las costuras", dict(img="2141-1.jpg", zoom=2.4, x=30, y=60, small="costuras", bg="#FFFFFF")),
           ("Giro lento del dibujo o del dije", dict(kind="end"))],
    text=["Esto no se ve en fotos", "Garfield, pero elegante", "Brillo bajo la luz", "Así se ve de verdad"],
    ojo=["Video borroso: acércate solo hasta que enfoque y no uses zoom digital", "Pelusas o huellas en los herrajes", "Luz amarilla del foco: cambia los colores"]),
 "D": dict(goal="Que comente: los comentarios empujan el video.", dur="8–10 s", ang="frontal", speed="Normal",
    need=["La misma cartera en 2 o 3 colores (solo los que tienes de verdad)", "Las dos manos libres; uñas arregladas"],
    shots=[("Las carteras juntas, a la altura del pecho", dict(kind="two", img="2128-1.jpg", img2="2128-2.jpg", text="¿Rosado o celeste?", bg="#FFFFFF")),
           ("Acercas una: 2 s", dict(img="2128-1.jpg", zoom=1.0, small="rosado", bg="#F8E2E8")),
           ("Acercas la otra: 2 s", dict(img="2128-2.jpg", zoom=1.0, small="celeste", bg="#E2EDF6")),
           ("Juntas otra vez: «Comenta tu color»", dict(kind="end"))],
    text=["¿Rosado o celeste?", "Elige: 1, 2 o 3", "Mafalda o Garfield", "¿Cuál te llevas?"],
    ojo=["Mostrar un color que no hay en stock", "Dejar comentarios sin responder: contesta todos", "Luz de foco: el rosado sale naranja"]),
 "E": dict(goal="Novedad: «llegó algo y lo ves primero».", dur="12–15 s", ang="45", speed="Normal + sonido real",
    need=["La caja cerrada", "Tijera o cúter, papel seda", "Si la caja trae logo de marca o datos de envío: tápalos"],
    shots=[("Caja cerrada", dict(kind="box", text="Llegó para Navidad", bg="#FFFFFF")),
           ("La abres: que se oiga el papel", dict(kind="gift", img="2122-1.jpg", zoom=0.5, y=100, small="shhh… papel", bg="#FFFFFF")),
           ("Sacas 2 o 3 modelos, uno por corte", dict(img="2122-1.jpg", zoom=1.0, bg="#F6EFE8")),
           ("Las alineas: «¿Cuál quieres?»", dict(kind="end"))],
    text=["Llegó para Navidad", "Abre conmigo", "Abrimos la caja", "Últimas que llegaron"],
    ojo=["Etiquetas con nombre o dirección a la vista", "El logo de otra marca en primer plano", "Caja rota o sucia"]),
 "F": dict(goal="El video que vende: a quién se lo vas a regalar.", dur="10–15 s", ang="45", speed="Normal",
    need=["Bolsa o caja de regalo, papel seda y moño", "Tarjeta escrita a mano: «Para mamá», «Para ti»", "La cartera + billetera para el combo"],
    shots=[("Una mano señala a cámara", dict(img="2128-1.jpg", zoom=0.55, text="¿Qué quieres de regalo?", bg="#F7EDE6")),
           ("Corte seco: aparece la cartera", dict(img="2128-1.jpg", zoom=1.0, text="Yo:", bg="#F7E3E8")),
           ("La guardas en la bolsa con la tarjeta", dict(kind="gift", img="2128-1.jpg", zoom=0.55, y=100, small="con tarjeta 🤍", bg="#F7E3E8")),
           ("Bolsa lista y cerrada", dict(kind="end"))],
    text=["¿Qué quieres de regalo?", "Para mamá esta Navidad", "Para tu mejor amiga", "Amigo secreto, resuelto", "Para ti, te lo mereces"],
    ojo=["Poner un precio que no esté confirmado", "Prometer que llega antes del 24 sin confirmar", "Una bolsa arrugada: el regalo tiene que verse lindo"]),
 "G": dict(goal="Confianza: hay personas reales detrás.", dur="10–15 s", ang="cenital", speed="Normal + sonido real",
    need=["Un pedido real", "Papel para rellenar, bolsa de tela, tarjeta de gracias", "Cinta o sticker para cerrar"],
    shots=[("El pedido sobre la mesa", dict(img="2125-1.jpg", zoom=0.8, text="Así te llega tu cartera", bg="#EFE8E1")),
           ("La rellenas con papel y la metes en la bolsa de tela", dict(img="2125-1.jpg", zoom=1.6, x=50, y=40, small="rellena con papel", bg="#EFE8E1")),
           ("Tarjeta y cierre con cinta", dict(kind="box", small="tarjeta de gracias", bg="#EFE8E1")),
           ("Una mano entrega la bolsa", dict(kind="end"))],
    text=["Así te llega tu cartera", "Preparando el viernes", "Empacando regalos", "Así entregamos en La Paz"],
    ojo=["Nombre, dirección o teléfono de la clienta", "La fachada o la placa de la casa en las entregas", "Grabar una entrega sin permiso"]),
 "H": dict(goal="Quitar el miedo a comprar por redes.", dur="12–18 s", ang="pantalla", speed="Normal",
    need=["Grabación de pantalla del celular", "Un chat de prueba (nunca uno de una clienta real)", "Modo no molestar activado"],
    shots=[("Título de los 3 pasos", dict(img="2125-1.jpg", zoom=0.7, text="Comprar en VESTA: 3 pasos", bg="#FFFFFF")),
           ("1 · Elige: pasas el dedo por los videos", dict(img="2128-2.jpg", zoom=0.9, small="1 · eliges", bg="#E2EDF6")),
           ("2 · Escribes por WhatsApp", dict(kind="msg", q="Hola, equipo VESTA. Me gusta esta 🤍", a="¡Hola! Te mandamos fotos reales y el precio", bg="#EFE8E1")),
           ("3 · QR, transferencia o pagas al recibir en La Paz", dict(kind="end"))],
    text=["Comprar en VESTA: 3 pasos", "En La Paz pagas al recibir", "¿No está? Lo traemos", "Cómo pedir hoy"],
    ojo=["Notificaciones que aparecen en la grabación", "Prometer plazos de entrega", "Para los encargos: aclarar el 50 % de adelanto"]),
 "I": dict(goal="Contestar con un video lo que otra persona también se pregunta.", dur="8–12 s", ang="frontal", speed="Normal",
    need=["Una pregunta real de los comentarios o de WhatsApp", "En TikTok: «Responder con video» desde el comentario (aparece como sticker)"],
    shots=[("La pregunta arriba, como sticker", dict(kind="msg", q="¿Puedo pagar al recibir?", a="Sí 🤍 En La Paz pagas cuando te la entregamos", bg="#FFF0D6")),
           ("Muestras la respuesta, no la explicas", dict(img="2125-1.jpg", zoom=0.9, text="Así de simple", bg="#FFFFFF")),
           ("Un texto corto con la respuesta", dict(img="2125-1.jpg", zoom=1.7, x=50, y=70, small="QR · transferencia · efectivo", bg="#FFFFFF")),
           ("Cierre", dict(kind="end"))],
    text=["¿Pagas al recibir? Sí", "¿Envían a todo Bolivia?", "¿Es original?", "¿Llega antes del 24?"],
    ojo=["Inventar preguntas: usa solo las que llegaron", "Responder con datos que no están confirmados", "En «¿es original?»: etiqueta y acabados, sin nombrar la marca"]),
 "J": dict(goal="Un personaje que la gente recuerde y que ayuda a elegir.", dur="8–12 s", ang="frontal", speed="Normal",
    need=["La mascota Vesta como sticker en CapCut (el PNG original, sin redibujar)", "2 o 3 carteras para elegir"],
    shots=[("Vesta saluda", dict(kind="mascot", img="2128-1.jpg", img2="2141-1.jpg", text="Hola, soy Vesta 🤍", bg="#F4EEE6")),
           ("Hace la pregunta", dict(kind="two", img="2122-1.jpg", img2="2141-2.jpg", text="¿Mafalda o Garfield?", bg="#F4EEE6")),
           ("Recomienda una", dict(img="2122-1.jpg", zoom=1.0, small="creo que te va a encantar", bg="#F4EEE6")),
           ("Cierre", dict(kind="end"))],
    text=["Hola, soy Vesta 🤍", "¿Te ayudo a elegir?", "¿Qué le regalo? Vesta te ayuda", "Feliz Navidad, de Vesta"],
    ojo=["Deformar, recolorear o redibujar a la mascota", "Que la mascota dé precios o plazos: deriva al equipo", "Usar la mascota más de 3 veces por semana"]),
}

EXTRA_CSS = r"""
.ang { width:15mm; height:15mm; }
.gh { display:grid; grid-template-columns: 74mm 1fr; gap:8mm; }
.gh .big { width:17mm; height:17mm; border-radius:99px; display:flex; align-items:center; justify-content:center;
           font-size:24pt; font-weight:700; margin-bottom:3mm; }
.gh h2 { font-size:22pt; margin-bottom:1.5mm; }
.goal { font-size:10.5pt; line-height:1.5; color:var(--ink2); margin-bottom:5mm; }
.facts2 { display:grid; grid-template-columns:1fr 1fr; gap:3mm; }
.facts2 > div { background:var(--nude); border-radius:4mm; padding:2.6mm 3mm; font-size:9pt; font-weight:700; }
.facts2 small { display:block; font-size:6.4pt; letter-spacing:.1em; text-transform:uppercase; color:var(--mut); margin-bottom:.6mm; font-weight:700; }
.facts2 .wide { grid-column: span 2; display:flex; align-items:center; gap:3mm; }
.shots { display:grid; grid-template-columns:repeat(4,1fr); gap:4mm; }
.shot { display:flex; flex-direction:column; align-items:center; text-align:center; }
.shot .phone { width:37mm; height:71mm; }
.shot .st { margin-top:2.6mm; font-size:8.8pt; line-height:1.4; max-width:40mm; }
.shot .st b { display:inline-flex; width:5mm; height:5mm; border-radius:99px; background:var(--cacao); color:#fff;
              font-size:7pt; align-items:center; justify-content:center; margin-right:1mm; vertical-align:-1mm; }
.bottom { display:grid; grid-template-columns: 1.1fr 1fr 1.1fr; gap:5mm; margin-top:8mm; }
.bottom .card { min-height:44mm; }
.bottom .card { padding:4.5mm 5mm; }
.pills { display:flex; flex-wrap:wrap; gap:1.8mm; }
.pills span { font-size:8.4pt; padding:1.4mm 3mm; border-radius:99px; background:#fff; border:1px solid var(--line); }
.setgrid { display:grid; grid-template-columns:repeat(4,1fr); gap:4.5mm; }
.setgrid .card h3 { display:flex; align-items:center; gap:2mm; }
.ix { display:inline-flex; width:7mm; height:7mm; border-radius:99px; background:var(--cacao); color:#fff; font-size:8.5pt;
      align-items:center; justify-content:center; flex:none; }
.order { display:grid; grid-template-columns: repeat(5, 1fr); gap:3mm; margin-top:3mm; }
.order div { border-radius:4mm; padding:3mm; font-size:8.4pt; line-height:1.4; }
.order b { display:block; font-size:10pt; margin-bottom:.8mm; }
.idx { display:grid; grid-template-columns:repeat(5,1fr); gap:3mm; margin-top:5mm; }
.idx div { border-radius:4mm; padding:3mm 3.4mm; font-size:8.6pt; display:flex; gap:2mm; align-items:center; }
"""


def foot(n):
    return (f'<div class="foot"><span>Guía de grabación · VESTA BAGS · noviembre 2026</span><span>{n}</span></div>')


def top(label):
    return (f'<div class="top"><span>VESTA BAGS · {label}</span><img src="{IMG}logo-dark.png"></div>')


def page_cover():
    idx = "".join(f'<div style="background:{bg};color:{fg}"><b style="font-size:12pt">{k}</b> {name}</div>'
                  for k, (name, _, bg, fg) in FORMATS.items())
    return f"""
<section class="page"><div class="cover">
  <div>
    <div class="kick">Guía de grabación</div>
    <h1>Cómo grabar<br>cada video</h1>
    <p class="lead" style="margin-top:6mm">Una página por tipo de video: qué necesitas, desde dónde grabar,
    cada toma, el texto para la pantalla y los errores que hay que evitar.</p>
    <div class="idx">{idx}</div>
  </div>
  <div class="arch"><img class="m" src="{IMG}mascota-vesta.png"><img class="p" src="{IMG}2141-1.jpg"></div>
</div></section>"""


def page_setup():
    cards = [
        ("1", "El set", ["Fondo blanco: cartulina, sábana o pared", "Mesa clara y despejada", "Ventana de costado, sin sol directo",
                         "Mañana o media tarde: la luz es pareja"]),
        ("2", "El celular", ["Video vertical, 1080p, 30 cuadros", "Mantén el dedo sobre la pantalla para fijar la luz y el foco",
                             "No uses el zoom digital", "Limpia la cámara antes de empezar"]),
        ("3", "Tus manos", ["Uñas arregladas, sin anillos que distraigan", "Movimientos lentos y limpios",
                            "Cada acción, de 1 a 2 s", "Graba 3 tomas de cada cosa"]),
        ("4", "Editar en CapCut", ["Corta el video a 8–15 s", "Texto en los primeros 2 s, de 6 palabras como máximo",
                                   "Pega la animación «Compra en Vesta Bags»", "Quita el clip final de CapCut (deja marca de agua)"]),
    ]
    ch = ""
    for n, t, items in cards:
        lis = "".join(f"<li>{x}</li>" for x in items)
        ch += f'<div class="card"><h3><span class="ix">{n}</span>{t}</h3><ul style="margin-top:2mm">{lis}</ul></div>'
    order = [("9:00", "Armar el set", "#F6E7DD"), ("9:20", "A y G · desde arriba", "#EFE8E1"),
             ("9:50", "B, E y F · en diagonal", "#F8E2E8"), ("10:30", "C · cámara lenta", "#E4EEE5"),
             ("10:50", "D, I y J · de frente; H, pantalla", "#E2EDF6")]
    oh = "".join(f'<div style="background:{bg}"><b>{a}</b>{b}</div>' for a, b, bg in order)
    return f"""
<section class="page">{top("Antes de grabar")}
  <h2>Antes de grabar</h2>
  <p class="lead" style="margin-bottom:5mm">Lo mismo para todos los videos. Se arma una vez y se graba en tanda.</p>
  <div class="setgrid">{ch}</div>
  <div class="card w" style="margin-top:5mm">
    <h3>La tanda del domingo, agrupada por ángulo para no mover el celular a cada rato</h3>
    <div class="order">{oh}</div>
    <p style="margin-top:3mm;font-size:8.6pt;color:var(--ink2)">Al publicar: la música agrégala <b>dentro de TikTok o Instagram</b> (de la biblioteca comercial), no en CapCut.
    Si usas voz de IA, pon la etiqueta «voz generada con IA». Responde los comentarios durante los primeros 30 min.</p>
  </div>
  {foot(2)}
</section>"""


def page_format(k, n):
    name, _, bg, fg = FORMATS[k]
    g = G[k]
    shots = "".join(f'<div class="shot">{phone(fr)}<div class="st"><b>{i+1}</b>{e(t)}</div></div>'
                    for i, (t, fr) in enumerate(g["shots"]))
    need = "".join(f"<li>{e(x)}</li>" for x in g["need"])
    txt = "".join(f"<span>{e(x)}</span>" for x in g["text"])
    ojo = "".join(f"<li>{e(x)}</li>" for x in g["ojo"])
    return f"""
<section class="page">{top("Guía de grabación")}
  <div class="gh">
    <div>
      <div class="big" style="background:{bg};color:{fg}">{k}</div>
      <h2>{name}</h2>
      <p class="goal">{e(g["goal"])}</p>
      <div class="facts2">
        <div><small>Duración</small>{g["dur"]}</div>
        <div><small>En el plan</small>{USES[k]} videos</div>
        <div class="wide">{angle_svg(g["ang"])}<div><small>Desde dónde grabar</small>{ANG_LABEL[g["ang"]]}</div></div>
        <div class="wide" style="grid-column:span 2"><div><small>Velocidad</small>{g["speed"]}</div></div>
      </div>
    </div>
    <div class="shots">{shots}</div>
  </div>
  <div class="bottom">
    <div class="card"><h3>Necesitas</h3><ul>{need}</ul></div>
    <div class="card w"><h3>Texto en pantalla (copia y pega)</h3><div class="pills">{txt}</div></div>
    <div class="card d"><h3>Ojo con esto</h3><ul>{ojo}</ul></div>
  </div>
  {foot(n)}
</section>"""


def build():
    pages = [page_cover(), page_setup()]
    for i, k in enumerate(FORMATS):
        pages.append(page_format(k, i + 3))
    head = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Guía de grabación VESTA</title>'
            '<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@400;500;600;700&display=swap" rel="stylesheet">'
            f'<style>{CSS}{EXTRA_CSS}</style></head><body>')
    (HERE / "guia.html").write_text(head + "".join(pages) + "</body></html>", encoding="utf-8")
    print("ok", len(pages), "páginas")


if __name__ == "__main__":
    build()
