# Diseño: skill «Vesta» (marca completa de VESTA BAGS)

Fecha: 2026-10-25 · Estado: borrador para aprobación

## Intención
Que cualquier pedido sobre VESTA BAGS (editar la web, catálogo, guiones de video, contenido para redes, diseño gráfico, ventas, bots de IA, estrategia) se haga siempre con la identidad de la marca, sin repetirla en cada mensaje y sin inventar datos.

## Lo que respondiste en la encuesta
- Ubicación: dentro del repo, en `.claude/skills/vesta/`. Se sube también todo el proyecto web (src, assets, catálogos, build.py, tests).
- Videos: guiones y storyboards (no archivos MP4).
- Redes: TikTok, Instagram y Facebook.
- Voz en redes: mezcla. Por defecto habla el equipo VESTA («te ayudamos») y en algunos formatos la mascota Vesta habla en primera persona.
- Clienta principal: mujeres jóvenes de 18 a 30 años.
- Contenido: calendarios semanales y mensuales.
- Alcance: toda la marca, es decir, web, catálogo, ventas, atención al cliente, diseño gráfico, fichas de producto, estrategia y anuncios, bots de IA y redes.
- Bots: prompt para un bot de WhatsApp con IA y guía para conectar la mascota de la web a una IA real (proyecto aparte, con servidor y clave de API).
- Estructura: una sola skill con módulos.

## Objetivos
1. `SKILL.md` corto: quién es VESTA, reglas que nunca se rompen y qué módulo leer según la tarea.
2. Módulos en `references/`:
   - `marca.md`: historia, propuesta, clienta (18–30), políticas confirmadas y datos pendientes.
   - `voz.md`: tono, palabras sí y no, uso de 🤍, voz del equipo frente a la mascota, ejemplos.
   - `visual.md`: paleta nude con sus códigos, tipografías, logo, mascota, lo que el dueño rechazó y formatos de redes.
   - `web.md`: cómo está hecha la tienda, dónde se edita cada cosa, build, pruebas y publicación en Netlify.
   - `catalogo.md`: colecciones, tipos, colores, catálogos Octubre y Licencias, y cómo leer precios y códigos de los JSON.
   - `contenido.md`: pilares, calendario, fechas bolivianas, captions y hashtags por red.
   - `videos.md`: plantilla de guion y storyboard, ganchos y formatos para TikTok y Reels.
   - `ventas.md`: proceso de venta por WhatsApp, respuestas tipo, objeciones y seguimiento.
   - `bots.md`: prompt listo del bot de WhatsApp, reglas del bot de la web y guía para conectarlo a una IA real.
   - `diseno.md`: cómo hacer posts, historias y flyers en HTML o imagen con la marca.
   - `estrategia.md`: lanzamientos de colecciones, Meta Ads y crecimiento.
3. Proyecto web en la raíz del repo, tal como venía en el zip.

## Lo que no hace (no objetivos)
- No genera MP4 ni conecta todavía un bot de IA real. Solo deja la guía; hacerlo es otro pedido.
- No inventa precios, stock, plazos, promociones, usuarios de redes ni dominio.

## Sería un fracaso si...
- El contenido suena genérico, «a IA», o usa fondo negro o diseños cuadrados.
- Se prometen cosas que la tienda no ha confirmado.
- Se redibujan el logo o la mascota.

## Enfoques considerados
- **A. Una skill con módulos (elegido):** carga solo lo necesario, es una sola «Vesta» y es fácil de actualizar.
- B. Varias skills: más ordenado, pero rompe la idea de una sola skill.
- C. Un archivo gigante: lento, caro y difícil de mantener.

## Decisiones mías (puedes cambiarlas)
- La paleta oficial es nude (CLAUDE.md), no «negro, blanco y dorado» (README antiguo). Corrijo el README.
- Si la tarea es de la web, siempre se ejecutan `python3 build.py` y las pruebas.
- Las fechas clave son D. de la Madre (27 de mayo), D. de la Mujer Boliviana (11 de octubre), San Valentín, regreso a clases (febrero), Navidad y Black Friday.
