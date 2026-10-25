# Página web (tienda VESTA)

HTML, CSS y JavaScript sin frameworks. Todo se construye con `build.py`.

## Mapa de archivos (raíz del repo)
| Archivo | Qué contiene |
|---|---|
| `src/config.js` | **Lo editable**: `VESTA_CONFIG` (tienda, paleta, anuncio, WhatsApp, horario, redes, ciudades, políticas `info`, `faq`), `VESTA_BOT` (todos los textos de la mascota) y `VESTA_ENCARGOS` (página de pedidos a una semana). |
| `src/catalog.js` | `VESTA_COLORS`, `VESTA_COLLECTIONS`, `VESTA_CATEGORIES` y `VESTA_CATALOG` (22 productos). |
| `src/body.html` | Estructura de la tienda. Secciones: `#vitrine` (portada con logo y nombres de colección), `#colecciones` (arcos), `#novedades` (carrusel), `#tipos` (compra por tipo), `#tienda` (filtros, búsqueda y grilla), «Cómo comprar», `#ayuda` (pestañas y FAQ), `#nosotros` (frase de marca y texto) y footer. Diálogos: carrito, filtros y menú móvil. |
| `src/styles.css` | Sistema visual: tokens `:root`, paletas `data-palette`, temas de sección `.stone` / `.light` / `.ink`, componentes. Los ajustes finales están al final del archivo. |
| `src/app.js` | Lógica: render de secciones, filtros, ficha de producto, carrito en 2 pasos («Tu pedido» y «Tus datos»), mensaje de WhatsApp. Emite eventos `vesta:*` que escucha el bot. |
| `src/bot.js` | Mascota Vesta: chat por botones, «Ayúdame a elegir», asomo al hacer scroll, mensajes en carrito y ficha, recordatorio, agradecimiento. |
| `src/pedidos.html/.css/.js` | Página «Pedidos a una semana»: catálogos Octubre (264 págs.) y Licencias (64 págs.), lista de encargo propia. |
| `assets/` | Logos, mascota, favicon, OG, `products/` (fotos propias), `catalogos/` (páginas .webp y su texto en JSON). |
| `build.py` | Genera `site/` (para Netlify) y `dist/` (archivo único). La mascota SVG se inserta en `{{MASCOT_SVG}}`. |
| `tests/e2e.py`, `tests/e2e_pedidos.py` | Pruebas Playwright. |

## Cambios frecuentes y dónde se hacen
- **Texto del anuncio superior**: `VESTA_CONFIG.announcement` (`""` lo oculta).
- **Paleta**: `VESTA_CONFIG.palette` (oficial `"nude"`).
- **Redes**: `VESTA_CONFIG.social`, solo con usuarios reales confirmados.
- **Políticas y FAQ**: `VESTA_CONFIG.info` y `faq`. Solo se escribe lo confirmado (ver `marca.md`).
- **Precio de un producto**: `price: 320` en `catalog.js`. `null` muestra «Precio por consultar». `refPEN` es solo una nota interna.
- **Disponibilidad**: `availability: "available" | "soldout" | "unknown"` y `stock`.
- **Fotos propias**: van en `assets/products/` y se cambia `images: { color: ["assets/products/…jpg"] }`.
- **Quitar el aviso de demo**: `isDemoCatalog: false` cuando el catálogo y las fotos sean reales.
- **Nuevo producto**: se agrega `item({ id, slug, name, collection, category, colors, images, … })` siguiendo el formato existente. El nombre lleva la forma «Tipo Colección Código».
- **Nueva colección**: se añade a `VESTA_COLLECTIONS`. Si no tiene productos, no se muestra.
- **Textos del bot**: `VESTA_BOT`. La frase por colección va en `collectionText: { mafalda: "…" }`.
- **Catálogos de encargo**: `VESTA_ENCARGOS.catalogs[].chapters` (página donde empieza cada sección).

## Reglas de edición
- Respeta la voz (`voz.md`) y lo visual (`visual.md`). No metas el fondo negro ni la franja de «confianza».
- No se inventan precios ni políticas. Tampoco se dice que un pedido quedó confirmado solo por abrir WhatsApp.
- Los campos de los formularios llevan 16 px (para que el celular no haga zoom).
- Sigue el estilo del código existente: JS vanilla, helpers `$`/`$$` y comentarios en español.

## Verificar siempre
```
python3 build.py
python3 tests/e2e.py && python3 tests/e2e_pedidos.py
cd site && python3 -m http.server 8000
```
Revisa en celular (320 a 430 px, sin scroll horizontal) y en escritorio. Si agregas funciones, añade pruebas en `tests/`.

## Publicar
Sube el contenido de `site/` (o un zip de esa carpeta) a Netlify, en la pestaña Deploys. No hay servidor ni claves.
