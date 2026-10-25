"""Estilo oficial «El charm de la casa» v2: correcciones de la crítica."""
import pathlib, sys, json
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen6 as g6
from gen6 import P, CAC, EX2, LT
from gen4 import tile, lx, q, ph, prop_page, CSS, M
from gen3 import u, sty, C, I
D = pathlib.Path(__file__).parent
A = json.load(open(D / "anchors.json"))

def bag(img, h, cy=50, cx=50, ch=2.3, cw=4.4, col=CAC, rot=-4, dx=None):
    """Cartera centrada + charm colgado del asa (punto calculado sobre el recorte), cadena inclinada hacia afuera."""
    import math
    fx, fy, ar = A[img]
    dx = DX.get(img, 0.9) if dx is None else dx
    w = h * ar
    x = 24 * cx / 100 - w / 2 + fx * w
    y = 30 * cy / 100 - h / 2 + fy * h
    ex, ey = x + dx, y + .4 + ch
    L = math.hypot(dx, ch); ang = math.degrees(math.atan2(-dx, ch))
    pr = (f'<img src="{C}{img}.png" style="position:absolute;left:{cx}%;top:{cy}%;transform:translate(-50%,-50%);height:{u(h)};'
          f'filter:drop-shadow(0 calc(var(--u)*.5) calc(var(--u)*.7) rgba(40,25,15,.2));z-index:4">')
    ring = f'<div class="ring" style="left:{u(x - .4)};top:{u(y - .4)};width:{u(.8)};height:{u(.8)};border-color:{col}"></div>'
    chain = (f'<div class="chain" style="left:{u(x)};top:{u(y + .4)};height:{u(L)};border-left:calc(var(--u)*.14) dotted {col};'
             f'transform-origin:top left;transform:rotate({ang:.1f}deg)"></div>')
    m = (f'<img src="{M}" style="position:absolute;left:{u(ex - cw / 2)};top:{u(ey - .2)};width:{u(cw)};transform:rotate({rot}deg);'
         f'transform-origin:top center;z-index:7;filter:drop-shadow(0 calc(var(--u)*.4) calc(var(--u)*.5) rgba(40,25,15,.25))">')
    return pr + ring + chain + m

DX = {"st_heart": 2.6, "hk_pink": 1.4, "caramel": 1.6, "quilted": 1.6, "gold": 1.2, "tote_green": 1.4}

def price(t, top=26.2, c="currentColor"):
    return f'<div style="position:absolute;left:0;right:0;top:{u(top)};text-align:center;font-family:var(--fd);font-size:{u(1.05)};letter-spacing:.06em;color:{c};z-index:6">{t}</div>'

def solo_charm(cw=7, cy=17, col=CAC):
    return (f'<div class="ring" style="left:{u(12 - .5)};top:{u(cy - 4.2)};width:{u(1)};height:{u(1)};border-color:{col}"></div>'
            f'<div class="chain" style="left:{u(12)};top:{u(cy - 3.2)};height:{u(2.4)};border-left:calc(var(--u)*.16) dotted {col}"></div>'
            f'<img src="{M}" style="position:absolute;left:{u(12 - cw / 2)};top:{u(cy - 1)};width:{u(cw)};z-index:7;filter:drop-shadow(0 calc(var(--u)*.4) calc(var(--u)*.5) rgba(40,25,15,.25))">')

T = {
 "logo": ("n_iv", f'<img src="{I}logo-dark.png" style="position:absolute;left:50%;top:30%;transform:translate(-50%,-50%);width:{u(11)}">' + solo_charm(6.4, 17.2) + lx("Vesta · el charm de la casa", 26.4)),
 "caramel": ("n_st", lx("Colección Primavera") + bag("caramel", 13, 50) + price("Caramelo · Bs 700")),
 "gold": ("n_dp", lx("Edición noche", 1.6, LT) + bag("gold", 12, 48, col=LT) + price("Dorada · Bs 700", c=LT)),
 "casa": ("n_iv", ph("casa", "center 30%", "filter:saturate(.8)") + q("<span style='color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.45)'>Hecha para tu día a día.</span>", 1.4, None, 2, "left")),
 "hk": ("n_s2", bag("hk_pink", 11.5, 52) + price("Hello Kitty &amp; Friends · Bs 735")),
 "quote": ("n_dp", q("Elegante por fuera.<br>Tierna por dentro.", 2, 7.6) + solo_charm(6.6, 19, LT) + lx("VESTA BAGS", 26.6, LT)),
 "quilted": ("n_st", lx("Colección Primavera") + bag("quilted", 11.5, 50) + price("Acolchada · Bs 700")),
 "stitch": ("n_dp", bag("st_heart", 14, 47, col=LT) + price("Corazón Stitch · Bs 630", c=LT)),
 "green": ("n_s2", q("La elegancia no es pasar desapercibida, es ser recordada.", 1.5, 4.6) + bag("tote_green", 9, 66)),
}
order = ["logo", "caramel", "gold", "casa", "hk", "quote", "quilted", "green", "stitch"]
tiles = [tile(*T[k]) for k in order]
page = prop_page("Oficial", "El charm de la casa · <em>versión final</em>", "Estilo oficial de VESTA. Cambios: el charm es más grande y cuelga del asa de cada cartera, cada fila tiene una pieza en cacao oscuro que da ritmo, la temporada es Primavera, el precio es más legible y la foto de casa ya no promete un charm que no tiene. El charm todavía es un ejemplo digital, hasta que exista el físico.",
 ["#FBF6F1", "#F0E2D6", "#E6D0BE", "#7A4B3A", "#4E3A30", "#221B18"], "Bodoni Moda · Instrument Sans · charm en cacao (ejemplo digital)",
 "Elevar el valor, vender al precio real y tener una firma única.", "Fotos propias consistentes en cuanto haya stock; el charm físico cuando se produzca.", tiles, "#4E3A30")
big = "".join(f'<div class="sl" style="--w:236px;{sty(T[k][0])}">{T[k][1]}</div>' for k in ["caramel", "quote", "stitch", "hk"])
p2 = f'''<section class="page"><div class="kick">Piezas en grande</div><h2 style="font-family:var(--fd);font-weight:400;font-size:28px;margin:3px 0 6mm">Así se ve <em>de cerca</em></h2>
<div class="row" style="--gap:16px">{big}</div>
<p style="font-size:10.5px;color:var(--ink2);line-height:1.55;margin-top:6mm;max-width:240mm">El charm cuelga del asa con argolla y cadena en cacao (en fondos oscuros, en nude). Es una representación digital de un charm que todavía no existe: cuando lo tengan, se fotografía colgado de verdad y estas piezas se rehacen con la foto real.</p>
<div class="foot"><span>VESTA BAGS · Estilo oficial</span><span>Precios de venta del catálogo: confirmar antes de publicar</span></div></section>'''
html = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>VESTA · Estilo oficial</title><style>{CSS}{EX2}</style></head><body>{page}{p2}</body></html>'
(D / "oficial.html").write_text(html); print("ok")
