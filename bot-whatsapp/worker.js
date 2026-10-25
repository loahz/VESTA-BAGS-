/* =========================================================
   VESTA BAGS — BOT DE WHATSAPP (API oficial de Meta · Cloud API)
   Se publica gratis en Cloudflare Workers: pega este archivo entero.
   Variables (Cloudflare → Settings → Variables and Secrets):
     WHATSAPP_TOKEN  token de acceso de Meta (secreto)
     VERIFY_TOKEN    una palabra que tú inventas, la misma que pones en Meta
     APP_SECRET      clave secreta de la app de Meta (secreto, recomendado)
     GRAPH_VERSION   opcional, por ejemplo "v23.0"
   Todos los textos se editan en CONFIG. No escribas precios, plazos
   ni promociones que no estén confirmados.
   ========================================================= */
const CONFIG = {
  humanNumber: "59176705942",            // WhatsApp donde atiende la familia (sin + ni espacios)
  humanHello: "Hola, equipo VESTA. Vengo del asistente y quiero hacer una consulta 🤍",
  openHour: 9, closeHour: 19,            // horario de atención (hora de Bolivia)
  webUrl: "",                            // enlace de la tienda; "" = aún no hay dominio
  menuButton: "Ver opciones",
  greeting: "¡Hola! Soy Vesta, el asistente de VESTA BAGS 🤍 Somos distribuidores oficiales de Tizza en Bolivia. ¿En qué te ayudamos?",
  menu: [
    { id: "catalogo", title: "Ver modelos",          description: "Colecciones y cómo elegir tu cartera" },
    { id: "precio",   title: "Precio y colores",     description: "Consulta un modelo" },
    { id: "envios",   title: "Envíos",               description: "Delivery en La Paz y envíos a Bolivia" },
    { id: "pagos",    title: "Formas de pago",       description: "QR, transferencia o efectivo" },
    { id: "encargo",  title: "Pedidos a una semana", description: "Te traemos cualquier pieza de Tizza" },
    { id: "original", title: "¿Son originales?",     description: "Distribuidores oficiales de Tizza" },
    { id: "equipo",   title: "Hablar con el equipo", description: "Te atiende la familia VESTA" }
  ],
  answers: {
    catalogo: "Tenemos carteras, morrales, mochilas y billeteras de Tizza, con colaboraciones oficiales de Mafalda, Garfield, Hello Kitty y Stitch 🤍\n\nMándanos la foto o captura del modelo que te gustó y te ayudamos con colores, precio y entrega.",
    precio: "¡Claro! Mándanos la foto o el nombre del modelo y el color que quieres 🤍 El equipo te confirma el precio y la disponibilidad.",
    envios: "En La Paz te lo llevamos por delivery 🤍 Al resto de Bolivia lo enviamos por flota y el envío lo paga quien compra. El día y el lugar los coordinamos contigo.",
    pagos: "Puedes pagar con QR, transferencia o en efectivo contra entrega 🤍 En los pedidos a una semana pedimos un adelanto del 50 %.",
    encargo: "¿No está en la tienda? ¡Lo traemos para ti! 🤍 Encargamos cualquier pieza de los catálogos de Tizza y llega en aproximadamente una semana, con el 50 % de adelanto. Mándanos la captura de la página del catálogo.",
    original: "Sí 🤍 Somos distribuidores oficiales de Tizza y traemos cada pieza directamente de la marca.",
    devolucion: "No manejamos devoluciones, por eso antes de confirmar te enviamos fotos reales, medidas y colores para que elijas segura 🤍",
    imagen: "¡Qué linda elección! 🤍 Para confirmarte precio, colores y disponibilidad de ese modelo, escríbele al equipo:",
    gracias: "¡Gracias a ti! 🤍 Aquí estamos cuando nos necesites.",
    noEntiendo: "Mmm, eso no lo entendí del todo 🤍 Elige una opción del menú o escribe al equipo.",
    equipo: "Te atiende la familia VESTA por aquí 🤍 Toca el enlace y envía el mensaje:",
    fueraHorario: "Ahora estamos fuera de horario (atendemos de 9:00 a 19:00). Déjanos tu mensaje y te respondemos a primera hora 🤍",
    pedido: "Un pedido queda confirmado cuando el equipo te responde con la disponibilidad y el total 🤍"
  },
  buttons: [ { id: "menu", title: "Ver menú" }, { id: "equipo", title: "Hablar con el equipo" } ],
  // Palabras que la clienta puede escribir (sin tildes, en minúscula) → respuesta
  keywords: [
    ["encargo",    ["encargo", "encargar", "una semana", "catalogo de tizza", "pedir a tizza"]],
    ["equipo",     ["persona", "humano", "asesor", "equipo", "hablar", "llamar", "comprar", "pedido", "reservar"]],
    ["envios",     ["envio", "envios", "enviar", "envian", "delivery", "flota", "entrega", "llega", "santa cruz", "cochabamba", "el alto", "sucre", "oruro", "potosi", "tarija", "beni", "pando"]],
    ["pagos",      ["pago", "pagar", "qr", "transferencia", "efectivo", "adelanto"]],
    ["original",   ["original", "originales", "replica", "falsa", "garantia"]],
    ["devolucion", ["devolucion", "devoluciones", "devolver", "cambio", "cambios", "cambiar"]],
    ["precio",     ["precio", "precios", "cuanto", "cuesta", "costo", "vale", "bs", "color", "colores", "stock", "disponible"]],
    ["catalogo",   ["catalogo", "modelos", "cartera", "carteras", "mochila", "mochilas", "morral", "morrales", "billetera", "billeteras", "mafalda", "garfield", "kitty", "stitch", "snoopy"]],
    ["gracias",    ["gracias", "grax", "genial", "perfecto"]],
    ["menu",       ["hola", "buenas", "buenos", "menu", "opciones", "info", "informacion", "inicio"]]
  ]
};

/* ---------- Lógica ---------- */
const norm = s => String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").trim();
const waLink = () => `https://wa.me/${CONFIG.humanNumber}?text=${encodeURIComponent(CONFIG.humanHello)}`;
// Bolivia es UTC-4 todo el año
const isOpen = (now = new Date()) => { const h = (now.getUTCHours() + 20) % 24; return h >= CONFIG.openHour && h < CONFIG.closeHour; };

function intentOf(text) {
  const t = norm(text);
  if (!t) return "menu";
  // Palabra completa (o frase), con plural opcional: "pago" también reconoce "pagos"
  for (const [id, words] of CONFIG.keywords)
    if (words.some(w => new RegExp(`(^|[^a-z])${w}(e?s)?([^a-z]|$)`).test(t))) return id;
  return "noEntiendo";
}

// Mensaje de la clienta → lista de mensajes a enviar (payloads de la Cloud API sin "to")
function reply(msg, now = new Date()) {
  let id;
  if (msg.type === "interactive") id = msg.interactive?.list_reply?.id || msg.interactive?.button_reply?.id;
  else if (msg.type === "button") id = intentOf(msg.button?.text);
  else if (msg.type === "text") id = intentOf(msg.text?.body);
  else if (msg.type === "image" || msg.type === "document") id = "imagen";
  else id = "menu";                                   // audio, sticker, ubicación…

  const A = CONFIG.answers;
  if (id === "menu" || !id) return [menuMessage()];
  if (id === "noEntiendo") return [menuMessage(A.noEntiendo)];
  if (id === "equipo" || id === "imagen") {
    const head = id === "imagen" ? A.imagen : A.equipo;
    const extra = isOpen(now) ? "" : `\n\n${A.fueraHorario}`;
    return [text(`${head}\n${waLink()}${extra}\n\n${A.pedido}`)];
  }
  let body = A[id] || A.noEntiendo;
  if (id === "catalogo" && CONFIG.webUrl) body += `\n\nTambién puedes verlos en la tienda: ${CONFIG.webUrl}`;
  return [buttons(body)];
}

const text = body => ({ type: "text", text: { body, preview_url: true } });
const buttons = body => ({ type: "interactive", interactive: { type: "button", body: { text: body },
  action: { buttons: CONFIG.buttons.map(b => ({ type: "reply", reply: { id: b.id, title: b.title } })) } } });
const menuMessage = (body = CONFIG.greeting) => ({ type: "interactive", interactive: { type: "list",
  body: { text: body }, footer: { text: "VESTA BAGS · Bolivia" },
  action: { button: CONFIG.menuButton, sections: [{ title: "¿En qué te ayudamos?", rows: CONFIG.menu }] } } });

async function send(env, phoneId, to, payload) {
  const v = env.GRAPH_VERSION || "v23.0";
  const r = await fetch(`https://graph.facebook.com/${v}/${phoneId}/messages`, {
    method: "POST",
    headers: { "Authorization": `Bearer ${env.WHATSAPP_TOKEN}`, "Content-Type": "application/json" },
    body: JSON.stringify({ messaging_product: "whatsapp", recipient_type: "individual", to, ...payload })
  });
  if (!r.ok) console.log("Error de Meta", r.status, await r.text());
}

async function validSignature(env, raw, header) {
  if (!env.APP_SECRET) return true;                   // sin APP_SECRET no se verifica (no recomendado)
  if (!header || !header.startsWith("sha256=")) return false;
  const key = await crypto.subtle.importKey("raw", new TextEncoder().encode(env.APP_SECRET),
    { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const sig = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(raw));
  const hex = [...new Uint8Array(sig)].map(b => b.toString(16).padStart(2, "0")).join("");
  const given = header.slice(7);
  if (given.length !== hex.length) return false;
  let diff = 0; for (let i = 0; i < hex.length; i++) diff |= hex.charCodeAt(i) ^ given.charCodeAt(i);
  return diff === 0;
}

async function handle(env, body) {
  for (const entry of body.entry || []) for (const change of entry.changes || []) {
    const value = change.value || {};
    const phoneId = value.metadata?.phone_number_id;
    for (const msg of value.messages || []) {
      for (const payload of reply(msg)) await send(env, phoneId, msg.from, payload);
    }
  }
}

export default {
  async fetch(req, env, ctx) {
    const url = new URL(req.url);
    // Verificación del webhook (Meta la hace una vez al configurarlo)
    if (req.method === "GET") {
      if (url.searchParams.get("hub.mode") === "subscribe" && url.searchParams.get("hub.verify_token") === env.VERIFY_TOKEN)
        return new Response(url.searchParams.get("hub.challenge") || "", { status: 200 });
      return new Response("VESTA BAGS · bot de WhatsApp activo 🤍", { status: env.VERIFY_TOKEN ? 403 : 200 });
    }
    if (req.method !== "POST") return new Response("Método no permitido", { status: 405 });
    const raw = await req.text();
    if (!(await validSignature(env, raw, req.headers.get("x-hub-signature-256")))) return new Response("Firma inválida", { status: 401 });
    let body; try { body = JSON.parse(raw); } catch { return new Response("JSON inválido", { status: 400 }); }
    ctx.waitUntil(handle(env, body).catch(e => console.log("Error del bot", e)));
    return new Response("OK", { status: 200 });      // responder rápido para que Meta no reintente
  }
};

