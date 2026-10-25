# Diseño gráfico (posts, historias, flyers)

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
