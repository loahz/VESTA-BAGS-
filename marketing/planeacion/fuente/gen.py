"""Genera la planificación de ventas y contenido VESTA (25 nov - 24 dic 2026).

Uso:  python3 gen.py            -> plan.html y frames.html (para las animaciones)
Luego print.cjs imprime el PDF y arma los GIF.
"""
import datetime as dt
import html
from pathlib import Path

HERE = Path(__file__).parent
IMG = "img/"

# ---------------------------------------------------------------- formatos
FORMATS = {
    "A": ("Qué llevo", "Sacas tus cosas una por una. Solo manos.", "#F6E7DD", "#4E3A30"),
    "B": ("Entra todo", "Llenas la cartera para mostrar cuánto le entra.", "#EEE4F2", "#4E3A30"),
    "C": ("Detalle", "Cierre, forro y costuras en cámara lenta.", "#E4EEE5", "#4E3A30"),
    "D": ("Elige color", "La misma cartera en 2 o 3 colores: «¿cuál?».", "#E2EDF6", "#4E3A30"),
    "E": ("Unboxing", "Abres la caja y ves el primer vistazo.", "#F8E2E8", "#4E3A30"),
    "F": ("Regalo", "Para mamá, la amiga o una misma. El que vende.", "#7A4B3A", "#FFFFFF"),
    "G": ("Detrás de cámara", "Empacar, preparar y entregar pedidos reales.", "#EFE8E1", "#4E3A30"),
    "H": ("Cómo comprar", "3 pasos y «en La Paz pagas al recibir».", "#4E3A30", "#FFFFFF"),
    "I": ("Respondo tu duda", "Una pregunta real de WhatsApp, respondida.", "#FFF0D6", "#4E3A30"),
    "J": ("Vesta te ayuda", "La mascota elige por ti según tu estilo.", "#F4EEE6", "#4E3A30"),
}
NEW = {"H", "I", "J"}

# ---------------------------------------------------------------- fases
PHASES = [
    ("bf", "Black Friday", dt.date(2026, 11, 25), dt.date(2026, 12, 1), "#F3E6DC",
     "Que te descubran y que confíen. El 27 es el día fuerte."),
    ("rg", "Mes del regalo", dt.date(2026, 12, 2), dt.date(2026, 12, 14), "#EDE3F1",
     "Regalo + aguinaldo. Último día para encargos: 15 dic."),
    ("ul", "Última llamada", dt.date(2026, 12, 15), dt.date(2026, 12, 24), "#E3EDE4",
     "Solo lo que hay en La Paz. Regalo de último minuto."),
]

# ---------------------------------------------------------------- día a día
# (fecha, (fmt, gancho, qué grabar), (fmt, gancho, qué grabar), venta del día, marca)
D = dt.date
PLAN = [
    (D(2026,11,25), ("C", "Esto no se ve en fotos", "Mafalda 2128: cierre y forro"),
                    ("H", "Comprar en VESTA: 3 pasos", "Celular + WhatsApp + entrega"),
                    "Difusión: «se viene Black Friday»", ""),
    (D(2026,11,26), ("D", "¿Rosado o celeste?", "Mafalda 2128 en las dos manos"),
                    ("G", "Preparando el viernes", "Empacando pedidos en la mesa"),
                    "Marketplace: 3 carteras con precio", ""),
    (D(2026,11,27), ("F", "Tu regalo de Black Friday", "Cartera + bolsa + tarjeta"),
                    ("E", "Abrimos la caja", "Caja nueva, 3 modelos"),
                    "9:00 difusión con la promo · estados cada 3 h", "Black Friday"),
    (D(2026,11,28), ("B", "¿Le entra todo? Mira", "Garfield 2141 hasta llenarla"),
                    ("I", "¿Pagas al recibir? Sí", "Respuesta escrita en pantalla"),
                    "Seguimiento a quien preguntó ayer (1 vez)", ""),
    (D(2026,11,29), ("J", "Vesta elige por ti", "Mascota + 3 carteras"),
                    ("A", "Lo que llevo un domingo", "Manos, cosas una por una"),
                    "Grabar en tanda + llenar planilla", "Tanda"),
    (D(2026,11,30), ("C", "Garfield, pero elegante", "Dibujo y costuras de cerca"),
                    ("F", "Para mamá esta Navidad", "Cartera y billetera juntas"),
                    "Difusión de novedades", ""),
    (D(2026,12,1),  ("D", "Elige: 1, 2 o 3", "Tres modelos en fila"),
                    ("G", "Así entregamos en La Paz", "Mano entrega la bolsa"),
                    "Marketplace: renovar publicaciones", ""),
    (D(2026,12,2),  ("F", "Para tu mejor amiga", "Bolsa de regalo + tarjeta"),
                    ("H", "¿No está? Lo traemos", "Catálogo en pantalla"),
                    "Aviso: encargos hasta el 15 dic", ""),
    (D(2026,12,3),  ("A", "Lo que lleva mi mamá", "Cosas de mamá, manos"),
                    ("J", "¿Qué le regalo? Vesta te ayuda", "Mascota + 2 opciones"),
                    "Estados de WhatsApp de la familia", ""),
    (D(2026,12,4),  ("E", "Llegó para Navidad", "Caja abierta, novedades"),
                    ("C", "Brillo bajo la luz", "Giro lento junto a la ventana"),
                    "Marketplace: 3 publicaciones", ""),
    (D(2026,12,5),  ("B", "¿Mini o grande?", "Billetera 2133 vs. cartera"),
                    ("I", "¿Envían a todo Bolivia?", "Respuesta + flota"),
                    "Seguimiento de consultas", ""),
    (D(2026,12,6),  ("F", "El combo que se nota", "Cartera + billetera Mafalda"),
                    ("G", "Empacando regalos (ASMR)", "Papel, cinta, tarjeta"),
                    "Tanda + revisar los primeros 10 videos", "Tanda"),
    (D(2026,12,7),  ("D", "Mafalda o Garfield", "Dos carteras lado a lado"),
                    ("F", "Para tu hermana", "Cartera colgada + moño"),
                    "Difusión: «regalos de Navidad»", ""),
    (D(2026,12,8),  ("C", "Stitch de cerca", "Mochila 2100: corazón y cierre"),
                    ("H", "En La Paz pagas al recibir", "Entrega + billete en mano"),
                    "Marketplace: renovar", ""),
    (D(2026,12,9),  ("F", "POV: ya sé qué regalarle", "Mano señala, aparece la cartera"),
                    ("A", "Lo que llevo a la oficina", "Cuaderno, cargador, lentes"),
                    "Aviso: encargos hasta el 15 dic", ""),
    (D(2026,12,10), ("J", "Vesta: según tu personaje", "Mascota + Mafalda/Garfield"),
                    ("E", "Unboxing de regalo", "Caja con moño se abre"),
                    "Estados de la familia", ""),
    (D(2026,12,11), ("B", "Todo para la fiesta", "Celular, labial, llaves"),
                    ("I", "¿Es original?", "Etiqueta y acabados"),
                    "Seguimiento de consultas", ""),
    (D(2026,12,12), ("F", "Idea para amigo secreto", "Billetera 2133 envuelta"),
                    ("G", "Un sábado de entregas", "Bolsas listas en fila"),
                    "Marketplace: 3 publicaciones", ""),
    (D(2026,12,13), ("D", "¿Cuál te pedirías?", "Tres modelos, comenta el número"),
                    ("F", "Para ti, te lo mereces", "Cartera al hombro"),
                    "Tanda + planilla de la semana", "Tanda"),
    (D(2026,12,14), ("H", "Mañana cierran los encargos", "Cuenta regresiva + catálogo"),
                    ("F", "Para mamá (versión 2)", "El que mejor rindió, repetido"),
                    "Difusión: último aviso de encargos", ""),
    (D(2026,12,15), ("F", "Lo que queda para Navidad", "Solo stock real en La Paz"),
                    ("G", "Empacando regalos", "Mesa llena de bolsas"),
                    "Difusión: stock disponible (solo real)", "Último encargo"),
    (D(2026,12,16), ("C", "Así se ve de verdad", "Luz natural, giro lento"),
                    ("I", "¿Llega antes del 24?", "«Te lo confirmamos por WhatsApp»"),
                    "Marketplace: lo que queda", ""),
    (D(2026,12,17), ("J", "Vesta: regalo según a quién", "Mamá · amiga · hermana"),
                    ("A", "Lo que llevo de compras", "Manos, cosas una por una"),
                    "Estados de la familia", ""),
    (D(2026,12,18), ("F", "Amigo secreto, resuelto", "Billetera + bolsa"),
                    ("E", "Últimas que llegaron", "Caja abierta"),
                    "Seguimiento de consultas", ""),
    (D(2026,12,19), ("B", "Todo para Nochebuena", "Llenas la cartera de fiesta"),
                    ("G", "Sábado de entregas", "Mano entrega la bolsa"),
                    "Marketplace: renovar", ""),
    (D(2026,12,20), ("F", "Llegó el aguinaldo: date un gusto", "Cartera al hombro"),
                    ("D", "¿Cuál te llevas?", "Dos colores lado a lado"),
                    "Difusión: «date un gusto»", "Aguinaldo"),
    (D(2026,12,21), ("F", "Regalo de último minuto", "Cartera envuelta en 10 s"),
                    ("H", "Cómo pedir hoy", "3 pasos rápidos"),
                    "Responder rápido: semana de cierre", ""),
    (D(2026,12,22), ("C", "El detalle que se nota", "Cierre y dije de cerca"),
                    ("G", "Así se van los regalos", "Bolsas que salen"),
                    "Seguimiento de consultas", ""),
    (D(2026,12,23), ("F", "Último día de entregas*", "Bolsa lista en la puerta"),
                    ("I", "Tu última duda", "Pregunta real"),
                    "Difusión: último aviso de entregas*", ""),
    (D(2026,12,24), ("J", "Feliz Navidad, de Vesta", "Mascota + logo"),
                    ("G", "Gracias por este año", "Manos de la familia, sin caras"),
                    "Mensaje de gracias a clientas", "Nochebuena"),
]

DIAS = ["lun", "mar", "mié", "jue", "vie", "sáb", "dom"]
MESES = {11: "nov", 12: "dic"}


def fdate(d):
    return f"{DIAS[d.weekday()]} {d.day} {MESES[d.month]}"


def phase_of(d):
    for p in PHASES:
        if p[2] <= d <= p[3]:
            return p
    return None


def chip(f, big=False):
    name, _, bg, fg = FORMATS[f]
    cls = "chip big" if big else "chip"
    return f'<span class="{cls}" style="background:{bg};color:{fg}">{f}</span>'


def e(s):
    return html.escape(s, quote=False)


# ---------------------------------------------------------------- teléfono
ICONS = """<div class="ui"><i class="ic heart"></i><i class="ic"></i><i class="ic"></i></div>"""


def phone(fr, cls=""):
    """fr: dict(img, img2, zoom, x, y, text, small, kind)"""
    kind = fr.get("kind", "photo")
    if kind == "end":
        inner = (f'<div class="scr end"><img class="mascot" src="{IMG}mascota-vesta.png">'
                 f'<img class="lw" src="{IMG}logo-white.png">'
                 f'<div class="endt">Compra en Vesta Bags</div>'
                 f'<div class="endw">Escríbenos por WhatsApp</div><div class="snow"></div></div>')
        return f'<div class="phone {cls}">{inner}</div>'
    bg = fr.get("bg", "#F3E9E1")
    z = fr.get("zoom", 1)
    x, y = fr.get("x", 50), fr.get("y", 50)
    if kind == "two":
        media = (f'<div class="two"><img src="{IMG}{fr["img"]}"><img src="{IMG}{fr["img2"]}"></div>')
    elif kind == "gift":
        media = (f'<img class="prod" style="transform:scale({z});transform-origin:{x}% {y}%" src="{IMG}{fr["img"]}">'
                 '<div class="box"><div class="lid"></div><div class="rib"></div></div>')
    elif kind == "box":
        media = '<div class="box solo"><div class="lid"></div><div class="rib"></div></div>'
    elif kind == "msg":
        media = (f'<div class="chat"><div class="b in">{e(fr["q"])}</div><div class="b out">{e(fr["a"])}</div></div>')
    elif kind == "mascot":
        media = (f'<img class="mascot2" src="{IMG}mascota-vesta.png">'
                 f'<div class="mini"><img src="{IMG}{fr["img"]}"><img src="{IMG}{fr["img2"]}"></div>')
    else:
        media = f'<img class="prod" style="transform:scale({z});transform-origin:{x}% {y}%" src="{IMG}{fr["img"]}">'
    txt = f'<div class="ost">{e(fr["text"])}</div>' if fr.get("text") else ""
    small = f'<div class="ost2">{e(fr["small"])}</div>' if fr.get("small") else ""
    cap = '<div class="cap"><b>VESTA BAGS</b><span>Escríbenos por WhatsApp 🤍</span></div>'
    return (f'<div class="phone {cls}"><div class="scr" style="background:{bg}">{media}{txt}{small}'
            f'{ICONS}{cap}</div></div>')


# ---------------------------------------------------------------- videos estrella
STARS = [
    dict(id="regalo-yo", fmt="F", title="«¿Qué quieres de regalo?» «Yo:»",
         ref="@carteras.lux (Ecuador)", refurl="https://www.tiktok.com/@carteras.lux",
         refdata="65,5 mil me gusta en su video de este formato",
         when="27 nov · 9 dic · 20 dic", est="150 – 600",
         basis="Es el ángulo de regalo, el de más alcance en las referencias. Tu base hoy es < 100.",
         audio="Audio en tendencia de la biblioteca comercial, alegre",
         steps=["Toma 1: una mano señala la cámara. Texto: «¿Qué quieres de regalo?»",
                "Toma 2: corte seco y la cartera aparece en tus manos. Texto: «Yo:»",
                "Toma 3: giro lento y detalle del dibujo, 3 s",
                "Cierre: la animación «Compra en Vesta Bags»"],
         frames=[dict(img="2128-1.jpg", zoom=0.55, text="¿Qué quieres de regalo?", bg="#F7EDE6"),
                 dict(img="2128-1.jpg", zoom=1.0, text="Yo:", bg="#F7E3E8"),
                 dict(img="2128-1.jpg", zoom=2.1, x=60, y=62, small="Mafalda 2128", bg="#F7E3E8"),
                 dict(kind="end")]),
    dict(id="caja-regalo", fmt="E", title="La caja de regalo que se abre",
         ref="@theprincesssboutiqu4", refurl="https://www.tiktok.com/@theprincesssboutiqu4",
         refdata="89,1 mil me gusta en su video de caja de regalo",
         when="27 nov · 10 dic · 18 dic", est="150 – 500",
         basis="El formato de caja de regalo fue de los más fuertes en las referencias. Tu base es < 100.",
         audio="Sonido ASMR del papel + música suave",
         steps=["Caja cerrada con cinta sobre una mesa blanca. Texto: «Abre conmigo»",
                "Tiras la cinta en un solo movimiento (con sonido real)",
                "Levantas la cartera despacio desde el papel",
                "Cierre: la animación «Compra en Vesta Bags»"],
         frames=[dict(kind="box", text="Abre conmigo", bg="#FFFFFF"),
                 dict(kind="gift", img="2122-1.jpg", zoom=0.5, y=100, small="shhh… papel", bg="#FFFFFF"),
                 dict(img="2122-1.jpg", zoom=1.0, text="Para ti", bg="#F6EFE8"),
                 dict(kind="end")]),
    dict(id="colgada", fmt="C", title="La cartera colgada que gira",
         ref="@jailinnebags (Colombia)", refurl="https://www.tiktok.com/@jailinnebags",
         refdata="Sus videos más vistos van de 266 mil a 1,9 millones de vistas, sin cara ni voz",
         when="30 nov · 7 dic · 22 dic", est="100 – 500 (puede dispararse)",
         basis="Es el formato con más vistas de todas las referencias, aunque es de otra cuenta y otro país.",
         audio="Audio en tendencia, lento y elegante",
         steps=["Cuelgas la cartera de un gancho sobre una pared blanca, con luz de ventana",
                "Le das un toque suave para que gire sola",
                "Primer plano del dije o del cierre mientras gira",
                "Cierre: la animación «Compra en Vesta Bags»"],
         frames=[dict(img="2141-1.jpg", zoom=0.9, text="Garfield, pero elegante", bg="#FFFFFF"),
                 dict(img="2141-2.jpg", zoom=0.9, bg="#FFFFFF"),
                 dict(img="2141-1.jpg", zoom=2.4, x=30, y=40, small="el dije ✨", bg="#FFFFFF"),
                 dict(kind="end")]),
    dict(id="por-dentro", fmt="B", title="¿Le entra todo? Mírala por dentro",
         ref="@moon_notes04 y @saenggiepp", refurl="https://www.tiktok.com/@saenggiepp",
         refdata="109,7 mil y 186,7 mil me gusta, decorando la cartera y viéndola por dentro",
         when="28 nov · 5 dic · 19 dic", est="100 – 400",
         basis="Ver la cartera por dentro tuvo mucho alcance en las referencias, y responde la duda de «¿me entra?».",
         audio="Audio en tendencia + sonido real de cada cosa al entrar",
         steps=["Cartera abierta y vacía, vista desde arriba. Texto: «¿Le entra todo?»",
                "Metes las cosas una por una: celular, billetera, labial, llaves, botella",
                "La cierras sin esfuerzo. Texto: «Sí, y sobra espacio»",
                "Cierre: la animación «Compra en Vesta Bags»"],
         frames=[dict(img="2144-1.jpg", zoom=0.8, text="¿Le entra todo?", bg="#F4EEE6"),
                 dict(img="2133-1.jpg", zoom=0.8, small="billetera ✓ celular ✓ labial ✓", bg="#F4EEE6"),
                 dict(img="2144-1.jpg", zoom=1.0, text="Sí, y sobra", bg="#F4EEE6"),
                 dict(kind="end")]),
    dict(id="rosado-celeste", fmt="D", title="¿Rosado o celeste?",
         ref="Sin video de referencia externo", refurl="",
         refdata="Es el formato de encuesta de tu calendario: genera comentarios",
         when="26 nov · 7 dic · 20 dic", est="80 – 300",
         basis="Rinde más en comentarios que en vistas, y los comentarios le dicen a TikTok que siga mostrando el video.",
         audio="Audio en tendencia, alegre",
         steps=["Una cartera en cada mano frente a la cámara. Texto: «¿Rosado o celeste?»",
                "Acercas la rosada (2 s) y después la celeste (2 s)",
                "Juntas las dos. Texto: «Comenta tu color»",
                "Cierre: la animación «Compra en Vesta Bags»"],
         frames=[dict(kind="two", img="2128-1.jpg", img2="2128-2.jpg", text="¿Rosado o celeste?", bg="#FFFFFF"),
                 dict(img="2128-1.jpg", zoom=1.0, small="rosado", bg="#F8E2E8"),
                 dict(img="2128-2.jpg", zoom=1.0, small="celeste", bg="#E2EDF6"),
                 dict(kind="end")]),
    dict(id="pagas-al-recibir", fmt="H", title="En La Paz pagas al recibir",
         ref="Sin video de referencia externo", refurl="",
         refdata="Sale de la investigación del 18 nov: la desconfianza es el gran freno para comprar",
         when="25 nov · 8 dic · 21 dic", est="80 – 250",
         basis="Tiene menos alcance, pero es el video que más convierte. Es una hipótesis que hay que medir con los mensajes.",
         audio="Voz de mujer (IA etiquetada o amiga) + música suave",
         steps=["Chat de WhatsApp en pantalla: «¿Puedo pagar al recibir?»",
                "Respuesta: «Sí 🤍 En La Paz pagas cuando te la entregamos»",
                "Mano que entrega la bolsa y mano que recibe (sin caras)",
                "Cierre: la animación «Compra en Vesta Bags»"],
         frames=[dict(kind="msg", q="¿Puedo pagar al recibir?", a="Sí 🤍 En La Paz pagas cuando te la entregamos", bg="#EFE8E1"),
                 dict(img="2125-1.jpg", zoom=0.9, text="Así de simple", bg="#FFFFFF"),
                 dict(img="2125-1.jpg", zoom=1.7, x=50, y=70, small="QR · transferencia · efectivo", bg="#FFFFFF"),
                 dict(kind="end")]),
]

FRAME_T = ["0–2 s", "2–6 s", "6–10 s", "cierre"]

# ---------------------------------------------------------------- estilos
CSS = r"""
@page { size: 297mm 210mm; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
:root { --ink:#221B18; --ink2:#4B3B33; --mut:#8A776B; --cacao:#7A4B3A; --deep:#4E3A30;
        --nude:#F3E9E1; --line:#EEE4DC; }
html, body { background:#FFFFFF; }
body { font-family: "Comfortaa", "Varela Round", Arial, sans-serif; color: var(--ink);
       -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.page { width:297mm; height:210mm; padding:13mm 16mm 11mm; position:relative; overflow:hidden;
        break-after: page; background:#FFFFFF; }
.page:last-child { break-after: auto; }
.top { display:flex; justify-content:space-between; align-items:center; font-size:7.5pt;
       color:var(--mut); letter-spacing:.14em; text-transform:uppercase; margin-bottom:6mm; }
.top img { height:6mm; }
h1 { font-weight:700; font-size:40pt; line-height:1.02; letter-spacing:-.02em; }
h2 { font-weight:700; font-size:22pt; letter-spacing:-.01em; margin-bottom:2mm; }
.lead { font-size:11pt; color:var(--ink2); line-height:1.55; max-width:150mm; }
.kick { font-size:8pt; letter-spacing:.2em; text-transform:uppercase; color:var(--cacao); font-weight:700; margin-bottom:2mm; }
.foot { position:absolute; left:16mm; right:16mm; bottom:7mm; display:flex; justify-content:space-between;
        font-size:7pt; color:var(--mut); }
.chip { display:inline-flex; align-items:center; justify-content:center; width:6.2mm; height:6.2mm;
        border-radius:999px; font-weight:700; font-size:8pt; flex:none; }
.chip.big { width:11mm; height:11mm; font-size:14pt; }
.tag { display:inline-block; font-size:6.8pt; font-weight:700; letter-spacing:.06em; text-transform:uppercase;
       padding:.8mm 2.4mm; border-radius:999px; border:1px solid var(--cacao); color:var(--cacao); }
.tag.fill { background:var(--cacao); color:#fff; }
.tag.soft { background:var(--nude); border-color:var(--nude); color:var(--deep); }

/* portada */
.cover { display:grid; grid-template-columns: 1.15fr 1fr; gap:10mm; height:100%; align-items:center; }
.cover .arch { height:172mm; border-radius:90mm 90mm 8mm 8mm; background:var(--nude); position:relative;
               display:flex; align-items:flex-end; justify-content:center; overflow:hidden; }
.cover .arch img.p { width:88%; mix-blend-mode:multiply; margin-bottom:6mm; }
.cover .arch img.m { position:absolute; width:30mm; right:8mm; top:30mm; }
.cover .dates { display:flex; gap:3mm; margin:7mm 0 8mm; flex-wrap:wrap; }
.cover .dates span { font-size:9pt; padding:2mm 4mm; border-radius:999px; background:var(--nude); }
.cover .dates span.on { background:var(--cacao); color:#fff; }

/* bases */
.grid3 { display:grid; grid-template-columns:repeat(3,1fr); gap:5mm; }
.grid4 { display:grid; grid-template-columns:repeat(4,1fr); gap:4mm; }
.grid5 { display:grid; grid-template-columns:repeat(5,1fr); gap:3.5mm; }
.card { background:var(--nude); border-radius:6mm; padding:5mm; }
.card.w { background:#fff; border:1px solid var(--line); }
.card.d { background:var(--deep); color:#fff; }
.card h3 { font-size:10.5pt; font-weight:700; margin-bottom:2mm; }
.card p, .card li { font-size:9.6pt; line-height:1.55; color:inherit; }
.card ul { list-style:none; }
.card li { padding-left:4mm; position:relative; margin-bottom:1.3mm; }
.card li:before { content:""; position:absolute; left:0; top:1.6mm; width:1.6mm; height:1.6mm; border-radius:99px; background:var(--cacao); }
.card.d li:before { background:#E6D0BE; }
.num { font-size:30pt; font-weight:700; color:var(--cacao); line-height:1; }
.card.d .num { color:#F0E2D6; }
.rule { display:flex; gap:3mm; align-items:flex-start; }
.rule b.n { flex:none; width:7mm; height:7mm; border-radius:99px; background:var(--cacao); color:#fff;
            display:flex; align-items:center; justify-content:center; font-size:8.5pt; }
.rule p { font-size:10pt; line-height:1.5; }

/* formatos */
.fmt { border-radius:6mm; padding:5mm; min-height:54mm; position:relative; }
.fmt .l { font-size:22pt; font-weight:700; line-height:1; }
.fmt .t { font-size:11.5pt; font-weight:700; margin:2.5mm 0 1.2mm; }
.fmt .s { font-size:9pt; line-height:1.45; opacity:.85; }
.fmt .new { position:absolute; top:4mm; right:4mm; font-size:6.5pt; font-weight:700; letter-spacing:.08em;
            text-transform:uppercase; padding:.6mm 2mm; border-radius:99px; background:#fff; color:var(--cacao); }
.fmt img.mm { position:absolute; right:3mm; bottom:2mm; width:12mm; }

/* mapa del mes */
.cal { display:grid; grid-template-columns:repeat(7,1fr); gap:2.2mm; margin-top:4mm; }
.cal .h { font-size:7.5pt; color:var(--mut); text-align:center; letter-spacing:.1em; text-transform:uppercase; padding-bottom:1mm; }
.cal .d { border-radius:3.5mm; height:23.5mm; padding:2mm 2.4mm; position:relative; font-size:7pt; }
.cal .d .n { font-size:11pt; font-weight:700; }
.cal .d .ch { display:flex; gap:1mm; position:absolute; left:2.4mm; bottom:2mm; }
.cal .d .ch .chip { width:5mm; height:5mm; font-size:6.5pt; }
.cal .d .mk { position:absolute; right:2mm; top:2.2mm; font-size:6pt; font-weight:700; color:#fff;
              background:var(--cacao); border-radius:99px; padding:.5mm 1.8mm; }
.cal .d.x { background:transparent; }
.legend { display:flex; gap:5mm; margin-top:4mm; font-size:8pt; align-items:center; flex-wrap:wrap; }
.legend i { display:inline-block; width:4mm; height:4mm; border-radius:99px; margin-right:1.5mm; vertical-align:-1mm; }

/* ventas */
.funnel { display:flex; align-items:stretch; gap:2.4mm; margin:3mm 0 5mm; }
.funnel .st { flex:1; border-radius:5mm; padding:3.5mm 3mm; text-align:center; font-size:8pt; line-height:1.4; }
.funnel .st b { display:block; font-size:9.5pt; margin-bottom:1mm; }
.funnel .ar { align-self:center; color:var(--cacao); font-size:12pt; }
.time { display:grid; grid-template-columns:17mm 1fr; gap:2.4mm 3mm; font-size:9.4pt; line-height:1.4; }
.time b { color:var(--cacao); }
.msg { background:#fff; border:1px solid var(--line); border-radius:5mm 5mm 5mm 1.5mm; padding:3mm 3.5mm;
       font-size:9.3pt; line-height:1.55; margin-bottom:3.5mm; }
.msg small { display:block; font-size:6.8pt; letter-spacing:.1em; text-transform:uppercase; color:var(--cacao); font-weight:700; margin-bottom:1mm; }

/* día a día */
.days { width:100%; border-collapse:separate; border-spacing:0 1.6mm; margin-top:1mm; }
.days th { font-size:7pt; color:var(--mut); letter-spacing:.12em; text-transform:uppercase; text-align:left;
           font-weight:700; padding:0 2.5mm; }
.days td { background:#fff; border-top:1px solid var(--line); border-bottom:1px solid var(--line);
           padding:2.1mm 2.5mm; vertical-align:middle; font-size:8.3pt; }
.days td:first-child { border-left:1px solid var(--line); border-radius:4mm 0 0 4mm; width:25mm; }
.days td:last-child { border-right:1px solid var(--line); border-radius:0 4mm 4mm 0; width:64mm; color:var(--ink2); font-size:7.9pt; }
.days td.dt b { display:block; font-size:10pt; }
.days td.dt span { font-size:7pt; color:var(--mut); }
.days tr.hot td { background:#FBF4EF; border-color:#EBD9CC; }
.vid { display:flex; gap:2.2mm; align-items:center; }
.vid div b { display:block; font-size:8.6pt; line-height:1.3; }
.vid div span { font-size:7.2pt; color:var(--mut); line-height:1.3; }
.mark { display:table; font-size:6.4pt; font-weight:700; background:var(--cacao); color:#fff; border-radius:99px; padding:.4mm 1.8mm;
        margin-top:1mm; white-space:nowrap; letter-spacing:.04em; }
.days.roomy td { padding:4.1mm 3mm; }
.days:not(.roomy) .mark { display:inline-block; margin:0 0 0 1mm; }
.days:not(.roomy) td { padding:1.8mm 2.5mm; }
.days td.dt span.mark { color:#fff; font-size:6.4pt; }
.days.roomy .vid div b { font-size:10pt; }
.days.roomy .vid div span { font-size:8pt; }
.days.roomy td:last-child { font-size:9pt; }
.days.roomy .chip { width:7.4mm; height:7.4mm; font-size:9pt; }
.phase-h { display:flex; align-items:baseline; gap:4mm; }
.phase-h .pill { font-size:8pt; padding:1.2mm 3.5mm; border-radius:99px; color:var(--deep); font-weight:700; }

/* teléfono */
.phone { width:31mm; height:60mm; border-radius:5.5mm; background:var(--deep); padding:1.3mm; flex:none;
         box-shadow: 0 2mm 5mm rgba(78,58,48,.16); }
.scr { width:100%; height:100%; border-radius:4.4mm; overflow:hidden; position:relative; }
.scr img.prod { position:absolute; left:6%; top:16%; width:88%; mix-blend-mode:multiply; }
.scr .two { position:absolute; left:3%; right:3%; top:26%; display:flex; gap:2%; }
.scr .two img { width:49%; mix-blend-mode:multiply; }
.ost { position:absolute; left:8%; right:8%; top:9%; text-align:center; font-weight:700; font-size:7.6pt; line-height:1.25;
       color:var(--ink); background:rgba(255,255,255,.92); border-radius:2.4mm; padding:1.4mm 1.6mm; }
.ost2 { position:absolute; left:10%; right:22%; bottom:17%; text-align:center; font-size:6pt; font-weight:700;
        color:#fff; background:rgba(78,58,48,.82); border-radius:99px; padding:.9mm 1.4mm; }
.ui { position:absolute; right:1.6mm; top:44%; display:flex; flex-direction:column; gap:1.8mm; }
.ui .ic { width:3.6mm; height:3.6mm; border-radius:99px; background:rgba(255,255,255,.9); box-shadow:0 0 0 .3mm rgba(78,58,48,.15); }
.ui .ic.heart { background:#E7B3C1; }
.cap { position:absolute; left:2.2mm; bottom:2.4mm; right:7mm; font-size:4.9pt; line-height:1.35; color:var(--ink); }
.cap b { display:block; font-size:5.4pt; }
.scr.end { background:var(--deep); display:flex; flex-direction:column; align-items:center; justify-content:center; gap:1.5mm; }
.scr.end .mascot { width:15mm; }
.scr.end .lw { width:16mm; }
.scr.end .endt { color:#fff; font-size:7pt; font-weight:700; text-align:center; }
.scr.end .endw { color:#E6D0BE; font-size:5.4pt; }
.box { position:absolute; left:20%; right:20%; bottom:20%; height:28%; background:#E6D0BE; border-radius:1.6mm; }
.box.solo { top:34%; bottom:auto; height:32%; }
.box .lid { position:absolute; left:-6%; right:-6%; top:-14%; height:26%; background:#D9BDA6; border-radius:1.4mm; }
.box .rib { position:absolute; left:44%; width:12%; top:-14%; bottom:0; background:var(--cacao); }
.chat { position:absolute; left:6%; right:6%; top:26%; display:flex; flex-direction:column; gap:2mm; }
.chat .b { font-size:6.2pt; line-height:1.35; padding:1.6mm 2mm; border-radius:2.4mm; max-width:85%; }
.chat .in { background:#fff; align-self:flex-start; }
.chat .out { background:#E3EFD9; align-self:flex-end; }
.mascot2 { position:absolute; width:13mm; left:50%; transform:translateX(-50%); top:25%; }
.mini { position:absolute; left:8%; right:8%; bottom:20%; display:flex; gap:4%; }
.mini img { width:48%; mix-blend-mode:multiply; background:#fff; border-radius:1.5mm; }

/* videos estrella */
.star { display:grid; grid-template-columns: auto 1fr; gap:7mm; height:79mm; padding:4mm 0; border-bottom:1px solid var(--line); }
.star:last-child { border-bottom:0; }
.frames { display:flex; gap:2.6mm; }
.frames .fw { display:flex; flex-direction:column; align-items:center; gap:1.4mm; }
.frames .fw small { font-size:6.6pt; color:var(--mut); }
.sinfo h3 { font-size:13pt; font-weight:700; margin:1mm 0 2.5mm; display:flex; gap:2.5mm; align-items:center; }
.sinfo ol { list-style:none; counter-reset:s; margin-bottom:2.5mm; }
.sinfo ol li { counter-increment:s; font-size:8.3pt; line-height:1.45; padding-left:6.5mm; position:relative; margin-bottom:1.1mm; }
.sinfo ol li:before { content:counter(s); position:absolute; left:0; top:.2mm; width:4.4mm; height:4.4mm; border-radius:99px;
                      background:var(--nude); color:var(--cacao); font-size:6.8pt; font-weight:700; display:flex; align-items:center; justify-content:center; }
.facts { display:grid; grid-template-columns: 1fr 1fr; gap:2mm 5mm; font-size:7.8pt; line-height:1.4; }
.facts div small { display:block; font-size:6.4pt; letter-spacing:.1em; text-transform:uppercase; color:var(--mut); font-weight:700; margin-bottom:.4mm; }
.facts a { color:var(--cacao); text-decoration:none; }
.est { font-weight:700; color:var(--cacao); font-size:10pt; }

/* medir */
.score { width:100%; border-collapse:collapse; font-size:8.3pt; margin-top:3mm; }
.score th { text-align:left; font-size:7pt; letter-spacing:.1em; text-transform:uppercase; color:var(--mut); padding:2mm; border-bottom:1.5px solid var(--line); }
.score td { padding:3.6mm 2mm; font-size:9.2pt; border-bottom:1px solid var(--line); }
.score td.blank { color:#D9C9BC; }
"""


def top(label):
    return (f'<div class="top"><span>VESTA BAGS · {label}</span>'
            f'<img src="{IMG}logo-dark.png"></div>')


def foot(n):
    return (f'<div class="foot"><span>Plan de ventas y contenido · 25 nov – 24 dic 2026</span>'
            f'<span>{n}</span></div>')


def page_cover():
    return f"""
<section class="page"><div class="cover">
  <div>
    <div class="kick">Plan de ventas y contenido</div>
    <h1>Navidad<br>con VESTA</h1>
    <div class="dates">
      <span class="on">25 nov – 24 dic</span><span>2 videos al día</span><span>12:00 · 19:30</span><span>Todo cierra en WhatsApp</span>
    </div>
    <p class="lead">Un mes, tres etapas, 60 videos y una rutina de ventas para cada día.
    Para que cada video lleve a una conversación y cada conversación, a una entrega.</p>
    <div style="display:flex;gap:2mm;margin-top:9mm;flex-wrap:wrap">
      <span class="tag fill">Dato</span><span class="tag">Estimación</span><span class="tag soft">Pendiente: lo decides tú</span>
    </div>
    <p style="font-size:7.5pt;color:var(--mut);margin-top:3mm;max-width:140mm;line-height:1.5">
    Fotos de producto de referencia: graba con tus carteras reales. Preparado el 18 nov 2026 a partir del
    calendario de 14 días y de la investigación «Cómo se vende en Bolivia».</p>
  </div>
  <div class="arch"><img class="m" src="{IMG}mascota-vesta.png"><img class="p" src="{IMG}2128-1.jpg"></div>
</div></section>"""


def page_bases():
    rules = [
        ("Un solo llamado", "«Escríbenos por WhatsApp». Nada más."),
        ("Siempre el mismo cierre", "La animación de Navidad «Compra en Vesta Bags», de 2 a 3 s."),
        ("Manos, no caras", "Manos, cartera, luz de ventana y fondo blanco o nude."),
        ("Confianza en cada video", "«En La Paz pagas al recibir», en el caption o en pantalla."),
        ("Solo lo confirmado", "Precio, stock y plazos solo si son reales. Si no: «te confirmamos por WhatsApp»."),
        ("IA etiquetada", "Si la voz es de IA: «voz generada con IA». No se menciona Tizza."),
    ]
    rules_html = "".join(f'<div class="rule"><b class="n">{i+1}</b><p><b>{a}</b><br>{b}</p></div>'
                         for i, (a, b) in enumerate(rules))
    return f"""
<section class="page">{top("Las bases")}
  <h2>Las bases</h2>
  <p class="lead" style="margin-bottom:6mm">Lo que no cambia en todo el mes.</p>
  <div class="grid3" style="margin-bottom:6mm">
    <div class="card d"><div class="num">60</div><h3 style="margin-top:2mm">videos en 30 días</h3>
      <p>2 al día, grabados en tanda los domingos y programados. Los mismos van a TikTok, Reels y Facebook.</p></div>
    <div class="card"><div class="num">12:00</div><h3 style="margin-top:2mm">y 19:30</h3>
      <p>Siguen siendo una hipótesis. La encuesta de 2023 marca el pico de uso entre las 19:00 y las 22:00 <span class="tag fill" style="font-size:5.8pt">Dato</span></p></div>
    <div class="card"><div class="num">9–19</div><h3 style="margin-top:2mm">horario de atención</h3>
      <p>Los mensajes que llegan después de las 19:30 reciben respuesta automática y se contestan a las 9:00 en punto.</p></div>
  </div>
  <div class="grid3" style="gap:5mm 8mm">{rules_html}</div>
  {foot(2)}
</section>"""


def page_formats():
    cards = []
    for k, (name, desc, bg, fg) in FORMATS.items():
        new = '<span class="new">Nuevo</span>' if k in NEW else ""
        mm = f'<img class="mm" src="{IMG}mascota-vesta.png">' if k == "J" else ""
        cards.append(f'<div class="fmt" style="background:{bg};color:{fg}">{new}{mm}<div class="l">{k}</div>'
                     f'<div class="t">{name}</div><div class="s">{e(desc)}</div></div>')
    return f"""
<section class="page">{top("Formatos")}
  <h2>10 formatos</h2>
  <p class="lead" style="margin-bottom:6mm">Los 7 de tu calendario más 3 nuevos que dan confianza.
  La letra aparece en cada día del plan.</p>
  <div class="grid5">{''.join(cards)}</div>
  <div class="card w" style="margin-top:6mm;display:flex;gap:8mm;align-items:center">
    <div style="flex:none" class="num">F</div>
    <p style="font-size:9pt;line-height:1.55">El <b>Regalo</b> es el formato del mes: aparece casi todos los días.
    <b>H</b>, <b>I</b> y <b>G</b> traen menos vistas, pero son los que hacen que alguien escriba.
    Lo que mejor rinda en la semana se repite la semana siguiente.</p>
  </div>
  {foot(3)}
</section>"""


def page_map():
    start = dt.date(2026, 11, 23)  # lunes
    end = dt.date(2026, 12, 27)
    plan = {p[0]: p for p in PLAN}
    cells = "".join(f'<div class="h">{d}</div>' for d in DIAS)
    d = start
    while d <= end:
        if d in plan:
            ph = phase_of(d)
            row = plan[d]
            mk = f'<span class="mk">{row[4]}</span>' if row[4] and row[4] != "Tanda" else ""
            cells += (f'<div class="d" style="background:{ph[4]}"><span class="n">{d.day}</span>'
                      f'<span style="color:var(--mut)"> {MESES[d.month]}</span>{mk}'
                      f'<div class="ch">{chip(row[1][0])}{chip(row[2][0])}</div></div>')
        else:
            cells += f'<div class="d x" style="color:#D9C9BC"><span class="n">{d.day}</span></div>'
        d += dt.timedelta(days=1)
    legend = "".join(f'<span><i style="background:{p[4]}"></i><b>{p[1]}</b> · {p[2].day} {MESES[p[2].month]} – {p[3].day} {MESES[p[3].month]}</span>' for p in PHASES)
    return f"""
<section class="page">{top("El mes de un vistazo")}
  <h2>El mes de un vistazo</h2>
  <div class="legend">{legend}</div>
  <div class="cal">{cells}</div>
  {foot(4)}
</section>"""


def page_phases():
    cards = ""
    goals = {
        "bf": ["Que te encuentren: 14 videos y 7 publicaciones en Marketplace",
               "Black Friday: promo [PENDIENTE: la decides tú]",
               "Primeras conversaciones; anota de dónde vienen"],
        "rg": ["El regalo, todos los días (formato F)",
               "Encargos a una semana hasta el 15 dic, con 50 % de adelanto",
               "El 6 dic: revisar los 10 primeros videos y repetir el mejor"],
        "ul": ["Solo vender lo que hay en La Paz",
               "Responder rápido: las clientas de último minuto no esperan",
               "Fecha límite de entregas: [PENDIENTE: confirmar]"],
    }
    for key, name, a, b, bg, line in PHASES:
        lis = "".join(f"<li>{x}</li>" for x in goals[key])
        cards += (f'<div class="card" style="background:{bg}"><div class="kick" style="color:var(--deep)">{a.day} {MESES[a.month]} – {b.day} {MESES[b.month]}</div>'
                  f'<h3 style="font-size:15pt">{name}</h3><p style="margin-bottom:3mm">{line}</p><ul>{lis}</ul></div>')
    return f"""
<section class="page">{top("Tres etapas")}
  <h2>Tres etapas</h2>
  <p class="lead" style="margin-bottom:6mm">Cada etapa tiene un objetivo de venta y su propio tipo de video.</p>
  <div class="grid3">{cards}</div>
  <div class="card w" style="margin-top:6mm">
    <h3>Fechas que mueven la plata</h3>
    <div class="grid4" style="margin-top:2mm">
      <div><span class="num" style="font-size:20pt">27</span><p><b>Black Friday</b><br>Está instalado en Bolivia desde 2015 <span class="tag fill" style="font-size:5.8pt">Dato</span></p></div>
      <div><span class="num" style="font-size:20pt">15</span><p><b>Último encargo</b><br>Pedidos para Navidad, según tu calendario</p></div>
      <div><span class="num" style="font-size:20pt">20</span><p><b>Aguinaldo</b><br>Se paga hasta el 20 dic <span class="tag" style="font-size:5.8pt">Por confirmar</span></p></div>
      <div><span class="num" style="font-size:20pt">24</span><p><b>Nochebuena</b><br>Regalo de último minuto</p></div>
    </div>
  </div>
  {foot(5)}
</section>"""


def page_sales():
    steps = [("Video", "TikTok · Reels · Facebook", "#F6E7DD"), ("WhatsApp", "Te escribe", "#F8E2E8"),
             ("Fotos reales", "y precio en Bs", "#E4EEE5"), ("Pago", "QR · transferencia · al recibir", "#E2EDF6"),
             ("Entrega", "La Paz o flota", "#EEE4F2"), ("Foto y recompra", "Lista de difusión", "#7A4B3A")]
    fun = ""
    for i, (a, b, bg) in enumerate(steps):
        col = "#fff" if bg == "#7A4B3A" else "var(--ink)"
        fun += f'<div class="st" style="background:{bg};color:{col}"><b>{a}</b>{b}</div>'
        if i < len(steps) - 1:
            fun += '<span class="ar">›</span>'
    day = [("9:00", "Responder todos los mensajes de la noche"),
           ("11:30", "Subir un estado de WhatsApp y publicar una cartera en Marketplace"),
           ("12:00", "Sale el video 1. Responder comentarios durante 30 min"),
           ("15:00", "Seguimiento: una sola vez a quien preguntó hace 24 h"),
           ("18:30", "Estado de WhatsApp con el video del día"),
           ("19:00", "Cierra la atención. Respuesta automática activada"),
           ("19:30", "Sale el video 2. Anotar los números en la planilla")]
    dayh = "".join(f"<b>{a}</b><span>{b}</span>" for a, b in day)
    week = [("Lunes", "Difusión de novedades"), ("Mié / sáb", "Renovar Marketplace"),
            ("Viernes", "Revisar qué video trajo mensajes"), ("Domingo", "Grabar en tanda y llenar la planilla")]
    weekh = "".join(f"<b>{a}</b><span>{b}</span>" for a, b in week)
    return f"""
<section class="page">{top("Plan de ventas")}
  <h2>Plan de ventas</h2>
  <p class="lead">Cómo un video se convierte en una entrega.</p>
  <div class="funnel">{fun}</div>
  <div class="grid3" style="grid-template-columns:1.2fr 1fr 1fr">
    <div class="card w"><h3>Rutina de cada día</h3><div class="time">{dayh}</div></div>
    <div class="card w"><h3>Rutina de cada semana</h3><div class="time" style="grid-template-columns:20mm 1fr">{weekh}</div>
      <h3 style="margin-top:5mm">Canales gratis</h3>
      <ul><li>Estados de WhatsApp de toda la familia</li><li>Marketplace con fotos reales y precio</li><li>Grupos de Facebook de La Paz que lo permitan</li></ul></div>
    <div class="card d"><h3>Metas de la semana</h3>
      <ul><li>14 videos publicados</li><li>14 estados de WhatsApp</li><li>7 publicaciones en Marketplace</li>
      <li>1 difusión</li><li>Todos los mensajes respondidos dentro del horario</li></ul>
      <p style="margin-top:3mm;opacity:.85">La meta de ventas en Bs se fija con los números de tu primera semana. Hoy: [PENDIENTE]</p></div>
  </div>
  {foot(6)}
</section>"""


def page_sales2():
    msgs = [
        ("Difusión Black Friday · 27 nov", "Hola 🤍 Hoy es Black Friday en VESTA: [PROMO CONFIRMADA]. Responde «QUIERO» y te mandamos fotos y precio. En La Paz pagas al recibir."),
        ("Difusión regalo · lunes de diciembre", "Hola 🤍 ¿Ya tienes el regalo de Navidad? Mira las que llegaron esta semana. Responde «QUIERO» y te mandamos fotos reales."),
        ("Último encargo · 14 dic", "Hola 🤍 Mañana 15 cerramos los encargos para Navidad. Si viste algo en el catálogo, escríbenos hoy y lo traemos con el 50 % de adelanto."),
        ("Seguimiento · una sola vez, a las 24 h", "Hola 🤍 ¿Pudiste ver la [modelo]? Si quieres, te ayudamos con el color o la entrega."),
    ]
    mh = "".join(f'<div class="msg"><small>{a}</small>{e(b)}</div>' for a, b in msgs)
    return f"""
<section class="page">{top("Plan de ventas")}
  <h2>Black Friday y mensajes listos</h2>
  <div class="grid3" style="grid-template-columns:1fr 1.25fr;margin-top:4mm">
    <div>
      <div class="card" style="margin-bottom:4mm"><h3>La promo del 27 <span class="tag">Pendiente: la decides tú</span></h3>
        <p style="margin-bottom:2mm">Tres opciones, ordenadas de la que más recomiendo a la que menos:</p>
        <ul><li><b>Regalo con la compra</b> (bolsa, tarjeta o un accesorio pequeño). No baja tu precio</li>
        <li><b>Delivery incluido en La Paz</b> ese día</li>
        <li><b>Descuento moderado</b>, solo si tu margen lo permite. Un precio «demasiado bueno» es justo la señal de estafa que la gente aprendió a evitar</li></ul></div>
      <div class="card d"><h3>Lo que nunca</h3>
        <ul><li>Precios, stock o plazos sin confirmar</li><li>Decir «pedido confirmado» solo porque te escribió</li>
        <li>Insistir más de una vez o escribir fuera de horario</li><li>Mencionar Tizza en piezas públicas</li></ul></div>
    </div>
    <div>{mh}</div>
  </div>
  {foot(7)}
</section>"""


def page_days(rows, title, n, note=""):
    body = ""
    for d, v1, v2, venta, marca in rows:
        mk = f'<span class="mark">{marca}</span>' if marca else ""
        hot = ' class="hot"' if marca and marca != "Tanda" else ""
        cell = lambda v: (f'<div class="vid">{chip(v[0])}<div><b>{e(v[1])}</b><span>{e(v[2])}</span></div></div>')
        body += (f'<tr{hot}><td class="dt"><b>{DIAS[d.weekday()]} {d.day}</b><span>{MESES[d.month]}</span>{mk}</td>'
                 f'<td>{cell(v1)}</td><td>{cell(v2)}</td><td>{e(venta)}</td></tr>')
    ph = phase_of(rows[0][0])
    return f"""
<section class="page">{top("Día a día")}
  <div class="phase-h"><h2>{title}</h2><span class="pill" style="background:{ph[4]}">{ph[1]}</span></div>
  <table class="days{' roomy' if len(rows) <= 7 else ''}"><tr><th>Día</th><th>12:00</th><th>19:30</th><th>Venta del día</th></tr>{body}</table>
  {f'<p style="font-size:7.2pt;color:var(--mut);margin-top:1mm">{note}</p>' if note else ''}
  {foot(n)}
</section>"""


def star_block(s):
    fr = "".join(f'<div class="fw">{phone(f)}<small>{FRAME_T[i]}</small></div>' for i, f in enumerate(s["frames"]))
    steps = "".join(f"<li>{e(x)}</li>" for x in s["steps"])
    ref = (f'<a href="{s["refurl"]}">{e(s["ref"])}</a>' if s["refurl"] else e(s["ref"]))
    return f"""
<div class="star"><div class="frames">{fr}</div>
  <div class="sinfo">
    <div style="display:flex;gap:2mm;align-items:center"><span class="tag soft">Sale el {s["when"]}</span></div>
    <h3>{chip(s["fmt"])} {e(s["title"])}</h3>
    <ol>{steps}</ol>
    <div class="facts">
      <div><small>Referencia</small>{ref}<br><span style="color:var(--mut)">{e(s["refdata"])}. Video exacto: sin dato</span></div>
      <div><small>Vistas estimadas <span class="tag" style="font-size:5.4pt;padding:.2mm 1.4mm">Estimación</span></small><span class="est">{s["est"]}</span><br><span style="color:var(--mut)">{e(s["basis"])}</span></div>
      <div><small>Audio</small>{e(s["audio"])}</div>
      <div><small>Animación</small>animaciones/{s["id"]}.gif</div>
    </div>
  </div>
</div>"""


def page_stars(pair, n, first=False):
    head = ('<h2>6 videos que te recomiendo</h2><p class="lead" style="margin-bottom:1mm">Así se vería cada uno en TikTok. '
            'Cada uno se repite 3 veces en el mes, con otra cartera.</p>') if first else ""
    return f"""
<section class="page">{top("Videos recomendados")}{head}
  {''.join(star_block(s) for s in pair)}
  {foot(n)}
</section>"""


def page_measure(n):
    rows = ["Videos publicados", "Vistas promedio por video", "% del público de Bolivia",
            "Conversaciones nuevas de WhatsApp", "¿Cómo nos encontraste? (la red que más aparece)",
            "Pedidos cerrados", "Venta de la semana (Bs)", "El video que trajo más mensajes"]
    tr = "".join(f'<tr><td>{r}</td><td class="blank">____</td><td class="blank">____</td><td class="blank">____</td><td class="blank">____</td></tr>' for r in rows)
    return f"""
<section class="page">{top("Medir")}
  <h2>Planilla de cada domingo</h2>
  <p class="lead">Lo que se mide no son las vistas sino las conversaciones. Llénala y mándame una captura.</p>
  <div class="grid3" style="grid-template-columns:2.2fr 1fr;margin-top:2mm">
    <table class="score"><tr><th>Número</th><th>Sem 1 · 29 nov</th><th>Sem 2 · 6 dic</th><th>Sem 3 · 13 dic</th><th>Sem 4 · 20 dic</th></tr>{tr}</table>
    <div class="card"><h3>Cómo decidir</h3>
      <ul><li>Los 3 formatos con más <b>mensajes</b> pasan a ser fijos</li>
      <li>Si un video pasa las 1.000 vistas: haz una parte 2 al día siguiente</li>
      <li>Si un video trae mensajes: úsalo para el primer anuncio en Meta («clic a WhatsApp»), con un monto chico [PENDIENTE]</li>
      <li>Meta de vistas del calendario: un promedio de 300 a 500 por video <span class="tag" style="font-size:5.4pt">Meta, no dato</span></li></ul></div>
  </div>
  {foot(n)}
</section>"""


def build():
    pages = [page_cover(), page_bases(), page_formats(), page_map(), page_phases(), page_sales(), page_sales2()]
    n = 8
    pages.append(page_days(PLAN[0:7], "25 nov – 1 dic", n)); n += 1
    pages.append(page_days(PLAN[7:14], "2 – 8 dic", n)); n += 1
    pages.append(page_days(PLAN[14:20], "9 – 14 dic", n)); n += 1
    pages.append(page_days(PLAN[20:30], "15 – 24 dic", n,
                           "* La fecha límite de entregas se confirma antes de publicarla. Mientras tanto: «te lo confirmamos por WhatsApp».")); n += 1
    pages.append(page_stars(STARS[0:2], n, first=True)); n += 1
    pages.append(page_stars(STARS[2:4], n)); n += 1
    pages.append(page_stars(STARS[4:6], n)); n += 1
    pages.append(page_measure(n))
    head = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Navidad con VESTA</title>'
            '<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@400;500;600;700&display=swap" rel="stylesheet">'
            f'<style>{CSS}</style></head><body>')
    (HERE / "plan.html").write_text(head + "".join(pages) + "</body></html>", encoding="utf-8")

    # frames grandes para los GIF
    fr = ""
    for s in STARS:
        for i, f in enumerate(s["frames"]):
            fr += f'<div class="gf" id="{s["id"]}-{i}">{phone(f)}</div>'
    gcss = CSS + ".gf{display:inline-block;padding:4mm;background:#fff;zoom:3}"
    (HERE / "frames.html").write_text(
        '<!doctype html><html><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@400;500;600;700&display=swap" rel="stylesheet">'
        f'<style>{gcss}</style></head><body>{fr}</body></html>', encoding="utf-8")
    print("ok", len(pages), "páginas")


if __name__ == "__main__":
    build()
