"""VESTA · Contenido v2: carruseles de estudio con color por colección (HTML → PDF)."""
import pathlib
D = pathlib.Path(__file__).parent

CSS = """
@import url(fonts/fonts.css);
@page{size:A4 landscape;margin:0}
:root{--ivory:#FBF6F1;--stone:#F0E2D6;--stone2:#E6D0BE;--line:#E8D7C9;--ink:#221B18;--ink2:#4B3B33;--muted:#715D51;--cacao:#7A4B3A;--deep:#4E3A30;
 --fd:'Bodoni Moda',Georgia,serif;--fu:'Instrument Sans',Arial,sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--fu);color:var(--ink);background:var(--ivory);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:297mm;height:210mm;padding:11mm 13mm;position:relative;overflow:hidden;page-break-after:always;background:var(--ivory)}
.kick{font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:var(--cacao);font-weight:600}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:10mm;border-bottom:1px solid var(--line);padding-bottom:5mm}
.head h2{font-family:var(--fd);font-weight:400;font-size:28px;line-height:1.05;margin-top:3px;letter-spacing:-.01em}
.head .idea{font-size:11.5px;color:var(--ink2);margin-top:4px;max-width:175mm;line-height:1.45}
.meta{display:flex;gap:6px;flex-wrap:wrap;justify-content:flex-end;max-width:85mm}
.chip{font-size:10px;padding:4px 10px;border-radius:999px;border:1px solid var(--line);background:#fff;white-space:nowrap}
.chip.main{background:var(--ink);border-color:var(--ink);color:var(--ivory);font-weight:600}
.row{display:flex;gap:var(--gap,14px);margin-top:7mm}
.slot{display:flex;flex-direction:column;gap:6px}
.slot small{font-size:9px;color:var(--muted);max-width:var(--w);line-height:1.35}
.notes{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:8mm;margin-top:6mm;font-size:10.5px;line-height:1.5;color:var(--ink2)}
.notes h4{font-size:9px;letter-spacing:.16em;text-transform:uppercase;color:var(--cacao);margin-bottom:4px}
.notes .cap{white-space:pre-line;border-left:2px solid var(--stone2);padding-left:10px}
.foot{position:absolute;bottom:6mm;left:13mm;right:13mm;display:flex;justify-content:space-between;font-size:8.5px;color:var(--muted)}
/* slides */
.sl{--u:calc(var(--w)/24);width:var(--w);height:calc(var(--w)*1.25);position:relative;overflow:hidden;border-radius:4px;background:var(--bg,var(--stone));color:var(--fg,var(--ink));box-shadow:0 10px 26px rgba(34,27,24,.14),0 1px 3px rgba(34,27,24,.08);flex:none}
.sl .word{position:absolute;left:50%;top:var(--wt,34%);transform:translate(-50%,-50%);font-family:var(--fd);font-size:calc(var(--u)*var(--ws,9));line-height:.8;letter-spacing:-.04em;color:var(--tint);white-space:nowrap}
.sl .word.it{font-style:italic}
.sl .p{position:absolute;left:50%;transform:translateX(-50%);filter:drop-shadow(0 calc(var(--u)*.7) calc(var(--u)*.8) rgba(34,27,24,.22))}
.sl .k{position:absolute;left:calc(var(--u)*1.4);top:calc(var(--u)*1.3);font-size:calc(var(--u)*.62);letter-spacing:.24em;text-transform:uppercase;font-weight:600}
.sl .n{position:absolute;right:calc(var(--u)*1.4);top:calc(var(--u)*1.25);font-size:calc(var(--u)*.62);letter-spacing:.1em;opacity:.7}
.sl .t{font-family:var(--fd);font-weight:400;line-height:1;letter-spacing:-.02em}
.sl .t em{font-style:italic}
.sl .b{font-size:calc(var(--u)*.82);line-height:1.45}
.sl .bot{position:absolute;left:calc(var(--u)*1.4);right:calc(var(--u)*1.4);bottom:calc(var(--u)*1.3);display:flex;justify-content:space-between;align-items:flex-end;gap:calc(var(--u)*.8)}
.sl .tag{font-size:calc(var(--u)*.68);letter-spacing:.06em;line-height:1.5}
.sl .tag b{font-weight:600}
.sl .px{font-family:var(--fd);font-size:calc(var(--u)*1.5);line-height:1;white-space:nowrap}
.sl .pad{position:absolute;inset:calc(var(--u)*1.4);display:flex;flex-direction:column}
.sl .btn{display:inline-block;border-radius:99px;font-size:calc(var(--u)*.75);font-weight:600;padding:calc(var(--u)*.55) calc(var(--u)*1.2);background:var(--fg);color:var(--bg)}
.sl .rule{height:1px;background:currentColor;opacity:.25;margin:calc(var(--u)*.8) 0}
.sl .tiles{position:absolute;left:calc(var(--u)*1.4);right:calc(var(--u)*1.4);bottom:calc(var(--u)*1.4);display:grid;grid-template-columns:1fr 1fr;gap:calc(var(--u)*.5)}
.sl .tiles div{position:relative;aspect-ratio:1/1.1;border-radius:3px;overflow:hidden;display:grid;place-items:center}
.sl .tiles img{max-width:78%;max-height:80%;filter:drop-shadow(0 calc(var(--u)*.3) calc(var(--u)*.4) rgba(34,27,24,.2))}
.sl .tiles span{position:absolute;left:calc(var(--u)*.5);bottom:calc(var(--u)*.4);font-size:calc(var(--u)*.6);font-weight:600;letter-spacing:.12em;text-transform:uppercase}
.sl .m{position:absolute;filter:drop-shadow(0 calc(var(--u)*.3) calc(var(--u)*.4) rgba(34,27,24,.18))}
.sl .num{font-family:var(--fd);font-size:calc(var(--u)*3.4);line-height:.9}
/* design page */
.sw{display:grid;grid-template-columns:repeat(4,1fr);gap:6mm;margin-top:6mm}
.sw div{border-radius:6px;padding:12px;height:34mm;display:flex;flex-direction:column;justify-content:space-between;font-size:10px}
.sw b{font-family:var(--fd);font-weight:400;font-size:20px}
.grid9{display:grid;grid-template-columns:repeat(3,1fr);gap:3px;width:max-content}
"""

# Colores por colección (fondo, tinta, palabra de fondo)
P = {
 "nude":   dict(bg="#F0E2D6", fg="#3A2A22", tint="#E0C4AC"),
 "ivory":  dict(bg="#FBF6F1", fg="#221B18", tint="#F0E2D6"),
 "garf":   dict(bg="#F7C98B", fg="#7A2E0E", tint="#EFA94F"),
 "stitch": dict(bg="#C8CDEF", fg="#1E2756", tint="#A9B0E2"),
 "hk":     dict(bg="#F6D2D5", fg="#A3182A", tint="#EAAAB1"),
 "ts":     dict(bg="#CFE3F3", fg="#1D4E86", tint="#A9CAE8"),
 "pink":   dict(bg="#F8DCE6", fg="#B2315F", tint="#EEB3C7"),
 "green":  dict(bg="#D3E6D7", fg="#1C5E3A", tint="#ABCFB3"),
 "fucsia": dict(bg="#F5CFDC", fg="#A3134F", tint="#E8A0BA"),
 "caramel":dict(bg="#EED8C1", fg="#5B3416", tint="#DDB690"),
 "navy":   dict(bg="#DCE2EC", fg="#1C2A48", tint="#B9C4D8"),
 "gold":   dict(bg="#EFE5D3", fg="#6E5321", tint="#DCCAA6"),
 "deep":   dict(bg="#4E3A30", fg="#FBF6F1", tint="#5C463A"),
}
def sty(c): p = P[c]; return f"--bg:{p['bg']};--fg:{p['fg']};--tint:{p['tint']}"
def u(x): return f"calc(var(--u)*{x})"
C = "cut/"
I = "img/"

def sl(c, inner, n, tot, kick="VESTA BAGS"):
    return f'<div class="sl" style="{sty(c)}"><span class="k">{kick}</span><span class="n">{n:02d} / {tot:02d}</span>{inner}</div>'

def prod(img, h=15, top=4.2, x=50):
    if x == 50 and h >= 11:
        h = min(h, 16.4); top = 8.2 + (16.4 - h) / 2
    return f'<img class="p" src="{C}{img}.png" style="height:{u(h)};top:{u(top)};left:{x}%">'

def word(w, size=9, top="36%", it=False):
    size = min(size, 38 / max(len(w), 1)) if len(w) > 1 else size
    if w != "Hola": top = "24%"
    return f'<div class="word{" it" if it else ""}" style="--ws:{size};--wt:{top}">{w}</div>'

def hero(name, code, price, extra=""):
    return f'<div class="bot"><div><div class="t" style="font-size:{u(1.55)}">{name}</div><div class="tag" style="margin-top:{u(.3)}">{extra}Cód. {code}</div></div><div class="px">Bs {price}</div></div>'

def carousel(c_list):
    t = len(c_list)
    return [(sl(c, inner, i + 1, t, k), lbl) for i, (c, inner, lbl, k) in enumerate(c_list)]

def page(num, kind, title, idea, redes, framework, slides, caption, how, why, w=None):
    w = w or {4: 238, 5: 190, 6: 158}[len(slides)]
    main, *rest = redes
    chips = f'<span class="chip main">{main}</span>' + "".join(f'<span class="chip">{r}</span>' for r in rest) + f'<span class="chip">{framework}</span><span class="chip">4:5 · {len(slides)} láminas</span>'
    row = "".join(f'<div class="slot">{s}<small>{l}</small></div>' for s, l in slides)
    return f'''<section class="page" style="--w:{w}px"><div class="head"><div><div class="kick">{kind} · {num:02d}</div><h2>{title}</h2><p class="idea">{idea}</p></div><div class="meta">{chips}</div></div>
<div class="row">{row}</div>
<div class="notes"><div><h4>Caption</h4><div class="cap">{caption}</div></div><div><h4>Producción</h4>{how}</div><div><h4>Por qué funciona</h4>{why}</div></div>
<div class="foot"><span>VESTA BAGS · Contenido v2</span><span>Productos: catálogos Tizza Octubre y Licencias · precios de venta del catálogo, confirmar antes de publicar</span></div></section>'''

pages = []
K = "VESTA BAGS"

# 01 · Bienvenida (la portada que gustó + carteras reales)
pages.append(page(1, "Presentación", "Hola, soy Vesta",
 "Se mantiene la portada que te gustó. Las demás láminas presentan la tienda con carteras reales y color.",
 ["Instagram (fijado)", "Facebook"], "Demo Walkthrough",
 carousel([
  ("nude", word("Hola", 12, "30%") + f'<img class="m" src="{I}mascota-vesta.png" style="width:{u(13)};left:{u(5.5)};top:{u(6.2)}">'
   + f'<div class="bot"><div class="t" style="font-size:{u(2.5)}">Hola, soy <em>Vesta</em></div><div class="tag" style="text-align:right">Desliza</div></div>', "Portada que te gustó, sin cambios de concepto", K),
  ("ivory", f'<div class="pad" style="top:{u(3.4)}"><div class="t" style="font-size:{u(2.1)}">Carteras originales de <em>Tizza</em>, en Bolivia.</div><div class="b" style="margin-top:{u(.7)};color:var(--muted)">Somos un emprendimiento familiar y distribuidores oficiales.</div></div>'
   + prod("caramel", 9.5, 12.5, 30) + prod("tote_fucsia", 7.2, 15.6, 72), "Dos carteras reales con aire alrededor", K),
  ("ivory", f'<div class="pad" style="top:{u(3.4)}"><div class="t" style="font-size:{u(2.1)}">Colecciones <em>oficiales</em></div></div>'
   f'<div class="tiles"><div style="background:{P["hk"]["bg"]};color:{P["hk"]["fg"]}"><img src="{C}hk_pink.png"><span>Hello Kitty</span></div><div style="background:{P["stitch"]["bg"]};color:{P["stitch"]["fg"]}"><img src="{C}st_back.png"><span>Stitch</span></div><div style="background:{P["garf"]["bg"]};color:{P["garf"]["fg"]}"><img src="{C}garf_face.png"><span>Garfield</span></div><div style="background:{P["ts"]["bg"]};color:{P["ts"]["fg"]}"><img src="{C}ts_back.png"><span>Toy Story</span></div></div>', "Mosaico: cada colección con su color", K),
  ("nude", f'<div class="pad" style="top:{u(3.4)}"><div class="t" style="font-size:{u(2.1)}">Así compras</div><div class="rule"></div>'
   f'<div class="b"><b>01</b>  Eliges tu cartera.</div><div class="rule"></div><div class="b"><b>02</b>  Nos escribes por WhatsApp.</div><div class="rule"></div><div class="b"><b>03</b>  Pagas con QR, transferencia o en efectivo contra entrega.</div><div class="rule"></div><div class="b"><b>04</b>  Delivery en La Paz o envío por flota al resto de Bolivia.</div></div>', "Lista editorial con líneas finas, sin íconos", K),
  ("deep", f'<div class="pad" style="justify-content:center;align-items:center;text-align:center"><img src="{I}logo-white.png" style="width:{u(9)}"><div class="b" style="margin:{u(1.2)} 0 {u(1.2)};opacity:.85">+591 76705942 · todos los días de 9:00 a 19:00</div><span class="btn">Escríbenos por WhatsApp</span></div>', "Cierre de marca sobre cacao", K),
 ]),
 "Hola, soy Vesta 🤍\nSomos VESTA BAGS, un emprendimiento familiar y distribuidores oficiales de Tizza en Bolivia. Hello Kitty, Stitch, Garfield, Toy Story y carteras clásicas.\nPedidos por WhatsApp al +591 76705942, de 9:00 a 19:00.\n#VestaBags #CarterasBolivia #TizzaBolivia",
 "<p>Canva 1080×1350. La mascota es el PNG original. Los productos van recortados (sin fondo) sobre color liso.</p>",
 "<p>Abre con la mascota, que ya es reconocible, y en la segunda lámina pasa a producto real. El mosaico de colores muestra variedad sin texto de más.</p>"))

# 02 · Un modelo, tres colores
tot = [("pink","tote_pink","Rosa"),("green","tote_green","Verde"),("fucsia","tote_fucsia","Fucsia")]
pages.append(page(2, "Producto", "Un modelo, tres colores",
 "Un mismo modelo en tres colores, cada uno con su fondo. El color es el contenido.",
 ["Instagram", "TikTok (modo foto)", "Facebook"], "Value-Stack",
 carousel([
  ("ivory", f'<div class="pad" style="top:{u(3.2)}"><div class="t" style="font-size:{u(2.6)}">Un modelo,<br><em>tres colores</em></div></div>'
   + prod("tote_pink", 7.4, 12.6, 22) + prod("tote_green", 8.2, 11.8, 50) + prod("tote_fucsia", 7.4, 12.6, 78)
   + f'<div class="bot"><div class="tag">Cód. 0797 · 26 × 13 cm</div><div class="px">Bs 350</div></div>', "Portada: los tres juntos", K)] +
  [(c, word(n, 8.5 if n != "Fucsia" else 7.5, "40%", True) + prod(img, 13.5, 6.2) + hero(n, "0797", 350, "26 × 13 cm · "), f"{n}: fondo del mismo tono", K) for c, img, n in tot] +
  [("ivory", f'<div class="pad" style="justify-content:center"><div class="t" style="font-size:{u(2.4)}">¿Rosa, verde<br>o <em>fucsia?</em></div><div class="b" style="margin:{u(.8)} 0 {u(1.2)};color:var(--muted)">Escríbenos tu color y te confirmamos la disponibilidad.</div><span class="btn" style="align-self:flex-start;background:var(--ink);color:var(--ivory)">Pedir por WhatsApp</span></div>', "Cierre con pregunta concreta", K)]),
 "Un modelo, tres colores: rosa, verde y fucsia.\nCartera Tizza Cód. 0797, 26 × 13 cm, Bs 350.\n¿Cuál es el tuyo? Escríbenos al +591 76705942 y te confirmamos la disponibilidad.\n#VestaBags #CarterasBolivia #ColorDeTemporada",
 "<p>Fondo liso de un tono más claro que la cartera; nombre del color enorme en Bodoni cursiva detrás. Repite la fórmula con cualquier modelo que venga en varios colores.</p>",
 "<p>El color es lo primero que la clienta decide. Cada lámina funciona sola como publicación y el carrusel completo invita a comentar su favorito.</p>", w=158))

# 03 · Garfield
pages.append(page(3, "Colección", "Garfield, colaboración oficial",
 "Lanzamiento de colección: color cálido de Garfield, el nombre en grande y dos piezas protagonistas.",
 ["Instagram", "TikTok (modo foto)"], "Value-Stack",
 carousel([
  ("garf", word("Garfield", 6.6, "30%", True) + prod("garf_face", 15.6, 4.8) + f'<div class="bot"><div class="t" style="font-size:{u(1.7)}">Colección <em>oficial</em></div><div class="tag">Tizza × Garfield</div></div>', "Portada: la pieza más icónica", "TIZZA × GARFIELD"),
  ("garf", word("Lunes", 9, "34%", True) + prod("garf_face", 16.9, 3.1) + hero("Cara Garfield", "2145", 700, "29 × 19 cm · "), "Producto + nombre + precio", "TIZZA × GARFIELD"),
  ("ivory", word("Garfield", 6.6, "34%", True) + prod("garf_back", 16.9, 3.3) + hero("Mochila Garfield", "2143", 810, "27 × 32 cm · "), "Alterna con fondo marfil para dar aire", "TIZZA × GARFIELD"),
  ("garf", f'<div class="pad" style="justify-content:center"><div class="t" style="font-size:{u(2.3)}">Para quienes odian los lunes <em>con estilo</em>.</div><div class="b" style="margin:{u(.9)} 0 {u(1.2)}">Piezas originales con licencia oficial. Pídelas por WhatsApp al +591 76705942.</div><span class="btn" style="align-self:flex-start">Ver la colección</span></div>', "Cierre con el tono de la colección", "TIZZA × GARFIELD"),
 ]),
 "Garfield llegó a VESTA 🧡\nCartera cara Garfield (Cód. 2145, Bs 700) y mochila Garfield (Cód. 2143, Bs 810). Colaboración oficial Tizza × Garfield.\nPídelas por WhatsApp: +591 76705942\n#VestaBags #Garfield #CarterasBolivia",
 "<p>Paleta de la colección: fondo #F7C98B y texto #7A2E0E. Alterna láminas de color con una marfil para que no canse.</p>",
 "<p>Cada colección con color propio hace que el feed se lea como una tienda ordenada por secciones. El precio visible filtra a quien realmente compra.</p>"))

# 04 · Stitch
pages.append(page(4, "Colección", "Stitch, edición corazón",
 "Dos piezas de la misma línea con el lila de Stitch. Ritmo: color, detalle y cierre.",
 ["Instagram", "TikTok (modo foto)"], "Value-Stack",
 carousel([
  ("stitch", word("Stitch", 8.5, "30%", True) + prod("st_heart", 18.9, 2.6) + f'<div class="bot"><div class="t" style="font-size:{u(1.7)}">Edición <em>corazón</em></div><div class="tag">Disney Stitch</div></div>', "Portada", "DISNEY · STITCH"),
  ("stitch", word("Corazón", 7, "34%", True) + prod("st_heart", 18.2, 2.6) + hero("Cartera corazón", "2102", 630, "22,5 × 19,5 cm · "), "Producto", "DISNEY · STITCH"),
  ("stitch", word("Mochila", 8, "36%", True) + prod("st_back", 16.9, 3.3) + hero("Mochila Stitch", "2100", 810, "29 × 34 cm · "), "Producto", "DISNEY · STITCH"),
  ("ivory", prod("st_heart", 10, 3.6, 30) + prod("st_back", 9, 5.6, 70) + f'<div class="bot"><div><div class="t" style="font-size:{u(1.6)}">¿Cartera o <em>mochila?</em></div><div class="tag" style="margin-top:{u(.3)}">Pídela por WhatsApp · +591 76705942</div></div></div>', "Cierre comparando las dos", "DISNEY · STITCH"),
 ]),
 "Stitch, edición corazón 💙\nCartera corazón (Cód. 2102, Bs 630) y mochila (Cód. 2100, Bs 810). Colección Disney Stitch.\n¿Cartera o mochila? Escríbenos al +591 76705942.\n#VestaBags #Stitch #CarterasBolivia",
 "<p>Fondo #C8CDEF, texto #1E2756. La palabra de fondo cambia en cada lámina (Stitch, Corazón, U) para contar algo sin añadir texto.</p>",
 "<p>La última lámina pone las dos piezas lado a lado: obliga a elegir y la respuesta llega por comentario o por WhatsApp.</p>"))

# 05 · Hello Kitty
pages.append(page(5, "Colección", "Hello Kitty & Friends",
 "Rosado y rojo de la marca. Un ícono (la cara) y una pieza para todos los días.",
 ["Instagram", "TikTok (modo foto)", "Facebook"], "Value-Stack",
 carousel([
  ("hk", word("Kitty", 10, "30%", True) + prod("hk_face", 19.5, 2.6) + f'<div class="bot"><div class="t" style="font-size:{u(1.7)}">Hello Kitty <em>&amp; Friends</em></div><div class="tag">Colección oficial</div></div>', "Portada", "HELLO KITTY"),
  ("hk", word("Icono", 9, "34%", True) + prod("hk_face", 19.5, 2.6) + hero("Hello Kitty", "2041", 700, "20 × 17 cm · "), "El ícono", "HELLO KITTY"),
  ("ivory", word("Friends", 7.5, "34%", True) + prod("hk_pink", 14.3, 4.6) + hero("Kitty &amp; Friends", "2056", 735, "24 × 14 cm · "), "Para todos los días", "HELLO KITTY"),
  ("hk", f'<div class="pad" style="justify-content:center"><div class="t" style="font-size:{u(2.4)}">Tierna, pero con <em>carácter</em>.</div><div class="b" style="margin:{u(.9)} 0 {u(1.2)}">Delivery en La Paz y envíos por flota a toda Bolivia.</div><span class="btn" style="align-self:flex-start">Pedir por WhatsApp</span></div>', "Cierre", "HELLO KITTY"),
 ]),
 "Hello Kitty & Friends 🎀\nCartera cara Hello Kitty (Cód. 2041, Bs 700) y cartera Hello Kitty & Friends (Cód. 2056, Bs 735).\nDelivery en La Paz y envíos por flota. Pídela al +591 76705942.\n#VestaBags #HelloKitty #CarterasBolivia",
 "<p>Fondo #F6D2D5, texto #A3182A. La pieza más llamativa siempre va en la portada, porque es la miniatura en el feed.</p>",
 "<p>Las licencias son lo que más se busca en tu público de 18 a 30 años. Presentarlas como «colección oficial» responde a la duda de originalidad antes de que pregunten.</p>"))

# 06 · Clásicas
pages.append(page(6, "Producto", "Clásicas que combinan con todo",
 "Carteras sin personaje en tonos neutros. Mismo sistema, paleta nude de la marca.",
 ["Instagram", "Facebook"], "Value-Stack",
 carousel([
  ("nude", f'<div class="pad" style="top:{u(3.2)}"><div class="t" style="font-size:{u(2.5)}">Clásicas que<br>combinan <em>con todo</em></div></div>' + prod("caramel", 11, 10.4, 34) + prod("gold", 7.6, 13.6, 74), "Portada con dos piezas", K),
  ("caramel", word("Trabajo", 7.4, "34%", True) + prod("caramel", 18.2, 2.6) + hero("Cartera caramelo", "1892", 700, "25 × 20 cm · "), "Para el trabajo", K),
  ("gold", word("Noche", 8.5, "34%", True) + prod("gold", 16.9, 3.3) + hero("Dorada acolchada", "1953", 700, "25 × 28 cm · "), "Para salir", K),
  ("navy", word("Diario", 8, "34%", True) + prod("navy", 17.6, 2.7) + hero("Mochila azul", "7800", 660, "40 × 29 cm · "), "Para el día a día", K),
  ("deep", f'<div class="pad" style="justify-content:center"><div class="t" style="font-size:{u(2.3)}">¿Para qué la <em>necesitas?</em></div><div class="b" style="margin:{u(.9)} 0 {u(1.2)};opacity:.85">Cuéntanos y te mandamos fotos reales y medidas antes de confirmar.</div><span class="btn" style="align-self:flex-start">Escríbenos</span></div>', "Cierre", K),
 ]),
 "Clásicas que combinan con todo.\nCaramelo para el trabajo (Cód. 1892), dorada para salir (Cód. 1953) y mochila azul para el día a día (Cód. 7800).\nCuéntanos para qué la necesitas: +591 76705942\n#VestaBags #CarterasBolivia #Tizza",
 "<p>Cada pieza toma un tono de fondo de su propio color (caramelo, dorado, azul grisáceo) dentro de la familia nude.</p>",
 "<p>Organizar por ocasión ayuda a decidir a quien no busca personajes, sino una cartera útil.</p>"))

# 07 · Antes de comprar
pages.append(page(7, "Confianza", "Antes de comprar en VESTA",
 "Responde las cuatro dudas que frenan la compra, con una cartera en cada lámina para no perder el producto.",
 ["Facebook", "Instagram"], "Problem-Proof",
 carousel([
  ("ivory", f'<div class="pad" style="top:{u(3.2)}"><div class="t" style="font-size:{u(2.5)}">Cuatro cosas antes de <em>comprar</em></div></div>' + prod("quilted", 13.7, 9.0), "Portada", K),
  ("nude", f'<div class="pad" style="top:calc(var(--u)*3.2)"><div class="num">01</div><div class="t" style="font-size:{u(1.8)};margin-top:{u(.5)}">Son originales</div><div class="b" style="margin-top:{u(.5)}">Somos distribuidores oficiales de Tizza y traemos cada pieza directamente de la marca.</div></div>' + prod("caramel", 10.5, 15.2), "Originalidad", K),
  ("nude", f'<div class="pad" style="top:calc(var(--u)*3.2)"><div class="num">02</div><div class="t" style="font-size:{u(1.8)};margin-top:{u(.5)}">Ves la pieza antes</div><div class="b" style="margin-top:{u(.5)}">No hay devoluciones, por eso te mandamos fotos reales, medidas y colores antes de confirmar.</div></div>' + prod("gold", 10.5, 15.2), "Sin devoluciones, explicado en positivo", K),
  ("nude", f'<div class="pad" style="top:calc(var(--u)*3.2)"><div class="num">03</div><div class="t" style="font-size:{u(1.8)};margin-top:{u(.5)}">Pagas como prefieras</div><div class="b" style="margin-top:{u(.5)}">QR, transferencia o efectivo contra entrega.</div></div>' + prod("tote_green", 10.5, 15.2), "Pagos", K),
  ("nude", f'<div class="pad" style="top:calc(var(--u)*3.2)"><div class="num">04</div><div class="t" style="font-size:{u(1.8)};margin-top:{u(.5)}">Llega a toda Bolivia</div><div class="b" style="margin-top:{u(.5)}">Delivery en La Paz. Al resto del país por flota; el envío lo paga quien compra.</div></div>' + prod("navy", 10.5, 15.2), "Envíos", K),
 ]),
 "Cuatro cosas antes de comprar en VESTA:\n1. Son originales, de Tizza.\n2. Te mandamos fotos reales y medidas antes de confirmar.\n3. Pagas con QR, transferencia o efectivo contra entrega.\n4. Delivery en La Paz y envíos por flota a toda Bolivia.\nEscríbenos: +591 76705942",
 "<p>Número grande en Bodoni, una idea por lámina y la cartera recortada en la esquina inferior. Todo con políticas confirmadas.</p>",
 "<p>Es el carrusel que más se guarda y el que conviene fijar en Facebook. Quita la desconfianza de pagar a una tienda nueva.</p>"))

# 08 · Pedidos a una semana
pages.append(page(8, "Servicio", "Pedidos a una semana",
 "Muestra el catálogo real de Tizza y el camino hasta la clienta, en cuatro pasos.",
 ["Instagram", "Facebook", "TikTok (modo foto)"], "Demo Walkthrough",
 carousel([
  ("ivory", f'<div class="pad" style="top:{u(3.2)}"><div class="t" style="font-size:{u(2.4)}">¿No está en la tienda? <em>Lo traemos.</em></div></div><img src="{I}cat-p089.webp" style="position:absolute;left:{u(3)};right:{u(3)};bottom:{u(2.6)};width:{u(18)};border-radius:3px;box-shadow:0 6px 18px rgba(34,27,24,.18)">', "Portada con una página real del catálogo", K),
  ("nude", f'<div class="pad" style="top:calc(var(--u)*3.2)"><div class="num">01</div><div class="t" style="font-size:{u(1.8)};margin-top:{u(.5)}">Elige en el catálogo</div><div class="b" style="margin-top:{u(.5)}">Octubre (264 páginas) o Licencias (64 páginas).</div></div><img src="{I}cat-l046.webp" style="position:absolute;left:{u(4)};width:{u(16)};bottom:{u(1.6)};border-radius:3px;box-shadow:0 6px 18px rgba(34,27,24,.18)">', "", K),
  ("nude", f'<div class="pad" style="top:calc(var(--u)*3.2)"><div class="num">02</div><div class="t" style="font-size:{u(1.8)};margin-top:{u(.5)}">Mándanos la captura</div><div class="b" style="margin-top:{u(.5)}">Por WhatsApp, con el color que quieres.</div></div>' + prod("st_heart", 13.0, 9.9), "", K),
  ("nude", f'<div class="pad" style="top:calc(var(--u)*3.2)"><div class="num">03</div><div class="t" style="font-size:{u(1.8)};margin-top:{u(.5)}">Confirmas con el 50 %</div><div class="b" style="margin-top:{u(.5)}">Y lo pedimos a Tizza. Llega en aproximadamente una semana.</div></div>' + prod("ts_back", 13.0, 9.9), "", K),
  ("deep", f'<div class="pad" style="justify-content:center;align-items:center;text-align:center"><div class="t" style="font-size:{u(2.2)}">Cualquier pieza de Tizza, <em>en Bolivia</em>.</div><div class="b" style="margin:{u(.9)} 0 {u(1.2)};opacity:.85">+591 76705942</div><span class="btn">Hacer mi encargo</span></div>', "Cierre", K),
 ]),
 "¿Viste algo de Tizza que no está en la tienda? Lo traemos.\n1. Elige en el catálogo. 2. Mándanos la captura. 3. Confirmas con el 50 % de adelanto y llega en aproximadamente una semana.\nEscríbenos: +591 76705942\n#VestaBags #TizzaBolivia",
 "<p>Usa páginas reales del catálogo como prueba visual. El resto, en la misma plantilla numerada del carrusel 07.</p>",
 "<p>Convierte 328 páginas de catálogo en tu inventario. Es el diferencial que ninguna tienda local tiene.</p>"))

# Feed preview
covers = [
 ("nude", word("Hola", 12, "30%") + f'<img class="m" src="{I}mascota-vesta.png" style="width:{u(13)};left:{u(5.5)};top:{u(6.2)}">' + f'<div class="bot"><div class="t" style="font-size:{u(2.5)}">Hola, soy <em>Vesta</em></div></div>'),
 ("garf", word("Garfield", 6.6, "30%", True) + prod("garf_face", 15.6, 4.8)),
 ("pink", word("Rosa", 8.5, "40%", True) + prod("tote_pink", 17.6, 3.9)),
 ("stitch", word("Stitch", 8.5, "30%", True) + prod("st_heart", 18.9, 2.6)),
 ("nude", f'<div class="pad" style="top:{u(3.2)}"><div class="t" style="font-size:{u(2.5)}">Cuatro cosas antes de <em>comprar</em></div></div>' + prod("quilted", 13.7, 9.0)),
 ("hk", word("Kitty", 10, "30%", True) + prod("hk_face", 19.5, 2.6)),
 ("caramel", word("Trabajo", 7.4, "34%", True) + prod("caramel", 18.2, 2.6)),
 ("green", word("Verde", 8.5, "40%", True) + prod("tote_green", 17.6, 3.9)),
 ("ts", word("Toy Story", 5.6, "30%", True) + prod("ts_back", 18.2, 2.6)),
]
grid = "".join(f'<div class="sl" style="{sty(c)};border-radius:0;box-shadow:none">{x}</div>' for c, x in covers)
feed = f'''<section class="page" style="display:grid;grid-template-columns:1fr auto;gap:12mm;align-items:center">
<div><div class="kick">Vista del perfil</div><h2 style="font-family:var(--fd);font-weight:400;font-size:34px;line-height:1.05;margin-top:4px">Así se vería <em>el feed</em></h2>
<p style="font-size:12px;color:var(--ink2);line-height:1.6;margin-top:10px;max-width:120mm">Cada colección tiene su color y las láminas de marca van en nude, así que el perfil se lee como una vitrina ordenada. La mascota aparece solo en la bienvenida. Todo lo demás son carteras.</p>
<p style="font-size:12px;color:var(--ink2);line-height:1.6;margin-top:10px;max-width:120mm"><b>Regla de ritmo:</b> nunca dos portadas del mismo color seguidas. Alterna color, nude y color.</p></div>
<div style="background:#fff;border:1px solid var(--line);border-radius:18px;padding:14px 12px;width:max-content">
<div style="display:flex;align-items:center;gap:10px;margin-bottom:10px"><div style="width:42px;height:42px;border-radius:50%;background:var(--stone);display:grid;place-items:center"><img src="{I}logo-dark.png" style="width:32px"></div><div style="font-size:11px"><b>[PENDIENTE: @usuario]</b><div style="color:var(--muted)">Distribuidores oficiales de Tizza en Bolivia</div></div></div>
<div class="grid9" style="--w:132px">{grid}</div></div></section>'''

# Design system
sw = "".join(f'<div style="background:{P[c]["bg"]};color:{P[c]["fg"]}"><b>{n}</b><span>Fondo {P[c]["bg"]} · Texto {P[c]["fg"]}</span></div>' for c, n in [("nude","Marca"),("garf","Garfield"),("stitch","Stitch"),("hk","Hello Kitty"),("ts","Toy Story"),("pink","Rosa"),("green","Verde"),("caramel","Clásicas")])
system = f'''<section class="page"><div class="kick">Sistema visual v2</div><h2 style="font-family:var(--fd);font-weight:400;font-size:30px;margin-top:4px">Las reglas de <em>este estilo</em></h2>
<div class="sw">{sw}</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:9mm;margin-top:8mm;font-size:11px;line-height:1.55;color:var(--ink2)">
<div><h4 class="kick" style="margin-bottom:5px">Composición</h4>La cartera recortada ocupa entre el 55 % y el 65 % de la lámina. Detrás va una palabra grande en Bodoni cursiva, en un tono más oscuro que el fondo. El texto va abajo a la izquierda y el precio abajo a la derecha.</div>
<div><h4 class="kick" style="margin-bottom:5px">Tipografía</h4>Bodoni Moda para títulos, nombres y precio. Instrument Sans en versalitas espaciadas para la etiqueta superior y los datos. Máximo 12 palabras por lámina.</div>
<div><h4 class="kick" style="margin-bottom:5px">Lo que ya no usamos</h4>Fotos recortadas con la mascota en todas las láminas, emojis como íconos, burbujas de diálogo, degradados oscuros sobre fotos y fondos sin producto.</div>
</div>
<div style="font-size:11px;color:var(--ink2);margin-top:8mm;line-height:1.55;max-width:230mm"><b>Fotos:</b> los recortes salen de los catálogos de Tizza. Para fotos propias con este estilo basta con una cartulina blanca, luz de ventana y la foto de frente. El recorte se hace en Canva (Quitar fondo) o con la herramienta que dejamos en el repo.</div>
<div class="foot"><span>VESTA BAGS · Contenido v2</span><span></span></div></section>'''

cover = f'''<section class="page" style="background:var(--stone);display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:10mm">
<div><img src="{I}logo-dark.png" style="width:150px;margin-bottom:24px"><h1 style="font-family:var(--fd);font-weight:400;font-size:50px;line-height:1.02;letter-spacing:-.02em">Contenido <em style="color:var(--cacao)">v2</em><br>Las carteras, primero.</h1>
<p style="font-size:13px;color:var(--ink2);line-height:1.6;margin-top:14px;max-width:125mm">Ocho carruseles rehechos con tu comentario: más limpios, con el color de cada colección y la cartera como protagonista. La mascota se queda solo en la portada «Hola, soy Vesta».</p>
<p style="font-size:10px;color:var(--muted);line-height:1.5;margin-top:18px;max-width:125mm">Hecho con las skills social (estructuras de carrusel), image (sistema visual) y copywriting (textos sin frases de IA). Productos y precios: catálogos Tizza de venta; confirmar antes de publicar. Para publicar, usa fotos propias o confirma con Tizza el uso de sus imágenes.</p></div>
<div style="position:relative;height:160mm">
<div class="sl" style="--w:230px;{sty('garf')};position:absolute;left:10px;top:20px;transform:rotate(-4deg)">{word("Garfield", 6.6, "30%", True)}{prod("garf_face", 15.6, 4.8)}</div>
<div class="sl" style="--w:230px;{sty('stitch')};position:absolute;right:20px;top:120px;transform:rotate(3deg)">{word("Stitch", 8.5, "30%", True)}{prod("st_heart", 18.9, 2.6)}</div>
<div class="sl" style="--w:200px;{sty('pink')};position:absolute;left:120px;bottom:10px;transform:rotate(-1deg)">{word("Rosa", 8.5, "40%", True)}{prod("tote_pink", 17.6, 3.9)}</div>
</div></section>'''

html = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>VESTA · Contenido v2</title><style>{CSS}</style></head><body>{cover}{feed}{"".join(pages)}{system}</body></html>'
(D / "v2.html").write_text(html)
print("ok", len(pages))
