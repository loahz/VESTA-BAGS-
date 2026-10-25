"""VESTA · 6 propuestas de feed (HTML → PDF). Reutiliza las piezas de gen3."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen3 as g
from gen3 import u, sty, P, floor, studio, word, stk, tape, notes, chat, receipt, google, bp, label, C, I

D = pathlib.Path(__file__).parent
M = I + "mascota-vesta.png"
P["lux"] = ("#F7F2EA", "#3B2A21", "#EADFCF", "#EFE6D8")
P["luxd"] = ("#4A3529", "#F3E9DC", "#5A4336", "#55402F")
P["sand"] = ("#EADBC8", "#3B2A21", "#DCC7AE", "#E2D0B8")
P["magenta"] = ("#F3D0E0", "#8E1450", "#E6A9C6", "#EBBCD2")
P["lime"] = ("#E4EDC4", "#3D5212", "#CFDC9C", "#D9E4B0")

EXTRA = """
.fr::after{content:"";position:absolute;inset:calc(var(--u)*.7);border:1px solid rgba(255,255,255,.55);pointer-events:none;z-index:9}
.lx{font-family:var(--fd);letter-spacing:.32em;text-transform:uppercase;font-size:calc(var(--u)*.62)}
.q{font-family:var(--fd);font-style:italic;line-height:1.08;letter-spacing:-.01em}
.crest{position:absolute;border-radius:50%;border:1px solid currentColor;display:grid;place-items:center}
.aguayo{position:absolute;left:0;right:0;height:calc(var(--u)*2.2);background:repeating-linear-gradient(90deg,#C2185B 0 calc(var(--u)*1.2),#F28C28 calc(var(--u)*1.2) calc(var(--u)*1.8),#1E7A4C calc(var(--u)*1.8) calc(var(--u)*2.6),#F6EBC8 calc(var(--u)*2.6) calc(var(--u)*2.9),#5B2A86 calc(var(--u)*2.9) calc(var(--u)*3.8),#F6EBC8 calc(var(--u)*3.8) calc(var(--u)*4.1));z-index:6}
.prop{display:grid;grid-template-columns:1fr auto;gap:10mm;align-items:center;height:100%}
.prop h2{font-family:var(--fd);font-weight:400;font-size:34px;line-height:1.02;letter-spacing:-.02em;margin:4px 0 8px}
.prop h2 em{font-style:italic}
.prop p{font-size:11px;line-height:1.55;color:var(--ink2);max-width:118mm}
.sw2{display:flex;gap:5px;margin:10px 0 4px}.sw2 b{width:26px;height:26px;border-radius:50%;border:1px solid rgba(0,0,0,.08)}
.pc{display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:8px;font-size:10px;line-height:1.5;color:var(--ink2)}
.pc h4{font-size:8.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--cacao);margin-bottom:3px}
.phone{background:#fff;border:1px solid var(--line);border-radius:22px;padding:14px 12px 12px;width:max-content;box-shadow:0 18px 40px rgba(34,27,24,.10)}
.phone .ph-h{display:flex;align-items:center;gap:10px;margin-bottom:10px}
.phone .av{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;overflow:hidden}
.g9{display:grid;grid-template-columns:repeat(3,1fr);gap:3px}
.g9 .sl{border-radius:0;box-shadow:none}
"""
CSS = g.CSS + EXTRA

def tile(c, inner, fr=False):
    return f'<div class="sl{" fr" if fr else ""}" style="{sty(c)}">{inner}</div>'
def lx(t, top=1.6, c="currentColor"):
    return f'<div class="lx" style="position:absolute;left:0;right:0;top:{u(top)};text-align:center;color:{c};z-index:6">{t}</div>'
def q(t, size=2, top=None, bottom=None, align="center", pad=2.2):
    pos = f"top:{u(top)}" if top is not None else f"bottom:{u(bottom)}"
    return f'<div class="q" style="position:absolute;left:{u(pad)};right:{u(pad)};{pos};text-align:{align};font-size:{u(size)};z-index:6">{t}</div>'
def small_prod(img, h=10, cy=52):
    return f'<img src="{C}{img}.png" style="position:absolute;left:50%;top:{cy}%;transform:translate(-50%,-50%);height:{u(h)};filter:drop-shadow(0 calc(var(--u)*.4) calc(var(--u)*.6) rgba(40,25,15,.18));z-index:4">'
def mascot(w, x, y, rot=0, z=5):
    return f'<img src="{M}" style="position:absolute;left:{u(x)};top:{u(y)};width:{u(w)};transform:rotate({rot}deg);z-index:{z};filter:drop-shadow(0 calc(var(--u)*.3) calc(var(--u)*.4) rgba(40,25,15,.15))">'
def ph(f, pos="center", extra=""):
    return f'<img class="ph" src="{I}{f}.jpg" style="object-position:{pos};{extra}">'
def big(t, size, top, c=None, font="var(--fp)", lh=1.42):
    col = f"color:{c};" if c else ""
    return f'<div style="position:absolute;left:{u(1.8)};right:{u(1.8)};top:{u(top)};font-family:{font};font-size:{u(size)};line-height:{lh};{col}z-index:6">{t}</div>'

props = []

# ---------- 1 · Vitrina Viva 2.0 ----------
t1 = [
 tile("pink", floor() + word("Rosa") + studio("tote_pink", 14, 6.4) + stk("350", "Bs", 16.8, 15, P["pink"][1], P["pink"][0], -8), True),
 tile("ivory", notes("Deseos 2026", [("<s>Un Porsche</s>", False), ("<s>Viaje a París</s>", False), ("Cartera VESTA", True)]), True),
 tile("garf", floor() + word("Garfield") + studio("garf_face", 11.5, 6.4) + stk("700", "Bs", 17, 15.2, P["garf"][1], P["garf"][0], -9), True),
 tile("ivory", ph("casa"), True),
 tile("stitch", floor() + word("Stitch") + studio("st_heart", 14.4, 6.4), True),
 tile("ivory", chat("Mamá 🤍", [("o", "¿Qué quieres de regalo?"), ("me", "nada mami"), ("img", ("hk_face", "hk"))]), True),
 tile("hk", floor() + word("Kitty") + studio("hk_face", 15, 6.4) + stk("700", "Bs", 17, 15.2, P["hk"][1], P["hk"][0], -9), True),
 tile("garf", receipt([("Cartera Garfield", "×1"), ("Lunes soportables", "×52"), ("Cumplidos", "×∞")], ("ARREPENTIMIENTOS", "0"), 2.4, 4, 19.2), True),
 tile("green", floor() + word("Verde") + studio("tote_green", 14, 6.4) + stk("350", "Bs", 16.8, 15, P["green"][1], P["green"][0], -8), True),
]
props.append(("01", "Vitrina Viva <em>2.0</em>", "La propuesta actual, ordenada. Un marco fino en todas las piezas une el feed, y el ritmo es fijo: producto, pantalla, producto en cada fila. Las diagonales repiten color y el perfil se ve como una tienda con humor.",
 [P["pink"][0], P["garf"][0], P["stitch"][0], P["hk"][0], "#FBF6F1"], "Bodoni Moda · Instrument Sans · mockups del sistema",
 "Vender y crecer a la vez. Es la más equilibrada.", "Necesita disciplina de ritmo; si se rompe el orden, se ve mezclado.", t1, "#F0E2D6"))

# ---------- 2 · Vesta protagonista ----------
t2 = [
 tile("nude", word("Hola", 30, 10) + mascot(13, 5.5, 6.2) + f'<div class="bot"><div class="t" style="font-size:{u(2.4)}">Hola, soy <em>Vesta</em></div></div>'),
 tile("garf", big("MI AMIGO<br>DE LOS LUNES", 1.9, 2.2, P["garf"][1]) + studio("garf_face", 10, 5.4, x=60) + mascot(8, 1.4, 15.4, -6)),
 tile("butter", big("VESTA<br>RECOMIENDA", 1.9, 2.2) + f'<div style="position:absolute;left:{u(2)};right:{u(2)};bottom:{u(2)};top:{u(8.4)};background:#fff;border-radius:{u(1)};z-index:3"></div>' + small_prod("tote_fucsia", 10, 64) + mascot(6.4, 15.6, 6.2, 8, 6)),
 tile("stitch", mascot(10, 2, 9, -4) + studio("st_back", 12, 5.6, x=68) + big("¿ME LLEVAS<br>A LA U?", 1.6, 2.2, P["stitch"][1])),
 tile("pink", f'<div style="position:absolute;left:50%;top:44%;transform:translate(-50%,-50%);font-family:var(--fp);font-size:{u(14)};color:#EEB3C7;z-index:2">?</div>' + mascot(10, 7, 9.5) + big("PREGÚNTALE<br>A VESTA", 1.6, 22.4, P["pink"][1])),
 tile("green", big("VESTA EMPACA<br>TU PEDIDO", 1.6, 2.2, P["green"][1]) + floor() + studio("tote_green", 9, 5.4, x=36) + mascot(9, 12.6, 12.4, 4)),
 tile("hk", mascot(7.4, 2, 15.8, -8) + studio("hk_face", 14, 5.4, x=62) + big("TIERNA PERO<br>CON CARÁCTER", 1.4, 2.2, P["hk"][1])),
 tile("caramel", big("VESTA EN<br>LA PAZ", 2, 2.2, P["caramel"][1]) + mascot(10, 7, 10.4) + f'<div class="hand" style="position:absolute;left:{u(2)};bottom:{u(2)};font-size:{u(1.3)};z-index:6">delivery a tu puerta</div>'),
 tile("ts", big("LA MOCHILA<br>FAVORITA", 1.7, 2.2, P["ts"][1]) + studio("ts_back", 13, 5.4, x=60) + mascot(7.4, 1.6, 15.6, -5)),
]
props.append(("02", "Vesta <em>protagonista</em>", "La mascota es la presentadora del feed: recomienda, pregunta, empaca y viaja. Siempre aparece junto a una cartera real, con titulares grandes y fondos de color planos. Es la cuenta más reconocible y la más tierna.",
 [P["garf"][0], P["butter"][0], P["stitch"][0], P["pink"][0], P["green"][0]], "Boldonse (titulares) · Bodoni Moda · letra a mano",
 "Crecer en alcance con un público joven y crear una marca recordable.", "Puede verse infantil si se abusa; hay que mantener siempre la cartera en primer plano.", t2, "#F7C98B"))

# ---------- 3 · Maison VESTA (lujo formal) ----------
t3 = [
 tile("lux", f'<img src="{I}logo-dark.png" style="position:absolute;left:50%;top:46%;transform:translate(-50%,-50%);width:{u(12)}">' + lx("La Paz · Bolivia", 24.6)),
 tile("lux", lx("Colección Otoño") + small_prod("caramel", 12.5, 50) + lx("Caramelo · Bs 700", 26.4)),
 tile("luxd", q("La elegancia no es pasar desapercibida, es ser recordada.", 1.7, 10.4) + lx("VESTA BAGS", 25.4, "#E6C9AE")),
 tile("lux", ph("casa", "center 30%", "filter:saturate(.75)")),
 tile("luxd", lx("Edición noche", 1.6, "#E6C9AE") + small_prod("gold", 11, 50) + lx("Dorada acolchada", 26.4, "#E6C9AE")),
 tile("lux", ph("mesa", "35% center", "filter:saturate(.7)")),
 tile("lux", q("Originales.<br>Directo de Tizza.", 2.2, 11.2) + lx("Distribuidores oficiales", 24.4)),
 tile("lux", lx("Colección Otoño") + small_prod("quilted", 11, 50) + lx("Acolchada · Bs 700", 26.4)),
 tile("sand", ph("pedestal", "center", "filter:saturate(.7)")),
]
props.append(("03", "Maison <em>VESTA</em>", "Lujo formal: marfil, arena y cacao profundo (nunca negro), productos pequeños con mucho aire, versalitas espaciadas y frases de marca. Pocas piezas de licencia y fotos con el color apagado. Se siente como una maison europea.",
 [P["lux"][0], P["sand"][0], P["luxd"][0], "#E6C9AE", "#3B2A21"], "Bodoni Moda en versalitas espaciadas · cursiva para frases",
 "Subir el valor percibido de las carteras clásicas y vender a clientas de 25 a 35 años.", "Menos viral; las licencias (Garfield, Stitch) pierden protagonismo.", t3, "#F7F2EA"))

# ---------- 4 · Lujo con humor ----------
t4 = [
 tile("lux", q("Lunes,<br>versión cuero.", 2.4, 4) + small_prod("caramel", 10.5, 64)),
 tile("lux", notes("Prioridades", [("<s>Ahorrar</s>", False), ("<s>Ir al gym</s>", False), ("Cartera nueva", True)])),
 tile("luxd", q("Sí, es original.<br>No, no te la presto.", 1.8, 10.6) + lx("VESTA BAGS", 25.4, "#E6C9AE")),
 tile("sand", lx("Mi terapeuta") + small_prod("quilted", 12, 50) + lx("24 × 19 cm · Bs 700", 26.4)),
 tile("lux", google("cartera que combine con todo", ["…<b>y con mi mal humor</b>", "…<b>y con el lunes</b>", "…<b>y que sea original</b>"], 6) ),
 tile("lux", ph("silla", "center 40%", "filter:saturate(.75)") + q("<span style=\'color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.45)\'>Cita conmigo misma.</span>", 1.5, None, 2, "left")),
 tile("lux", receipt([("Cartera caramelo", "×1"), ("Elegancia", "incluida"), ("Arrepentimientos", "0")], ("TOTAL", "Bs 700"), 2.4, 4, 19.2)),
 tile("luxd", lx("Edición noche", 1.6, "#E6C9AE") + small_prod("gold", 11, 48) + q("Para cuando el plan es «solo uno».", 1.2, None, 2.2)),
 tile("lux", q("Lo pensé.<br>Lo pensé mucho.<br>Me la llevé.", 2, 4.4) + small_prod("tote_green", 7.4, 74)),
]
props.append(("04", "Lujo <em>con humor</em>", "La estética de Maison VESTA, pero con frases que hacen sonreír, del estilo de Kate Spade y Coach: humor fino, nunca de meme barato. Los mockups (notas, buscador, ticket) van en marfil y cacao para no romper la elegancia. Sin personaje.",
 [P["lux"][0], P["sand"][0], P["luxd"][0], "#E6C9AE", P["green"][0]], "Bodoni Moda cursiva (frases) · versalitas · mockups en marfil",
 "Diferenciarse: se ve cara y se comparte por las frases.", "Las frases deben ser muy buenas; si son flojas, se siente vacía.", t4, "#EADBC8"))

# ---------- 5 · Vesta de lujo ----------
def crest(s=6, x=None, y=2, col="currentColor"):
    left = f"left:calc(50% - var(--u)*{s/2})" if x is None else f"left:{u(x)}"
    return f'<div class="crest" style="{left};top:{u(y)};width:{u(s)};height:{u(s)};color:{col};z-index:6"><img src="{M}" style="width:76%"></div>'
t5 = [
 tile("lux", crest(11, None, 6.2) + q("Hola, soy Vesta.", 2, None, 6.4) + lx("Desde La Paz", 25.6)),
 tile("lux", crest(4, None, 1.6) + small_prod("caramel", 12, 54) + lx("Caramelo · Bs 700", 26.4)),
 tile("luxd", crest(4, None, 1.6, "#E6C9AE") + q("Vesta aprueba<br>esta elección.", 1.9, 11) + small_prod("gold", 7, 76)),
 tile("lux", ph("casa", "center 30%", "filter:saturate(.75)") + crest(4, 18, 1.4, "#fff")),
 tile("stitch", crest(4, None, 1.6) + floor() + studio("st_heart", 13.4, 6) + lx("Corazón Stitch", 26.4)),
 tile("lux", mascot(5.6, 9.2, 14.4) + q("Pregúntame lo que quieras.", 1.6, 5.6) + lx("WhatsApp · 9:00 a 19:00", 25.4)),
 tile("luxd", crest(4, None, 1.6, "#E6C9AE") + small_prod("quilted", 11, 50) + lx("Acolchada · Bs 700", 26.4, "#E6C9AE")),
 tile("hk", crest(4, None, 1.6) + floor() + studio("hk_face", 14, 6) + lx("Hello Kitty", 26.4)),
 tile("sand", ph("mesa", "35% center", "filter:saturate(.7)") + crest(4, 18, 1.4, "#fff")),
]
props.append(("05", "Vesta <em>de lujo</em>", "La mascota pasa a ser el emblema de la marca: un sello pequeño dentro de un círculo fino, como el escudo de una casa de moda. Aparece en todas las piezas, pero discreta, y solo habla en las piezas de bienvenida y de ayuda. Lujo con un guiño tierno.",
 [P["lux"][0], P["luxd"][0], P["stitch"][0], P["hk"][0], "#E6C9AE"], "Bodoni Moda · versalitas · sello de la mascota",
 "Tener una marca premium y aun así propia y cercana.", "El sello debe usarse siempre igual (mismo tamaño y lugar) para que se vea intencional.", t5, "#4A3529"))

# ---------- 6 · Vitrina Paceña (propuesta extra) ----------
def ag(bottom=True):
    return f'<div class="aguayo" style="{"bottom:0" if bottom else "top:0"}"></div>'
t6 = [
 tile("lux", f'<img src="{I}logo-dark.png" style="position:absolute;left:50%;top:40%;transform:translate(-50%,-50%);width:{u(12)}">' + q("Hecho para La Paz.", 1.6, None, 4.8) + ag()),
 tile("magenta", floor() + word("Fucsia") + studio("tote_fucsia", 13.4, 4.6) + stk("350", "Bs", 16.8, 14.4, P["magenta"][1], P["magenta"][0], -8) + ag()),
 tile("butter", big("DEL ILLIMANI<br>A TU PUERTA", 1.7, 2.4, "#8E1450") + f'<div class="hand" style="position:absolute;left:{u(2)};right:{u(2)};top:{u(8.4)};font-size:{u(1.2)};z-index:6">delivery en La Paz<br>flota a todo el país</div>' + studio("garf_face", 9, 4.4, x=62) + ag()),
 tile("ivory", ph("casa", "center 30%") + ag()),
 tile("green", floor() + word("Verde") + studio("tote_green", 13.4, 4.6) + ag()),
 tile("ivory", bp("Santa Cruz", "VVI", "Mochila Stitch", "Flota") + studio("st_back", 8.5, 4)+ ag()),
 tile("garf", floor() + word("Garfield") + studio("garf_face", 11, 4.8) + ag()),
 tile("luxd", q("La elegancia no es pasar desapercibida,<br>es ser recordada.", 1.6, 8.6) + ag()),
 tile("stitch", floor() + word("Stitch") + studio("st_heart", 13.6, 4.6) + ag()),
]
props.append(("06", "Vitrina <em>Paceña</em> (extra)", "Mi propuesta: una franja inspirada en los colores del aguayo como firma en todas las piezas, con orgullo paceño y referencias locales (el Illimani, delivery en La Paz, flota). Es la única que nadie más en Bolivia puede copiar tal cual, porque cuenta de dónde es VESTA.",
 ["#C2185B", "#F28C28", "#1E7A4C", "#5B2A86", P["lux"][0]], "Bodoni Moda · Boldonse · franja aguayo",
 "Diferenciarse localmente y conectar con orgullo boliviano.", "Hay que usar la franja con respeto y siempre igual; mejor validar con clientas.", t6, "#F6EBC8"))

def prop_page(n, name, desc, sw, fonts, best, risk, tiles, av):
    sws = "".join(f'<b style="background:{c}"></b>' for c in sw)
    grid = "".join(tiles)
    return f'''<section class="page"><div class="prop"><div><div class="kick">Propuesta de feed · {n}</div><h2>{name}</h2><p>{desc}</p>
<div class="sw2">{sws}</div><p style="font-size:9.5px;color:var(--muted)">{fonts}</p>
<div class="pc"><div><h4>Ideal para</h4>{best}</div><div><h4>Cuidado con</h4>{risk}</div></div></div>
<div class="phone"><div class="ph-h"><div class="av" style="background:{av}"><img src="{I}logo-dark.png" style="width:34px"></div><div style="font-size:11px"><b>[PENDIENTE: @usuario]</b><div style="color:var(--muted)">Distribuidores oficiales de Tizza en Bolivia</div></div></div>
<div class="g9" style="--w:150px">{grid}</div></div></div>
<div class="foot"><span>VESTA BAGS · Propuestas de feed</span><span>Productos de los catálogos Tizza como referencia</span></div></section>'''

cover = f'''<section class="page" style="background:var(--stone);display:flex;flex-direction:column;justify-content:center">
<img src="{I}logo-dark.png" style="width:140px;margin-bottom:22px"><div class="kick">Elige tu estilo</div>
<h1 style="font-family:var(--fd);font-weight:400;font-size:60px;line-height:.98;letter-spacing:-.03em;margin-top:6px">Seis feeds,<br><em style="color:var(--cacao)">una VESTA</em></h1>
<p style="font-size:13px;color:var(--ink2);line-height:1.6;margin-top:14px;max-width:150mm">Cinco propuestas como las pediste y una sexta mía. Cada página muestra cómo se vería tu perfil con 9 publicaciones, la paleta, las tipografías, para qué sirve y qué cuidar. Al final hay una comparación para decidir.</p>
<div style="display:flex;gap:10px;margin-top:22px;flex-wrap:wrap">{"".join(f'<span class="chip" style="font-size:11px;padding:6px 12px">{n} · {nm.replace("<em>", "").replace("</em>", "")}</span>' for n, nm, *_ in props)}</div></section>'''

rows = [("Vitrina Viva 2.0", "Media", "Alta", "Media", "Media", "Bajo"), ("Vesta protagonista", "Baja", "Muy alta", "Baja", "Alta", "Medio"),
        ("Maison VESTA", "Muy alta", "Baja", "Alta", "Baja", "Bajo"), ("Lujo con humor", "Alta", "Alta", "Alta", "Media", "Medio"),
        ("Vesta de lujo", "Alta", "Media", "Alta", "Alta", "Medio"), ("Vitrina Paceña", "Media", "Alta", "Media", "Muy alta", "Medio")]
tr = "".join(f'<tr><td style="font-family:var(--fd);font-size:15px">{r[0]}</td>' + "".join(f"<td>{x}</td>" for x in r[1:]) + "</tr>" for r in rows)
compare = f'''<section class="page"><div class="kick">Comparación</div><h2 style="font-family:var(--fd);font-weight:400;font-size:30px;margin:3px 0 6mm">¿Cuál <em>elegir?</em></h2>
<table style="width:100%;border-collapse:collapse;font-size:11px;color:var(--ink2)"><thead><tr style="text-align:left;font-size:9px;letter-spacing:.14em;text-transform:uppercase;color:var(--cacao)"><th style="padding:8px 6px">Propuesta</th><th>Se ve de lujo</th><th>Potencial viral</th><th>Vende clásicas</th><th>Personalidad propia</th><th>Esfuerzo</th></tr></thead>
<tbody>{tr}</tbody></table>
<p style="font-size:11.5px;line-height:1.6;color:var(--ink2);margin-top:8mm;max-width:230mm"><b>Mi recomendación:</b> <b>04 · Lujo con humor</b> como base del feed, con piezas de <b>02 · Vesta protagonista</b> solo en historias y Reels. Así el perfil se ve caro y el contenido igual se comparte. Si quieres que la mascota sea la marca, la mejor opción es <b>05 · Vesta de lujo</b>.</p>
<style>tbody tr td{{padding:9px 6px;border-top:1px solid var(--line)}}</style>
<div class="foot"><span>VESTA BAGS · Propuestas de feed</span><span></span></div></section>'''

html = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>VESTA · Propuestas de feed</title><style>{CSS}</style></head><body>{cover}{"".join(prop_page(*p) for p in props)}{compare}</body></html>'
(D / "feeds.html").write_text(html)
print("ok")
