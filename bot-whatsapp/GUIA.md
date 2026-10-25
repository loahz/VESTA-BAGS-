# Bot de WhatsApp de VESTA BAGS (oficial de Meta): guía paso a paso

Este es el asistente «Vesta» para WhatsApp. Responde solo, las 24 horas, con un menú de botones:

- Ver modelos
- Precio y colores
- Envíos
- Formas de pago
- Pedidos a una semana
- ¿Son originales?
- Hablar con el equipo

Cuando la clienta quiere comprar, manda una foto o pide hablar con alguien, el bot le pasa el enlace a tu WhatsApp de atención, el **+591 76705942**, y desde ahí atiende la familia.

Usa la **API oficial de Meta** (WhatsApp Cloud API), así que **no hay riesgo de bloqueo**. El bot funciona en **Cloudflare Workers**, que es gratis, y no necesita computadora encendida.

---

## Antes de empezar: lo que necesitas
1. **Un chip nuevo**, con un número que **no** tenga WhatsApp. Ese será el número del bot. Tu número actual (76705942) se queda como está, para que la familia atienda.
   - ¿Por qué otro número? Un número conectado a la API ya no funciona en la app normal de WhatsApp, y te quedarías sin ver tus chats.
2. Una cuenta de **Facebook** personal (la tuya o la de tu mamá).
3. Un **correo** para crear la cuenta de Cloudflare.
4. Una computadora con navegador, solo para configurar (unos 40 minutos).

## ¿Cuánto cuesta?
- **Cloudflare Workers**: gratis, con hasta 100.000 mensajes al día, mucho más de lo que necesitas.
- **Meta**: responder a una clienta que te escribió primero es un «mensaje de servicio». Según la información disponible, desde octubre de 2026 cada número tiene **1.000 mensajes de servicio gratis al mes**, y a partir de ahí Meta cobra por mensaje. Revisa la tabla actual en la página de precios de WhatsApp de Meta antes de lanzar.
- Este bot **solo responde**, nunca escribe primero ni manda publicidad. Por eso no gasta en mensajes de plantilla.

---

## Paso 1: Crear la app en Meta
1. Entra a **developers.facebook.com** con tu Facebook y toca **Comenzar** para registrarte como desarrollador (es gratis).
2. Ve a **Mis apps → Crear app**.
3. Ponle de nombre **VESTA BAGS Bot**.
4. En el caso de uso, elige **«Conectarse con los clientes a través de WhatsApp»**. Si Meta muestra otra pantalla, elige el tipo **Empresa**.
5. Si te pide un **portfolio comercial** (Business Manager), crea uno llamado **VESTA BAGS**.
6. Dentro de la app, abre **WhatsApp → Configuración de la API** (API Setup).

Ahí verás tres datos importantes:
- **Número de prueba**: Meta te regala uno para probar.
- **Identificador del número de teléfono** (Phone number ID).
- **Token de acceso temporal**, que dura 24 horas y sirve para probar.

7. En **«Para» / Destinatarios**, agrega **tu número personal** y verifícalo con el código que te llega. Con el número de prueba solo puedes hablar con los números que agregues aquí, hasta 5.

## Paso 2: Copiar la clave secreta de la app
En la app de Meta, ve a **Configuración de la app → Básica** y toca **Mostrar** en **Clave secreta de la app**. Cópiala y guárdala. Sirve para que nadie más pueda hacerse pasar por Meta ante tu bot.

## Paso 3: Publicar el bot en Cloudflare (gratis)
1. Crea una cuenta en **dash.cloudflare.com**.
2. En el menú, ve a **Compute (Workers) → Workers & Pages → Create → Create Worker**. El nombre puede variar un poco según la versión.
3. Llámalo **vesta-bot** y toca **Deploy**.
4. Toca **Edit code**, borra todo lo que aparece, **pega todo el archivo `worker.js`** de esta carpeta y toca **Deploy**.
5. Copia la dirección del worker. Se ve así: `https://vesta-bot.TU-USUARIO.workers.dev`.
6. Ve a **Settings → Variables and Secrets** y agrega:

| Nombre | Tipo | Valor |
|---|---|---|
| `WHATSAPP_TOKEN` | Secret | el token de acceso de Meta (el temporal por ahora) |
| `VERIFY_TOKEN` | Secret | una palabra que inventas, por ejemplo `vesta-carteras-2026` |
| `APP_SECRET` | Secret | la clave secreta de la app (paso 2) |

7. Toca **Deploy** de nuevo para que tome las variables.
8. Abre la dirección del worker en el navegador. Debe aparecer una página que dice que el acceso no está permitido (error 403). Eso es normal: significa que funciona y que está protegido.

## Paso 4: Conectar Meta con el bot (webhook)
1. En la app de Meta, ve a **WhatsApp → Configuración** (Configuration).
2. En **Webhook**, toca **Editar**:
   - **URL de devolución de llamada**: la dirección de tu worker.
   - **Token de verificación**: la misma palabra que pusiste en `VERIFY_TOKEN`.
3. Toca **Verificar y guardar**. Si sale un error, revisa que la palabra sea exactamente igual.
4. En **Campos del webhook**, busca **messages** y toca **Suscribirse**.

## Paso 5: Probar
Desde tu WhatsApp personal, escríbele **«Hola»** al número de prueba de Meta. Deberías recibir el saludo de Vesta con el botón **«Ver opciones»**. Prueba también con:
- «¿Hacen envíos a Santa Cruz?»
- «¿Son originales?»
- Una foto de una cartera
- «Quiero hablar con alguien»

Si no responde, en Cloudflare abre el worker, ve a **Logs → Begin log stream**, vuelve a escribir y mira el error (ver **Problemas comunes**).

## Paso 6: Token permanente (para que no deje de funcionar a las 24 h)
1. Ve a **business.facebook.com → Configuración → Usuarios → Usuarios del sistema → Agregar**.
2. Ponle de nombre **vesta-bot** y de rol **Administrador**.
3. Toca **Asignar activos**: elige tu **app** (control total) y tu **cuenta de WhatsApp** (control total).
4. Toca **Generar token**:
   - En la app, elige VESTA BAGS Bot.
   - En la caducidad, elige **Nunca**.
   - En los permisos, marca `whatsapp_business_messaging` y `whatsapp_business_management`.
5. Copia el token. En Cloudflare, reemplaza el valor de `WHATSAPP_TOKEN` y toca **Deploy**.

## Paso 7: Pasar del número de prueba a tu número real
1. En Meta, ve a **WhatsApp → Configuración de la API → Agregar número de teléfono**.
2. **Nombre visible**: **VESTA BAGS**. Meta lo revisa, así que debe coincidir con tu marca.
3. Categoría: **Ropa y accesorios**. Descripción: «Distribuidores oficiales de Tizza en Bolivia 🤍».
4. Pon el número del **chip nuevo** y verifícalo con el SMS o la llamada.
5. Si Meta te lo pide, agrega un **método de pago**. Solo se cobra si pasas el límite gratis.
6. Listo. No hay que cambiar nada en el bot: responde desde el número que reciba el mensaje.
7. Pon una foto de perfil (el logo `assets/logo-dark.png` sobre fondo nude) en **WhatsApp Manager → Números de teléfono → Perfil**.

La **verificación del negocio** no es obligatoria para empezar a responder. Hazla después si quieres el nombre más visible o más límites.

---

## Cómo cambiar los textos
Todo está al inicio de `worker.js`, dentro de `CONFIG`:
- `greeting`: el saludo con el menú.
- `menu`: las opciones del menú. El título va con máximo 24 letras y la descripción con máximo 72.
- `answers`: cada respuesta.
- `keywords`: las palabras que activan cada respuesta, escritas sin tildes y en minúsculas.
- `humanNumber`: el WhatsApp donde atiende la familia.
- `webUrl`: cuando tengas el dominio de la tienda, ponlo aquí y el bot lo compartirá.
- `openHour` / `closeHour`: el horario.

Después de editar, en Cloudflare toca **Edit code**, pega el archivo nuevo y toca **Deploy**.

**Reglas de marca**: no escribas precios, plazos ni promociones que no estén confirmados. El bot nunca confirma pedidos: siempre manda a la clienta con el equipo.

## Problemas comunes
| Problema | Solución |
|---|---|
| «Verificar y guardar» falla | `VERIFY_TOKEN` en Cloudflare debe ser idéntico al de Meta. Después de cambiarlo, toca Deploy. |
| No responde y el log dice `401` | El token venció. Haz el paso 6 (token permanente). |
| El log dice «Firma inválida» | `APP_SECRET` está mal copiado. Vuelve a copiarlo desde Configuración → Básica. |
| El log dice `131030` | Con el número de prueba, agrega tu número como destinatario (paso 1.7). |
| Nada llega al log | Falta suscribirse al campo **messages** en el webhook (paso 4.4). |
| Error con la versión | Agrega la variable `GRAPH_VERSION` con la versión que muestra Meta en su ejemplo (por ejemplo `v23.0`). |

## Pruebas (para desarrolladores)
```
node --test bot-whatsapp/test.mjs
```
Comprueban las palabras clave, el horario de Bolivia, los límites de los botones de WhatsApp, la verificación del webhook, la firma de seguridad y el envío a Meta, todo sin conectarse a internet.
