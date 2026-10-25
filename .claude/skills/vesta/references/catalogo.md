# Catálogo y productos

## Tienda (src/catalog.js)
22 modelos de Tizza agrupados por modelo, con los colores como variantes.
- **Mafalda** (colaboración oficial Tizza x Mafalda): Cartera 2128 (rosado, celeste), 2122 (dorado, celeste), 2125 (azul); Morral 2132, 2129, 2126, 2123; Mochila 2131, 2121; Billetera 2133, 2130, 2124; Portacelular 2127.
- **Garfield** (colaboración oficial Tizza x Garfield): Cartera 2141, 2144; Morral 2145; Mochila 2143; Billetera 2142, 2146.
- **Hello Kitty & Friends**: Cartera 2056, Billetera 2057.
- **Stitch** (Disney): Mochila 2100.
- Colecciones preparadas sin productos todavía: Snoopy, Princesas y Toy Story.
- Tipos: carteras, morrales, mochilas, billeteras, maletas y accesorios.
- Colores: negro, rosado, celeste, azul, dorado, hueso, verde y único.
- Hoy todo tiene `price: null` («Precio por consultar») y `availability: "unknown"`. Las fotos son de referencia, del CDN de Tizza.

Lee `src/catalog.js` para ver los detalles exactos antes de nombrar un producto.

## Catálogos para pedidos a una semana
- `assets/catalogos/octubre.json` (264 páginas) y `assets/catalogos/licencias.json` (64 páginas): una lista de `{ n, img, text }`. `text` es el texto extraído de la página, con medidas, `Cód.`, código de barras y precio en **Bs**. `img` apunta a `assets/catalogos/<catálogo>/pNNN.webp`.
- **Capítulos de Octubre**:
  - Carteras: p.2
  - Morrales: p.99
  - Mochilas: p.142
  - Billeteras: p.154
  - Tarjeteros: p.214
  - Cosméticos: p.218
  - Vanité: p.221
  - Hombre: p.232
  - Maletas: p.247
- **Capítulos de Licencias**:
  - Garfield: p.2
  - Toy Story: p.28
  - Hello Kitty: p.38
  - Stitch: p.44
  - Princesas: p.51
  - Mickey y Minnie: p.55
  - Relojes: p.56
  - Snoopy: p.59
  - Poleras: p.62
- Los precios en Bs de los catálogos son **precios de venta** y se pueden mostrar. El 30 % de descuento de mayorista es interno.

### Buscar en los catálogos
```
python3 -c "import json;d=json.load(open('assets/catalogos/octubre.json'));[print(p['n'],p['text'].replace(chr(10),' | ')) for p in d if 'Cód. 2018' in p['text']]"
```
Para ver la pieza, abre la imagen `assets/catalogos/octubre/pNNN.webp` con la herramienta de lectura de imágenes. Describe solo lo que ves: color, forma, material aparente y detalles. No inventes el material si no se ve claro.

## Fichas de producto
Formato:
1. **Nombre**: Tipo + Colección/línea + Código (ej. «Cartera Mafalda 2128»).
2. **Una línea emocional** en voz VESTA (máx. 15 palabras).
3. **Detalles**: colores disponibles, medidas (del catálogo), compartimentos y asas (solo si se ven o constan).
4. **Ideal para**: la ocasión (salir, el día a día, la U, un regalo).
5. **Precio**: el Bs confirmado o «Precio por consultar».
6. **CTA**: «Pídela por WhatsApp 🤍».

Ejemplo:
> **Cartera Mafalda 2128**. Para las que piensan distinto y se visten igual de bien.
> Colores: rosado y celeste. Colaboración oficial Tizza x Mafalda.
> Ideal para salir y para regalar a tu amiga más Mafalda.
> Precio por consultar · Pídela por WhatsApp 🤍
