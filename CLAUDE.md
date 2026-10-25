# VESTA BAGS — contexto del proyecto

Tienda web de VESTA BAGS: reventa en Bolivia de carteras y accesorios de Tizza (Perú). Emprendimiento familiar (Matheo y su mamá); atienden la familia y un bot de IA, de 9:00 a 19:00. Distribuidores oficiales de Tizza. Voz de marca neutra («te ayudamos», nunca «asesora»). Los pedidos se cierran por WhatsApp al +591 76705942 (`59176705942`).

## Estructura
- `src/body.html`, `src/styles.css`, `src/app.js`: la tienda (index.html).
- `src/config.js`: todo lo editable.
  - `VESTA_CONFIG`: tienda, paleta, WhatsApp e info de ayuda.
  - `VESTA_BOT`: textos de la mascota Vesta.
  - `VESTA_ENCARGOS`: página de pedidos a una semana.
- `src/catalog.js`: productos, colores, colecciones (Mafalda, Garfield, Hello Kitty, Stitch…) y tipos. Las fotos de referencia vienen del CDN de Tizza.
- `src/bot.js`: Vesta, la mascota asistente. Incluye el chat por botones, «Ayúdame a elegir», el asomo al hacer scroll, los mensajes en el carrito y en la ficha, el recordatorio y el agradecimiento.
- `src/pedidos.html`, `src/pedidos.css`, `src/pedidos.js`: página aparte «Pedidos a una semana», con los catálogos Octubre (264 págs.) y Licencias (64 págs.). Tiene su propia lista de encargo, separada del carrito.
- `assets/`: logos (originales, con fondo transparente), mascota (`mascota-vesta.svg`, no redibujar), favicon y catálogos en `assets/catalogos/`.
- `build.py`: genera `site/` (para Netlify: index.html, pedidos.html y assets) y `dist/` (versión de un solo archivo).
- `tests/e2e.py` (tienda) y `tests/e2e_pedidos.py` (encargos): pruebas con Playwright.

## Comandos
```
python3 build.py
python3 tests/e2e.py && python3 tests/e2e_pedidos.py
cd site && python3 -m http.server 8000
```
Para publicar en Netlify, sube el contenido de `site/` (o un zip de esa carpeta) en la pestaña Deploys.

## Diseño actual
- Paleta fija: `nude` (elegida por el dueño): nude cálido, tinta espresso, acento cacao y superficies oscuras cacao (#4E3A30) en vez de negro. Otras guardadas: rosa, lavanda, salvia, celeste, blanco, piedra.
- Tipografía: Bodoni Moda solo para títulos grandes; Instrument Sans para la interfaz y los nombres de producto.
- Portada con el logo animado; colecciones en arcos; carrito en dos pasos («Tu pedido» y «Tus datos»), con campos de 16 px para celular.
- El dueño rechazó: el fondo negro, la franja de «confianza», la cartera recortada en la portada y los diseños cuadrados o con apariencia de IA.

## Reglas
- No inventar precios, stock, plazos, políticas de pago, envío o cambios, ni promociones. Si falta un dato: «Precio por consultar» o «te lo confirmamos por WhatsApp».
- No afirmar que un pedido quedó confirmado solo porque se abrió WhatsApp.
- Mantener el logo y la mascota originales.
- Después de cada cambio: ejecutar build y pruebas, revisar en celular (320–430 px) y en escritorio.

## Pendiente
- Precios reales en Bs, stock y fotos propias. Hoy el catálogo de la tienda trae `price: null` y fotos de referencia de Tizza.
- Los precios en Bs de ambos catálogos son precios de VENTA (el dueño compra con 30 % de descuento de mayorista). Se muestran.
- Redes sociales, dominio propio, inventario de las 10 primeras carteras (precios y fotos), stock automático (Google Sheets o la app de inventario).

## Políticas confirmadas
- Pagos: QR, transferencia o efectivo contra entrega.
- Envíos: delivery en La Paz; resto de Bolivia por flota, pagado por quien compra.
- Sin devoluciones.
- Pedidos a una semana: 50 % de adelanto.

## Skill de marca
Toda tarea de VESTA (web, contenido, videos, ventas, bots, diseño, estrategia) usa la skill `.claude/skills/vesta/` (SKILL.md + references/).
También están instaladas las 52 skills de marketing de Corey Haines (`.claude/skills/`, licencia MIT). Su contexto de marca está en `.agents/product-marketing.md`, y ante cualquier duda manda la skill `vesta`.
