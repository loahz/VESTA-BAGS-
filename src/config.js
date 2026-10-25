/* =========================================================
   VESTA BAGS — CONFIGURACIÓN DE LA TIENDA
   Todo lo editable sin tocar el código de la interfaz.
   ========================================================= */
window.VESTA_CONFIG = {
  brand: "VESTA BAGS",
  palette: "nude",                  // colores: "rosa" | "nude" | "lavanda" | "salvia" | "celeste" | "blanco" | "piedra"
  announcement: "Distribuidores oficiales de Tizza en Bolivia. Pedidos por WhatsApp de 9:00 a 19:00.",   // "" oculta la franja
  seller: "Equipo VESTA",            // nombre que se muestra en contacto (voz neutra: atiende el equipo)
  waHello: "Hola, equipo VESTA.",   // saludo con el que empiezan los mensajes de WhatsApp
  hours: "Todos los días de 9:00 a 19:00",
  whatsapp: "59176705942",          // internacional, sin + ni espacios (+591 76705942)
  currencyLabel: "Bs",
  shippingCost: null,               // número en Bs si existe un costo fijo confirmado; null = por coordinar
  maxQtyPerItem: 10,
  isDemoCatalog: true,              // true = muestra el aviso "fotos de referencia / precios por confirmar"
  storage: { cart: "vesta-cart-v2", customer: "vesta-customer-v1" },

  // Redes sociales: dejar "" las que no existan (no se muestran)
  social: { instagram: "", tiktok: "", facebook: "" },

  // Ciudades sugeridas en el formulario de entrega (el cliente puede escribir otra)
  cities: ["La Paz", "El Alto", "Santa Cruz de la Sierra", "Cochabamba", "Sucre", "Oruro", "Potosí", "Tarija", "Trinidad", "Cobija"],

  // Información de compra. pending:true = política aún NO confirmada por la tienda.
  // Mientras esté pendiente se muestra el texto "fallback" en la web.
  info: [
    { id: "entregas", title: "Entregas", pending: false,
      body: "En La Paz entregamos por delivery. Al resto de Bolivia enviamos por flota y el costo del envío lo cubre quien compra. Coordinamos contigo el día y el lugar por WhatsApp." },
    { id: "pagos", title: "Pagos", pending: false,
      body: "Puedes pagar con QR, transferencia o en efectivo contra entrega. Para los pedidos a una semana pedimos un adelanto del 50 %." },
    { id: "cambios", title: "Devoluciones", pending: false,
      body: "No aceptamos devoluciones. Antes de confirmar tu pedido, pregúntanos todo lo que necesites: medidas, colores y fotos reales de la pieza." },
    { id: "original", title: "Productos originales", pending: false,
      body: "Somos distribuidores oficiales de Tizza: traemos cada pieza directamente de la marca." },
    { id: "cuidados", title: "Cuidados", pending: false,
      body: "Guarda tu cartera rellena con papel para que conserve la forma, dentro de una bolsa de tela y lejos del sol directo y la humedad. Límpiala con un paño suave y seco." }
  ],

  // Preguntas frecuentes
  faq: [
    { q: "¿Cómo hago un pedido?", a: "Añade las carteras al carrito, completa tus datos de entrega y pulsa «Finalizar pedido por WhatsApp». Se abre el chat con tu pedido escrito; solo tienes que enviarlo." },
    { q: "¿Mi pedido queda reservado al enviarlo?", a: "Todavía no. Queda confirmado cuando te respondemos por WhatsApp con la disponibilidad de cada pieza." },
    { q: "¿Los productos son originales?", a: "Sí. Somos distribuidores oficiales de Tizza y traemos cada pieza directamente de la marca." },
    { q: "¿En qué horario atienden?", a: "Te respondemos por WhatsApp todos los días de 9:00 a 19:00." },
    { q: "¿Qué significa «Precio por consultar»?", a: "El precio de ese modelo aún no está publicado. Puedes añadirlo al carrito o consultarlo directamente; te confirmamos el precio antes de cerrar el pedido." },
    { q: "¿Puedo pedir más de un color del mismo modelo?", a: "Sí. Cada color se añade al carrito como un artículo distinto." },
    { q: "¿Por qué no veo precios?", a: "Estamos confirmando los precios en bolivianos de la nueva mercadería. Añade lo que te guste al carrito y te enviamos el precio y la disponibilidad por WhatsApp." }
  ]
};

/* =========================================================
   VESTA · ASISTENTE (mini bot de ayuda)
   Todos los textos del bot se editan aquí. No escribas precios,
   plazos ni políticas que no estén confirmados.
   ========================================================= */
window.VESTA_BOT = {
  title: "Vesta · Asistente",
  whatsapp: "",                       // vacío = usa el número de VESTA_CONFIG.whatsapp
  teaser: "Hola, soy Vesta 🤍",        // globito que aparece unos segundos al cargar
  teaserDelayMs: 1800,
  teaserOncePerVisit: true,         // el globito "Hola, soy Vesta" solo la primera vez de cada visita
  teaserDurationMs: 5000,
  greeting: "Hola, soy Vesta 🤍 Te ayudo a encontrar tu cartera ideal. ¿Qué quieres saber?",

  // Menú principal (el orden aquí es el orden en pantalla)
  menu: [
    { id: "elegir",      label: "Ayúdame a elegir" },
    { id: "colecciones", label: "Ver colecciones" },
    { id: "comprar",     label: "Cómo comprar" },
    { id: "pagos",       label: "Pagos" },
    { id: "envios",      label: "Envíos" },
    { id: "asesora",     label: "Hablar con nosotros" }
  ],

  // Respuestas. "wa" = mensaje prellenado para WhatsApp.
  answers: {
    colecciones: { text: "Estas son nuestras colecciones. ¿Cuál te gusta?" },
    comprar: {
      text: "Comprar es muy fácil:",
      steps: [
        "Elige tu cartera en la tienda y añádela al carrito.",
        "Envía tu pedido por WhatsApp desde el carrito.",
        "Coordinamos contigo el pago y la entrega."
      ],
      wa: "Hola, quiero hacer un pedido en VESTA BAGS"
    },
    pagos:   { text: "Puedes pagar con QR, transferencia o en efectivo contra entrega 🤍 En los pedidos a una semana pedimos un adelanto del 50 %.", wa: "Hola, quiero consultar las formas de pago de VESTA BAGS" },
    envios:  { text: "En La Paz te lo llevamos por delivery 🤍 Al resto de Bolivia enviamos por flota y el envío lo pagas tú. Coordinamos el día por WhatsApp.", wa: "Hola, quiero consultar el envío de VESTA BAGS a mi ciudad" },
    asesora: { text: "Te abrí WhatsApp para que hables con nosotros 🤍 Atendemos de 9:00 a 19:00.", wa: "Hola, quiero hacer una consulta en VESTA BAGS" },
    unknown: "Eso te lo confirmamos por WhatsApp 🤍",
    // "Ayúdame a elegir": 2 preguntas y Vesta recomienda productos reales de la tienda
    elegir: {
      q1: "¡Me encanta ayudarte! ¿Qué estás buscando? 🤍",
      q1Options: [
        { label: "Una cartera para salir", cat: "carteras" },
        { label: "Un morral para el día a día", cat: "morrales" },
        { label: "Una mochila", cat: "mochilas" },
        { label: "Una billetera", cat: "billeteras" },
        { label: "Sorpréndeme", cat: "" }
      ],
      q2: "¿Y qué colección te gusta más?",
      anyCollection: "Cualquiera",
      result: "Mira estas, creo que te van a encantar 🤍",
      noMatch: "Esa combinación todavía no la tengo, pero mira estas 🤍",
      seeAll: "Ver todas en la tienda"
    }
  },

  // Colecciones: se toman solas de la tienda. Aquí puedes escribir una frase propia por colección
  // (id: texto). Si no hay frase, el bot dice cuántos modelos y qué tipos tiene.
  collectionText: {},
  collectionWa: "Hola, me interesa la colección {nombre} de VESTA BAGS",

  // Vesta en la página -------------------------------------------------
  // Se asoma desde abajo cuando la clienta lleva un rato mirando (una vez por visita)
  peek: {
    text: "¿Qué quieres comprar hoy? 🤍",
    afterSeconds: 20,          // tiempo mínimo en la página
    scrollPercent: 40,         // y haber bajado al menos este % de la página
    hideAfterMs: 9000,         // se esconde sola si no la tocan
    options: [
      { label: "Carteras", cat: "carteras" },
      { label: "Mochilas", cat: "mochilas" },
      { label: "Ver colecciones", go: "colecciones" },
      { label: "Hablar con Vesta", chat: true }
    ]
  },
  // Vesta en grande dentro del carrito
  cart: {
    empty: "Tu carrito está vacío. ¿Qué quieres comprar hoy? 🤍",
    ready: "¡Qué linda elección! Completa tus datos y te preparo el pedido para WhatsApp 🤍",
    pending: "Algunas piezas tienen precio por consultar. Envía tu pedido y te confirmamos el total 🤍",
    many: "¡Llevas {n} piezas! Revisa colores y cantidades antes de enviar tu pedido 🤍",
    form: "Casi listo. Escribe tus datos y te preparo el mensaje para WhatsApp 🤍"
  },
  // Consejito de Vesta dentro de la ficha de cada producto
  productTip: {
    colors: "Este modelo viene en {n} colores. Toca cada color para verlo 🤍",
    ask: "El precio de este modelo te lo confirmo por WhatsApp 🤍",
    other: "¿Te ayudo con este modelo? Pregúntame lo que quieras 🤍",
    button: "Preguntar por este modelo"
  },
  // Recordatorio si deja piezas en el carrito (al intentar salir o tras un rato sin moverse). Una vez por visita.
  remind: { text: "¡No olvides tu pedido! Tienes {n} en el carrito 🤍", idleSeconds: 0 },   // 0 = solo al intentar salir (computadora), nunca por inactividad
  // Después de enviar el pedido a WhatsApp
  thanks: "¡Gracias por tu pedido! 🤍 Envía el mensaje en WhatsApp y te respondemos pronto.",
  thanksPeek: false,                // true = Vesta se asoma a agradecer después del pedido (además del aviso)
  // Cuando una búsqueda no encuentra nada
  emptySearch: "No encontré nada con eso. Prueba con otra palabra o pregúntame a mí 🤍",

  labels: { back: "Volver al menú", wa: "Pedir por WhatsApp", waTalk: "Escribir por WhatsApp", shop: "Ver en la tienda",
            open: "Abrir asistente de VESTA", close: "Cerrar asistente", dismiss: "Cerrar mensaje de Vesta", askMe: "Preguntarle a Vesta",
            see: "Ver", myCart: "Ver mi carrito", keep: "Seguir mirando" }
};

/* =========================================================
   PEDIDOS A UNA SEMANA (encargos desde los catálogos de Tizza)
   Página aparte: pedidos.html. No cambia la tienda principal.
   ========================================================= */
window.VESTA_ENCARGOS = {
  title: "Pedidos a una semana",
  leadTime: "aproximadamente una semana",
  showPrices: true,                 // false = oculta los precios de catálogo en las fichas de página (siguen en las imágenes)
  storageKey: "vesta-encargo-v1",
  // Catálogos. "chapters": página donde empieza cada sección (para los filtros rápidos)
  catalogs: [
    { id: "octubre", title: "Catálogo Octubre", subtitle: "Carteras, morrales, mochilas, billeteras, hombre y maletas",
      chapters: [
        { label: "Carteras", from: 2 }, { label: "Morrales", from: 99 }, { label: "Mochilas", from: 142 },
        { label: "Billeteras", from: 154 }, { label: "Tarjeteros", from: 214 }, { label: "Cosméticos", from: 218 },
        { label: "Vanité", from: 221 }, { label: "Hombre", from: 232 }, { label: "Maletas", from: 247 } ] },
    { id: "licencias", title: "Catálogo Licencias", subtitle: "Garfield, Toy Story, Hello Kitty, Stitch, Princesas, Snoopy y más",
      chapters: [
        { label: "Garfield", from: 2 }, { label: "Toy Story", from: 28 }, { label: "Hello Kitty", from: 38 },
        { label: "Stitch", from: 44 }, { label: "Princesas", from: 51 }, { label: "Mickey y Minnie", from: 55 },
        { label: "Relojes", from: 56 }, { label: "Snoopy", from: 59 }, { label: "Poleras", from: 62 } ] }
  ],
  intro: "Elige cualquier pieza de los catálogos de Tizza, aunque no esté en la tienda. La encargamos para ti y llega en aproximadamente una semana.",
  vesta: "¿No está en la tienda? Lo traemos para ti 🤍",
  steps: ["Abre un catálogo y busca la pieza que te gusta.", "Toca «Encargar» en esa página y escribe el color si hay varios.", "Envía tu encargo por WhatsApp. Te confirmamos disponibilidad y llegada, y con el 50 % de adelanto lo pedimos a Tizza."],
  waGreeting: "Quiero hacer un pedido a una semana en VESTA BAGS:",
  waClose: "¿Me confirman la disponibilidad y cuándo llegaría? Sé que se pide un adelanto del 50 %."
};
