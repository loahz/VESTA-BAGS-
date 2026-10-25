"""Construye:
  site/                      sitio listo para publicar (HTML + CSS + JS + assets)
  dist/vesta-artifact.html   versión de un solo archivo con imágenes incrustadas
Uso: python3 build.py"""
import base64, json, shutil, pathlib, mimetypes
R = pathlib.Path(__file__).resolve().parent
S = R / "src"
FONTS = "https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..600;1,6..96,400&family=Instrument+Sans:wght@400;500;600;700&display=swap"
DESC = "VESTA BAGS: carteras seleccionadas para Bolivia. Elige tu modelo y confirma tu pedido por WhatsApp."
def mascot_inline():
    """Inserta el SVG original de la mascota sin cambiar su dibujo; solo agrupa ojos y manitas para animarlos."""
    svg = (R / "assets/mascota-vesta.svg").read_text()
    svg = svg.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">',
                      '<svg class="mascot" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" focusable="false" aria-hidden="true">')
    a = svg.index("<!-- ojitos -->"); b = svg.index("<!-- mejillas -->")
    svg = svg[:a] + '<g class="m-eyes">' + svg[a:b] + "</g>\n  " + svg[b:]
    lines = svg.split("\n")
    out = []
    for ln in lines:
        if 'cx="82" cy="344"' in ln: ln = '<g class="m-hand m-hand-l">' + ln.strip() + "</g>"
        if 'cx="430" cy="344"' in ln: ln = '<g class="m-hand m-hand-r">' + ln.strip() + "</g>"
        out.append(ln)
    return "\n".join(out)
body = (S / "body.html").read_text().replace("{{MASCOT_SVG}}", mascot_inline())
css = (S / "styles.css").read_text()
JS_FILES = ("config.js", "catalog.js", "app.js", "bot.js")
js = [(S / f).read_text() for f in JS_FILES]
import re as _re
_m = _re.search(r'palette:\s*"(\w+)"', js[0]); PALETTE = _m.group(1) if _m else "piedra"
fonts = f'''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">'''

# ---- sitio publicable ----
site = R / "site"
if site.exists(): shutil.rmtree(site)
site.mkdir(parents=True)
shutil.copytree(R / "assets", site / "assets", ignore=shutil.ignore_patterns(".gitkeep", "logo-original.jpg", "*.json"))
(site / "index.html").write_text(f'''<!doctype html>
<html lang="es" data-palette="{PALETTE}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>VESTA BAGS | Carteras en Bolivia</title>
<meta name="description" content="{DESC}">
<meta name="theme-color" content="#F0E2D6">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="apple-touch-icon" href="assets/favicon.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_BO">
<meta property="og:title" content="VESTA BAGS">
<meta property="og:description" content="{DESC}">
<meta property="og:image" content="assets/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Store","name":"VESTA BAGS","description":"{DESC}","telephone":"+59176705942","areaServed":"Bolivia","currenciesAccepted":"BOB"}}</script>
{fonts}
<style>
{css}
</style>
</head>
<body>
{body}
<script>
{js[0]}
</script>
<script>
{js[1]}
</script>
<script>
{js[2]}
</script>
<script>
{js[3]}
</script>
</body>
</html>
''')

(site / "_headers").write_text("/assets/*\n  Cache-Control: public, max-age=604800\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n")

# ---- artifact de un solo archivo ----
def uri(p):
    mt = mimetypes.guess_type(p.name)[0] or ("image/webp" if p.suffix == ".webp" else "application/octet-stream")
    return f"data:{mt};base64," + base64.b64encode(p.read_bytes()).decode()
embed = {f"assets/products/{p.name}": uri(p) for p in sorted((R / "assets/products").glob("*.webp"))}
embed["assets/logo-white.png"] = uri(R / "assets/logo-white.png")
embed["assets/logo-dark.png"] = uri(R / "assets/logo-dark.png")
art_body = body.replace('src="assets/logo-white.png"', f'src="{embed["assets/logo-white.png"]}"').replace('src="assets/logo-dark.png"', f'src="{embed["assets/logo-dark.png"]}"')
(R / "dist").mkdir(exist_ok=True)
art = f'''<title>VESTA BAGS</title>
<script>document.documentElement.dataset.palette="{PALETTE}"</script>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{DESC}">
{fonts}
<style>
{css}
</style>
{art_body}
<script>window.VESTA_EMBED={json.dumps(embed)};</script>
<script>
{js[0]}
{js[1]}
{js[2]}
{js[3]}
</script>
'''
(R / "dist/vesta-artifact.html").write_text(art)
print(f"site/ listo · artifact {len(art)/1e6:.2f} MB")

# ---- Pedidos a una semana (página aparte) ----
import re as _re2
def catalog_pages(thumbs=True):
    out = {}
    for slug in ("octubre", "licencias"):
        f = R / "assets/catalogos" / f"{slug}.json"
        if not f.exists(): continue
        pages = []
        for p in json.loads(f.read_text()):
            t = p["text"]
            prices = sorted({int(a or b) for a, b in _re2.findall(r"(?:\bBs\.?[ \t]*(\d{2,4})\b)|(?:\b(\d{2,4})[ \t]*[bB]s\b)", t)})
            codes = list(dict.fromkeys(_re2.findall(r"C[óÓoO][dD]\.?\s*(\d{3,5})", t)))
            skus = list(dict.fromkeys(_re2.findall(r"\b(20\d{5})\b", t)))
            img = f"assets/catalogos/{p['img']}"
            th = img.replace(f"/{slug}/", f"/{slug}/t/") if thumbs and (R / "assets/catalogos" / slug / "t" / p["img"].split("/")[-1]).exists() else img
            pages.append({"n": p["n"], "img": img, "thumb": th, "prices": prices, "codes": codes, "skus": skus})
        out[slug] = pages
    return out
def cat_js(thumbs): return "window.VESTA_CATALOG_PAGES = " + json.dumps(catalog_pages(thumbs), ensure_ascii=False, separators=(",", ":")) + ";"
ped_body = (S / "pedidos.html").read_text().replace("{{MASCOT_SVG}}", mascot_inline())
ped_css = css + "\n" + (S / "pedidos.css").read_text()
ped_js = (S / "pedidos.js").read_text()
PED_DESC = "Pedidos a una semana: encarga cualquier pieza de los catálogos de Tizza y te la traemos a Bolivia."
def pedidos_doc(thumbs=True):
    CAT_JS = cat_js(thumbs)
    return f'''<!doctype html>
<html lang="es" data-palette="{PALETTE}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Pedidos a una semana | VESTA BAGS</title>
<meta name="description" content="{PED_DESC}">
<link rel="icon" type="image/png" href="assets/favicon.png">
{fonts}
<style>
{ped_css}
</style>
</head>
<body>
{ped_body}
<script>
{js[0]}
</script>
<script>
{CAT_JS}
</script>
<script>
{ped_js}
</script>
</body>
</html>
'''
(site / "pedidos.html").write_text(pedidos_doc())
(R / "dist/pedidos.html").write_text(pedidos_doc(thumbs=False))   # el artifact usa las páginas completas (límite de archivos)
print("pedidos.html listo")
