"""VESTA · Contenido v3 «Vitrina Viva»: catálogo, creativos, escenas, Reels y calendario (HTML → PDF)."""
import pathlib
D = pathlib.Path(__file__).parent
C, I = "cut/", "img/"

P = {
 "nude":   ("#F0E2D6", "#3A2A22", "#E0C4AC", "#E6D2C1"),
 "ivory":  ("#FBF6F1", "#221B18", "#F0E2D6", "#EFE5DB"),
 "garf":   ("#F7C98B", "#7A2E0E", "#EFA94F", "#EDB46F"),
 "stitch": ("#C8CDEF", "#1E2756", "#A9B0E2", "#B4BAE6"),
 "hk":     ("#F6D2D5", "#A3182A", "#EAAAB1", "#EDBDC2"),
 "ts":     ("#CFE3F3", "#1D4E86", "#A9CAE8", "#B9D5EC"),
 "pink":   ("#F8DCE6", "#B2315F", "#EEB3C7", "#F0C6D5"),
 "green":  ("#D3E6D7", "#1C5E3A", "#ABCFB3", "#BDD8C3"),
 "fucsia": ("#F5CFDC", "#A3134F", "#E8A0BA", "#EBB6C9"),
 "caramel":("#EED8C1", "#5B3416", "#DDB690", "#E2C3A3"),
 "deep":   ("#4E3A30", "#FBF6F1", "#5C463A", "#5A443A"),
 "butter": ("#F6EBC8", "#5A4410", "#EAD58F", "#EEDFAE"),
}
def sty(c):
    bg, fg, tint, floor = P[c]
    return f"--bg:{bg};--fg:{fg};--tint:{tint};--floor:{floor}"
def u(x): return f"calc(var(--u)*{x})"

CSS = r"""
@import url(fonts/fonts.css);
@page{size:A4 landscape;margin:0}
:root{--ivory:#FBF6F1;--stone:#F0E2D6;--stone2:#E6D0BE;--line:#E8D7C9;--ink:#221B18;--ink2:#4B3B33;--muted:#715D51;--cacao:#7A4B3A;--deep:#4E3A30;
 --fd:'Bodoni Moda',Georgia,serif;--fu:'Instrument Sans',Arial,sans-serif;--fh:'Hand',cursive;--fm:'Mono',monospace;--fi:'ISerif',Georgia,serif;--fp:'Pop',Impact,sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--fu);color:var(--ink);background:var(--ivory);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:297mm;height:210mm;padding:11mm 13mm;position:relative;overflow:hidden;page-break-after:always;background:var(--ivory)}
.kick{font-size:9.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--cacao);font-weight:600}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:10mm;border-bottom:1px solid var(--line);padding-bottom:4.5mm}
.head h2{font-family:var(--fd);font-weight:400;font-size:27px;line-height:1.05;margin-top:3px;letter-spacing:-.01em}
.head h2 em{font-style:italic}
.head .idea{font-size:11px;color:var(--ink2);margin-top:4px;max-width:180mm;line-height:1.45}
.meta{display:flex;gap:5px;flex-wrap:wrap;justify-content:flex-end;max-width:92mm}
.chip{font-size:9.5px;padding:3.5px 9px;border-radius:999px;border:1px solid var(--line);background:#fff;white-space:nowrap}
.chip.main{background:var(--ink);border-color:var(--ink);color:var(--ivory);font-weight:600}
.chip.pr{background:#E8F1E4;border-color:#CFE0C7;color:#2F5A35}
.chip.np{background:#F6E6E1;border-color:#EBCFC6;color:#8A3B2A}
.row{display:flex;gap:var(--gap,13px);margin-top:6mm;align-items:flex-start}
.slot{display:flex;flex-direction:column;gap:5px}
.slot small{font-size:8.5px;color:var(--muted);max-width:var(--w);line-height:1.35}
.notes{display:grid;grid-template-columns:1.35fr 1fr 1fr;gap:8mm;margin-top:5mm;font-size:10px;line-height:1.5;color:var(--ink2)}
.notes h4{font-size:8.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--cacao);margin-bottom:3px}
.notes .cap{white-space:pre-line;border-left:2px solid var(--stone2);padding-left:9px}
.foot{position:absolute;bottom:6mm;left:13mm;right:13mm;display:flex;justify-content:space-between;font-size:8px;color:var(--muted)}
.sec{background:var(--deep);color:var(--ivory);display:flex;flex-direction:column;justify-content:flex-end}
.sec h1{font-family:var(--fd);font-weight:400;font-size:64px;line-height:.95;letter-spacing:-.03em}
.sec h1 em{font-style:italic;color:#E6C9AE}
.sec p{font-size:13px;max-width:150mm;line-height:1.55;opacity:.85;margin-top:14px}
.sec .n{font-family:var(--fd);font-size:150px;line-height:.8;position:absolute;right:16mm;top:12mm;color:#5E483D}

/* ===== lámina ===== */
.sl{--u:calc(var(--w)/24);width:var(--w);height:calc(var(--w)*1.25);position:relative;overflow:hidden;border-radius:3px;background:var(--bg);color:var(--fg);box-shadow:0 10px 24px rgba(34,27,24,.15),0 1px 3px rgba(34,27,24,.08);flex:none}
.sl.v{height:calc(var(--w)*16/9)}
.sl .k{position:absolute;left:u14;top:u13;font-size:u62;letter-spacing:.24em;text-transform:uppercase;font-weight:600;z-index:5}
.sl .n{position:absolute;right:u14;top:u125;font-size:u62;letter-spacing:.1em;opacity:.7;z-index:5}
.sl .word{position:absolute;left:50%;transform:translate(-50%,-50%);font-family:var(--fd);font-style:italic;line-height:.8;letter-spacing:-.04em;color:var(--tint);white-space:nowrap}
.sl .t{font-family:var(--fd);font-weight:400;line-height:1;letter-spacing:-.02em}
.sl .t em{font-style:italic}
.sl .b{font-size:u82;line-height:1.45}
.sl .pad{position:absolute;inset:calc(var(--u)*3.2) u14 u14;display:flex;flex-direction:column}
.sl .bot{position:absolute;left:u14;right:u14;bottom:u13;display:flex;justify-content:space-between;align-items:flex-end;gap:u8;z-index:4}
.sl .tag{font-size:u66;letter-spacing:.06em;line-height:1.5}
/* estudio: pared + piso con curva + sombras */
.sl .studio{position:absolute;inset:0;background:linear-gradient(to bottom,var(--bg) 0%,var(--bg) 58%,var(--floor) 74%,var(--floor) 100%)}
.sl .studio::after{content:"";position:absolute;inset:0;background:radial-gradient(ellipse 80% 55% at 50% 38%,rgba(255,255,255,.35),transparent 70%)}
.sl .prod{position:absolute;left:50%;transform:translateX(-50%);z-index:3}
.sl .prod img{height:100%;display:block;filter:drop-shadow(0 u2 u3 rgba(40,25,15,.18))}
.sl .prod .cast{position:absolute;left:0;bottom:0;height:100%;filter:brightness(0) blur(calc(var(--u)*.5));opacity:.16;transform-origin:bottom center;transform:skewX(-38deg) scaleY(.32);z-index:-1}
.sl .contact{position:absolute;left:50%;transform:translateX(-50%);height:u9;border-radius:50%;background:radial-gradient(ellipse at center,rgba(40,25,15,.38),rgba(40,25,15,0) 70%);z-index:2}
/* stickers y collage */
.sl .stk{position:absolute;z-index:6;width:u48;height:u48;border-radius:50%;display:grid;place-items:center;text-align:center;font-family:var(--fd);line-height:1;transform:rotate(-10deg);box-shadow:0 u2 u5 rgba(0,0,0,.15)}
.sl .stk small{display:block;font-family:var(--fu);font-size:u5;letter-spacing:.14em;text-transform:uppercase;font-weight:600;margin-bottom:u2}
.sl .tape{position:absolute;z-index:7;height:u12;background:rgba(246,238,214,.78);box-shadow:0 1px 2px rgba(0,0,0,.08);clip-path:polygon(2% 0,98% 6%,100% 94%,0 100%)}
.sl .paper{position:absolute;background:#FFFDF8;box-shadow:0 u3 u8 rgba(0,0,0,.14);z-index:4}
.sl .torn{clip-path:polygon(0 3%,8% 0,17% 4%,28% 1%,39% 4%,50% 0,61% 3%,72% 0,83% 4%,92% 1%,100% 3%,100% 97%,91% 100%,80% 96%,69% 100%,58% 97%,47% 100%,36% 96%,25% 100%,14% 97%,5% 100%,0 97%)}
.sl .hand{font-family:var(--fh);font-size:u13;line-height:1.15}
.sl .mono{font-family:var(--fm)}
.sl .pop{font-family:var(--fp);letter-spacing:-.01em;line-height:1.18}
.sl .ph{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
/* iPhone notas */
.notes-ui{position:absolute;inset:0;background:#FFFFFF;font-family:-apple-system,'Instrument Sans',sans-serif;color:#1C1C1E}
.notes-ui .bar{display:flex;justify-content:space-between;align-items:center;padding:u12 u14 u6;color:#E0A100;font-size:u8;font-weight:600}
.notes-ui h3{font-size:u16;font-weight:700;padding:u4 u14 u2}
.notes-ui .date{font-size:u6;color:#8E8E93;padding:0 u14 u8}
.notes-ui li{list-style:none;display:flex;gap:u6;align-items:center;font-size:u9;padding:u45 u14;border-bottom:1px solid #F0F0F2}
.notes-ui li i{width:u9;height:u9;border-radius:50%;border:1.4px solid #C7C7CC;flex:none;display:grid;place-items:center;font-style:normal;font-size:u6;color:#fff}
.notes-ui li.done i{background:#E0A100;border-color:#E0A100}
.notes-ui li.done span{text-decoration:line-through;color:#8E8E93}
/* WhatsApp */
.wa{position:absolute;inset:0;background:#EFE7DE;font-family:'Instrument Sans',sans-serif}
.wa .top{background:#F7F5F2;display:flex;gap:u6;align-items:center;padding:u10 u10 u6;font-size:u8;font-weight:600;color:#111;border-bottom:1px solid #E2DDD6}
.wa .top b{width:u14;height:u14;border-radius:50%;background:#D9C6B5;display:block}
.wa .top span small{display:block;font-weight:400;color:#6B6B6B;font-size:u6}
.wa .msgs{padding:u8 u8;display:flex;flex-direction:column;gap:u5}
.wa .m{max-width:78%;padding:u5 u7;border-radius:u7;font-size:u8;line-height:1.35;background:#fff;box-shadow:0 1px .5px rgba(0,0,0,.08);align-self:flex-start;position:relative}
.wa .m.me{background:#D9FDD3;align-self:flex-end}
.wa .m time{display:block;text-align:right;font-size:u5;color:#8A8A8A;margin-top:u2}
.wa .m.img{padding:u3}
.wa .m.img div{width:u90;height:u90;border-radius:u5;display:grid;place-items:center}
.wa .m.img img{height:calc(var(--u)*7.8);width:auto;max-width:90%;object-fit:contain}
/* ticket */
.rc{position:absolute;background:#FFFEFA;font-family:var(--fm);color:#2B2B2B;padding:u10 u10 u12;box-shadow:0 u4 u10 rgba(0,0,0,.18);z-index:4;
 -webkit-mask:linear-gradient(#000 0 0) center/100% calc(100% - var(--u)*2.4) no-repeat,conic-gradient(from -45deg at bottom,#0000,#000 1deg 90deg,#0000 91deg) bottom/calc(var(--u)*2.4) calc(var(--u)*1.2) repeat-x,conic-gradient(from 135deg at top,#0000,#000 1deg 90deg,#0000 91deg) top/calc(var(--u)*2.4) calc(var(--u)*1.2) repeat-x}
.rc .row2{display:flex;justify-content:space-between;font-size:u72;line-height:1.7}
.rc hr{border:none;border-top:1px dashed #9A9A9A;margin:u5 0}
/* buscador */
.gs{position:absolute;left:u14;right:u14;background:#fff;border-radius:u12;box-shadow:0 u3 u10 rgba(0,0,0,.1);font-family:Arial,sans-serif;color:#202124;overflow:hidden;z-index:4}
.gs .q{display:flex;align-items:center;gap:u6;padding:u7 u9;font-size:u9;border-bottom:1px solid #EEE}
.gs .q b{width:u8;height:u8;border:1.5px solid #9AA0A6;border-radius:50%;flex:none}
.gs .s{padding:u45 u9 u45 u24;font-size:u8;color:#202124}
.gs .s b{font-weight:700}
/* pase de abordar */
.bp{position:absolute;left:u14;right:u14;background:#FFFDF9;border-radius:u8;box-shadow:0 u4 u10 rgba(0,0,0,.14);overflow:hidden;z-index:4;font-family:var(--fu)}
.bp .h{background:var(--fg);color:var(--bg);display:flex;justify-content:space-between;padding:u6 u9;font-size:u6;letter-spacing:.2em;font-weight:600;text-transform:uppercase}
.bp .r{display:flex;justify-content:space-between;align-items:center;padding:u7 u9}
.bp .city{font-family:var(--fd);font-size:u24;line-height:1}
.bp .lab{font-size:u5;letter-spacing:.18em;text-transform:uppercase;color:#8A7A70}
.bp .val{font-size:u75;font-weight:600}
.bp .bar{height:u14;margin:0 u9 u8;background:repeating-linear-gradient(90deg,#222 0 2px,transparent 2px 4px,#222 4px 5px,transparent 5px 8px,#222 8px 11px,transparent 11px 12px)}
/* reel UI */
.rui{position:absolute;right:u8;bottom:u55;display:flex;flex-direction:column;gap:u9;z-index:8}
.rui i{width:u12;height:u12;border-radius:50%;background:rgba(255,255,255,.85);display:block;box-shadow:0 1px 3px rgba(0,0,0,.2)}
.cap1{position:absolute;left:u12;right:u12;text-align:center;font-family:var(--fu);font-weight:700;color:#fff;font-size:calc(var(--u)*2.1);line-height:1.15;-webkit-text-stroke:calc(var(--u)*.35) #111;paint-order:stroke fill;z-index:9}
.rlabel{position:absolute;left:u10;bottom:u14;right:u30;color:#fff;font-size:u7;line-height:1.35;z-index:8;text-shadow:0 1px 3px rgba(0,0,0,.4)}
.rlabel b{display:block;font-size:u8}
.play{position:absolute;left:u10;top:u10;font-size:u7;color:#fff;font-weight:600;z-index:8;letter-spacing:.06em;text-shadow:0 1px 3px rgba(0,0,0,.4)}
/* calendario */
.cal{display:grid;grid-template-columns:repeat(7,1fr);gap:5px;margin-top:5mm}
.cal .dh{font-size:9px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);font-weight:600;padding-left:3px}
.cal .d{border:1px solid var(--line);border-radius:6px;background:#fff;height:31mm;padding:6px 7px;position:relative;overflow:hidden}
.cal .d .dn{font-family:var(--fd);font-size:17px;line-height:1}
.cal .d .ty{display:inline-block;font-size:7.5px;letter-spacing:.12em;text-transform:uppercase;font-weight:700;padding:2px 6px;border-radius:99px;margin:4px 0 3px}
.cal .d .ti{font-size:9.5px;line-height:1.3;color:var(--ink)}
.cal .d .rd{font-size:7.5px;color:var(--muted);position:absolute;left:7px;bottom:5px}
.lg{display:flex;gap:10px;font-size:9px;color:var(--ink2);margin-top:4mm;flex-wrap:wrap}
.lg span{display:flex;gap:5px;align-items:center}
.lg b{width:10px;height:10px;border-radius:3px;display:block}
"""
import re
# u12 -> calc(var(--u)*1.2) ; u125 -> 1.25 ; u5 -> .5 ; u90 -> 9.0 ...
UV = {"14": 1.4, "13": 1.3, "62": .62, "125": 1.25, "82": .82, "8": .8, "66": .66, "2": .2, "3": .3, "9": .9, "48": 4.8, "5": .5,
      "12": 1.2, "6": .6, "10": 1.0, "16": 1.6, "4": .4, "45": .45, "7": .7, "90": 9.0, "72": .72, "24": 2.4, "75": .75, "55": 5.5,
      "17": 1.7, "30": 3.0}
def _u(m):
    return f"calc(var(--u)*{UV[m.group(1)]:g})"
CSS = re.sub(r"\bu(\d+)\b", _u, CSS)

def sl(c, inner, n=None, tot=None, kick="VESTA BAGS", v=False, extra=""):
    num = f'<span class="n">{n:02d} / {tot:02d}</span>' if n and kick else ""
    k = f'<span class="k">{kick}</span>' if kick else ""
    return f'<div class="sl{" v" if v else ""}" style="{sty(c)};{extra}">{k}{num}{inner}</div>'

def word(w, top=24, size=None):
    size = size or min(10, 38 / max(len(w), 1))
    return f'<div class="word" style="top:{top}%;font-size:{u(size)}">{w}</div>'

def studio(img, h=15, bottom=6.2, shadow=True, x=50, cw=None):
    """Producto apoyado en el piso del estudio: sombra de contacto + sombra proyectada."""
    cw = cw or h * 0.62
    sh = f'<div class="contact" style="left:{x}%;bottom:{u(bottom - 1.1)};width:{u(cw)}"></div>' if shadow else ""
    cast = f'<img class="cast" src="{C}{img}.png">' if shadow else ""
    return f'{sh}<div class="prod" style="left:{x}%;height:{u(h)};bottom:{u(bottom)}">{cast}<img src="{C}{img}.png"></div>'

def floor(): return '<div class="studio"></div>'

def stk(txt, small, x, y, bg, fg, rot=-10, size=4.8):
    return f'<div class="stk" style="left:{u(x)};top:{u(y)};background:{bg};color:{fg};transform:rotate({rot}deg);width:{u(size)};height:{u(size)}"><div><small>{small}</small><span style="font-size:{u(size*.3)}">{txt}</span></div></div>'

def tape(x, y, w=6, rot=-6):
    return f'<div class="tape" style="left:{u(x)};top:{u(y)};width:{u(w)};transform:rotate({rot}deg)"></div>'

def hero(name, info, price=None):
    pr = f'<div class="t" style="font-size:{u(1.6)};white-space:nowrap">Bs {price}</div>' if price else ""
    return f'<div class="bot"><div><div class="t" style="font-size:{u(1.55)}">{name}</div><div class="tag" style="margin-top:{u(.3)}">{info}</div></div>{pr}</div>'

def carousel(items, v=False):
    t = len(items)
    out = []
    for i, it in enumerate(items):
        c, inner, lbl = it[0], it[1], it[2]
        k = it[3] if len(it) > 3 else "VESTA BAGS"
        out.append((sl(c, inner, i + 1, t, k, v), lbl))
    return out

def page(num, kind, title, idea, redes, tipo, precio, slides, caption, how, why, w=None, gap=13):
    w = w or {3: 250, 4: 236, 5: 188, 6: 157}[len(slides)]
    main, *rest = redes
    pc = '<span class="chip pr">Con precio</span>' if precio else '<span class="chip np">Sin precio</span>'
    chips = f'<span class="chip main">{main}</span>' + "".join(f'<span class="chip">{r}</span>' for r in rest) + f'<span class="chip">{tipo}</span>{pc}'
    row = "".join(f'<div class="slot">{s}<small>{l}</small></div>' for s, l in slides)
    return f'''<section class="page" style="--w:{w}px;--gap:{gap}px"><div class="head"><div><div class="kick">{kind} · {num:02d}</div><h2>{title}</h2><p class="idea">{idea}</p></div><div class="meta">{chips}</div></div>
<div class="row">{row}</div>
<div class="notes"><div><h4>Caption</h4><div class="cap">{caption}</div></div><div><h4>Producción</h4>{how}</div><div><h4>Por qué funciona</h4>{why}</div></div>
<div class="foot"><span>VESTA BAGS · Contenido v3 «Vitrina Viva»</span><span>Productos de los catálogos Tizza · reemplazar por fotos propias o confirmar uso con Tizza</span></div></section>'''

def section(n, title, text):
    return f'<section class="page sec"><div class="n">{n}</div><div class="kick" style="color:#E6C9AE">Sección {n}</div><h1>{title}</h1><p>{text}</p></section>'

pages = []
WA = "+591 76705942"

# ====================== 1 · CATÁLOGO ======================
pages.append(section("01", "Vitrina <em>de color</em>", "El estilo que te gustó, ahora con piso de estudio, sombra real, sticker de precio y cinta de collage. Las piezas de producto solo llevan precio cuando son carrusel de catálogo o la cartera sola."))

tot = [("pink", "tote_pink", "Rosa"), ("green", "tote_green", "Verde"), ("fucsia", "tote_fucsia", "Fucsia")]
pages.append(page(1, "Catálogo", "Un modelo, <em>tres colores</em>", "Cada color con su set de estudio. El precio va en un sticker redondo, como etiqueta de tienda.",
 ["Instagram", "TikTok (modo foto)", "Facebook"], "Carrusel catálogo", True,
 carousel([
  ("ivory", floor() + f'<div class="pad" style="top:{u(3.2)}"><div class="t" style="font-size:{u(2.7)}">Un modelo,<br><em>tres colores</em></div></div>'
   + studio("tote_pink", 7.6, 5.2, x=24) + studio("tote_green", 8.6, 5.2, x=50) + studio("tote_fucsia", 7.6, 5.2, x=76)
   + stk("350", "Bs", 17.2, 9.2, "#221B18", "#FBF6F1", 8), "Portada: los tres en el mismo piso"),
 ] + [(c, floor() + word(n) + studio(img, 14, 6.6) + stk("350", "Bs", 16.6, 14.6, P[c][1], P[c][0], -8) + tape(1.5, 9, 6, -8)
       + hero(n, "Cód. 0797 · 26 × 13 cm"), f"{n}: set de estudio del mismo tono") for c, img, n in tot]
 + [("deep", f'<div class="pad" style="justify-content:center"><div class="t" style="font-size:{u(2.5)}">¿Rosa, verde<br>o <em>fucsia?</em></div><div class="b" style="margin:{u(.9)} 0 {u(1.2)};opacity:.85">Escríbenos tu color y te confirmamos si hay.</div><div class="tag">WhatsApp {WA}</div></div>', "Cierre")]),
 f"Un modelo, tres colores. ¿Cuál te llevas?\nCartera Tizza Cód. 0797, 26 × 13 cm, Bs 350.\nEscríbenos tu color al {WA} y te confirmamos si hay.\n#VestaBags #CarterasBolivia #LaPaz",
 "<p>Set: cartulina del color pegada a la pared que baja en curva al piso. La sombra suave sale de una luz de ventana a 45°. Sticker de precio en el color de texto de la colección.</p>",
 "<p>Charles &amp; Keith y JW Pei venden el color como tema del carrusel. El precio visible filtra a quien compra y ahorra preguntas por WhatsApp.</p>"))

cols = [("garf", "garf_face", "Garfield", "Cara Garfield", "Cód. 2145 · 29 × 19 cm", 700, "TIZZA × GARFIELD"),
        ("stitch", "st_heart", "Stitch", "Corazón Stitch", "Cód. 2102 · 22,5 × 19,5 cm", 630, "DISNEY · STITCH"),
        ("hk", "hk_face", "Kitty", "Hello Kitty", "Cód. 2041 · 20 × 17 cm", 700, "HELLO KITTY"),
        ("ts", "ts_back", "Toy Story", "Mochila Toy Story", "Cód. 2118 · 31 × 36 cm", 810, "DISNEY · PIXAR")]
pages.append(page(2, "Catálogo", "Colecciones <em>oficiales</em>", "Una lámina por licencia, cada una con su color. El sello «oficial» responde a la duda de si es original.",
 ["Instagram", "Facebook"], "Carrusel catálogo", True,
 carousel([("ivory", f'<div class="pad" style="top:{u(3.2)}"><div class="t" style="font-size:{u(2.6)}">Colecciones<br><em>oficiales</em></div><div class="b" style="margin-top:{u(.6)};color:#715D51">Tizza · Disney · Sanrio · Nickelodeon</div></div>'
   + "".join(f'<div style="position:absolute;left:{u(1.4 + i * 5.4)};bottom:{u(1.6)};width:{u(5)};height:{u(10 + (i % 2) * 2)};background:{P[c][0]};border-radius:999px 999px 3px 3px;display:grid;place-items:end center;overflow:hidden"><img src="{C}{img}.png" style="width:86%;margin-bottom:{u(.6)}"></div>' for i, (c, img, *_r) in enumerate(cols)), "Portada: cuatro arcos de color")]
  + [(c, floor() + word(wd) + studio(img, 14.6 if img != "garf_face" else 11.5, 6.4) + stk(str(pr), "Bs", 17, 15.2, P[c][1], P[c][0], -9)
      + f'<div style="position:absolute;left:{u(1.4)};top:{u(3.2)};z-index:6;border:1px solid currentColor;border-radius:99px;font-size:{u(.6)};letter-spacing:.2em;padding:{u(.25)} {u(.6)};font-weight:600">OFICIAL</div>'
      + hero(nm, info), nm, k) for c, img, wd, nm, info, pr, k in cols]),
 "Colecciones oficiales en VESTA: Garfield, Stitch, Hello Kitty y Toy Story.\nOriginales, traídas directamente de Tizza.\nPídelas por WhatsApp: +591 76705942\n#VestaBags #HelloKitty #Stitch #Garfield #ToyStory",
 "<p>Misma plantilla en las cuatro láminas: palabra cursiva arriba, cartera en el piso, sticker de precio a la derecha y etiqueta OFICIAL arriba a la izquierda.</p>",
 "<p>Funciona como un mini catálogo que se guarda. El color hace que cada lámina se reconozca incluso pequeña en el feed.</p>"))

# ====================== 2 · CREATIVOS ======================
pages.append(section("02", "Creativos <em>con tendencia</em>", "Formatos que ya funcionan en redes, como notas del iPhone, chats, tickets, buscadores y pases de abordar, adaptados a VESTA. El chiste sale del formato y la cartera es el remate. Sin precio."))

# Lista de deseos (Notas)
def notes(title, items, date="hoy 9:41"):
    lis = "".join(f'<li class="{"done" if d else ""}"><i>{"✓" if d else ""}</i><span>{t}</span></li>' for t, d in items)
    return f'<div class="notes-ui"><div class="bar"><span>‹ Notas</span><span>Listo</span></div><h3>{title}</h3><div class="date">{date}</div><ul>{lis}</ul></div>'
pages.append(page(1, "Creativo · meme aspiracional", "Mi lista de deseos <em>2026</em>", "La idea del Porsche, en formato nota del iPhone. Todo lo inalcanzable se tacha y la cartera queda marcada.",
 ["Instagram", "TikTok (modo foto)"], "Mockup Notas", False,
 carousel([
  ("ivory", notes("Deseos 2026", [("Un Porsche", False), ("Viaje a París", False), ("Depa con vista al Illimani", False), ("Cartera VESTA", False)]), "Portada: la lista sin tachar", None),
  ("ivory", notes("Deseos 2026", [("<s>Un Porsche</s>", False), ("Viaje a París", False), ("Depa con vista al Illimani", False), ("Cartera VESTA", False)]) + f'<div class="hand" style="position:absolute;left:{u(2.5)};bottom:{u(3)};color:#B2315F;transform:rotate(-4deg);font-size:{u(1.5)}">el banco dijo que no</div>', "Se tacha el Porsche", None),
  ("ivory", notes("Deseos 2026", [("<s>Un Porsche</s>", False), ("<s>Viaje a París</s>", False), ("<s>Depa con vista al Illimani</s>", False), ("Cartera VESTA", False)]) + f'<div class="hand" style="position:absolute;left:{u(2.5)};bottom:{u(3)};color:#B2315F;transform:rotate(-3deg);font-size:{u(1.5)}">bueno, el 2027</div>', "Caen los demás", None),
  ("pink", floor() + f'<div class="pad" style="top:{u(3)}"><div class="t" style="font-size:{u(2.4)}">Lo que sí <em>se cumplió</em></div></div>' + studio("hk_pink", 12.5, 6.4) + f'<div class="hand" style="position:absolute;right:{u(1.6)};top:{u(8)};color:#B2315F;transform:rotate(6deg);font-size:{u(1.4)};z-index:6">✓ hecho</div>' + hero("Hello Kitty &amp; Friends", "Pídela por WhatsApp"), "Remate: la cartera, sin precio"),
 ]),
 "Mi lista de deseos 2026, versión realista 🤍\nEl Porsche puede esperar. La cartera llega esta semana.\n¿Qué hay en tu lista? Te leemos.\n#VestaBags #ListaDeDeseos #CarterasBolivia",
 "<p>Haz la nota de verdad en tu iPhone y toma captura (o grábala para el Reel 10). Tacha con el lápiz de Notas. La última lámina es foto de estudio.</p>",
 "<p>Meme aspiracional con autoironía, como el anuncio clásico de Porsche: no se burla de nadie y deja a la cartera como el lujo posible. Se comparte con «literal yo».</p>"))

# Chat con mamá
def chat(name, msgs, sub="en línea"):
    ms = ""
    for who, txt in msgs:
        if who == "img":
            ms += f'<div class="m me img"><div style="background:{P[txt[1]][0]}"><img src="{C}{txt[0]}.png"></div><time>21:14 ✓✓</time></div>'
        else:
            ms += f'<div class="m{" me" if who == "me" else ""}">{txt}<time>21:1{len(ms) % 9}{" ✓✓" if who == "me" else ""}</time></div>'
    return f'<div class="wa"><div class="top"><b></b><span>{name}<small>{sub}</small></span></div><div class="msgs">{ms}</div></div>'
pages.append(page(2, "Creativo · chat", "Cuando mamá pregunta <em>qué quieres</em>", "Conversación de WhatsApp que todas reconocen. La pausa y la foto final hacen el chiste.",
 ["Instagram", "TikTok (modo foto)", "Facebook"], "Mockup WhatsApp", False,
 carousel([
  ("ivory", chat("Mamá 🤍", [("o", "Hija, ¿qué quieres para tu cumple?"), ("me", "Nada mami, en serio"), ("o", "¿Segura?")]), "Arranca inocente", None),
  ("ivory", chat("Mamá 🤍", [("o", "Hija, ¿qué quieres para tu cumple?"), ("me", "Nada mami, en serio"), ("o", "¿Segura?"), ("me", "Bueno… una cosita"), ("me", "chiquita")]), "La pausa", None),
  ("ivory", chat("Mamá 🤍", [("me", "Bueno… una cosita"), ("img", ("st_heart", "stitch")), ("me", "Esta. Es de VESTA. Hacen delivery 🥹")]), "Llega la foto", None),
  ("stitch", floor() + word("Stitch") + studio("st_heart", 14, 6.4) + hero("Corazón Stitch", "El regalo que sí querías"), "Remate de producto"),
 ]),
 "Todas le dijimos «nada» a mamá alguna vez 🙈\nY todas terminamos mandando la foto de la cartera.\nCorazón Stitch, colección Disney Stitch. Delivery en La Paz y envíos por flota.\n#VestaBags #Stitch #Cumpleaños",
 "<p>Recrea el chat con un contacto real (o una plantilla de chat en Canva). No uses nombres ni números reales de clientas.</p>",
 "<p>El formato de conversación (iMessage o WhatsApp reveal) es de los más fuertes en 2026: se lee como contenido de amigas, no como anuncio, y la foto final es la venta.</p>"))

# Recibo
def receipt(lines, total, x=2.2, top=3.6, w=19.6):
    rows = "".join(f'<div class="row2"><span>{a}</span><span>{b}</span></div>' for a, b in lines)
    return f'<div class="rc" style="left:{u(x)};top:{u(top)};width:{u(w)}"><div style="text-align:center;font-size:{u(.95)};letter-spacing:.25em">VESTA BAGS</div><div style="text-align:center;font-size:{u(.62)};margin-top:{u(.2)}">LA PAZ · BOLIVIA</div><hr>{rows}<hr><div class="row2" style="font-weight:600"><span>{total[0]}</span><span>{total[1]}</span></div><hr><div style="text-align:center;font-size:{u(.62)}">GRACIAS POR ELEGIR VESTA</div></div>'
pages.append(page(3, "Creativo · ticket", "El ticket de <em>tu autoestima</em>", "Un recibo que no cobra plata: cobra días buenos. Muy guardable y fácil de repetir con cada colección.",
 ["Instagram", "Facebook"], "Mockup ticket", False,
 carousel([
  ("garf", receipt([("Cartera Garfield", "×1"), ("Lunes soportables", "×52"), ("Cumplidos", "×∞"), ("Ganas de volver a la cama", "-50%")], ("ARREPENTIMIENTOS", "0")) + tape(9, 2.2, 6, 3), "Ticket Garfield"),
  ("hk", receipt([("Hello Kitty", "×1"), ("«¿dónde la compraste?»", "×14"), ("Fotos para historias", "×23"), ("Mal humor", "agotado")], ("ARREPENTIMIENTOS", "0")) + tape(9, 2.2, 6, -4), "Ticket Hello Kitty"),
  ("green", receipt([("Cartera verde", "×1"), ("Outfits que combinan", "todos"), ("Veces que dijiste «solo miro»", "1"), ("Fuerza de voluntad", "0")], ("ARREPENTIMIENTOS", "0")) + tape(9, 2.2, 6, 5), "Ticket temporada"),
  ("deep", f'<div class="pad" style="justify-content:center"><div class="t" style="font-size:{u(2.4)}">¿Cuál es <em>tu ticket?</em></div><div class="b" style="margin-top:{u(.8)};opacity:.85">Pídela por WhatsApp<br>{WA}</div></div>', "Cierre"),
 ]),
 "Ticket de compra, versión honesta 🧾\nArrepentimientos: 0. Cumplidos: incontables.\n¿Cuál sería tu ticket? Etiqueta a quien necesita uno.\n#VestaBags #CarterasBolivia",
 "<p>Ticket en tipografía monoespaciada sobre el color de cada colección, con cinta arriba. Haz uno por colección para tener una serie.</p>",
 "<p>Convierte la compra en una historia personal (el «trabajo» que hace la cartera) en vez de describir el producto. Se etiqueta mucho.</p>"))

# Google
def google(q, sugs, top=3.4):
    s = "".join(f'<div class="s">{x}</div>' for x in sugs)
    return f'<div class="gs" style="top:{u(top)}"><div class="q"><b></b><span>{q}</span></div>{s}</div>'
pages.append(page(4, "Creativo · buscador", "Cómo justificar <em>otra cartera</em>", "El autocompletado del buscador como chiste. Cada lámina siguiente «responde» con una cartera.",
 ["TikTok (modo foto)", "Instagram"], "Mockup buscador", False,
 carousel([
  ("butter", google("cómo justificar otra cartera", ["cómo justificar otra cartera <b>si es de Stitch</b>", "cómo justificar otra cartera <b>si combina con todo</b>", "cómo justificar otra cartera <b>si es original</b>", "cómo justificar otra cartera <b>si me la traen a casa</b>"]) + f'<div class="hand" style="position:absolute;left:{u(2)};bottom:{u(2.5)};font-size:{u(1.5)};transform:rotate(-3deg)">te ayudamos →</div>', "Portada: búsqueda real", None),
  ("stitch", floor() + f'<div class="pad"><div class="hand" style="font-size:{u(1.6)};margin-top:{u(2)}">razón 1:<br>es de Stitch</div></div>' + studio("st_back", 13.5, 6.4, x=58), "Razón 1"),
  ("caramel", floor() + f'<div class="pad"><div class="hand" style="font-size:{u(1.6)};margin-top:{u(2)}">razón 2:<br>combina con todo</div></div>' + studio("caramel", 14, 6.4, x=58), "Razón 2"),
  ("nude", floor() + f'<div class="pad"><div class="hand" style="font-size:{u(1.6)};margin-top:{u(2)}">razón 3:<br>es original Tizza</div></div>' + studio("quilted", 12, 6.4, x=58), "Razón 3"),
  ("deep", f'<div class="pad" style="justify-content:center"><div class="hand" style="font-size:{u(1.7)}">razón 4:<br>te la llevamos a casa</div><div class="b" style="margin-top:{u(1)};opacity:.85">Delivery en La Paz · flota a toda Bolivia<br>{WA}</div></div>', "Razón 4 = servicio"),
 ]),
 "Buscamos «cómo justificar otra cartera» y encontramos 4 razones muy válidas.\nGuárdalo para cuando lo necesites 🤍\n#VestaBags #CarterasBolivia",
 "<p>Haz la búsqueda real y captura el autocompletado, o recréalo en Canva con la tipografía del buscador. Las razones van escritas a mano (letra tipo marcador).</p>",
 "<p>El humor viene de una situación real (justificarse una compra). Cada razón resuelve una objeción: gusto, uso, originalidad y entrega.</p>"))

# Pase de abordar
def bp(city_to, code, bag, gate, top=4.2, c="stitch"):
    return f'''<div class="bp" style="top:{u(top)}"><div class="h"><span>VESTA AIR · Pase</span><span>Equipaje de mano</span></div>
<div class="r"><div><div class="lab">De</div><div class="city">LPZ</div></div><div style="font-size:{u(1.3)}">✈</div><div style="text-align:right"><div class="lab">A</div><div class="city">{code}</div></div></div>
<div class="r" style="padding-top:0"><div><div class="lab">Pasajera</div><div class="val">Tú</div></div><div><div class="lab">Equipaje</div><div class="val">{bag}</div></div><div><div class="lab">Vía</div><div class="val">{gate}</div></div></div><div class="bar"></div></div>'''
pages.append(page(5, "Creativo · pase de abordar", "Destino: <em>tu ciudad</em>", "Envíos explicados como un pase de abordar. Informativo y bonito a la vez.",
 ["Facebook", "Instagram"], "Mockup pase", False,
 carousel([
  ("stitch", bp("Santa Cruz", "VVI", "Mochila Stitch", "Flota") + studio("st_back", 9.5, 2.2), "Santa Cruz"),
  ("garf", bp("Cochabamba", "CBB", "Cara Garfield", "Flota") + studio("garf_face", 8, 2.6), "Cochabamba"),
  ("hk", bp("La Paz", "LPZ", "Hello Kitty", "Delivery") + studio("hk_face", 10, 2.2), "La Paz: delivery"),
  ("deep", f'<div class="pad" style="justify-content:center"><div class="t" style="font-size:{u(2.3)}">¿A qué ciudad <em>viaja</em> la tuya?</div><div class="b" style="margin-top:{u(.9)};opacity:.85">Delivery en La Paz. Al resto de Bolivia por flota; el envío lo paga quien compra.</div></div>', "Política clara"),
 ]),
 "Tu cartera también viaja ✈\nDelivery en La Paz y envíos por flota a toda Bolivia (el envío lo paga quien compra).\n¿A qué ciudad la mandamos? Escríbenos al +591 76705942.\n#VestaBags #EnvíosBolivia",
 "<p>Pase de abordar en blanco roto con una franja del color de la colección. La cartera abajo, en el mismo set de estudio.</p>",
 "<p>Responde «¿envían a mi ciudad?» antes de que pregunten, en un formato que se guarda y se comparte en grupos de compras de Facebook.</p>"))

# Starter pack (collage revista)
def label(txt, x, y, rot=-4):
    return f'<div class="paper" style="left:{u(x)};top:{u(y)};padding:{u(.35)} {u(.7)};transform:rotate({rot}deg);font-family:var(--fh);font-size:{u(1.05)}">{txt}</div>'
pages.append(page(6, "Creativo · collage revista", "Starter pack: <em>la que llega tarde</em>, pero bien", "Collage tipo revista con recortes, cinta y etiquetas escritas a mano. Muy de Instagram 2026.",
 ["Instagram", "TikTok (modo foto)"], "Collage", False,
 carousel([
  ("butter", f'<div class="pad" style="top:{u(1.6)}"><div class="pop" style="font-size:{u(2.3)}">STARTER PACK</div><div class="t" style="font-size:{u(1.3)};margin-top:{u(.5)}"><em>la que llega tarde, pero bien</em></div></div>'
   + f'<div style="position:absolute;left:{u(1.6)};top:{u(9)};width:{u(11)};height:{u(13)};background:#F7C98B;transform:rotate(-3deg)"></div><img src="{C}garf_face.png" style="position:absolute;left:{u(2.2)};top:{u(10.6)};width:{u(10)};transform:rotate(-3deg);z-index:3">'
   + tape(4, 8.6, 5, -10) + f'<div style="position:absolute;right:{u(1.6)};top:{u(12)};width:{u(9.5)};height:{u(12)};background:#C8CDEF;transform:rotate(4deg)"></div><img src="{C}st_back.png" style="position:absolute;right:{u(2.2)};top:{u(12.6)};width:{u(8.4)};transform:rotate(4deg);z-index:3">'
   + tape(15.5, 11.4, 5, 8) + label("combina con TODO", 2.2, 23.6, -3) + label("para la U", 15.6, 25.8, 4), "Portada collage", None),
  ("ivory", f'<div class="pop" style="position:absolute;left:{u(1.6)};top:{u(3.4)};font-size:{u(1.8)}">01 · LA CARTERA</div>' + f'<div style="position:absolute;left:{u(3)};top:{u(7)};width:{u(18)};height:{u(17)};background:#F7C98B;transform:rotate(-2deg)"></div><img src="{C}garf_face.png" style="position:absolute;left:{u(4.5)};top:{u(8.5)};width:{u(15)};transform:rotate(-2deg)">' + tape(9, 6.2, 6, 4) + label("«ya voy, ya voy»", 3, 25.4, -4), "Pieza 1"),
  ("ivory", f'<div class="pop" style="position:absolute;left:{u(1.6)};top:{u(3.4)};font-size:{u(1.8)}">02 · LA MOCHILA</div>' + f'<div style="position:absolute;left:{u(3)};top:{u(7)};width:{u(18)};height:{u(17)};background:#C8CDEF;transform:rotate(2deg)"></div><img src="{C}st_back.png" style="position:absolute;left:{u(5)};top:{u(7.8)};width:{u(14)};transform:rotate(2deg)">' + tape(9, 6.2, 6, -5) + label("entra todo, hasta las excusas", 3, 25.4, 3), "Pieza 2"),
  ("deep", f'<div class="pad" style="justify-content:center"><div class="pop" style="font-size:{u(1.35)}">¿CUÁL ES TU STARTER PACK?</div><div class="b" style="margin-top:{u(1)};opacity:.85">Comenta y armamos el tuyo.</div></div>', "Cierre: invitación a comentar"),
 ]),
 "Starter pack: la que llega tarde, pero bien vestida.\nCartera Garfield y mochila Stitch, colaboraciones oficiales.\n¿Cuál es tu starter pack? Comenta y armamos el tuyo.\n#VestaBags #StarterPack",
 "<p>Collage en Canva: rectángulos de color girados unos grados, la cartera recortada encima, cinta translúcida y etiquetas de papel con letra manuscrita.</p>",
 "<p>El «starter pack» es un formato de meme que todas reconocen. Habla de identidad y pide que comenten el suyo.</p>"))

# Catálogo vs mi casa
pages.append(page(7, "Creativo · expectativa vs. realidad", "Catálogo vs. <em>lo que llegó</em>", "El formato de «expectativa y realidad», pero aquí son iguales. Prueba de que es original.",
 ["Facebook", "Instagram"], "Antes / después", False,
 carousel([
  ("ivory", f'<div class="pad"><div class="t" style="font-size:{u(2.5)}">Lo que pedí<br>vs. <em>lo que llegó</em></div></div><img src="{I}cat-l046.webp" style="position:absolute;left:{u(1.6)};bottom:{u(2.4)};width:{u(10.4)};box-shadow:0 4px 12px rgba(0,0,0,.18);transform:rotate(-3deg)">'
   + f'<div style="position:absolute;right:{u(1.6)};bottom:{u(2.4)};width:{u(10.4)};height:{u(10.4)};background:{P["stitch"][0]};transform:rotate(3deg);display:grid;place-items:center;box-shadow:0 4px 12px rgba(0,0,0,.18)"><img src="{C}st_heart.png" style="height:{u(9.4)}"></div>'
   + label("catálogo", 2, 25.6, -4) + label("mi casa", 15, 25.6, 3), "Portada lado a lado"),
  ("ivory", f'<img src="{I}cat-l046.webp" style="position:absolute;inset:{u(3.4)} {u(1.6)} {u(5)};width:calc(100% - var(--u)*3.2);object-fit:cover">' + label("lo que pedí", 2, 26, -3), "El catálogo"),
  ("stitch", floor() + studio("st_heart", 15, 6.4) + label("lo que llegó: igualita", 2, 26, 2), "La pieza real (tu foto)"),
  ("deep", f'<div class="pad" style="justify-content:center"><div class="t" style="font-size:{u(2.3)}">Originales, <em>directo de Tizza</em>.</div><div class="b" style="margin-top:{u(.9)};opacity:.85">Antes de confirmar te mandamos fotos reales y medidas.</div></div>', "Cierre de confianza"),
 ]),
 "Lo que pedí vs. lo que llegó: igualita 💙\nSomos distribuidores oficiales de Tizza. Antes de confirmar te mandamos fotos reales y medidas.\n#VestaBags #Original #Stitch",
 "<p>Cuando tengas las carteras, la lámina 3 debe ser <b>tu foto real</b> de la pieza que llegó. Así el carrusel es prueba, no promesa.</p>",
 "<p>Toma un formato de humor (expectativa vs. realidad) y le da la vuelta: el remate es que no hay diferencia. Resuelve la duda número uno: ¿es original?</p>"))

# ====================== 3 · FOTOS EN ESCENA ======================
pages.append(section("03", "Fotos <em>en escena</em>", "Producto solo, con fondo bonito. Estudio de color (cartulina y luz de ventana) y casa decorada (sillón, mesa, pedestal). Las de cartera sola llevan precio y las de escena completa, no."))

singles = [("pink", "tote_pink", 15, 6.4, "350"), ("garf", "garf_face", 12, 6.8, "700"), ("stitch", "st_back", 15, 6.4, "810"), ("caramel", "caramel", 15.5, 6.2, "700")]
row = "".join(f'<div class="slot">{sl(c, floor() + studio(img, h, b) + stk(pr, "Bs", 17.2, 3.2, P[c][1], P[c][0], -8, 4.2), kick="VESTA BAGS")}<small>Estudio {c}: cartera sola, con precio</small></div>' for c, img, h, b, pr in singles)
casa = [("casa", "Sillón: bolso acolchado junto a la mesa"), ("silla", "Silla de madera: luz de tarde"), ("pedestal", "Pedestal: primer plano"), ("mesa", "Mesa con flores: dos piezas")]
row2 = "".join(f'<div class="slot"><div class="sl" style="{sty("ivory")}"><img class="ph" src="{I}{f}.jpg" style="object-position:center 40%"><span class="k" style="color:#fff;text-shadow:0 1px 3px rgba(0,0,0,.4)">VESTA BAGS</span></div><small>{t} · sin precio</small></div>' for f, t in casa)
pages.append(f'''<section class="page" style="--w:150px"><div class="head"><div><div class="kick">Fotos en escena · 01</div><h2>Estudio de color y <em>casa decorada</em></h2><p class="idea">Arriba: la cartera sola en estudio de color (publicación de una sola foto, con precio). Abajo: escenas reales de casa (sin precio). Hasta que tengas tus carteras, salen de los catálogos.</p></div><div class="meta"><span class="chip main">Instagram</span><span class="chip">Facebook</span><span class="chip">Foto única 4:5</span></div></div>
<div style="display:flex;gap:28px;margin-top:5mm"><div class="row" style="margin:0;--gap:10px">{row}</div></div>
<div style="display:flex;gap:28px;margin-top:5mm"><div class="row" style="margin:0;--gap:10px">{row2}</div></div>
<div class="foot"><span>VESTA BAGS · Contenido v3</span><span>Escenas: fotos del catálogo Tizza como referencia</span></div></section>''')

pages.append(f'''<section class="page"><div class="kick">Fotos en escena · 02</div><h2 style="font-family:var(--fd);font-weight:400;font-size:28px;margin-top:3px">Cómo hacer estas fotos <em>con el celular</em></h2>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8mm;margin-top:7mm;font-size:10.5px;line-height:1.55;color:var(--ink2)">
<div><div class="sl" style="--w:200px;{sty('green')};margin-bottom:10px">{floor()}{studio("tote_green", 15, 6.4)}</div><h3 style="font-family:var(--fd);font-weight:400;font-size:18px;color:var(--ink)">1. Estudio de color</h3>Una cartulina grande pegada a la pared y doblada hasta la mesa, sin esquina. Luz de ventana de lado, nunca flash. Celular a la altura de la cartera, en modo retrato desactivado. Una cartulina por colección: naranja, lila, rosado, verde.</div>
<div><div class="sl" style="--w:200px;{sty('ivory')};margin-bottom:10px"><img class="ph" src="{I}casa.jpg"></div><h3 style="font-family:var(--fd);font-weight:400;font-size:18px;color:var(--ink)">2. Casa decorada</h3>Elige un rincón con textura: sillón de lino, mesa de madera, florero, libro, taza. La cartera en el centro y a la luz de la tarde. Ordena antes de disparar: menos objetos, más elegante.</div>
<div><div class="sl" style="--w:200px;{sty('ivory')};margin-bottom:10px"><img class="ph" src="{I}mesa.jpg" style="object-position:30% center"></div><h3 style="font-family:var(--fd);font-weight:400;font-size:18px;color:var(--ink)">3. Pedestal y flores</h3>Una caja blanca o una tabla de picar como pedestal, y flores secas al costado. Sirve para las clásicas y para las fotos de dos colores.</div>
</div><div class="foot"><span>VESTA BAGS · Contenido v3</span><span>Kit sugerido: 4 cartulinas de color, una tela de lino, un florero y una caja blanca</span></div></section>''')

# ====================== 4 · REELS ======================
pages.append(section("04", "Ideas de <em>Reels</em>", "Doce Reels sacados de tendencias reales de TikTok e Instagram, adaptados a VESTA: solo manos y producto, o una amiga que lleva la cartera. Cada uno trae storyboard, audio sugerido y texto en pantalla."))

def frame(c, inner, cap, pos=38, kick=None):
    capd = f'<div class="cap1" style="top:{pos}%">{cap}</div>' if cap else ""
    return sl(c, inner + capd + '<div class="rui"><i></i><i></i><i></i></div><div class="rlabel"><b>vestabags</b>[PENDIENTE: usuario]</div>', kick=None, v=True)
def bg(c): return floor()
def reel(n, name, base, audio, dur, who, frames, cta):
    fr = "".join(f'<div class="slot">{frame(f[0], f[1], f[2], f[3])}<small>{f[4]}</small></div>' for f in frames)
    return f'''<div style="display:grid;grid-template-columns:62mm 1fr;gap:6mm;align-items:start;padding:3.5mm 0;border-bottom:1px solid var(--line)">
<div><div class="kick">Reel {n:02d}</div><div style="font-family:var(--fd);font-size:19px;line-height:1.1;margin:3px 0 5px">{name}</div>
<div style="font-size:9.5px;line-height:1.5;color:var(--ink2)"><b>Tendencia:</b> {base}<br><b>Audio:</b> {audio}<br><b>Duración:</b> {dur} · <b>Quién:</b> {who}<br><b>Cierre:</b> {cta}</div></div>
<div class="row" style="margin:0;--w:71px;--gap:10px">{fr}</div></div>'''
def reelpage(k, items):
    return f'<section class="page"><div class="kick">Reels · {k}</div>{"".join(items)}<div class="foot"><span>VESTA BAGS · Contenido v3</span><span>Texto en pantalla: blanco con borde negro, máximo 2 líneas, dentro de la zona segura</span></div></section>'

R = [
 reel(1, "No tengo un Porsche, pero…", "Meme aspiracional «need money for Porsche»", "Sonido de motor + beat de tendencia", "9 s", "Solo producto",
  [("deep", "", "Lo que quería en 2026:", 40, "0–2 s"), ("deep", '<div class="pop" style="position:absolute;left:0;right:0;top:44%;text-align:center;font-size:calc(var(--u)*3.3);color:#E6C9AE;text-decoration:line-through">PORSCHE</div>', "", 0, "2–4 s: se tacha"),
   ("garf", bg("garf") + studio("garf_face", 10, 9), "Lo que tengo:", 18, "4–7 s: corte al ritmo"), ("garf", bg("garf") + studio("garf_face", 10, 9), "y me siento igual 😌", 18, "7–9 s")], "«Pídela por WhatsApp»"),
 reel(2, "Bag catch: todo cae adentro", "Bag Catch edit (objetos que caen dentro)", "Audio rítmico con golpes", "8 s", "Manos y producto",
  [("stitch", bg("stitch") + studio("st_back", 12, 8), "¿Entra todo?", 20, "Mochila abierta"), ("stitch", bg("stitch") + studio("st_back", 12, 8), "📱", 30, "Cae el celular"), ("stitch", bg("stitch") + studio("st_back", 12, 8), "💄 🔑 🎧", 30, "Cae todo, en cada golpe"), ("stitch", bg("stitch") + studio("st_back", 12, 8), "y todavía cierra", 20, "Cierre")], "Nombre de la mochila"),
 reel(3, "Cambio de color con un chasquido", "Transición de color (snap transition)", "Audio de chasquido en tendencia", "6 s", "Manos y producto",
  [("pink", bg("pink") + studio("tote_pink", 12, 8), "rosa…", 22, "Chasquido"), ("green", bg("green") + studio("tote_green", 12, 8), "verde…", 22, "Chasquido"), ("fucsia", bg("fucsia") + studio("tote_fucsia", 12, 8), "¿o fucsia?", 22, "Chasquido"), ("ivory", bg("ivory") + studio("tote_pink", 7, 9, x=26) + studio("tote_green", 7.6, 9, x=50) + studio("tote_fucsia", 7, 9, x=74), "comenta tu color", 22, "Los tres")], "«Comenta tu color»"),
 reel(4, "ASMR: llegó la caja de Tizza", "Unboxing ASMR", "Sonido real, sin música", "15 s", "Manos",
  [("caramel", bg("caramel"), "llegó la caja 📦", 40, "Caja cerrada"), ("caramel", bg("caramel") + studio("caramel", 9, 7.6), "", 0, "Papel de seda"), ("caramel", bg("caramel") + studio("caramel", 12.5, 7.6), "", 0, "Reveal lento"), ("caramel", bg("caramel") + studio("caramel", 12.5, 7.6), "original Tizza ✨", 18, "Detalle del logo")], "«Ya disponible en VESTA»"),
]
R += [
 reel(5, "Lo que cabe en mi mochila", "What's in my bag", "Voz en off + audio suave", "20 s", "Manos",
  [("ts", bg("ts") + studio("ts_back", 12, 8), "¿qué cabe?", 20, "Mochila cerrada"), ("ts", bg("ts") + studio("ts_back", 12, 8), "1 · laptop", 24, "Uno por uno"), ("ts", bg("ts") + studio("ts_back", 12, 8), "4 · botella", 24, "Contador"), ("ts", bg("ts") + studio("ts_back", 12, 8), "y cierra 🙌", 20, "Cierre")], "Medidas reales en pantalla"),
 reel(6, "Mi cartera elige mi outfit", "Outfit change al ritmo", "Tendencia de transición", "12 s", "Amiga, del cuello para abajo",
  [("hk", bg("hk") + studio("hk_face", 13, 7), "la cartera manda", 18, "Cartera sola"), ("hk", '<img class="ph" src="img/garf_hand.jpg" style="filter:saturate(.9)">', "look 1", 70, "Amiga, look 1"), ("hk", '<img class="ph" src="img/silla.jpg">', "look 2", 70, "Look 2"), ("hk", bg("hk") + studio("hk_face", 13, 7), "¿cuál te gusta?", 18, "Vuelve la cartera")], "«¿Look 1 o 2?»"),
 reel(7, "POV: es lunes", "POV + humor de lunes", "Alarma + audio de tendencia", "7 s", "Manos",
  [("deep", "", "POV: es lunes 😩", 40, "Alarma"), ("deep", "", "pero hoy estreno…", 40, "Mano apaga"), ("garf", bg("garf") + studio("garf_face", 10, 9), "", 0, "Reveal Garfield"), ("garf", bg("garf") + studio("garf_face", 10, 9), "el lunes puede esperar", 16, "Sale con ella")], "Colección Garfield"),
 reel(8, "Catálogo vs. lo que llegó", "Expectativa vs. realidad", "Audio de «expectativa/realidad»", "8 s", "Manos",
  [("ivory", '<img class="ph" src="img/cat-l046.webp">', "catálogo:", 14, "Página del catálogo"), ("stitch", bg("stitch") + studio("st_heart", 13, 7), "lo que llegó:", 14, "Tu foto real"), ("stitch", bg("stitch") + studio("st_heart", 13, 7), "igualita 💙", 70, "Zoom"), ("deep", "", "original, directo de Tizza", 40, "Cierre")], "«Te mandamos fotos reales antes»"),
]
R += [
 reel(9, "Rating de mis carteras del 1 al 10", "Rating / ranking con voz en off", "Voz en off de la amiga", "20 s", "Amiga (voz) y manos",
  [("butter", bg("butter") + studio("hk_pink", 10, 8), "10/10 para salir", 18, "Pieza 1"), ("butter", bg("butter") + studio("caramel", 12, 8), "11/10 para la oficina", 18, "Pieza 2"), ("butter", bg("butter") + studio("st_back", 12, 8), "10/10 para la U", 18, "Pieza 3"), ("deep", "", "¿cuál te llevas?", 40, "Cierre")], "Comentarios"),
 reel(10, "Notas del iPhone en vivo", "Apple Notes reveal (se escribe en vivo)", "Sonido de teclado", "10 s", "Pantalla",
  [("ivory", notes("Deseos 2026", [("Un Porsche", False)]), "", 0, "Se escribe"), ("ivory", notes("Deseos 2026", [("<s>Un Porsche</s>", False), ("Viaje a París", False)]), "", 0, "Se tacha"), ("ivory", notes("Deseos 2026", [("<s>Un Porsche</s>", False), ("<s>Viaje a París</s>", False), ("Cartera VESTA", True)]), "", 0, "Se marca"), ("pink", bg("pink") + studio("hk_pink", 10, 9), "cumplido ✓", 18, "Reveal")], "«¿Y tu lista?»"),
 reel(11, "Chat con mamá", "Chat reveal (burbuja por burbuja)", "Sonido de mensaje", "10 s", "Pantalla",
  [("ivory", chat("Mamá 🤍", [("o", "¿Qué quieres de regalo?")]), "", 0, "Pregunta"), ("ivory", chat("Mamá 🤍", [("o", "¿Qué quieres de regalo?"), ("me", "nada mami")]), "", 0, "Responde"), ("ivory", chat("Mamá 🤍", [("me", "nada mami"), ("img", ("st_heart", "stitch"))]), "", 0, "Manda foto"), ("stitch", bg("stitch") + studio("st_heart", 13, 7), "", 0, "Reveal")], "«Etiqueta a tu mamá»"),
 reel(12, "Empacando tu pedido", "Packing orders ASMR (emprendimiento)", "Sonido real", "15 s", "Manos",
  [("nude", bg("nude") + studio("quilted", 11, 8), "empacando tu pedido 🤍", 18, "Pieza sobre la mesa"), ("nude", bg("nude"), "papel de seda", 40, "Envolver"), ("nude", bg("nude"), "tarjeta escrita a mano", 40, "Tarjeta"), ("deep", "", "rumbo a Cochabamba 🚌", 40, "Caja cerrada")], "«Delivery en La Paz y flota»"),
]
pages.append(reelpage("01 a 04", R[0:4]))
pages.append(reelpage("05 a 08", R[4:8]))
pages.append(reelpage("09 a 12", R[8:12]))

# ====================== 5 · CALENDARIO ======================
TY = {"Reel": ("#221B18", "#FBF6F1"), "Creativo": ("#F7C98B", "#7A2E0E"), "Catálogo": ("#C8CDEF", "#1E2756"), "Escena": ("#D3E6D7", "#1C5E3A"), "Historias": ("#F0E2D6", "#3A2A22"), "Fijado": ("#4E3A30", "#FBF6F1")}
plan = [
 ("Fijado", "«Hola, soy Vesta» + Reel 01 Porsche"), ("Creativo", "Lista de deseos 2026"), ("Reel", "02 Bag catch Stitch"), ("Catálogo", "Un modelo, tres colores"), ("Reel", "04 ASMR caja Tizza"), ("Escena", "Estudio rosa (Bs 350)"), ("Historias", "Encuesta: ¿qué colección traemos?"),
 ("Reel", "03 Cambio de color"), ("Creativo", "Chat con mamá"), ("Reel", "05 Qué cabe en mi mochila"), ("Catálogo", "Colecciones oficiales"), ("Reel", "06 Mi cartera elige mi outfit"), ("Escena", "Casa: sillón"), ("Historias", "Caja de preguntas"),
 ("Reel", "07 POV: es lunes"), ("Creativo", "Ticket de autoestima"), ("Reel", "08 Catálogo vs. lo que llegó"), ("Catálogo", "Garfield en estudio"), ("Reel", "09 Rating del 1 al 10"), ("Escena", "Estudio lila Stitch"), ("Historias", "Detrás de cámaras"),
 ("Reel", "10 Notas del iPhone"), ("Creativo", "Cómo justificar otra cartera"), ("Reel", "12 Empacando tu pedido"), ("Catálogo", "Hello Kitty en estudio"), ("Reel", "11 Chat con mamá · Black Friday solo si hay promo confirmada"), ("Creativo", "Destino: tu ciudad"), ("Historias", "Resumen del mes + encuesta"),
]
days = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
cells = "".join(f'<div class="dh">{d}</div>' for d in days)
for i, (t, txt) in enumerate(plan):
    bgc, fgc = TY[t]
    cells += f'<div class="d"><div class="dn">{2 + i}</div><span class="ty" style="background:{bgc};color:{fgc}">{t}</span><div class="ti">{txt}</div><div class="rd">{"TikTok · IG · FB" if t == "Reel" else ("IG · FB" if t in ("Catálogo", "Escena", "Creativo", "Fijado") else "IG")}</div></div>'
legend = "".join(f'<span><b style="background:{a}"></b>{k}</span>' for k, (a, b) in TY.items())
pages.append(section("05", "Calendario <em>de noviembre</em>", "Cuatro semanas: 3 Reels, 1 creativo, 1 catálogo, 1 escena y historias por semana. Cabe en 5 a 8 horas: una sesión de fotos y videos el domingo y edición en la semana."))
pages.append(f'''<section class="page"><div class="head"><div><div class="kick">Calendario · noviembre 2026</div><h2>Del 2 al 29 de <em>noviembre</em></h2><p class="idea">Reels de lunes a viernes alternos para alcance, y catálogo, escenas y creativos para vender. Publica de 19:00 a 21:00 y ajusta con tus estadísticas.</p></div><div class="meta"><span class="chip main">Meta: seguidores + ventas</span><span class="chip">5 a 8 h por semana</span></div></div>
<div class="cal">{cells}</div><div class="lg">{legend}</div>
<div class="foot"><span>VESTA BAGS · Contenido v3</span><span>Black Friday (27/11): solo con una promoción confirmada por el dueño</span></div></section>''')

# ====================== portada, dirección, feed ======================
cover = f'''<section class="page" style="background:var(--stone);display:grid;grid-template-columns:1.05fr 1fr;align-items:center;gap:8mm">
<div><img src="{I}logo-dark.png" style="width:140px;margin-bottom:22px"><div class="kick">Contenido v3</div><h1 style="font-family:var(--fd);font-weight:400;font-size:58px;line-height:.98;letter-spacing:-.03em;margin-top:6px">Vitrina<br><em style="color:var(--cacao)">Viva</em></h1>
<p style="font-size:12.5px;color:var(--ink2);line-height:1.6;margin-top:14px;max-width:120mm">Catálogo con más impacto, creativos sacados de tendencias reales, fotos en escena, 12 ideas de Reels y el calendario de noviembre. Hecho a partir de tu encuesta.</p>
<p style="font-size:9.5px;color:var(--muted);line-height:1.5;margin-top:16px;max-width:120mm">Skills usadas: social, copywriting, image, ad-creative, marketing-psychology, canvas-design, banner-design, design, brand y theme-factory. Las fotos de producto son de los catálogos de Tizza: hasta tener tus carteras, confirma con Tizza su uso o reemplázalas. Los precios son de venta del catálogo y hay que confirmarlos.</p></div>
<div style="position:relative;height:165mm">
<div class="sl" style="--w:205px;{sty('ivory')};position:absolute;left:0;top:10px;transform:rotate(-5deg)">{notes("Deseos 2026", [("<s>Un Porsche</s>", False), ("<s>Viaje a París</s>", False), ("Cartera VESTA", True)])}</div>
<div class="sl" style="--w:215px;{sty('garf')};position:absolute;right:0;top:60px;transform:rotate(4deg)">{floor()}{word("Garfield")}{studio("garf_face", 11.5, 6.4)}{stk("700", "Bs", 17, 15.2, P["garf"][1], P["garf"][0], -9)}</div>
<div class="sl" style="--w:190px;{sty('hk')};position:absolute;left:95px;bottom:0;transform:rotate(-1deg)">{receipt([("Hello Kitty", "×1"), ("Cumplidos", "×∞"), ("Mal humor", "agotado")], ("ARREPENTIMIENTOS", "0"), 2.4, 4, 19.2)}</div>
</div></section>'''

direction = f'''<section class="page"><div class="kick">Dirección creativa</div><h2 style="font-family:var(--fd);font-weight:400;font-size:28px;margin-top:3px">Cuatro lenguajes, <em>una sola marca</em></h2>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:7mm;margin-top:6mm">
<div><div class="sl" style="--w:170px;{sty('pink')}">{floor()}{word("Rosa")}{studio("tote_pink", 13.5, 6.4)}{stk("350", "Bs", 16.8, 15, P["pink"][1], P["pink"][0], -8)}</div><h3 style="font-family:var(--fd);font-weight:400;font-size:17px;margin-top:8px">Vitrina de color</h3><p style="font-size:9.5px;line-height:1.5;color:var(--ink2)">Catálogo. Estudio con piso, sombra real y sticker de precio. <b>Con precio.</b> Referencia: Charles &amp; Keith, JW Pei.</p></div>
<div><div class="sl" style="--w:170px;{sty('ivory')}">{notes("Deseos 2026", [("<s>Un Porsche</s>", False), ("Cartera VESTA", True)])}</div><h3 style="font-family:var(--fd);font-weight:400;font-size:17px;margin-top:8px">Pantalla cotidiana</h3><p style="font-size:9.5px;line-height:1.5;color:var(--ink2)">Notas, chat, ticket, buscador, pase. Humor real de tendencia. <b>Sin precio.</b> Referencia: memes de marca de Coach y Kate Spade.</p></div>
<div><div class="sl" style="--w:170px;{sty('butter')}"><div class="pad"><div class="pop" style="font-size:calc(var(--u)*2.4)">STARTER<br>PACK</div></div><div style="position:absolute;left:calc(var(--u)*3);top:calc(var(--u)*9);width:calc(var(--u)*16);height:calc(var(--u)*15);background:#F7C98B;transform:rotate(-3deg)"></div><img src="{C}garf_face.png" style="position:absolute;left:calc(var(--u)*4.5);top:calc(var(--u)*10.6);width:calc(var(--u)*13);transform:rotate(-3deg)">{tape(8, 8.4, 6, -8)}</div><h3 style="font-family:var(--fd);font-weight:400;font-size:17px;margin-top:8px">Collage revista</h3><p style="font-size:9.5px;line-height:1.5;color:var(--ink2)">Recortes, cinta, papel y letra a mano. Identidad y memes de formato. <b>Sin precio.</b> Referencia: editoriales de revista.</p></div>
<div><div class="sl" style="--w:170px;{sty('ivory')}"><img class="ph" src="{I}casa.jpg"></div><h3 style="font-family:var(--fd);font-weight:400;font-size:17px;margin-top:8px">Foto en escena</h3><p style="font-size:9.5px;line-height:1.5;color:var(--ink2)">Producto real en casa decorada. Cartera sola en estudio: con precio. Escena completa: sin precio. Referencia: tiendas latinas de Instagram.</p></div>
</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8mm;margin-top:6mm;font-size:9.5px;line-height:1.5;color:var(--ink2)">
<div><b style="color:var(--ink)">La mascota</b> se queda solo en la portada fijada «Hola, soy Vesta» y en el bot de la web. No sale en el resto del feed.</div>
<div><b style="color:var(--ink)">Ritmo del feed:</b> nunca dos piezas del mismo lenguaje seguidas. Vitrina, pantalla, Reel, escena, collage…</div>
<div><b style="color:var(--ink)">Texto:</b> sin emojis en las láminas (solo dentro de los mockups), máximo 12 palabras y sin frases de IA.</div></div>
<div class="foot"><span>VESTA BAGS · Contenido v3</span><span>Filosofía completa: filosofia-de-diseno.md</span></div></section>'''

feedc = [
 ("ivory", f'{word("Hola", 30, 10)}<img src="{I}mascota-vesta.png" style="position:absolute;width:{u(13)};left:{u(5.5)};top:{u(6.2)}"><div class="bot"><div class="t" style="font-size:{u(2.4)}">Hola, soy <em>Vesta</em></div></div>'),
 ("ivory", notes("Deseos 2026", [("<s>Un Porsche</s>", False), ("<s>Viaje a París</s>", False), ("Cartera VESTA", True)])),
 ("pink", floor() + word("Rosa") + studio("tote_pink", 13.5, 6.4) + stk("350", "Bs", 16.8, 15, P["pink"][1], P["pink"][0], -8)),
 ("garf", receipt([("Cartera Garfield", "×1"), ("Lunes soportables", "×52"), ("Cumplidos", "×∞")], ("ARREPENTIMIENTOS", "0"), 2.4, 4, 19.2)),
 ("stitch", floor() + word("Stitch") + studio("st_heart", 14.4, 6.4)),
 ("ivory", f'<img class="ph" src="{I}casa.jpg">'),
 ("butter", google("cómo justificar otra cartera", ["…<b>si es de Stitch</b>", "…<b>si combina con todo</b>", "…<b>si es original</b>"], 6)),
 ("hk", floor() + word("Kitty") + studio("hk_face", 15, 6.4) + stk("700", "Bs", 17, 15.2, P["hk"][1], P["hk"][0], -9)),
 ("stitch", bp("Santa Cruz", "VVI", "Mochila Stitch", "Flota") + studio("st_back", 9.5, 2.2)),
]
grid = "".join(f'<div class="sl" style="{sty(c)};border-radius:0;box-shadow:none">{x}</div>' for c, x in feedc)
feed = f'''<section class="page" style="display:grid;grid-template-columns:1fr auto;gap:12mm;align-items:center">
<div><div class="kick">Vista del perfil</div><h2 style="font-family:var(--fd);font-weight:400;font-size:34px;line-height:1.05;margin-top:4px">Así se vería <em>el feed</em></h2>
<p style="font-size:12px;color:var(--ink2);line-height:1.6;margin-top:10px;max-width:115mm">Mezcla de vitrina de color, pantallas con humor, escenas reales y collage. Se ve como una tienda con personalidad: cada fila tiene algo para vender, algo para reír y algo para guardar.</p></div>
<div style="background:#fff;border:1px solid var(--line);border-radius:18px;padding:14px 12px;width:max-content">
<div style="display:flex;align-items:center;gap:10px;margin-bottom:10px"><div style="width:42px;height:42px;border-radius:50%;background:var(--stone);display:grid;place-items:center"><img src="{I}logo-dark.png" style="width:32px"></div><div style="font-size:11px"><b>[PENDIENTE: @usuario]</b><div style="color:var(--muted)">Distribuidores oficiales de Tizza en Bolivia</div></div></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:3px;--w:132px">{grid}</div></div></section>'''

html = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>VESTA · Contenido v3</title><style>{CSS}</style></head><body>{cover}{direction}{feed}{"".join(pages)}</body></html>'
(D / "v3.html").write_text(html)
print("ok", html.count('class="page'))
