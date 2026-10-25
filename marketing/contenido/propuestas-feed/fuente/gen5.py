"""VESTA · 3 propuestas de balance: elegancia formal + identidad de la mascota."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen4 as g4
from gen4 import tile, lx, q, small_prod, mascot, ph, crest, prop_page, CSS, M
from gen3 import u, sty, P, floor, studio, word, C, I

D = pathlib.Path(__file__).parent
P["wine"] = ("#5A1F2C", "#F3E4D6", "#6A2A37", "#62242F")
P["emer"] = ("#1F4A3A", "#EFE6D3", "#2A5747", "#245040")
P["navyj"] = ("#1F2B4A", "#EDE4D6", "#2A3858", "#243150")
P["blush"] = ("#F2E1DA", "#5A1F2C", "#E6CCC1", "#EAD5CC")
GOLD = "#B8955A"

EX = """
.chain{position:absolute;width:0;border-left:calc(var(--u)*.12) dotted #B8955A;z-index:6}
.ring{position:absolute;width:calc(var(--u)*.7);height:calc(var(--u)*.7);border:calc(var(--u)*.14) solid #B8955A;border-radius:50%;z-index:6}
"""

def charm(x, y, chain=2.4, w=3.4, rot=-6):
    """La mascota colgando como charm: argolla + cadena dorada + mascota."""
    return (f'<div class="ring" style="left:{u(x - .35)};top:{u(y - .7)}"></div><div class="chain" style="left:{u(x)};top:{u(y)};height:{u(chain)}"></div>'
            f'<img src="{M}" style="position:absolute;left:{u(x - w / 2)};top:{u(y + chain - .2)};width:{u(w)};transform:rotate({rot}deg);transform-origin:top center;z-index:7;filter:drop-shadow(0 calc(var(--u)*.3) calc(var(--u)*.4) rgba(40,25,15,.2))">')

def prod_at(img, h, cy=50, x=50):
    return f'<img src="{C}{img}.png" style="position:absolute;left:{x}%;top:{cy}%;transform:translate(-50%,-50%);height:{u(h)};filter:drop-shadow(0 calc(var(--u)*.5) calc(var(--u)*.7) rgba(40,25,15,.2));z-index:4">'

props = []

# ---------- A · Maison con anfitriona ----------
tA = [
 tile("lux", f'<img src="{I}logo-dark.png" style="position:absolute;left:50%;top:46%;transform:translate(-50%,-50%);width:{u(12)}">' + lx("La Paz · Bolivia", 24.6)),
 tile("pink", mascot(12, 6, 7.4) + q("Hola, soy Vesta.<br><span style='font-size:.6em'>Tu anfitriona en VESTA.</span>", 1.8, None, 3.2) + lx("Vesta", 1.6)),
 tile("lux", lx("Colección Otoño") + small_prod("caramel", 12.5, 50) + lx("Caramelo · Bs 700", 26.4)),
 tile("luxd", q("La elegancia no es pasar desapercibida, es ser recordada.", 1.7, 10.4) + lx("VESTA BAGS", 25.4, "#E6C9AE")),
 tile("stitch", mascot(6.4, 2, 17.6, -6) + prod_at("st_heart", 13.4, 47, 58) + lx("Vesta elige · Corazón Stitch", 26.4)),
 tile("lux", ph("casa", "center 30%", "filter:saturate(.75)")),
 tile("lux", lx("Edición noche") + small_prod("gold", 11, 50) + lx("Dorada · Bs 700", 26.4)),
 tile("lux", ph("mesa", "35% center", "filter:saturate(.7)")),
 tile("hk", mascot(9, 7.6, 11) + q("Pregúntame<br>lo que quieras.", 1.6, 4.2) + lx("WhatsApp · 9:00 a 19:00", 26.4)),
]
props.append(("A", "Maison con <em>anfitriona</em>", "El feed es Maison VESTA (marfil, cacao, carteras con aire y versalitas). La mascota tiene un solo trabajo: es la anfitriona. Aparece en su propia columna con un fondo de color suave y se reconoce de lejos, sin ensuciar las fotos de producto.",
 [P["lux"][0], P["luxd"][0], P["pink"][0], P["stitch"][0], P["hk"][0]], "Bodoni Moda · versalitas · mascota solo en su columna",
 "Que el feed se vea caro y la mascota tenga un lugar fijo y reconocible.", "La columna de la mascota debe respetarse siempre (posts 2, 5, 8…).", tA, "#F7F2EA"))

# ---------- B · El charm de la casa (recomendada) ----------
tB = [
 tile("lux", f'<img src="{I}logo-dark.png" style="position:absolute;left:50%;top:40%;transform:translate(-50%,-50%);width:{u(11)}">' + charm(12, 15.4, 2.2, 4.4, 0) + lx("Vesta · el charm de la casa", 26)),
 tile("lux", lx("Colección Otoño") + prod_at("caramel", 13, 50) + charm(15.8, 13.4, 2, 3.2) + lx("Caramelo · Bs 700", 26.4)),
 tile("luxd", lx("Edición noche", 1.6, "#E6C9AE") + prod_at("gold", 12, 48) + charm(16.4, 10.8, 2.6, 3.2) + lx("Dorada · Bs 700", 26.4, "#E6C9AE")),
 tile("lux", ph("casa", "center 30%", "filter:saturate(.75)") + q("<span style='color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.4)'>Cada VESTA lleva su charm.</span>", 1.4, None, 2, "left")),
 tile("blush", prod_at("hk_pink", 11.5, 52) + charm(17.6, 13.2, 2.2, 3) + lx("Hello Kitty &amp; Friends · Bs 735", 26.4)),
 tile("luxd", q("Elegante por fuera.<br>Tierna por dentro.", 2, 9.6) + charm(12, 18, 1.6, 3.6, 0) + lx("VESTA BAGS", 26.2, "#E6C9AE")),
 tile("lux", lx("Colección Otoño") + prod_at("quilted", 11.5, 50) + charm(16.6, 12.6, 2, 3) + lx("Acolchada · Bs 700", 26.4)),
 tile("stitch", prod_at("st_heart", 14, 46) + lx("Corazón Stitch · Bs 630", 26.4)),
 tile("lux", q("La elegancia no es pasar desapercibida, es ser recordada.", 1.5, 6) + prod_at("tote_green", 8.4, 66) + charm(14.6, 17.2, 1.6, 2.6)),
]
props.append(("B", "El charm <em>de la casa</em> · recomendada", "Lujo formal con un giro que nadie más tiene: Vesta aparece colgada de cada cartera como un charm de lujo, con argolla y cadena dorada. Los charms son tendencia en 2026 y son justo lo que hacen las marcas caras. La mascota deja de verse infantil y pasa a ser la firma de la casa.",
 [P["lux"][0], P["luxd"][0], P["blush"][0], GOLD, P["stitch"][0]], "Bodoni Moda · versalitas · detalle dorado · Vesta como charm",
 "Elevar el precio percibido y tener una identidad imposible de copiar.", "El charm siempre igual: mismo tamaño, del lado derecho y con cadena dorada.", tB, "#4A3529"))

# ---------- C · Joya y sello ----------
tC = [
 tile("wine", crest(10, None, 7, "#E6C9AE") + q("VESTA", 2.6, None, 6.2) + lx("Casa de carteras · La Paz", 25.6, "#E6C9AE")),
 tile("lux", crest(3.6, None, 1.4, GOLD) + small_prod("caramel", 12.5, 52) + lx("Caramelo · Bs 700", 26.4)),
 tile("emer", crest(3.6, None, 1.4, "#E6C9AE") + small_prod("tote_green", 11, 52) + lx("Verde esmeralda · Bs 350", 26.4, "#E6C9AE")),
 tile("lux", ph("casa", "center 30%", "filter:saturate(.75)") + crest(3.6, 18.6, 1.4, "#fff")),
 tile("navyj", crest(3.6, None, 1.4, "#E6C9AE") + small_prod("st_heart", 13, 50) + lx("Corazón Stitch · Bs 630", 26.4, "#E6C9AE")),
 tile("lux", mascot(5.4, 9.3, 15) + q("Hola, soy Vesta.", 1.8, 7) + lx("Pregúntame por WhatsApp", 25.4)),
 tile("wine", crest(3.6, None, 1.4, "#E6C9AE") + small_prod("gold", 11, 50) + lx("Dorada · Bs 700", 26.4, "#E6C9AE")),
 tile("lux", ph("mesa", "35% center", "filter:saturate(.7)")),
 tile("emer", q("Originales.<br>Directo de Tizza.", 2.2, 10) + crest(4, None, 20.4, "#E6C9AE")),
]
props.append(("C", "Joya <em>y sello</em>", "Formal, pero con color profundo tipo joya (vino, esmeralda, azul noche) en vez de pasteles. La mascota es un sello pequeño en cada pieza, como el escudo de una casa de moda, y solo aparece completa en la bienvenida. Se ve muy caro y con carácter.",
 [P["wine"][0], P["emer"][0], P["navyj"][0], P["lux"][0], GOLD], "Bodoni Moda · versalitas · sello dorado",
 "Verse premium de inmediato y diferenciarse de las tiendas pastel.", "Los tonos profundos piden fotos muy bien iluminadas.", tC, "#5A1F2C"))

cover = f'''<section class="page" style="background:var(--stone);display:flex;flex-direction:column;justify-content:center">
<img src="{I}logo-dark.png" style="width:140px;margin-bottom:22px"><div class="kick">El balance</div>
<h1 style="font-family:var(--fd);font-weight:400;font-size:56px;line-height:.98;letter-spacing:-.03em;margin-top:6px">Elegante para vender.<br><em style="color:var(--cacao)">Única para recordarte.</em></h1>
<p style="font-size:13px;color:var(--ink2);line-height:1.6;margin-top:14px;max-width:160mm">Tomé lo que te gustó de la propuesta formal (Maison VESTA) y de la mascota, y los mezclé de tres formas. En las tres manda la elegancia, y la mascota tiene <b>un rol fijo</b> que la hace parte del lujo y no un adorno. La B es mi recomendación.</p></section>'''

rules = f'''<section class="page"><div class="kick">Por qué esto sube el valor</div><h2 style="font-family:var(--fd);font-weight:400;font-size:28px;margin:3px 0 6mm">Siete reglas para que <em>se vea del precio que vale</em></h2>
<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:6mm 12mm;font-size:11px;line-height:1.55;color:var(--ink2)">
<div><b style="color:var(--ink)">1. Aire.</b> La cartera ocupa menos de la mitad de la pieza. El espacio vacío es lo que hace ver caro un producto.</div>
<div><b style="color:var(--ink)">2. Precio discreto.</b> En versalitas pequeñas abajo («Caramelo · Bs 700»), nunca en stickers grandes. Un precio que no grita se percibe como más alto.</div>
<div><b style="color:var(--ink)">3. Paleta corta.</b> Marfil, arena, cacao y un solo acento por pieza. El color de la colección aparece, pero suave.</div>
<div><b style="color:var(--ink)">4. La mascota con un rol, no de adorno.</b> Charm, anfitriona o sello: uno solo, siempre igual. Así se vuelve firma de marca.</div>
<div><b style="color:var(--ink)">5. Frases de casa.</b> «La elegancia no es pasar desapercibida, es ser recordada.» Repite tus frases como un eslogan.</div>
<div><b style="color:var(--ink)">6. Menos emojis y memes.</b> El humor queda para Reels e historias. El feed es la vitrina.</div>
<div><b style="color:var(--ink)">7. Fotos propias consistentes.</b> Misma luz, mismo fondo y mismo ángulo en todo el catálogo.</div>
<div><b style="color:var(--ink)">Lo que no cambia:</b> logo y mascota originales, voz cálida («te ayudamos») y pedidos por WhatsApp.</div>
</div>
<div style="display:flex;gap:16px;margin-top:8mm;align-items:flex-end">
<div class="sl" style="--w:200px;{sty('lux')}">{lx("Colección Otoño")}{prod_at("caramel", 13, 50)}{charm(15.8, 13.4, 2, 3.2)}{lx("Caramelo · Bs 700", 26.4)}</div>
<div class="sl" style="--w:200px;{sty('luxd')}">{q("Elegante por fuera.<br>Tierna por dentro.", 2, 9.6)}{charm(12, 18, 1.6, 3.6, 0)}{lx("VESTA BAGS", 26.2, "#E6C9AE")}</div>
<div class="sl" style="--w:200px;{sty('blush')}">{prod_at("hk_pink", 11.5, 52)}{charm(17.6, 13.2, 2.2, 3)}{lx("Hello Kitty &amp; Friends · Bs 735", 26.4)}</div>
<p style="font-size:10px;color:var(--muted);max-width:60mm;line-height:1.5">Ejemplos en grande de la propuesta B. Cuando tengas las carteras, la idea puede volverse real: un charm físico de Vesta para colgar en cada cartera vendida.</p></div>
<div class="foot"><span>VESTA BAGS · El balance</span><span>Precios de venta del catálogo: confirmar antes de publicar</span></div></section>'''

html = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>VESTA · El balance</title><style>{CSS}{EX}</style></head><body>{cover}{"".join(prop_page(*p) for p in props)}{rules}</body></html>'
(D / "balance.html").write_text(html)
print("ok")
