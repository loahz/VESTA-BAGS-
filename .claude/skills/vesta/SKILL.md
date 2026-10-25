---
name: vesta
description: Identidad completa de VESTA BAGS (carteras Tizza en Bolivia). Úsala SIEMPRE que la tarea toque a VESTA o a sus carteras: editar la página web o el catálogo, crear guiones de video para TikTok/Instagram/Facebook, ideas y calendarios de contenido, captions, posts, historias, flyers, fichas de producto, mensajes de venta por WhatsApp, atención al cliente, bots de IA, anuncios, lanzamientos o estrategia. También cuando digan "Vesta", "la tienda", "la marca", "mis carteras" o "la mascota".
---

# Vesta: la marca VESTA BAGS

Todo lo que hagas para VESTA debe sonar, verse y decir lo que la marca es. Esta guía es la base. Para cada tarea, lee **solo** el módulo que corresponde.

## Quiénes somos (resumen)
- **VESTA BAGS**: emprendimiento familiar boliviano (Matheo y su mamá) y **distribuidores oficiales de Tizza** (Perú) en Bolivia. Vende carteras, morrales, mochilas, billeteras, maletas y accesorios, incluidas las licencias Mafalda, Garfield, Hello Kitty, Stitch, Snoopy, Toy Story y Princesas.
- **Clienta principal**: mujeres de 18 a 30 años, fans de las tendencias y de los personajes.
- **Venta**: todo cierra por **WhatsApp +591 76705942** (`59176705942`). Atendemos todos los días de 9:00 a 19:00. Atienden la familia y un asistente.
- **Frase de marca**: «La elegancia no es pasar desapercibida, es ser recordada.»
- **Mascota**: Vesta, una carterita beige con gorro blanco y ojitos. Saluda con «Hola, soy Vesta 🤍».

## Reglas que nunca se rompen
1. **No inventar** precios, stock, plazos, promociones, descuentos, sorteos, políticas, cuentas de redes ni dominio. Si falta el dato, escribe «Precio por consultar», «te lo confirmamos por WhatsApp» o `[PENDIENTE: …]`.
2. **Las políticas confirmadas son las únicas que se citan**:
   - Pagos con QR, transferencia o efectivo contra entrega.
   - Delivery en La Paz. Al resto de Bolivia se envía por flota, y el envío lo paga quien compra.
   - No hay devoluciones.
   - Los pedidos a una semana se encargan con un adelanto del 50 %.
3. **Un pedido no está confirmado** solo porque se abrió WhatsApp. Se confirma cuando el equipo responde con la disponibilidad.
4. **Voz neutra y cálida**: decimos «te ayudamos» y «el equipo VESTA», nunca «tu asesora». Se usa 🤍 con moderación.
5. **Logo y mascota originales**: no se redibujan ni se deforman, y no se cambia su color.
6. **Estética nude cálida**: nada de fondo negro, de diseños cuadrados o rígidos ni de apariencia de IA genérica. No se usa la franja de «confianza».
7. **Licencias**: los personajes son de sus titulares. Se presentan como «colaboración oficial Tizza x …». Nunca se usa a los personajes como si fueran de VESTA.
8. Todo en **español de Bolivia**, con tuteo («tú»).

## Qué módulo leer
| Tarea | Lee |
|---|---|
| Historia, propuesta, clienta, políticas, datos pendientes | `references/marca.md` |
| Escribir cualquier texto (tono, palabras, mascota frente a equipo) | `references/voz.md` |
| Colores, tipografías, logo, mascota, formatos visuales | `references/visual.md` |
| Editar la página web, la tienda, el bot de la web o los pedidos a una semana | `references/web.md` |
| Productos, colecciones, catálogos Octubre y Licencias, precios | `references/catalogo.md` |
| Ideas de contenido, calendarios, captions, hashtags, fechas | `references/contenido.md` |
| Guiones y storyboards de video (TikTok, Reels) | `references/videos.md` |
| Venta por WhatsApp, respuestas tipo, objeciones, seguimiento | `references/ventas.md` |
| Bot de IA de WhatsApp, IA real en la web | `references/bots.md` |
| Posts, historias, flyers y piezas gráficas | `references/diseno.md` |
| Lanzamientos, campañas, Meta Ads, crecimiento | `references/estrategia.md` |

Casi siempre combinarás `voz.md` con el módulo de la tarea. Por ejemplo, para un video lees `voz.md`, `videos.md` y, si nombras productos, `catalogo.md`.

## Antes de entregar, revisa
- ¿Suena a VESTA? Debe ser cálido, elegante y cercano, nunca agresivo ni genérico.
- ¿Hay algún dato inventado, como un precio, un plazo o una promo? Quítalo o márcalo como pendiente.
- ¿Respeta la paleta nude, Bodoni e Instrument Sans, el logo y la mascota?
- ¿Termina llevando a WhatsApp cuando corresponde?
- Si cambiaste la web, ejecuta `python3 build.py && python3 tests/e2e.py && python3 tests/e2e_pedidos.py` y revisa entre 320 y 430 px y en escritorio.
