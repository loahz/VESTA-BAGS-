# VESTA BAGS — Tienda online

Tienda de carteras y accesorios Tizza para Bolivia: colecciones (Mafalda, Garfield, Hello Kitty, Stitch), filtros por colección y tipo, fichas con galería, carrito persistente y cierre de pedido por WhatsApp. Diseño en paleta nude (nude cálido, tinta espresso y acento cacao).
HTML, CSS y JavaScript sin frameworks ni dependencias en producción.

## Estructura

```
src/
  body.html        Estructura de la página
  styles.css       Sistema visual (colores, tipografía, componentes)
  config.js        Configuración editable: WhatsApp, anuncio, envío, redes, ayuda, preguntas
  catalog.js       Productos, colores, colecciones y tipos
  app.js           Lógica: carrito, filtros, ficha, WhatsApp
assets/
  logo-original.jpg  Logo original sin modificar
  logo-dark.png      Logo con transparencia, tinta oscura
  logo-white.png     Logo con transparencia, blanco
  favicon.png, og-image.jpg
  products/          Aquí van tus fotos propias de producto
build.py           Genera site/ (para publicar) y dist/vesta-artifact.html
site/              Sitio listo para subir a un hosting
tests/e2e.py       Pruebas en navegador
```

## Ejecutar en local

```
python3 build.py
cd site && python3 -m http.server 8000
```
Abrir http://localhost:8000

## Configuración (`src/config.js`)

- `whatsapp`: número internacional sin `+` ni espacios. Es el único lugar donde aparece.
- `announcement`: texto de la franja superior (`""` la oculta).
- `shippingCost`: `null` = envío por coordinar. Un número en Bs lo suma al total.
- `social`: enlaces de Instagram, TikTok y Facebook. Los vacíos no se muestran.
- `info`: textos de Entregas, Pagos, Cambios y Cuidados. Con `pending: true` la web muestra el texto `fallback`; al confirmar la política, escribe `body` y pon `pending: false`.
- `faq`: preguntas frecuentes.
- `isDemoCatalog`: poner `false` cuando el catálogo y las fotos sean reales.

## Productos, colecciones, precios y fotos (`src/catalog.js`)

El catálogo trae 22 productos reales de Tizza agrupados por modelo: cada color es una variante del mismo producto.

- **Colecciones** (`VESTA_COLLECTIONS`): Mafalda, Garfield, Hello Kitty, Stitch, más Snoopy, Princesas y Toy Story preparadas. Una colección sin productos no se muestra.
- **Tipos** (`VESTA_CATEGORIES`): carteras, morrales, mochilas, billeteras, maletas y accesorios.
- **Precios**: todos están en `price: null` y se muestran como «Precio por consultar». `refPEN` es solo una nota interna con el precio de Tizza en soles y no aparece en la web. Cuando definas el precio en bolivianos, escribe el número en `price`, por ejemplo `price: 320`.
- **Disponibilidad**: todo está en `"unknown"` («Disponibilidad por confirmar»). Cuando llegue la mercadería, cambia a `"available"`, pon el `stock` y quita el aviso con `isDemoCatalog: false` en `config.js`.
- **Fotos**: hoy son fotos de referencia que se cargan desde el servidor de Tizza. Si alguna no carga, la web prueba la siguiente y, si no queda ninguna, muestra «Foto pendiente». Para usar tus propias fotos, cópialas a `assets/products/` y cambia las rutas:

```js
images: { rosado: ["assets/products/cartera-2128-rosado-1.jpg", "assets/products/cartera-2128-rosado-2.jpg"] }
```

Te recomiendo confirmar con Tizza que puedes usar sus fotos, o reemplazarlas por las tuyas. Así no dependes de su servidor.

Después de cualquier cambio, ejecuta `python3 build.py`.

## Publicar

Sube el contenido de `site/` a cualquier hosting estático, como Netlify (arrastrando la carpeta), Vercel, Cloudflare Pages o GitHub Pages. No necesita servidor ni variables de entorno, así que no hay `.env`. El proyecto no contiene contraseñas ni tokens.

## Pruebas

```
pip install playwright && playwright install chromium
python3 build.py && python3 tests/e2e.py
```

La última ejecución pasó 53 de 53 pruebas. Cubren:

- La vitrina de colecciones, las cajas de colecciones y el menú por tipo.
- Los filtros combinados de colección, tipo, color y disponibilidad, con sus pastillas y el botón de limpiar.
- La búsqueda, incluida la búsqueda rápida, y la ficha con galería, color elegido y relacionados.
- El pedido como consulta cuando faltan precios.
- Los cálculos con precios de prueba inyectados solo durante el test: subtotales, total, límite de stock, eliminar y persistencia.
- La validación de los datos de entrega y el mensaje de WhatsApp completo y bien codificado.
- La depuración de datos guardados corruptos y los productos agotados.
- La ausencia de desbordamiento horizontal en 7 anchos y la ausencia de errores de JavaScript.

## Pendiente de datos reales

- Precios en Bs, stock y disponibilidad de cada producto.
- Fotos propias o permiso de Tizza para usar las suyas.
- Políticas de entrega, pago y cambios (marcadas `pending: true`).
- Enlaces de redes sociales.
- Dominio y hosting.

## Limitaciones

- El carrito y los datos de entrega se guardan en el navegador del cliente (localStorage). No es un inventario central; el stock se actualiza en `catalog.js`.
- WhatsApp solo abre el chat con el mensaje escrito; el cliente debe enviarlo.
- Las fotos de Tizza dependen de su servidor; si cambian sus archivos, esas fotos mostrarán «Foto pendiente». En el entorno de pruebas no se pudieron cargar esas fotos, wa.me ni Google Fonts, así que se verificó que el enlace se genera y abre una pestaña nueva, y se revisó el diseño con tipografías de respaldo.
- No se midió Lighthouse ni se probó con un lector de pantalla real.

## Vesta · Asistente (mini bot)

- Textos, menú y mensajes de WhatsApp del bot: objeto `VESTA_BOT` en `src/config.js` (en el sitio publicado, busca `VESTA_BOT` dentro de `index.html`).
- Las colecciones del bot salen solas de `VESTA_COLLECTIONS` en `src/catalog.js`; en `collectionText` puedes escribir una frase propia por colección.
- El número de WhatsApp es `whatsapp` en `VESTA_CONFIG`; si quieres otro solo para el bot, escríbelo en `VESTA_BOT.whatsapp`.
- La mascota es el archivo original `assets/mascota-vesta.svg`; se inserta tal cual, solo se agrupan los ojos y la manita para el parpadeo y el saludo.
- Vesta en la página: en `VESTA_BOT.peek` editas cuándo se asoma (segundos y % de la página), su frase y sus botones; en `VESTA_BOT.cart` lo que dice dentro del carrito; en `emptySearch` el mensaje de búsqueda sin resultados.
