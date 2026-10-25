"""Genera los dos HTML de ideas de carruseles VESTA (luego se imprimen a PDF)."""
import pathlib
D = pathlib.Path(__file__).parent
I = "img/"
M = I + "mascota-vesta.png"

CSS = """
@import url(fonts/fonts.css);
@page{size:A4 landscape;margin:0}
:root{--ivory:#FBF6F1;--stone:#F0E2D6;--stone2:#E6D0BE;--line:#E8D7C9;--ink:#221B18;--ink2:#4B3B33;--muted:#715D51;--cacao:#7A4B3A;--deep:#4E3A30;--beige:#E8DED2;
 --fd:'Bodoni Moda',Georgia,serif;--fu:'Instrument Sans',Arial,sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--fu);color:var(--ink);background:var(--ivory);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:297mm;height:210mm;padding:12mm 13mm;position:relative;overflow:hidden;page-break-after:always;background:var(--ivory)}
.page.cover{background:var(--stone);display:grid;grid-template-columns:1.1fr .9fr;align-items:center;gap:10mm}
.cover h1{font-family:var(--fd);font-weight:400;font-size:54px;line-height:1.02;letter-spacing:-.02em}
.cover h1 em{font-style:italic;color:var(--cacao)}
.cover p{font-size:14px;line-height:1.55;color:var(--ink2);max-width:120mm;margin-top:14px}
.cover .logo{width:150px;margin-bottom:26px}
.cover .art{position:relative;height:160mm}
.kick{font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--cacao);font-weight:600}
.head{display:flex;justify-content:space-between;align-items:flex-start;gap:10mm}
.head h2{font-family:var(--fd);font-weight:400;font-size:30px;line-height:1.05;margin-top:4px;letter-spacing:-.01em}
.head .idea{font-size:12.5px;color:var(--ink2);margin-top:5px;max-width:165mm;line-height:1.45}
.chips{display:flex;flex-direction:column;gap:5px;align-items:flex-end;flex:none}
.chip{font-size:10.5px;padding:4px 11px;border-radius:999px;border:1px solid var(--line);background:#fff;white-space:nowrap}
.chip.main{background:var(--cacao);border-color:var(--cacao);color:var(--ivory);font-weight:600}
.row{display:flex;gap:14px;margin-top:10mm;justify-content:flex-start}
.slot{display:flex;flex-direction:column;gap:5px;align-items:center}
.slot small{font-size:9.5px;color:var(--muted);text-align:center;max-width:var(--w);line-height:1.3}
.notes{display:grid;grid-template-columns:1.25fr 1fr 1fr;gap:9mm;margin-top:9mm;font-size:11.5px;line-height:1.5;color:var(--ink2)}
.notes h4{font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--cacao);margin-bottom:4px}
.notes .cap{background:#fff;border:1px solid var(--line);border-radius:10px;padding:9px 11px;white-space:pre-line}
.foot{position:absolute;bottom:7mm;left:13mm;right:13mm;display:flex;justify-content:space-between;font-size:9px;color:var(--muted)}
/* ---------- slides ---------- */
.sl{--u:calc(var(--w)/24);width:var(--w);height:calc(var(--w)*1.25);position:relative;overflow:hidden;border-radius:7px;background:var(--ivory);box-shadow:0 8px 22px rgba(34,27,24,.13),0 1px 3px rgba(34,27,24,.08);flex:none}
.sl.stone{background:var(--stone)} .sl.deep{background:var(--deep);color:var(--ivory)} .sl.beige{background:var(--beige)}
.sl .ph{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.sl .shade{position:absolute;inset:auto 0 0 0;height:55%;background:linear-gradient(transparent,rgba(34,27,24,.72))}
.sl .shadeT{position:absolute;inset:0 0 auto 0;height:45%;background:linear-gradient(rgba(34,27,24,.55),transparent)}
.sl .pad{position:absolute;inset:0;padding:calc(var(--u)*1.6);display:flex;flex-direction:column}
.sl .t{font-family:var(--fd);font-weight:400;line-height:1.02;letter-spacing:-.015em}
.sl .t em{font-style:italic}
.sl .s{font-size:calc(var(--u)*.95);line-height:1.4}
.sl .k{font-size:calc(var(--u)*.72);letter-spacing:.2em;text-transform:uppercase;font-weight:600}
.sl .n{position:absolute;top:calc(var(--u)*1);right:calc(var(--u)*1);font-size:calc(var(--u)*.7);padding:calc(var(--u)*.2) calc(var(--u)*.6);border-radius:99px;background:rgba(251,246,241,.85);color:var(--ink)}
.sl .pill{display:inline-block;background:var(--cacao);color:var(--ivory);border-radius:99px;font-size:calc(var(--u)*.85);font-weight:600;padding:calc(var(--u)*.45) calc(var(--u)*1.1)}
.sl .pill.l{background:var(--ivory);color:var(--ink)}
.sl .m{position:absolute;width:calc(var(--u)*var(--ms,7));filter:drop-shadow(0 calc(var(--u)*.3) calc(var(--u)*.4) rgba(34,27,24,.18))}
.sl .bub{position:absolute;background:#fff;color:var(--ink);border-radius:calc(var(--u)*1.2);padding:calc(var(--u)*.7) calc(var(--u)*.9);font-size:calc(var(--u)*.9);line-height:1.3;box-shadow:0 2px 8px rgba(34,27,24,.12)}
.sl .arch{position:absolute;overflow:hidden;border-radius:999px 999px calc(var(--u)*.6) calc(var(--u)*.6)}
.sl .arch img{width:100%;height:100%;object-fit:cover}
.sl .logo{position:absolute;width:calc(var(--u)*5)}
.sl .big{font-family:var(--fd);position:absolute;color:var(--stone2);line-height:.85;white-space:nowrap;letter-spacing:-.03em}
.sl .card{background:#fff;border-radius:calc(var(--u)*.9);padding:calc(var(--u)*.9) calc(var(--u)*1);box-shadow:0 2px 8px rgba(34,27,24,.08)}
.sl .tag{display:inline-block;font-size:calc(var(--u)*.75);font-weight:700;letter-spacing:.12em;padding:calc(var(--u)*.25) calc(var(--u)*.7);border-radius:99px}
.sl .ok{background:#E3EBDD;color:#3F6B4E} .sl .no{background:#F3DCD6;color:#9E2A2B}
.sl .ic{display:flex;gap:calc(var(--u)*.7);align-items:center;font-size:calc(var(--u)*.95);margin-top:calc(var(--u)*.8)}
.sl .ic b{flex:none;width:calc(var(--u)*2.2);height:calc(var(--u)*2.2);border-radius:50%;background:var(--stone);display:grid;place-items:center;font-size:calc(var(--u)*1.1);font-weight:600;color:var(--cacao);font-family:var(--fd)}
.sl .price{position:absolute;background:var(--ivory);color:var(--ink);border-radius:99px;font-size:calc(var(--u)*.8);font-weight:600;padding:calc(var(--u)*.3) calc(var(--u)*.8)}
.sl .grid2{display:grid;grid-template-columns:1fr 1fr;gap:calc(var(--u)*.6)}
.sl .grid2 div{border-radius:calc(var(--u)*.7);overflow:hidden;position:relative;aspect-ratio:1/1.15;background:#fff}
.sl .grid2 img{width:100%;height:100%;object-fit:cover}
.sl .grid2 span{position:absolute;left:calc(var(--u)*.4);bottom:calc(var(--u)*.4);background:var(--ivory);border-radius:99px;font-size:calc(var(--u)*.72);font-weight:600;padding:calc(var(--u)*.15) calc(var(--u)*.6)}
.tip{display:grid;grid-template-columns:repeat(3,1fr);gap:7mm;margin-top:8mm}
.tip>div{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 14px;font-size:11px;line-height:1.5;color:var(--ink2)}
.tip h3{font-family:var(--fd);font-weight:400;font-size:19px;color:var(--ink);margin-bottom:5px}
.tip .sk{height:170px;border-radius:8px;background:var(--stone);margin-bottom:9px;position:relative;overflow:hidden}
"""

def page(num, kind, title, idea, redes, slides, caption, how, why, w=None, cls=""):
    w = w or {4: 240, 5: 192, 6: 158}[len(slides)]
    main, *rest = redes
    chips = f'<span class="chip main">Red objetivo: {main}</span>' + "".join(f'<span class="chip">También: {r}</span>' for r in rest)
    chips += f'<span class="chip">Formato: carrusel 4:5 · {len(slides)} láminas</span>'
    row = "".join(f'<div class="slot">{s}<small>{lbl}</small></div>' for s, lbl in slides)
    return f'''<section class="page {cls}" style="--w:{w}px">
<div class="head"><div><div class="kick">{kind} · Carrusel {num:02d}</div><h2>{title}</h2><p class="idea">{idea}</p></div><div class="chips">{chips}</div></div>
<div class="row">{row}</div>
<div class="notes"><div><h4>Caption listo</h4><div class="cap">{caption}</div></div><div><h4>Cómo hacerlo</h4>{how}</div><div><h4>Por qué funciona</h4>{why}</div></div>
<div class="foot"><span>VESTA BAGS · Ideas de contenido</span><span>Fotos de referencia: catálogos Tizza (Octubre y Licencias)</span></div></section>'''

def sl(inner, cls="", n=None, total=None):
    num = f'<span class="n">{n}/{total}</span>' if n else ""
    return f'<div class="sl {cls}">{inner}{num}</div>'

def mascot(style, ms=7):
    return f'<img class="m" src="{M}" style="--ms:{ms};{style}">'

def ph(src, pos="center"):
    return f'<img class="ph" src="{I}{src}.jpg" style="object-position:{pos}">'

def carousel(items):
    t = len(items)
    return [(sl(h, c, i + 1, t), lbl) for i, (h, c, lbl) in enumerate(items)]

U = "calc(var(--u)*{})"
def u(x): return U.format(x)

# ================= PDF 1: DIVERTIDOS CON VESTA =================
fun = []

fun.append(page(1, "Divertido con Vesta", "Hola, soy Vesta",
 "La mascota presenta la tienda. Es el primer carrusel de la cuenta y el que fijas arriba del perfil.",
 ["📸 Instagram", "📘 Facebook"],
 carousel([
  (f'<div class="big" style="font-size:{u(13)};left:{u(-1)};top:{u(1)}">Hola</div>'+mascot(f"left:{u(4.5)};top:{u(6)}",15)+
   f'<div class="pad" style="justify-content:flex-end"><div class="t" style="font-size:{u(2.6)}">Hola, soy <em>Vesta</em> 🤍</div><div class="s" style="margin-top:{u(.5)};color:var(--muted)">Desliza y te cuento</div></div>',"stone","Portada: la mascota grande y el saludo"),
  (f'<div class="pad"><div class="k" style="color:var(--cacao)">Te presento</div><div class="t" style="font-size:{u(2.2)};margin-top:{u(.5)}">Soy una carterita que te ayuda a elegir <em>la tuya</em></div></div>'
   f'<div class="arch" style="left:{u(1.5)};bottom:{u(1.5)};width:{u(6.4)};height:{u(10)}"><img src="{I}garf_pizza.jpg"></div>'
   f'<div class="arch" style="left:{u(8.8)};bottom:{u(1.5)};width:{u(6.4)};height:{u(12)}"><img src="{I}hk_face.jpg"></div>'
   f'<div class="arch" style="left:{u(16.1)};bottom:{u(1.5)};width:{u(6.4)};height:{u(10)}"><img src="{I}st_heart.jpg"></div>',"","Tres colecciones en arcos (estilo de la web)"),
  (f'<div class="pad"><div class="t" style="font-size:{u(2.2)}">Lo que hacemos</div>'
   f'<div class="ic"><b>✓</b>Carteras originales, directo de Tizza</div><div class="ic"><b>📍</b>Delivery en La Paz</div><div class="ic"><b>🚌</b>Envíos por flota a toda Bolivia</div><div class="ic"><b>✦</b>Pedidos a una semana</div></div>'
   +mascot(f"right:{u(.8)};bottom:{u(.8)}",6),"","Íconos simples y la mascota en la esquina"),
  (f'<div class="pad"><div class="t" style="font-size:{u(2.2)}">Comprar es <em>fácil</em></div>'
   f'<div class="card" style="margin-top:{u(1)}"><div class="ic" style="margin:0"><b>1</b>Elige tu cartera</div></div>'
   f'<div class="card" style="margin-top:{u(.6)}"><div class="ic" style="margin:0"><b>2</b>Escríbenos por WhatsApp</div></div>'
   f'<div class="card" style="margin-top:{u(.6)}"><div class="ic" style="margin:0"><b>3</b>Coordinamos pago y entrega</div></div></div>',"stone","Pasos en tarjetas blancas"),
  (mascot(f"left:{u(7)};top:{u(3)}",10)+f'<div class="pad" style="justify-content:flex-end;text-align:center;align-items:center"><div class="t" style="font-size:{u(2.1)}">¿Te ayudo a elegir?</div><div class="s" style="margin:{u(.4)} 0 {u(.9)};opacity:.85">+591 76705942 · de 9:00 a 19:00</div><span class="pill l">Escríbenos por WhatsApp 🤍</span>'
   f'<img src="{I}logo-white.png" style="width:{u(5)};margin-top:{u(1)}"></div>',"deep","Cierre con CTA sobre cacao oscuro"),
 ]),
 "Hola, soy Vesta 🤍 La carterita que te ayuda a encontrar la tuya.\nEn VESTA BAGS traemos carteras originales de Tizza a Bolivia: delivery en La Paz y envíos por flota a todo el país.\nEscríbenos por WhatsApp: +591 76705942\n#VestaBags #CarterasBolivia #LaPazBolivia #TizzaBolivia",
 "<p>Canva, tamaño 1080×1350. Fondo #F0E2D6, títulos en Bodoni Moda y texto en Instrument Sans.</p><p style='margin-top:5px'>La mascota es <b>mascota-vesta.png</b>: solo se cambia su tamaño, nunca su color.</p>",
 "<p>Presenta la marca con un personaje en vez de una cara. Resuelve las 3 dudas de entrada (qué es, si es original, cómo compro) y sirve como publicación fija del perfil.</p>"))

fun.append(page(2, "Divertido con Vesta", "Vesta te dice qué personaje eres",
 "Un test rápido: cada lámina une una personalidad con una colección. La gente comenta y etiqueta a sus amigas.",
 ["🎵 TikTok (modo foto)", "📸 Instagram"],
 carousel([
  (mascot(f"left:{u(1.5)};bottom:{u(1.5)}",9)+f'<div class="bub" style="left:{u(10)};bottom:{u(8)};width:{u(12)}">¡Te leo la personalidad! 🔮</div>'
   f'<div class="pad"><div class="k" style="color:var(--cacao)">Test</div><div class="t" style="font-size:{u(2.9)};margin-top:{u(.4)}">¿Qué personaje <em>eres?</em></div></div>',"stone","Portada con Vesta «adivina»"),
  (ph("garf_pizza")+'<div class="shade"></div>'+f'<div class="pad" style="justify-content:flex-end;color:var(--ivory)"><div class="s">Si odias los lunes y amas la pizza…</div><div class="t" style="font-size:{u(2.6)}">eres <em>Garfield</em> 🧡</div><div class="s" style="opacity:.8;margin-top:{u(.3)}">Cartera Garfield · Cód. 2145</div></div>',"","Foto real + frase"),
  (ph("hk_face","left center")+'<div class="shade"></div>'+f'<div class="pad" style="justify-content:flex-end;color:var(--ivory)"><div class="s">Si eres tierna pero con carácter…</div><div class="t" style="font-size:{u(2.6)}">eres <em>Hello Kitty</em> 🎀</div><div class="s" style="opacity:.8;margin-top:{u(.3)}">Cartera Hello Kitty · Cód. 2041</div></div>',"",""),
  (ph("st_heart")+'<div class="shade"></div>'+f'<div class="pad" style="justify-content:flex-end;color:var(--ivory)"><div class="s">Si eres un caos adorable…</div><div class="t" style="font-size:{u(2.6)}">eres <em>Stitch</em> 💙</div><div class="s" style="opacity:.8;margin-top:{u(.3)}">Cartera corazón Stitch · Cód. 2102</div></div>',"",""),
  (mascot(f"right:{u(1.5)};bottom:{u(1.5)}",8)+f'<div class="pad"><div class="t" style="font-size:{u(2.4)}">¿Cuál <em>eres tú?</em></div><div class="s" style="margin-top:{u(.6)};color:var(--muted)">Comenta tu personaje y etiqueta a tu amiga que es igualita 👇</div><div style="margin-top:{u(1.2)}"><span class="pill">Pídela por WhatsApp</span></div></div>',"","Cierre: pregunta y CTA"),
 ]),
 "¿Qué personaje eres? 👀 Vesta ya lo sabe.\nGarfield, Hello Kitty o Stitch: comenta el tuyo y etiqueta a tu amiga 👇\nColaboraciones oficiales Tizza x Garfield, Hello Kitty y Disney Stitch · Pídelas por WhatsApp +591 76705942\n#VestaBags #Garfield #HelloKitty #Stitch #CarterasBolivia",
 "<p>En TikTok súbelo como <b>fotos</b> (modo foto, que se desliza solo) con un audio en tendencia. En IG va como carrusel.</p><p style='margin-top:5px'>La foto ocupa toda la lámina, con un degradado oscuro abajo para que se lea el texto.</p>",
 "<p>Los tests de personalidad generan comentarios y etiquetas, que es lo que más alcance da. Los personajes siempre van como «colaboración oficial».</p>"))

fun.append(page(3, "Divertido con Vesta", "¿Este o este?",
 "Una encuesta visual entre dos piezas de la misma colección. Es la forma más fácil de que comenten.",
 ["📸 Instagram", "🎵 TikTok (modo foto)"],
 carousel([
  (f'<div class="pad" style="align-items:center;text-align:center"><div class="t" style="font-size:{u(3.2)};margin-top:{u(1.2)}">¿Este<br>o <em>este?</em></div><div class="s" style="color:var(--muted);margin-top:{u(.5)}">Edición Stitch 💙</div></div>'
   f'<div class="arch" style="left:{u(2)};bottom:{u(1.6)};width:{u(9.5)};height:{u(12)}"><img src="{I}st_heart.jpg"></div><div class="arch" style="right:{u(2)};bottom:{u(1.6)};width:{u(9.5)};height:{u(12)}"><img src="{I}st_back.jpg"></div>'
   +mascot(f"left:{u(9.5)};bottom:{u(.6)}",5),"stone","Portada: las dos opciones en arcos"),
  (ph("st_heart")+f'<div class="pad"><span class="pill" style="align-self:flex-start;font-size:{u(1.3)}">A</span></div><span class="price" style="left:{u(1.6)};bottom:{u(1.6)}">Cartera corazón · Cód. 2102</span>',"","Opción A"),
  (ph("st_back")+f'<div class="pad"><span class="pill" style="align-self:flex-start;font-size:{u(1.3)}">B</span></div><span class="price" style="left:{u(1.6)};bottom:{u(1.6)}">Mochila Stitch · Cód. 2100</span>',"","Opción B"),
  (mascot(f"left:{u(8)};top:{u(4)}",8)+f'<div class="bub" style="left:{u(3)};top:{u(1.5)};width:{u(18)};text-align:center">Yo me quedo con la A… ¿y tú? 🤭</div>'
   f'<div class="pad" style="justify-content:flex-end;align-items:center;text-align:center"><div class="t" style="font-size:{u(2.3)}">Vota en comentarios</div><div class="s" style="margin:{u(.3)} 0 {u(.8)};opacity:.85">A o B</div><span class="pill l">Pídela por WhatsApp 🤍</span></div>',"deep","Vesta opina y pide el voto"),
 ], ),
 "¿Este o este? 💙 Edición Stitch.\nA: cartera corazón · B: mochila. Vota en comentarios y te contamos cuál ganó.\nColección Disney Stitch · Pídela por WhatsApp +591 76705942\n#VestaBags #Stitch #EsteOEste #CarterasBolivia",
 "<p>Repítelo cada semana con otra colección (Garfield, Hello Kitty) o con dos colores del mismo modelo.</p><p style='margin-top:5px'>En historias, usa la misma foto con el sticker de encuesta.</p>",
 "<p>Elegir entre dos es muy fácil y hace que la gente comente sin pensarlo. Además te dice qué pieza prefieren para traer más stock.</p>"))

fun.append(page(4, "Divertido con Vesta", "Mito o verdad, con Vesta",
 "Vesta responde las dudas que más llegan por WhatsApp. Solo con políticas confirmadas.",
 ["📘 Facebook", "📸 Instagram"],
 carousel([
  (mascot(f"left:{u(8)};top:{u(8.5)}",9)+f'<div class="pad" style="align-items:center;text-align:center"><div class="k" style="color:var(--cacao)">Vesta responde</div><div class="t" style="font-size:{u(3)};margin-top:{u(.4)}">¿Mito o <em>verdad?</em></div></div>',"stone","Portada"),
  (f'<div class="pad"><span class="tag no" style="align-self:flex-start">MITO</span><div class="t" style="font-size:{u(2)};margin-top:{u(.8)}">«Son réplicas»</div><div class="card s" style="margin-top:{u(1)}">Somos <b>distribuidores oficiales de Tizza</b> y traemos cada pieza directamente de la marca.</div></div>'+mascot(f"right:{u(1)};bottom:{u(1)}",5.5),"",""),
  (f'<div class="pad"><span class="tag ok" style="align-self:flex-start">VERDAD</span><div class="t" style="font-size:{u(2)};margin-top:{u(.8)}">«Envían a toda Bolivia»</div><div class="card s" style="margin-top:{u(1)}">En La Paz, por <b>delivery</b>. Al resto del país, por <b>flota</b> (el envío lo paga quien compra).</div></div>'+mascot(f"right:{u(1)};bottom:{u(1)}",5.5),"",""),
  (f'<div class="pad"><span class="tag ok" style="align-self:flex-start">VERDAD</span><div class="t" style="font-size:{u(2)};margin-top:{u(.8)}">«Te traen algo que no está en la tienda»</div><div class="card s" style="margin-top:{u(1)}"><b>Pedidos a una semana</b>: cualquier pieza de los catálogos de Tizza, con el 50 % de adelanto.</div></div>'+mascot(f"right:{u(1)};bottom:{u(1)}",5.5),"",""),
  (f'<div class="pad"><div class="t" style="font-size:{u(2.1)}">¿Otra duda?</div><div class="s" style="margin-top:{u(.5)};opacity:.85">Pagas con QR, transferencia o en efectivo contra entrega.</div></div>'+mascot(f"left:{u(8)};top:{u(8)}",8)+
   f'<div class="pad" style="justify-content:flex-end;align-items:center"><span class="pill l">Escríbenos 🤍 +591 76705942</span></div>',"deep","Cierre con pagos y CTA"),
 ]),
 "¿Mito o verdad? Vesta responde lo que más nos preguntan 🤍\n✔ Originales: somos distribuidores oficiales de Tizza.\n✔ Delivery en La Paz y envíos por flota a toda Bolivia.\n✔ Pedidos a una semana con el 50 % de adelanto.\n¿Otra duda? Escríbenos: +591 76705942",
 "<p>Usa una sola plantilla (etiqueta, frase entre comillas y tarjeta blanca) y cambia solo el texto.</p><p style='margin-top:5px'>No incluyas «¿hay devoluciones?» como mito: la política es <b>sin devoluciones</b>. Esa va en otro formato.</p>",
 "<p>Quita miedos antes de comprar y te ahorra responder lo mismo por WhatsApp. En Facebook se comparte mucho en grupos de compras.</p>"))

fun.append(page(5, "Divertido con Vesta", "Lo que Vesta lleva en su cartera",
 "Una parodia tierna del «qué hay en mi bolso». Vesta saca objetos y al final muestra la billetera real.",
 ["🎵 TikTok (modo foto)", "📸 Instagram"],
 carousel([
  (mascot(f"left:{u(6)};top:{u(7)}",12)+f'<div class="pad"><div class="t" style="font-size:{u(2.5)}">Lo que llevo en <em>mi cartera</em></div><div class="s" style="color:var(--muted);margin-top:{u(.4)}">por Vesta 🤍</div></div>',"stone","Portada"),
  (f'<div class="pad" style="align-items:center;text-align:center;justify-content:center"><div style="font-size:{u(5)}">💄</div><div class="t" style="font-size:{u(2)};margin-top:{u(.5)}">Labial «por si acaso»</div><div class="s" style="color:var(--muted);margin-top:{u(.4)}">nunca se usa, pero siempre va</div></div>'+mascot(f"right:{u(1)};bottom:{u(1)}",5),"",""),
  (f'<div class="pad" style="align-items:center;text-align:center;justify-content:center"><div style="font-size:{u(5)}">🔌</div><div class="t" style="font-size:{u(2)};margin-top:{u(.5)}">Cargador al 3 %</div><div class="s" style="color:var(--muted);margin-top:{u(.4)}">el mío no, el tuyo</div></div>'+mascot(f"right:{u(1)};bottom:{u(1)}",5),"",""),
  (ph("garf_camera")+'<div class="shadeT"></div>'+f'<div class="pad" style="color:var(--ivory)"><div class="t" style="font-size:{u(2)}">Y lo más importante…</div><div class="s" style="opacity:.9">la billetera Garfield 🧡</div></div><span class="price" style="left:{u(1.6)};bottom:{u(1.6)}">Billetera Garfield · Cód. 2146</span>',"","Remate con foto real"),
  (mascot(f"left:{u(1.4)};bottom:{u(1.4)}",7)+f'<div class="pad"><div class="t" style="font-size:{u(2.2)}">¿Y tú qué llevas?</div><div class="s" style="margin-top:{u(.4)};opacity:.85">Cuéntanos en comentarios</div></div><div class="pad" style="justify-content:flex-end;align-items:flex-end"><span class="pill l">Pídela por WhatsApp</span></div>',"deep",""),
 ]),
 "Lo que Vesta lleva en su cartera 👜\nLabial por si acaso, cargador al 3 % y lo más importante: la Billetera Garfield 🧡\n¿Y tú qué llevas? Cuéntanos 👇\nColaboración oficial Tizza x Garfield · Pídela por WhatsApp +591 76705942",
 "<p>Los emojis grandes en el centro funcionan como «objetos». No hacen falta fotos hasta la lámina final.</p><p style='margin-top:5px'>Si tienes los objetos, también puedes fotografiarlos desde arriba sobre la tela nude.</p>",
 "<p>El humor cercano genera guardados y compartidos. La venta aparece al final, sin presionar.</p>"))

fun.append(page(6, "Divertido con Vesta", "Vesta elige según tu plan",
 "La mascota recomienda una pieza para cada plan del fin de semana. Combina el humor con producto real.",
 ["📸 Instagram", "📘 Facebook"],
 carousel([
  (mascot(f"right:{u(1.5)};bottom:{u(1.5)}",10)+f'<div class="bub" style="left:{u(1.5)};bottom:{u(9)};width:{u(11)}">Dime tu plan y yo elijo 💁‍♀️</div><div class="pad"><div class="t" style="font-size:{u(2.8)}">Tu cartera según <em>tu plan</em></div></div>',"stone","Portada"),
  (ph("hk_face","30% center")+mascot(f"right:{u(.8)};top:{u(.8)}",4.5)+'<div class="shade"></div>'+f'<div class="pad" style="justify-content:flex-end;color:var(--ivory)"><div class="k">Plan</div><div class="t" style="font-size:{u(2.2)}">Salida con amigas</div><div class="s" style="opacity:.85">Hello Kitty · Cód. 2041</div></div>',"","La mascota se asoma en cada foto"),
  (ph("garf_hand")+mascot(f"right:{u(.8)};top:{u(.8)}",4.5)+'<div class="shade"></div>'+f'<div class="pad" style="justify-content:flex-end;color:var(--ivory)"><div class="k">Plan</div><div class="t" style="font-size:{u(2.2)}">Pizza el viernes</div><div class="s" style="opacity:.85">Garfield · Cód. 2138</div></div>',"",""),
  (ph("casa")+mascot(f"right:{u(.8)};top:{u(.8)}",4.5)+'<div class="shade"></div>'+f'<div class="pad" style="justify-content:flex-end;color:var(--ivory)"><div class="k">Plan</div><div class="t" style="font-size:{u(2.2)}">Trabajo o U</div><div class="s" style="opacity:.85">Bolso acolchado · Cód. 2439</div></div>',"",""),
  (mascot(f"left:{u(8)};top:{u(3)}",8)+f'<div class="pad" style="justify-content:flex-end;align-items:center;text-align:center"><div class="t" style="font-size:{u(2)}">¿Cuál es tu plan?</div><div class="s" style="margin:{u(.3)} 0 {u(.8)}">Comenta y Vesta te elige una 🤍</div><span class="pill">Escríbenos por WhatsApp</span></div>',"",""),
 ]),
 "Dime tu plan y Vesta elige tu cartera 🤍\nSalida con amigas → Hello Kitty · Pizza el viernes → Garfield · Trabajo o U → bolso acolchado.\n¿Cuál es tu plan? Comenta y te elegimos una.\nPídelas por WhatsApp +591 76705942 #VestaBags",
 "<p>La mascota pequeña en la esquina de cada foto mantiene el hilo divertido sin tapar el producto.</p><p style='margin-top:5px'>Responde los comentarios «como Vesta»: «Para tu cumple te elijo…».</p>",
 "<p>Convierte el catálogo en una conversación. Cada respuesta en comentarios es una oportunidad para mandar a la clienta a WhatsApp.</p>"))

fun.append(page(7, "Divertido con Vesta", "Diccionario Vesta: ¿cartera, morral o mochila?",
 "Un contenido educativo y tierno que explica los tipos de piezas. Se guarda mucho.",
 ["📸 Instagram", "📘 Facebook"],
 carousel([
  (mascot(f"left:{u(1.5)};bottom:{u(1.5)}",8)+f'<div class="pad"><div class="k" style="color:var(--cacao)">Diccionario Vesta</div><div class="t" style="font-size:{u(2.5)};margin-top:{u(.4)}">¿Cartera, morral o <em>mochila?</em></div></div><div class="bub" style="right:{u(1.5)};bottom:{u(4)};width:{u(11)}">Te lo explico en 3 láminas 🤓</div>',"stone","Portada"),
  (f'<div class="pad"><div class="t" style="font-size:{u(2.1)}">Cartera</div><div class="s" style="color:var(--muted)">Se lleva en la mano o al hombro. Para salir.</div><div class="arch" style="left:{u(4)};right:{u(4)};bottom:{u(1.6)};height:{u(15)};position:absolute"><img src="{I}hk_bag.jpg"></div></div>',"","Definición + foto en arco"),
  (f'<div class="pad"><div class="t" style="font-size:{u(2.1)}">Cartera cruzada</div><div class="s" style="color:var(--muted)">Con correa larga: manos libres todo el día.</div><div class="arch" style="left:{u(4)};right:{u(4)};bottom:{u(1.6)};height:{u(15)};position:absolute"><img src="{I}st_heart.jpg"></div></div>',"",""),
  (f'<div class="pad"><div class="t" style="font-size:{u(2.1)}">Mochila</div><div class="s" style="color:var(--muted)">En la espalda. Entra todo para la U.</div><div class="arch" style="left:{u(4)};right:{u(4)};bottom:{u(1.6)};height:{u(15)};position:absolute"><img src="{I}st_back.jpg"></div></div>',"",""),
  (f'<div class="pad"><div class="t" style="font-size:{u(2.1)}">Billetera</div><div class="s" style="color:var(--muted)">Pequeña, para tarjetas y monedas. Regalo ideal.</div><div class="arch" style="left:{u(4)};right:{u(4)};bottom:{u(1.6)};height:{u(15)};position:absolute"><img src="{I}garf_wallet.jpg"></div></div>',"",""),
  (mascot(f"left:{u(8)};top:{u(3)}",8)+f'<div class="pad" style="justify-content:flex-end;align-items:center;text-align:center"><div class="t" style="font-size:{u(2)}">¿Cuál te falta?</div><div class="s" style="margin:{u(.3)} 0 {u(.8)};opacity:.85">Guárdalo para tu próxima compra</div><span class="pill l">Pregúntanos por WhatsApp</span></div>',"deep",""),
 ]),
 "Diccionario Vesta 🤓 ¿Cartera, cruzada, mochila o billetera?\nGuárdalo para tu próxima compra y cuéntanos cuál te falta 👇\nPídela por WhatsApp +591 76705942\n#VestaBags #CarterasBolivia #TipsDeModa",
 "<p>Usa la misma plantilla para cada tipo: título en Bodoni, una línea explicativa y la foto en arco abajo.</p>",
 "<p>El contenido útil se <b>guarda</b>, y los guardados le dicen a Instagram que muestre más tu cuenta.</p>"))

fun.append(page(8, "Divertido con Vesta", "Cómo comprar, paso a paso con Vesta",
 "El tutorial de compra con la mascota. Ideal para fijarlo en el perfil de Facebook y en las destacadas.",
 ["📘 Facebook", "📸 Instagram"],
 carousel([
  (mascot(f"left:{u(6)};top:{u(7)}",12)+f'<div class="pad"><div class="t" style="font-size:{u(2.6)}">Así compras en <em>VESTA</em></div><div class="s" style="color:var(--muted)">en 3 pasos</div></div>',"stone","Portada"),
  (f'<div class="pad"><div class="t" style="font-size:{u(5)};color:var(--cacao)">1</div><div class="t" style="font-size:{u(2)}">Elige tu cartera</div><div class="s" style="color:var(--muted);margin-top:{u(.3)}">En nuestras redes, la web o los catálogos de Tizza</div></div><div class="arch" style="right:{u(1.5)};bottom:{u(1.5)};width:{u(9)};height:{u(11)}"><img src="{I}garf_lazy.jpg"></div>',"",""),
  (f'<div class="pad"><div class="t" style="font-size:{u(5)};color:var(--cacao)">2</div><div class="t" style="font-size:{u(2)}">Escríbenos por WhatsApp</div><div class="s" style="color:var(--muted);margin-top:{u(.3)}">+591 76705942 · de 9:00 a 19:00</div><div class="bub" style="position:relative;margin-top:{u(1.2)};align-self:flex-start">Hola, equipo VESTA. Quiero esta 🤍</div></div>'+mascot(f"right:{u(1)};bottom:{u(1)}",6),"",""),
  (f'<div class="pad"><div class="t" style="font-size:{u(5)};color:var(--cacao)">3</div><div class="t" style="font-size:{u(2)}">Pago y entrega</div><div class="s" style="color:var(--muted);margin-top:{u(.3)}">QR, transferencia o efectivo contra entrega. Delivery en La Paz o flota al resto de Bolivia.</div></div>'+mascot(f"right:{u(1)};bottom:{u(1)}",6),"",""),
  (f'<div class="pad"><div class="t" style="font-size:{u(2)}">¿No está en la tienda?</div><div class="s" style="margin-top:{u(.4)};opacity:.85">Lo traemos para ti: pedidos a una semana con el 50 % de adelanto 🤍</div></div>'+mascot(f"left:{u(8)};bottom:{u(4)}",8)+f'<div class="pad" style="justify-content:flex-end;align-items:center"><span class="pill l">Escríbenos</span></div>',"deep",""),
 ]),
 "Así compras en VESTA 🤍\n1. Elige tu cartera.\n2. Escríbenos por WhatsApp: +591 76705942 (de 9:00 a 19:00).\n3. Pagas con QR, transferencia o efectivo contra entrega. Delivery en La Paz o flota al resto de Bolivia.\n¿No está en la tienda? Pedidos a una semana con el 50 % de adelanto.",
 "<p>Números grandes en cacao y una sola idea por lámina. Mismo texto que la web, para no contradecirse.</p>",
 "<p>Quien llega de un anuncio entiende en 10 segundos cómo comprar. Así te escriben con la decisión casi tomada.</p>"))

# ================= PDF 2: FOTOS REALES SIN CARAS =================
real = []

real.append(page(1, "Foto real sin caras", "Tu cartera según el plan",
 "Tres escenas reales, cada pieza en su ambiente: paseo, tarde en casa y día de trabajo. Ninguna muestra caras.",
 ["📸 Instagram", "📘 Facebook"],
 carousel([
  (f'<div class="pad"><div class="t" style="font-size:{u(2.6)}">Tres planes,<br><em>tres carteras</em></div></div>'
   f'<div class="arch" style="left:{u(1.5)};bottom:{u(1.5)};width:{u(6.4)};height:{u(11)}"><img src="{I}dunas.jpg" style="object-position:center 70%"></div><div class="arch" style="left:{u(8.8)};bottom:{u(1.5)};width:{u(6.4)};height:{u(13)}"><img src="{I}silla.jpg"></div><div class="arch" style="left:{u(16.1)};bottom:{u(1.5)};width:{u(6.4)};height:{u(11)}"><img src="{I}casa.jpg"></div>',"stone","Portada: las tres escenas en arcos"),
  (ph("dunas","center 70%")+'<div class="shade"></div>'+f'<div class="pad" style="justify-content:flex-end;color:var(--ivory)"><div class="k">Plan 01</div><div class="t" style="font-size:{u(2.1)}">De paseo</div><div class="s" style="opacity:.85">Cartera blanca · Cód. 2000</div></div>',"","Producto en un taburete al aire libre"),
  (ph("silla")+'<div class="shade"></div>'+f'<div class="pad" style="justify-content:flex-end;color:var(--ivory)"><div class="k">Plan 02</div><div class="t" style="font-size:{u(2.1)}">Tarde de jardín</div><div class="s" style="opacity:.85">Cód. 2019</div></div>',"","Colgada en una silla de madera"),
  (ph("casa")+'<div class="shade"></div>'+f'<div class="pad" style="justify-content:flex-end;color:var(--ivory)"><div class="k">Plan 03</div><div class="t" style="font-size:{u(2.1)}">Día de trabajo</div><div class="s" style="opacity:.85">Bolso acolchado · Cód. 2439</div></div>',"","En el piso, con laptop asomando"),
  (f'<div class="pad" style="justify-content:center;align-items:center;text-align:center"><div class="t" style="font-size:{u(2.3)}">¿Cuál es <em>tu plan?</em></div><div class="s" style="color:var(--muted);margin:{u(.4)} 0 {u(1)}">Te ayudamos a elegir la tuya</div><span class="pill">Escríbenos por WhatsApp 🤍</span><img src="{I}logo-dark.png" style="width:{u(5)};margin-top:{u(1.3)}"></div>',"stone","Cierre limpio en nude"),
 ]),
 "Tres planes, tres carteras 🤍\nDe paseo, tarde de jardín o día de trabajo: ¿cuál es tu plan?\nPregúntanos colores y precio por WhatsApp: +591 76705942\n#VestaBags #CarterasBolivia #OutfitBolivia",
 "<p><b>Foto:</b> la cartera sola en un mueble (taburete, silla, piso de madera), con luz de ventana o al aire libre en la tarde.</p><p style='margin-top:5px'>Usa el celular a la altura de la cartera, en modo retrato, y deja espacio arriba para el texto.</p>",
 "<p>Las escenas reales hacen que la clienta se imagine usándola. El producto es el protagonista y no hace falta modelo.</p>"))

real.append(page(2, "Foto real sin caras", "Garfield en la vida real",
 "Las piezas Garfield en escenas de diner: mano sosteniendo, sobre la mesa y junto a la pizza. Solo manos.",
 ["🎵 TikTok (modo foto)", "📸 Instagram"],
 carousel([
  (ph("garf_pizza")+'<div class="shade"></div>'+f'<div class="pad" style="justify-content:flex-end;color:var(--ivory)"><div class="k">Colaboración oficial Tizza x Garfield</div><div class="t" style="font-size:{u(2.6)}">Garfield <em>en la vida real</em> 🧡</div></div>',"","Portada: la pieza más llamativa"),
  (ph("garf_hand")+f'<span class="price" style="left:{u(1.6)};bottom:{u(1.6)}">Cartera Garfield · Cód. 2138 · 700 Bs</span>',"","Mano sosteniendo por el asa"),
  (ph("garf_lazy")+f'<span class="price" style="left:{u(1.6)};bottom:{u(1.6)}">Lazy Day · Cód. 2141 · 810 Bs</span>',"","Mismo encuadre, otra pieza"),
  (ph("garf_wallet")+f'<span class="price" style="left:{u(1.6)};bottom:{u(1.6)}">Billetera · Cód. 2139 · 350 Bs</span>',"","Sobre la mesa, en diagonal"),
  (ph("garf_det")+'<div class="shade"></div>'+f'<div class="pad" style="justify-content:flex-end;color:var(--ivory)"><div class="t" style="font-size:{u(2)}">¿Cuál te llevas?</div><div class="s" style="opacity:.85;margin-bottom:{u(.6)}">Pídela por WhatsApp 🤍</div></div>',"","Detalle en primer plano + CTA"),
 ]),
 "Garfield en la vida real 🧡🍕\nCartera 2138 · Lazy Day 2141 · Billetera 2139.\nColaboración oficial Tizza x Garfield · Pídelas por WhatsApp +591 76705942\n#VestaBags #Garfield #CarterasBolivia #LaPazBolivia",
 "<p><b>Foto:</b> solo el brazo entrando desde arriba y sosteniendo el asa. Fondo de color (pared, mantel) que combine con la colección.</p><p style='margin-top:5px'>Precios del catálogo de venta: confírmalos antes de publicar.</p>",
 "<p>La mano da escala y sensación real sin mostrar cara. El mismo encuadre en todas las láminas hace que el carrusel se vea profesional.</p>"))

real.append(page(3, "Foto real sin caras", "Así se lleva",
 "Las piezas puestas, del cuello para abajo: cómo se ven en la mano y en el cuerpo. La duda clave antes de comprar.",
 ["📸 Instagram", "🎵 TikTok (modo foto)"],
 carousel([
  (ph("manos2","center 30%")+'<div class="shadeT"></div>'+f'<div class="pad" style="color:var(--ivory)"><div class="t" style="font-size:{u(2.8)}">Así <em>se lleva</em></div></div>',"","Portada: torso con la cartera"),
  (ph("manos2","center 40%")+f'<span class="price" style="left:{u(1.6)};bottom:{u(1.6)}">En la mano · Cód. 1942</span>',"","Encuadre de los hombros a las rodillas"),
  (ph("manos")+f'<span class="price" style="left:{u(1.6)};bottom:{u(1.6)}">Al frente · Cód. 0976</span>',"","Las dos manos sosteniendo"),
  (ph("garf_hand")+f'<span class="price" style="left:{u(1.6)};bottom:{u(1.6)}">Colgando del asa · Cód. 2138</span>',"","Solo el brazo"),
  (f'<div class="pad" style="justify-content:center"><div class="t" style="font-size:{u(2.2)}">¿Quieres ver cómo te queda?</div><div class="s" style="color:var(--muted);margin:{u(.5)} 0 {u(1)}">Te mandamos fotos y medidas reales por WhatsApp antes de confirmar.</div><span class="pill" style="align-self:flex-start">Escríbenos 🤍</span></div>',"stone","Cierre: refuerza «fotos reales antes de comprar»"),
 ]),
 "Así se lleva 🤍 En la mano, al frente o colgando del asa.\n¿Quieres ver cómo te queda? Te mandamos fotos y medidas reales por WhatsApp antes de confirmar: +591 76705942\n#VestaBags #CarterasBolivia #OOTD",
 "<p><b>Foto:</b> pide a alguien de la familia que la lleve. Encuadra del cuello a las rodillas, con ropa neutra (blanco, beige, jean) frente a una pared clara.</p>",
 "<p>Responde «¿de qué tamaño es en persona?», la duda que más frena la compra. Como no hay devoluciones, mostrar el tamaño real da confianza.</p>"))

real.append(page(4, "Foto real sin caras", "Detalles que enamoran",
 "La foto general y luego acercamientos: asas, logo y textura. Muestra la calidad de la pieza original.",
 ["📸 Instagram", "📘 Facebook"],
 carousel([
  (ph("banco")+f'<div class="pad"><div class="t" style="font-size:{u(2.4)}">Azul o <em>blanca</em></div><div class="s">Cód. 0883</div></div>',"","Las dos versiones juntas"),
  (ph("banco_det")+'<div class="shade"></div>'+f'<div class="pad" style="justify-content:flex-end;color:var(--ivory)"><div class="k">Detalle</div><div class="t" style="font-size:{u(1.9)}">Asas firmes y logo metálico</div></div>',"","Acercamiento a las asas"),
  (ph("garf_det")+'<div class="shade"></div>'+f'<div class="pad" style="justify-content:flex-end;color:var(--ivory)"><div class="k">Detalle</div><div class="t" style="font-size:{u(1.9)}">Ilustración oficial</div></div>',"","Acercamiento al estampado"),
  (f'<div class="pad"><div class="t" style="font-size:{u(2.1)}">Originales, <em>directo de Tizza</em></div></div><div class="grid2" style="position:absolute;left:{u(1.6)};right:{u(1.6)};bottom:{u(1.6)}"><div><img src="{I}banco_det.jpg"><span>Asas</span></div><div><img src="{I}garf_det.jpg"><span>Estampado</span></div></div>',"stone","Resumen en dos fotos"),
 ]),
 "Los detalles hacen la diferencia 🤍\nAsas firmes, logo metálico e ilustraciones oficiales. Originales, directo de Tizza.\nPídela por WhatsApp: +591 76705942\n#VestaBags #TizzaBolivia #CarterasBolivia",
 "<p><b>Foto:</b> primero la pieza completa y después, con el celular a 15 cm, el asa, el cierre, el logo y el interior. Luz lateral de ventana para que se note la textura.</p>",
 "<p>Muestra la calidad sin decir «calidad». Responde a la duda de si es original con pruebas visuales.</p>"))

real.append(page(5, "Foto real sin caras", "Para regalar",
 "Una guía de regalos con piezas pequeñas (billeteras y carteras chicas), con fotos flat lay y de mesa.",
 ["📘 Facebook", "📸 Instagram"],
 carousel([
  (f'<div class="pad"><div class="k" style="color:var(--cacao)">Guía de regalos</div><div class="t" style="font-size:{u(2.6)}">Para <em>regalar</em> 🎁</div></div><div class="grid2" style="position:absolute;left:{u(1.6)};right:{u(1.6)};bottom:{u(1.6)}"><div><img src="{I}garf_wallet.jpg"></div><div><img src="{I}hk_bag.jpg"></div></div>',"stone","Portada: collage en nude"),
  (ph("garf_camera","70% 60%")+f'<span class="price" style="left:{u(1.6)};bottom:{u(1.6)}">Para tu amiga fan de Garfield · Cód. 2146</span>',"",""),
  (ph("hk_bag")+f'<span class="price" style="left:{u(1.6)};bottom:{u(1.6)}">Para la más tierna · Cód. 2056</span>',"","Producto sobre fondo blanco"),
  (ph("garf_wallet")+f'<span class="price" style="left:{u(1.6)};bottom:{u(1.6)}">Para ti misma · Cód. 2139</span>',"",""),
  (f'<div class="pad" style="justify-content:center;text-align:center;align-items:center"><div class="t" style="font-size:{u(2.2)}">¿Para quién es <em>tu regalo?</em></div><div class="s" style="opacity:.85;margin:{u(.4)} 0 {u(1)}">Te ayudamos a elegir por WhatsApp. Si no está en la tienda, lo encargamos (pedidos a una semana).</div><span class="pill l">+591 76705942</span></div>',"deep",""),
 ]),
 "Guía de regalos VESTA 🎁\nPara tu amiga fan de Garfield, para la más tierna o para ti misma.\nTe ayudamos a elegir por WhatsApp: +591 76705942. ¿No está en la tienda? Lo encargamos para ti.\n#VestaBags #RegaloPerfecto #CarterasBolivia",
 "<p><b>Foto flat lay:</b> desde arriba, sobre un mantel o tela, con 2 o 3 objetos que cuenten algo (cámara, flores, tarjeta). La pieza va en diagonal.</p><p style='margin-top:5px'>Ideal para el Día de la Madre, Navidad y cumpleaños.</p>",
 "<p>Quien compra un regalo decide rápido si le das ideas concretas por persona. Funciona muy bien en Facebook.</p>"))

real.append(page(6, "Foto real sin caras", "Colores que alegran",
 "Piezas de licencia fotografiadas como producto sobre fondos de color. Es el carrusel más «de vitrina».",
 ["📸 Instagram", "🎵 TikTok (modo foto)"],
 carousel([
  (f'<div class="pad"><div class="t" style="font-size:{u(2.5)}">Colores que <em>alegran</em></div><div class="s" style="color:var(--muted)">Hello Kitty y Stitch</div></div><div class="grid2" style="position:absolute;left:{u(1.6)};right:{u(1.6)};bottom:{u(1.6)}"><div><img src="{I}hk_face.jpg"></div><div><img src="{I}st_heart.jpg"></div></div>',"stone","Portada: collage de dos"),
  (ph("hk_face","30% center")+f'<span class="price" style="left:{u(1.6)};bottom:{u(1.6)}">Hello Kitty · Cód. 2041 · 700 Bs</span>',"","Fondo rojo y rosado"),
  (ph("st_heart")+f'<span class="price" style="left:{u(1.6)};bottom:{u(1.6)}">Stitch corazón · Cód. 2102 · 630 Bs</span>',"","Fondo lila"),
  (ph("st_back")+f'<span class="price" style="left:{u(1.6)};bottom:{u(1.6)}">Mochila Stitch · Cód. 2100 · 810 Bs</span>',"",""),
  (f'<div class="pad" style="justify-content:center;align-items:center;text-align:center"><div class="t" style="font-size:{u(2.2)}">¿Con cuál te quedas?</div><div class="s" style="color:var(--muted);margin:{u(.4)} 0 {u(1)}">Colaboraciones oficiales</div><span class="pill">Pídela por WhatsApp 🤍</span></div>',"",""),
 ]),
 "Colores que alegran 🎀💙\nHello Kitty 2041 · Stitch corazón 2102 · Mochila Stitch 2100.\nColecciones Hello Kitty & Friends y Disney Stitch · Pídelas por WhatsApp +591 76705942\n#VestaBags #HelloKitty #Stitch #CarterasBolivia",
 "<p><b>Foto de producto:</b> una cartulina de color de fondo (rosado o lila) que haga curva hacia la mesa (sin esquinas), con luz de ventana de frente y el celular a la altura de la pieza.</p>",
 "<p>Los colores de las licencias llaman la atención en el feed. Al alternarlo con láminas nude, el perfil se ve ordenado.</p>"))

# guía de fotos sin cara
real.append(f'''<section class="page"><div class="kick">Guía rápida</div><h2 style="font-family:var(--fd);font-weight:400;font-size:30px;margin-top:4px">Cómo tomar fotos reales <em>sin mostrar caras</em></h2>
<p class="idea" style="font-size:12.5px;color:var(--ink2);margin-top:5px">Todo con el celular, con luz de ventana y estos 6 encuadres. Repítelos y el perfil se verá coherente.</p>
<div class="tip">
<div><div class="sk"><img src="{I}garf_hand.jpg" style="width:100%;height:100%;object-fit:cover"></div><h3>1. La mano que sostiene</h3>El brazo entra desde arriba y sostiene el asa. Fondo de color liso. Es el encuadre más fácil y el que más vende.</div>
<div><div class="sk"><img src="{I}garf_camera.jpg" style="width:100%;height:100%;object-fit:cover"></div><h3>2. Flat lay</h3>Desde arriba, sobre tela o mantel. La pieza en diagonal más 2 o 3 objetos (cámara, flores, café).</div>
<div><div class="sk"><img src="{I}silla.jpg" style="width:100%;height:100%;object-fit:cover;object-position:center 40%"></div><h3>3. En un mueble</h3>Colgada de una silla o sobre un taburete. Exterior de tarde o junto a una ventana.</div>
<div><div class="sk"><img src="{I}manos2.jpg" style="width:100%;height:100%;object-fit:cover;object-position:center 30%"></div><h3>4. Del cuello para abajo</h3>La pieza puesta, con ropa neutra. Muestra el tamaño real en el cuerpo.</div>
<div><div class="sk"><img src="{I}banco_det.jpg" style="width:100%;height:100%;object-fit:cover"></div><h3>5. Detalle</h3>A 15 cm: asas, cierres, logo e interior. Luz lateral para que se note la textura.</div>
<div><div class="sk"><img src="{I}hk_face.jpg" style="width:100%;height:100%;object-fit:cover"></div><h3>6. Vitrina de color</h3>Cartulina de color que hace curva hacia la mesa, sin esquinas. Para las piezas de licencia.</div>
</div>
<div class="foot"><span>VESTA BAGS · Ideas de contenido</span><span>Ejemplos con fotos del catálogo Tizza como referencia</span></div></section>''')

def cover(title, sub, art):
    return f'''<section class="page cover"><div><img class="logo" src="{I}logo-dark.png"><h1>{title}</h1><p>{sub}</p>
<p style="font-size:11px;margin-top:22px;color:var(--muted)">Las fotos de ejemplo son de los catálogos de Tizza (Octubre y Licencias) y sirven como referencia de estilo. Para publicar, usa fotos propias o confirma con Tizza que puedes usar las suyas. Los precios son los de venta del catálogo: confírmalos antes de publicar. Cuentas de redes: [PENDIENTE].</p></div>
<div class="art">{art}</div></section>'''

def index(items, title):
    lis = "".join(f'<div style="display:flex;gap:14px;padding:10px 0;border-bottom:1px solid var(--line)"><span style="font-family:var(--fd);font-size:22px;color:var(--cacao);width:34px">{i+1:02d}</span><div><b style="font-size:13px">{t}</b><div style="font-size:11px;color:var(--muted)">{r}</div></div></div>' for i,(t,r) in enumerate(items))
    return f'<section class="page"><div class="kick">Índice</div><h2 style="font-family:var(--fd);font-weight:400;font-size:30px;margin:4px 0 14px">{title}</h2><div style="columns:2;column-gap:14mm">{lis}</div><div class="foot"><span>VESTA BAGS · Ideas de contenido</span><span></span></div></section>'

art1 = f'''<div class="sl stone" style="--w:250px;position:absolute;left:10px;top:40px;transform:rotate(-5deg)"><img class="m" src="{M}" style="--ms:15;left:calc(var(--u)*4.5);top:calc(var(--u)*5)"><div class="pad" style="justify-content:flex-end"><div class="t" style="font-size:calc(var(--u)*2.6)">Hola, soy <em>Vesta</em> 🤍</div></div></div>
<div class="sl" style="--w:220px;position:absolute;right:0;top:170px;transform:rotate(4deg)"><img class="ph" src="{I}garf_pizza.jpg"><div class="shade"></div><div class="pad" style="justify-content:flex-end;color:#fff"><div class="t" style="font-size:calc(var(--u)*2.4)">eres <em>Garfield</em> 🧡</div></div></div>'''
art2 = f'''<div class="sl" style="--w:240px;position:absolute;left:0;top:30px;transform:rotate(-4deg)"><img class="ph" src="{I}garf_hand.jpg"></div>
<div class="sl" style="--w:230px;position:absolute;right:0;top:200px;transform:rotate(4deg)"><img class="ph" src="{I}dunas.jpg" style="object-position:center 70%"><div class="shadeT"></div><div class="pad" style="color:#fff"><div class="t" style="font-size:calc(var(--u)*2.4)">Tres planes,<br><em>tres carteras</em></div></div></div>'''

head1 = cover("Carruseles <em>divertidos</em><br>con Vesta", "8 tipos de carrusel con la mascota como protagonista, ya diseñados con la paleta nude, Bodoni Moda e Instrument Sans. Cada uno trae sus láminas, la red objetivo, el caption listo, cómo hacerlo y por qué funciona.", art1)
idx1 = index([("Hola, soy Vesta","Presentación · 📸 IG + 📘 FB"),("Vesta te dice qué personaje eres","Test · 🎵 TikTok + 📸 IG"),("¿Este o este?","Encuesta · 📸 IG + 🎵 TikTok"),("Mito o verdad, con Vesta","Dudas · 📘 FB + 📸 IG"),("Lo que Vesta lleva en su cartera","Humor · 🎵 TikTok + 📸 IG"),("Vesta elige según tu plan","Recomendación · 📸 IG + 📘 FB"),("Diccionario Vesta","Educativo · 📸 IG + 📘 FB"),("Cómo comprar con Vesta","Tutorial · 📘 FB + 📸 IG")], "8 carruseles con la mascota")
head2 = cover("Carruseles con <em>fotos reales</em>,<br>sin mostrar caras", "6 carruseles con fotos de la vida real (manos, mesas, muebles y flat lay), ya diseñados con la estética VESTA. Incluye una guía de los 6 encuadres para tomar tus propias fotos con el celular.", art2)
idx2 = index([("Tu cartera según el plan","Escenas · 📸 IG + 📘 FB"),("Garfield en la vida real","Manos y mesa · 🎵 TikTok + 📸 IG"),("Así se lleva","Del cuello para abajo · 📸 IG + 🎵 TikTok"),("Detalles que enamoran","Acercamientos · 📸 IG + 📘 FB"),("Para regalar","Flat lay · 📘 FB + 📸 IG"),("Colores que alegran","Vitrina de color · 📸 IG + 🎵 TikTok"),("Guía de fotos sin cara","Los 6 encuadres")], "6 carruseles reales y una guía")

def html(body, title):
    return f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{title}</title><style>{CSS}</style></head><body>{body}</body></html>'

(D / "divertidos.html").write_text(html(head1 + idx1 + "".join(fun), "VESTA · Carruseles divertidos con Vesta"))
(D / "reales.html").write_text(html(head2 + idx2 + "".join(real), "VESTA · Carruseles con fotos reales"))
print("ok")
