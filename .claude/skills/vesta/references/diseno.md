# Diseño gráfico (posts, historias, flyers)

## ★ ESTILO OFICIAL: «El charm de la casa» (aprobado por el dueño el 25/10/2026)
Úsalo para TODO el feed. Lo anterior (v1, v2, v3) queda solo como historial.
- **Paleta: solo los 6 colores de la web.** Fondos: marfil #FBF6F1, piedra #F0E2D6 y nude profundo #E6D0BE. Fondo noche: cacao oscuro #4E3A30. Acento: cacao #7A4B3A. Texto: espresso #221B18. **Nada de lila, rosado, dorado ni colores de colección en los fondos**: el color lo pone solo la cartera.
- **Charm:** la mascota Vesta cuelga del asa de cada cartera con argolla y cadena punteada en cacao (en fondos oscuros, nude #E6D0BE), inclinada hacia afuera sin tapar el producto. Hoy es un **ejemplo digital**; cuando exista el charm físico, se fotografía de verdad. Las posiciones del asa están en `marketing/contenido/estilo-oficial/fuente/anchors.json`.
- **Ritmo:** cada fila de 3 tiene una pieza en cacao oscuro (columna 3).
- **Composición:** la cartera ocupa menos de la mitad de la pieza, centrada, con sombra suave. Etiqueta superior en versalitas espaciadas («Colección Primavera»: en Bolivia, de oct. a dic. es primavera). Nombre y precio abajo en Bodoni ~1,05u («Caramelo · Bs 700»).
- **Piezas de frase:** «Elegante por fuera. Tierna por dentro.» (eslogan) y «La elegancia no es pasar desapercibida, es ser recordada.», con el charm solo.
- **Fotos de escena:** sin texto que prometa charm si no lo tienen.
- **Humor, memes y tendencias:** solo en Reels e historias. El feed es la vitrina.
- Referencia: `marketing/contenido/estilo-oficial/VESTA-estilo-oficial-charm-de-la-casa.pdf`. Generador: `fuente/gen7.py` (función `bag()`).

## v3 «Vitrina Viva» (historial)
Encuesta del dueño: quiere más personalidad, humor real sacado de tendencias (meme aspiracional, formatos de TikTok), collage tipo revista y mockups de tendencia (notas del iPhone, chat, ticket, buscador, pase de abordar). Referencias: Charles & Keith, JW Pei, Coach, Kate Spade, tiendas latinas y revistas.
- **Cuatro lenguajes:** vitrina de color (catálogo, con precio) · pantalla cotidiana (creativos, sin precio) · collage revista (sin precio) · foto en escena (estudio de color con cartera sola: con precio; casa decorada: sin precio).
- **Estudio:** pared y piso con curva, sombra de contacto y sombra proyectada, sticker redondo de precio.
- **Mascota:** solo en el post fijado «Hola, soy Vesta». El dueño dijo que el resto con mascota «se ve de IA y sin personalidad».
- **Reels:** solo manos y producto, o una amiga del cuello para abajo. 12 ideas con storyboard en `marketing/contenido/v3/`.
- Filosofía: `marketing/contenido/v3/filosofia-de-diseno.md`. Generador: `marketing/contenido/v3/fuente/gen3.py` (+ `export.cjs` para láminas 1080×1350 y 1080×1920).

## Estilo «Vitrina de color» (v2, octubre 2026)
El dueño **rechazó** la v1: mascota en todas las láminas, burbujas, emojis como íconos, fotos con degradado oscuro. Le pareció genérica, «de IA», sin color y sin carteras. El estilo vigente es este:
- **La cartera es la protagonista**: recortada sin fondo, ocupa del 55 al 65 % de la lámina.
- **Color por colección**: fondo liso del tono de la pieza. Garfield #F7C98B/#7A2E0E · Stitch #C8CDEF/#1E2756 · Hello Kitty #F6D2D5/#A3182A · Toy Story #CFE3F3/#1D4E86 · clásicas en nude, caramelo, dorado o azul grisáceo. Las láminas de marca van en nude #F0E2D6 o marfil, y el cierre en cacao #4E3A30.
- **Una palabra grande en Bodoni cursiva** detrás de la cartera, en un tono más oscuro que el fondo (como la portada de la web).
- **Etiqueta arriba** en Instrument Sans versalita, nombre abajo a la izquierda en Bodoni, precio abajo a la derecha.
- **Máximo 12 palabras** por lámina. Sin emojis en las láminas.
- **La mascota solo en la portada «Hola, soy Vesta»** (le gustó). En las demás no va.
- Ejemplos, PDF y láminas 1080×1350: `marketing/contenido/v2/`. El generador está en `marketing/contenido/v2/fuente/gen2.py` y los recortes en `fuente/cut/`.
- **Recortes**: `rembg` (modelo isnet-general-use) con los colores originales, rellenando solo huecos pequeños (no el interior de las asas). Ver gen y el historial del repo.

Lee primero `visual.md`.

## Cómo producir una pieza
1. Se hace como **HTML/CSS** del tamaño exacto (ver formatos en `visual.md`), usando los tokens de la paleta nude, Bodoni Moda y Instrument Sans (Google Fonts) y los logos de `assets/`.
2. Se exporta a PNG con Playwright (Chromium ya instalado):
```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width":1080,"height":1350})
    pg.goto("file:///ruta/pieza.html"); pg.wait_for_timeout(800)
    pg.screenshot(path="pieza.png"); b.close()
```
3. Revisa el PNG antes de entregarlo (la tipografía cargó, nada se corta, el texto se lee en el celular).
4. Guarda las piezas en `marketing/disenos/AAAA-MM-tema/` (HTML + PNG).

## Composición
- Fondo `--ivory` #FBF6F1 o `--stone` #F0E2D6. Para un bloque oscuro, cacao #4E3A30 con texto marfil y `logo-white.png`.
- El producto es el héroe: una foto grande, con aire alrededor, sobre una forma de **arco** (border-radius superior 50 %).
- Nombre de la colección en Bodoni enorme (en `--stone-2` detrás o en espresso delante).
- Máximo 3 niveles de texto: título en Bodoni, una línea en Instrument Sans y el CTA en píldora cacao #7A4B3A con texto marfil.
- Logo pequeño, abajo o arriba al centro. Un solo logo por pieza.
- Mascota Vesta solo en piezas lúdicas o de ayuda, con su SVG original.

## Plantillas típicas
- **Novedad**: foto en arco, «Nuevo» en versalitas, nombre del modelo y «Pídela por WhatsApp».
- **Carrusel educativo** (4:5): portada con pregunta, 3 o 4 slides de valor y cierre con el CTA.
- **Historia de encuesta**: dos fotos lado a lado, «¿Cuál eliges?» y espacio para el sticker (deja 250 px libres arriba y 340 px abajo).
- **Flyer de fecha especial**: título en Bodoni («Para mamá, con amor») y 3 productos en arcos, sin precios inventados.
- **Políticas** (destacadas de Instagram): Pagos, Envíos, Pedidos a una semana, Cuidados. Íconos de línea fina en cacao.

## Evitar
Fondo negro, dorado brillante, degradados neón, sombras duras, cajas cuadradas rígidas, tipografías script ajenas al logo, stock genérico con caras de IA y más de dos tipografías.
