"""Propuesta B (El charm de la casa) solo con la paleta nude oficial."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen5 as g5
from gen5 import prod_at, EX
from gen4 import tile, lx, q, ph, prop_page, CSS, M
from gen3 import u, sty, P, C, I
D = pathlib.Path(__file__).parent
# Paleta oficial (src/styles.css, palette "nude")
P["n_iv"] = ("#FBF6F1", "#221B18", "#F0E2D6", "#F0E2D6")
P["n_st"] = ("#F0E2D6", "#221B18", "#E6D0BE", "#E6D0BE")
P["n_s2"] = ("#E6D0BE", "#221B18", "#DCC6B4", "#DCC6B4")
P["n_dp"] = ("#4E3A30", "#FBF6F1", "#5C463A", "#5C463A")
CAC = "#7A4B3A"
EX2 = EX.replace("#B8955A", CAC)
def charm(x, y, chain=2.4, w=3.4, rot=-6, col=CAC):
    return (f'<div class="ring" style="left:{u(x - .35)};top:{u(y - .7)};border-color:{col}"></div><div class="chain" style="left:{u(x)};top:{u(y)};height:{u(chain)};border-left-color:{col}"></div>'
            f'<img src="{M}" style="position:absolute;left:{u(x - w / 2)};top:{u(y + chain - .2)};width:{u(w)};transform:rotate({rot}deg);transform-origin:top center;z-index:7;filter:drop-shadow(0 calc(var(--u)*.3) calc(var(--u)*.4) rgba(40,25,15,.2))">')
LT = "#E6D0BE"
t = [
 tile("n_iv", f'<img src="{I}logo-dark.png" style="position:absolute;left:50%;top:40%;transform:translate(-50%,-50%);width:{u(11)}">' + charm(12, 15.4, 2.2, 4.4, 0) + lx("Vesta · el charm de la casa", 26)),
 tile("n_st", lx("Colección Otoño") + prod_at("caramel", 13, 50) + charm(15.8, 13.4, 2, 3.2) + lx("Caramelo · Bs 700", 26.4)),
 tile("n_dp", lx("Edición noche", 1.6, LT) + prod_at("gold", 12, 48) + charm(16.4, 10.8, 2.6, 3.2, -6, LT) + lx("Dorada · Bs 700", 26.4, LT)),
 tile("n_iv", ph("casa", "center 30%", "filter:saturate(.75)") + q("<span style='color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.4)'>Cada VESTA lleva su charm.</span>", 1.4, None, 2, "left")),
 tile("n_s2", prod_at("hk_pink", 11.5, 52) + charm(17.6, 13.2, 2.2, 3) + lx("Hello Kitty &amp; Friends · Bs 735", 26.4)),
 tile("n_dp", q("Elegante por fuera.<br>Tierna por dentro.", 2, 9.6) + charm(12, 18, 1.6, 3.6, 0, LT) + lx("VESTA BAGS", 26.2, LT)),
 tile("n_st", lx("Colección Otoño") + prod_at("quilted", 11.5, 50) + charm(16.6, 12.6, 2, 3) + lx("Acolchada · Bs 700", 26.4)),
 tile("n_iv", prod_at("st_heart", 14, 46) + lx("Corazón Stitch · Bs 630", 26.4)),
 tile("n_s2", q("La elegancia no es pasar desapercibida, es ser recordada.", 1.5, 6) + prod_at("tote_green", 8.4, 66) + charm(14.6, 17.2, 1.6, 2.6)),
]
page = prop_page("B", "El charm de la casa · <em>paleta nude</em>", "La misma idea que te gustó, ahora solo con la paleta oficial de la web: marfil, piedra, nude profundo, cacao y espresso. La argolla y la cadena del charm pasan a cacao, sin dorado. El único color fuerte lo ponen las carteras, así que la marca se mantiene igual en todas las piezas.",
 ["#FBF6F1", "#F0E2D6", "#E6D0BE", "#7A4B3A", "#4E3A30", "#221B18"], "Bodoni Moda · Instrument Sans · versalitas · charm en cacao",
 "Elevar el valor con una paleta 100 % de marca y una firma única.", "No meter fondos de color de colección; el color va solo en el producto.", t, "#4E3A30")
big = "".join(f'<div class="sl" style="--w:205px;{sty(c)}">{x}</div>' for c, x in [
 ("n_st", lx("Colección Otoño") + prod_at("caramel", 13, 50) + charm(15.8, 13.4, 2, 3.2) + lx("Caramelo · Bs 700", 26.4)),
 ("n_dp", q("Elegante por fuera.<br>Tierna por dentro.", 2, 9.6) + charm(12, 18, 1.6, 3.6, 0, LT) + lx("VESTA BAGS", 26.2, LT)),
 ("n_s2", prod_at("hk_pink", 11.5, 52) + charm(17.6, 13.2, 2.2, 3) + lx("Hello Kitty &amp; Friends · Bs 735", 26.4)),
 ("n_iv", prod_at("st_heart", 14, 46) + charm(16.6, 9.4, 2.2, 3) + lx("Corazón Stitch · Bs 630", 26.4))])
sw = "".join(f'<div style="flex:1;height:30mm;border-radius:6px;background:{c};padding:10px;display:flex;flex-direction:column;justify-content:flex-end;color:{t};font-size:10px;border:1px solid #E8D7C9"><b style="font-family:var(--fd);font-weight:400;font-size:16px">{n}</b>{c} · {r}</div>'
 for c, t, n, r in [("#FBF6F1", "#221B18", "Marfil", "fondo"), ("#F0E2D6", "#221B18", "Piedra", "fondo"), ("#E6D0BE", "#221B18", "Nude profundo", "fondo"), ("#7A4B3A", "#FBF6F1", "Cacao", "acento y charm"), ("#4E3A30", "#FBF6F1", "Cacao oscuro", "fondo noche"), ("#221B18", "#FBF6F1", "Espresso", "texto")])
p2 = f'''<section class="page"><div class="kick">Paleta oficial · solo estos 6 colores</div><h2 style="font-family:var(--fd);font-weight:400;font-size:28px;margin:3px 0 5mm">Toda la marca en <em>seis tonos</em></h2>
<div style="display:flex;gap:8px">{sw}</div>
<div class="row" style="--gap:16px;margin-top:8mm">{big}</div>
<p style="font-size:10.5px;color:var(--ink2);line-height:1.55;margin-top:6mm;max-width:240mm">Son los mismos colores de tu web (paleta «nude»). Los fondos rotan entre marfil, piedra, nude profundo y cacao oscuro. El cacao se usa en la argolla y la cadena del charm. Garfield, Stitch y Hello Kitty aportan su color solo a través de la cartera.</p>
<div class="foot"><span>VESTA BAGS · El charm de la casa</span><span>Precios de venta del catálogo: confirmar antes de publicar</span></div></section>'''
html = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>VESTA · Charm nude</title><style>{CSS}{EX2}</style></head><body>{page}{p2}</body></html>'
(D / "charm-nude.html").write_text(html); print("ok")
