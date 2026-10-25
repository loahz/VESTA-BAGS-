"""Feed oficial aplicando el análisis de @tizzaoficial."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from gen7 import bag, price, solo_charm, CAC, LT, EX2
from gen4 import tile, lx, q, ph, CSS, M
from gen3 import u, sty, C, I
D = pathlib.Path(__file__).parent
PLAY = f'<div style="position:absolute;right:{u(1.2)};top:{u(1.1)};width:0;height:0;border-left:{u(1.1)} solid rgba(255,255,255,.9);border-top:{u(.7)} solid transparent;border-bottom:{u(.7)} solid transparent;z-index:9;filter:drop-shadow(0 1px 2px rgba(0,0,0,.3))"></div>'
def num(n, dark=False):
    b = "#FBF6F1" if dark else "#221B18"; c = "#221B18" if dark else "#FBF6F1"
    return f'<div style="position:absolute;left:{u(1)};bottom:{u(1)};width:{u(2.2)};height:{u(2.2)};border-radius:50%;background:{b};color:{c};display:grid;place-items:center;font-size:{u(1.1)};font-weight:700;z-index:10;font-family:var(--fu)">{n}</div>'
tiles = {
 1: ("n_iv", f'<img src="{I}logo-dark.png" style="position:absolute;left:50%;top:30%;transform:translate(-50%,-50%);width:{u(11)}">' + solo_charm(6.4, 17.2) + lx("Fijado · Bienvenida", 26.4)),
 2: ("n_st", lx("Ya en Bolivia") + bag("hk_pink", 11.5, 50) + price("Hello Kitty &amp; Friends · Bs 735")),
 3: ("n_dp", PLAY + q("La caja de Tizza<br>llegó a La Paz.", 2, 7.4) + solo_charm(6, 19.6, LT) + lx("Reel · unboxing", 26.6, LT)),
 4: ("n_iv", ph("mesa", "35% center", "filter:saturate(.8)") + f'<div style="position:absolute;left:0;right:0;bottom:0;height:{u(5)};background:linear-gradient(transparent,rgba(34,27,24,.45));z-index:5"></div>' + q("<span style='color:#fff'>Bodegón de primavera</span>", 1.3, None, 1.6)),
 5: ("n_s2", lx("Guía") + q("Cómo comprar<br>Tizza en Bolivia", 2.1, 5) + f'<div style="position:absolute;left:{u(3)};right:{u(3)};top:{u(13.4)};font-size:{u(.95)};line-height:2;color:#4B3B33;z-index:6;font-family:var(--fu)">01 · Eliges la pieza<br>02 · Nos escribes por WhatsApp<br>03 · Pagas en bolivianos<br>04 · Delivery o flota</div>'),
 6: ("n_dp", lx("Desde el 2000", 1.6, LT) + q("Tizza desde el 2000.<br>VESTA, ahora en Bolivia.", 1.75, 8) + solo_charm(5.6, 20.4, LT)),
 7: ("n_iv", lx("Ya en Bolivia") + bag("st_heart", 13.4, 47) + price("Corazón Stitch · Bs 630")),
 8: ("n_st", lx("Colección Primavera") + bag("caramel", 13, 50) + price("Caramelo · Bs 700")),
 9: ("n_dp", PLAY + lx("Tizza lanza · VESTA lo trae", 1.6, LT) + bag("gold", 12, 48, col=LT) + price("Reel · lanzamiento", c=LT)),
}
legend = [
 (1, "Bienvenida fijada con el charm", "Identidad"),
 (2, "«Ya en Bolivia»: lanzamiento de Tizza en menos de 48 h, en Bs", "Idea 1"),
 (3, "Reel «La caja de Tizza llegó a La Paz»", "Idea 4"),
 (4, "Bodegón real (accesorios y carteras en mesa nude)", "Idea 3"),
 (5, "Carrusel «Cómo comprar Tizza en Bolivia»", "Idea 5"),
 (6, "Serie «Desde el 2000, ahora en Bolivia»", "Idea 7"),
 (7, "«Ya en Bolivia» · Stitch", "Idea 1"),
 (8, "Colección primavera con precio en Bs", "Catálogo"),
 (9, "Reel «Tizza lanza, VESTA lo trae»", "Idea 1"),
]
grid = "".join(f'<div class="sl" style="{sty(tiles[k][0])};border-radius:0;box-shadow:none">{tiles[k][1]}{num(k, tiles[k][0] == "n_dp")}</div>' for k in range(1, 10))
hl = [("Mafalda", "M"), ("Hello Kitty", "HK"), ("Disney", "D"), ("Cómo comprar", "?"), ("Envíos", "✈"), ("Encargos", "7d"), ("Clientas", "♡")]
hls = "".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:3px;width:50px"><div style="width:44px;height:44px;border-radius:50%;border:1.5px solid #E6D0BE;padding:2px"><div style="width:100%;height:100%;border-radius:50%;background:#F0E2D6;display:grid;place-items:center;font-family:var(--fd);font-style:italic;font-size:13px;color:#7A4B3A">{s}</div></div><span style="font-size:7.5px;color:#4B3B33;white-space:nowrap">{n}</span></div>' for n, s in hl)
leg = "".join(f'<div style="display:flex;gap:9px;align-items:flex-start;padding:5px 0;border-bottom:1px solid var(--line)"><b style="flex:none;width:20px;height:20px;border-radius:50%;background:#221B18;color:#FBF6F1;display:grid;place-items:center;font-size:10px">{n}</b><div style="font-size:10.5px;line-height:1.4;color:var(--ink2)">{t} <span style="color:var(--cacao);font-size:9px;letter-spacing:.1em;text-transform:uppercase;margin-left:4px">{tag}</span></div></div>' for n, t, tag in legend)
page = f'''<section class="page" style="display:grid;grid-template-columns:1fr auto;gap:10mm;align-items:center">
<div><div class="kick">Feed oficial · aplicado el análisis de @tizzaoficial</div><h2 style="font-family:var(--fd);font-weight:400;font-size:32px;line-height:1.05;margin:4px 0 8px">Tizza lanza, <em>VESTA lo trae</em></h2>
<p style="font-size:11px;line-height:1.55;color:var(--ink2);max-width:120mm">Tomamos lo que Tizza hace bien (las licencias primero, destacadas como menú, bodegones y lanzamientos) y lo que no tiene: precios en bolivianos, comunidad, una firma propia (el charm) y la palabra «Bolivia» en todo. La paleta nude y el ritmo oscuro por fila se mantienen.</p>
<div style="margin-top:8px;max-width:125mm">{leg}</div></div>
<div class="phone" style="padding:14px 12px 12px">
<div style="display:flex;align-items:center;gap:14px;margin-bottom:8px"><div style="width:58px;height:58px;border-radius:50%;background:#4E3A30;display:grid;place-items:center;flex:none"><img src="{I}logo-white.png" style="width:44px"></div>
<div style="display:flex;gap:18px;font-size:10px;text-align:center"><div><b style="font-size:13px">9</b><br>publicaciones</div><div><b style="font-size:13px">—</b><br>seguidores</div><div><b style="font-size:13px">—</b><br>seguidos</div></div></div>
<div style="font-size:9.5px;line-height:1.45;color:#221B18;max-width:390px;margin-bottom:8px"><b>VESTA BAGS</b> · [PENDIENTE: @usuario]<br>Distribuidores oficiales de Tizza en Bolivia 🤍<br>Precios en Bs · Delivery en La Paz · Envíos a toda Bolivia<br>Lo nuevo de Tizza, encargado en una semana<br>WhatsApp +591 76705942</div>
<div style="display:flex;gap:4px;margin-bottom:10px">{hls}</div>
<div class="g9" style="--w:120px">{grid}</div></div>
<div class="foot"><span>VESTA BAGS · Feed oficial</span><span>Precios de venta del catálogo y lanzamientos: confirmar disponibilidad antes de publicar</span></div></section>'''
big = "".join(f'<div class="slot"><div class="sl" style="--w:236px;{sty(tiles[k][0])}">{tiles[k][1]}</div><small style="font-size:9.5px">{t}</small></div>' for k, t in [(2, "«Ya en Bolivia»"), (5, "Cómo comprar Tizza en Bolivia"), (6, "Desde el 2000, ahora en Bolivia"), (3, "Portada del Reel unboxing")])
p2 = f'''<section class="page"><div class="kick">Las piezas nuevas en grande</div><h2 style="font-family:var(--fd);font-weight:400;font-size:28px;margin:3px 0 6mm">Lo que <em>Tizza no tiene</em> y VESTA sí</h2>
<div class="row" style="--gap:16px;--w:236px">{big}</div>
<p style="font-size:10.5px;color:var(--ink2);line-height:1.55;margin-top:6mm;max-width:240mm"><b>Cómo funciona «Ya en Bolivia»:</b> cuando @tizzaoficial publica un lanzamiento, confirmas con Tizza disponibilidad y precio de venta en Bs. En menos de 48 h publicas la pieza en este estilo, y en historias abres la encuesta «¿Cuál traemos?» con el enlace a WhatsApp para encargar (50 % de adelanto, llega en aproximadamente una semana).</p>
<div class="foot"><span>VESTA BAGS · Feed oficial</span><span>Charm: ejemplo digital hasta tener el físico</span></div></section>'''
html = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>VESTA · Feed oficial</title><style>{CSS}{EX2}</style></head><body>{page}{p2}</body></html>'
(D / "feed-oficial.html").write_text(html); print("ok")
