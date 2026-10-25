/* =========================================================
   VESTA · ASISTENTE — mini bot de ayuda sin servidor
   Solo botones. Lee textos de window.VESTA_BOT (config.js)
   y las colecciones reales de la tienda (window.VESTA).
   ========================================================= */
(function () {
  "use strict";
  const BOT = window.VESTA_BOT, STORE = window.VESTA, CONFIG = window.VESTA_CONFIG;
  if (!BOT || !STORE) return;
  const $ = s => document.querySelector(s);
  const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const reduced = () => matchMedia("(prefers-reduced-motion: reduce)").matches;
  const number = () => BOT.whatsapp || CONFIG.whatsapp;
  const waLink = text => `https://wa.me/${number()}?text=${encodeURIComponent(text)}`;
  const mascot = () => $("#mascotTpl").innerHTML;

  const root = $("#bot"), fab = $("#botFab"), panel = $("#botPanel"), log = $("#botLog"), teaser = $("#botTeaser");
  const ICON_WA = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20l1.3-3.9A8 8 0 1 1 8 18.8L4 20Z"/><path d="M9 9.5c0 3 2.5 5.5 5.5 5.5l1.2-1.4-1.9-.9-.8.8a4 4 0 0 1-2.4-2.4l.8-.8-.9-1.9L9 9.5Z"/></svg>';

  // Mascota en el botón flotante y en el encabezado
  fab.insertAdjacentHTML("afterbegin", mascot());
  $("#botHeadAvatar").innerHTML = mascot();
  $("#botTitle").textContent = BOT.title;
  fab.setAttribute("aria-label", BOT.labels.open);
  $("#botClose").setAttribute("aria-label", BOT.labels.close);
  teaser.querySelector("span").textContent = BOT.teaser;

  /* ---------- Mensajes ---------- */
  let started = false;
  function botSay(html, actions) {
    clearActions();
    const typing = document.createElement("div");
    typing.className = "bmsg bmsg--bot";
    typing.innerHTML = `<span class="bavatar" aria-hidden="true">${mascot()}</span><span class="bbubble btyping" aria-label="Vesta está escribiendo"><i></i><i></i><i></i></span>`;
    log.appendChild(typing); scrollEnd();
    setTimeout(() => {
      typing.querySelector(".bbubble").outerHTML = `<div class="bbubble">${html}</div>`;
      if (actions) renderActions(actions);
      scrollEnd();
    }, reduced() ? 0 : 520);
  }
  function userSay(text) {
    clearActions();
    log.insertAdjacentHTML("beforeend", `<div class="bmsg bmsg--me"><div class="bbubble">${esc(text)}</div></div>`);
    scrollEnd();
  }
  function clearActions() { const a = log.querySelector(".bactions"); if (a) a.remove(); }
  // actions: [{label, go} | {label, wa, primary} | {label, shop}]
  function renderActions(list) {
    const html = list.map(a => a.wa
      ? `<a class="bbtn bbtn--wa" href="${waLink(a.wa)}" target="_blank" rel="noopener">${ICON_WA}${esc(a.label)}</a>`
      : `<button class="bbtn${a.ghost ? " bbtn--ghost" : ""}" type="button" data-bgo="${esc(a.go || "")}" data-bshop="${esc(a.shop || "")}">${esc(a.label)}</button>`).join("");
    log.insertAdjacentHTML("beforeend", `<div class="bactions" role="group" aria-label="Opciones">${html}</div>`);
    const first = log.querySelector(".bactions .bbtn");
    if (first && panel.contains(document.activeElement)) first.focus({ preventScroll: true });
  }
  const scrollEnd = () => { log.scrollTop = log.scrollHeight; };
  // Miniaturas de productos reales dentro del chat
  function productsHTML(list) {
    return `<div class="bprods">${list.map(p => `<button class="bprod" type="button" data-bopen="${esc(p.id)}">
      <span class="plate">${STORE.plate(p, p.colors[0], { sizes: "120px" })}</span>
      <b>${esc(p.name)}</b><small>${STORE.Money.isPrice(p.price) ? STORE.Money.format(p.price) : "Precio por consultar"}</small></button>`).join("")}</div>`;
  }
  const pick = (list, n = 3) => list.slice().sort((a, b) => (b.featured - a.featured) || (b.isNew - a.isNew)).slice(0, n);
  const quiz = { cat: "" };
  const tail = wa => [{ label: BOT.labels.back, go: "menu", ghost: true }, { label: BOT.labels.waTalk, wa: wa || BOT.answers.asesora.wa }];

  /* ---------- Flujo ---------- */
  function menu() {
    botSay(esc(BOT.greeting), BOT.menu.map(m => m.id === "asesora"
      ? { label: m.label, wa: BOT.answers.asesora.wa, menuId: "asesora" }
      : { label: m.label, go: m.id }));
  }
  function answer(id) {
    const A = BOT.answers;
    if (id === "menu") return menu();
    if (id === "colecciones") {
      const cols = STORE.COLS;
      if (!cols.length) return botSay(esc(A.unknown), tail());
      return botSay(esc(A.colecciones.text), [...cols.map(c => ({ label: c.label, go: "col:" + c.id })), { label: BOT.labels.back, go: "menu", ghost: true }]);
    }
    if (id.startsWith("col:")) {
      const c = STORE.COLS.find(x => x.id === id.slice(4));
      if (!c) return botSay(esc(A.unknown), tail());
      const items = STORE.productsOf(c.id);
      const types = [...new Set(items.map(p => STORE.catOf(p).label.toLowerCase()))];
      const auto = `La colección ${c.label} tiene ${items.length} ${items.length === 1 ? "modelo" : "modelos"}: ${types.join(", ").replace(/, ([^,]*)$/, " y $1")}.`;
      const text = BOT.collectionText[c.id] || auto;
      return botSay(esc(text) + productsHTML(pick(items)), [
        { label: BOT.labels.wa, wa: BOT.collectionWa.replace("{nombre}", c.label) },
        { label: BOT.labels.shop, shop: c.id },
        { label: BOT.labels.back, go: "menu", ghost: true }]);
    }
    if (id === "elegir") {
      const E = A.elegir;
      const cats = E.q1Options.filter(o => !o.cat || STORE.CATALOG.some(p => p.category === o.cat));
      return botSay(esc(E.q1), [...cats.map(o => ({ label: o.label, go: "q1:" + o.cat })), { label: BOT.labels.back, go: "menu", ghost: true }]);
    }
    if (id.startsWith("q1:")) {
      const E = A.elegir; quiz.cat = id.slice(3);
      const cols = STORE.COLS.filter(c => !quiz.cat || STORE.CATALOG.some(p => p.collection === c.id && p.category === quiz.cat));
      return botSay(esc(E.q2), [...cols.map(c => ({ label: c.label, go: "q2:" + c.id })), { label: E.anyCollection, go: "q2:" }]);
    }
    if (id.startsWith("q2:")) {
      const E = A.elegir, col = id.slice(3);
      let list = STORE.CATALOG.filter(p => (!quiz.cat || p.category === quiz.cat) && (!col || p.collection === col));
      let text = E.result;
      if (!list.length) { list = STORE.CATALOG.filter(p => !quiz.cat || p.category === quiz.cat); text = E.noMatch; }
      if (!list.length) { list = STORE.CATALOG; text = E.noMatch; }
      quiz.col = list.some(p => p.collection === col) ? col : "";
      return botSay(esc(text) + productsHTML(pick(list)), [
        { label: E.seeAll, go: "quizshop" },
        { label: BOT.labels.waTalk, wa: BOT.answers.asesora.wa },
        { label: BOT.labels.back, go: "menu", ghost: true }]);
    }
    if (id === "quizshop") {
      close(false);
      STORE.applyFilters({ cats: quiz.cat ? [quiz.cat] : [], cols: quiz.col ? [quiz.col] : [] });
      return;
    }
    if (id === "comprar") {
      const steps = A.comprar.steps.map(s => `<li>${esc(s)}</li>`).join("");
      return botSay(`${esc(A.comprar.text)}<ol>${steps}</ol>`, tail(A.comprar.wa));
    }
    if (A[id] && A[id].text) return botSay(esc(A[id].text), tail(A[id].wa));
    return botSay(esc(A.unknown), tail());
  }

  /* ---------- Abrir y cerrar ---------- */
  function open() {
    hideTeaser(); if (typeof hidePeek === "function") hidePeek();
    root.classList.add("is-open"); panel.hidden = false;
    fab.setAttribute("aria-expanded", "true");
    requestAnimationFrame(() => panel.classList.add("is-shown"));
    if (!started) { started = true; menu(); }
    setTimeout(() => { const b = log.querySelector(".bactions .bbtn") || $("#botClose"); b.focus({ preventScroll: true }); }, reduced() ? 0 : 560);
  }
  function close(returnFocus = true) {
    root.classList.remove("is-open"); panel.classList.remove("is-shown");
    fab.setAttribute("aria-expanded", "false");
    setTimeout(() => { if (!root.classList.contains("is-open")) panel.hidden = true; }, reduced() ? 0 : 260);
    if (returnFocus) fab.focus({ preventScroll: true });
  }
  fab.addEventListener("click", () => root.classList.contains("is-open") ? close() : open());
  $("#botClose").addEventListener("click", () => close());
  document.addEventListener("keydown", e => {
    if (e.key !== "Escape" || !root.classList.contains("is-open")) return;
    if (document.querySelector("dialog[open]")) return;   // primero se cierra el diálogo abierto
    close();
  });

  log.addEventListener("click", e => {
    const pb = e.target.closest("[data-bopen]");
    if (pb) { close(false); STORE.openProduct(pb.dataset.bopen); return; }
    const t = e.target.closest(".bbtn"); if (!t) return;
    if (t.tagName === "A") {                               // botón de WhatsApp: abre el chat
      if (t.closest(".bactions") && t.textContent.trim() === BOT.menu.find(m => m.id === "asesora").label) {
        userSay(t.textContent.trim()); botSay(esc(BOT.answers.asesora.text), tail());
      }
      return;
    }
    if (t.dataset.bshop) { close(false); STORE.showOnly("col", t.dataset.bshop); return; }
    if (t.dataset.bgo === "quizshop") return answer("quizshop");
    userSay(t.textContent.trim());
    answer(t.dataset.bgo);
  });

  /* ---------- Saludo al cargar (una vez) ---------- */
  let teaserT;
  function hideTeaser() { clearTimeout(teaserT); teaser.classList.remove("is-shown"); }
  teaser.addEventListener("click", open);
  root.hidden = false;
  if (!reduced()) fab.classList.add("is-waving");
  const teaserSeen = (() => { try { return sessionStorage.getItem("vesta-teaser") === "1"; } catch (e) { return false; } })();
  setTimeout(() => {
    if (root.classList.contains("is-open") || root.classList.contains("is-peeking")) return;
    if (BOT.teaserOncePerVisit && teaserSeen) return;
    try { sessionStorage.setItem("vesta-teaser", "1"); } catch (e) { /* sin almacenamiento */ }
    teaser.classList.add("is-shown");
    teaserT = setTimeout(hideTeaser, BOT.teaserDurationMs);
  }, BOT.teaserDelayMs);
  fab.addEventListener("animationend", e => { if (e.animationName === "botWave") fab.classList.remove("is-waving"); });

  /* =========================================================
     VESTA EN LA PÁGINA
     1) Se asoma desde abajo cuando la clienta lleva un rato bajando
     2) Aparece en grande dentro del carrito y acompaña
     3) Da un saltito cuando se añade algo al carrito
     4) Acompaña la búsqueda sin resultados
     ========================================================= */
  const store = {
    get(k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } },
    set(k, v) { try { sessionStorage.setItem(k, v); } catch (e) { /* sin almacenamiento */ } }
  };
  const anyDialogOpen = () => !!document.querySelector("dialog[open]");

  /* ---------- 1) Vesta se asoma (al bajar, recordatorio y gracias) ---------- */
  const peek = $("#peek"), P = BOT.peek;
  let peekShown = store.get("vesta-peek") === "1", peekHideT, peekOpts = [];
  $("#peekMascot").innerHTML = mascot();
  $("#peekClose").setAttribute("aria-label", BOT.labels.dismiss);

  // Muestra a Vesta asomándose con un mensaje y botones. options: {label, cat|col|go|chat|cart|dismiss}
  function say({ text, options = [], hideAfter = P.hideAfterMs }) {
    if (root.classList.contains("is-open") || anyDialogOpen()) return false;
    hideTeaser(); clearTimeout(peekHideT);
    peekOpts = options;
    $("#peekText").textContent = text;
    $("#peekOpts").innerHTML = options.map((o, i) =>
      `<button class="bbtn${o.chat || o.dismiss ? " bbtn--ghost" : ""}" type="button" data-pk="${i}">${esc(o.label)}</button>`).join("");
    peek.hidden = false; root.classList.add("is-peeking");
    peek.classList.remove("is-shown");
    requestAnimationFrame(() => requestAnimationFrame(() => peek.classList.add("is-shown")));
    if (hideAfter) peekHideT = setTimeout(hidePeek, hideAfter);
    return true;
  }
  function showPeek() {
    if (peekShown) return;
    if (say({ text: P.text, options: P.options })) { peekShown = true; store.set("vesta-peek", "1"); }
  }
  function hidePeek() {
    clearTimeout(peekHideT);
    if (peek.hidden) return;
    peek.classList.remove("is-shown"); root.classList.remove("is-peeking");
    setTimeout(() => { if (!peek.classList.contains("is-shown")) peek.hidden = true; }, reduced() ? 0 : 600);
  }
  const loadedAt = Date.now();
  function checkPeek() {
    if (peekShown) return removeEventListener("scroll", onScroll);
    const max = document.documentElement.scrollHeight - innerHeight;
    const pct = max > 0 ? (scrollY / max) * 100 : 0;
    if (pct >= P.scrollPercent && Date.now() - loadedAt >= P.afterSeconds * 1000) showPeek();
  }
  let scrollT;
  function onScroll() { clearTimeout(scrollT); scrollT = setTimeout(checkPeek, 450); }   // espera a que deje de bajar
  addEventListener("scroll", onScroll, { passive: true });

  $("#peekClose").addEventListener("click", hidePeek);
  peek.addEventListener("keydown", e => { if (e.key === "Escape") hidePeek(); });
  $("#peekOpts").addEventListener("click", e => {
    const b = e.target.closest("[data-pk]"); if (!b) return;
    const o = peekOpts[Number(b.dataset.pk)];
    hidePeek();
    if (!o || o.dismiss) return;
    if (o.cart) STORE.openCart();
    else if (o.cat) STORE.showOnly("cat", o.cat);
    else if (o.col) STORE.showOnly("col", o.col);
    else if (o.go) { const t = document.getElementById(o.go); if (t) t.scrollIntoView({ behavior: reduced() ? "auto" : "smooth" }); }
    else if (o.chat) open();
  });

  /* ---------- 2) Vesta en el carrito ---------- */
  function cartMessage(t) {
    const C = BOT.cart, n = t.lines.reduce((s, l) => s + l.qty, 0);
    if (!t.lines.length) return C.empty;
    if ($("#cart").dataset.step === "2") return C.form;
    if (!t.allPriced) return C.pending;
    if (n >= 3) return C.many.replace("{n}", n);
    return C.ready;
  }
  function renderCartPal(t) {
    const body = $("#cartBody"); if (!body) return;
    let pal = body.querySelector(".cartpal");
    if (!pal) {
      body.insertAdjacentHTML("afterbegin", `<div class="cartpal">
        <span class="cartpal__mascot" aria-hidden="true">${mascot()}</span>
        <div class="cartpal__bubble"><p class="cartpal__text" aria-live="polite"></p>
          <button class="textlink cartpal__ask" type="button">${esc(BOT.labels.askMe)}</button></div>
      </div>`);
      pal = body.querySelector(".cartpal");
      pal.querySelector(".cartpal__ask").addEventListener("click", () => { $("#cart").close(); open(); });
    }
    pal.querySelector(".cartpal__text").textContent = cartMessage(t);
  }
  document.addEventListener("vesta:cart", e => renderCartPal(e.detail));
  document.addEventListener("vesta:cartopen", e => {
    renderCartPal(e.detail);
    hidePeek();
    const pal = $("#cartBody .cartpal");
    if (pal && !reduced()) { pal.classList.remove("is-hello"); void pal.offsetWidth; pal.classList.add("is-hello"); }
  });
  renderCartPal(STORE.Cart.totals());

  /* ---------- Botón flotante: se aparta mientras haces scroll en el celular ---------- */
  let fabT;
  addEventListener("scroll", () => {
    if (!matchMedia("(max-width:600px)").matches || root.classList.contains("is-open")) return;
    root.classList.add("is-scrolling"); clearTimeout(fabT);
    fabT = setTimeout(() => root.classList.remove("is-scrolling"), 900);
  }, { passive: true });

  /* ---------- 3) Saltito al añadir ---------- */
  document.addEventListener("vesta:added", () => {
    if (reduced()) return;
    fab.classList.remove("is-hop"); void fab.offsetWidth; fab.classList.add("is-hop");
  });
  fab.addEventListener("animationend", e => { if (e.animationName === "botHop") fab.classList.remove("is-hop"); });

  /* ---------- 4) Búsqueda sin resultados ---------- */
  document.addEventListener("vesta:grid", e => {
    const empty = $("#grid .empty"); if (!empty || empty.querySelector(".emptypal")) return;
    empty.insertAdjacentHTML("afterbegin", `<span class="emptypal" aria-hidden="true">${mascot()}</span>`);
    const p = empty.querySelector("p");
    if (p && e.detail && e.detail.query) p.textContent = BOT.emptySearch;
    if (p) p.insertAdjacentHTML("afterend", `<button class="textlink" type="button" data-askvesta>${esc(BOT.labels.askMe)}</button>`);
  });
  document.addEventListener("click", e => { if (e.target.closest("[data-askvesta]")) open(); });

  /* ---------- 5) Consejito en la ficha del producto ---------- */
  let tipShown = false;   // el consejito sale en la primera ficha que se abre en la visita (y en esa misma al cambiar color)
  let tipFor = null;
  document.addEventListener("vesta:pd", e => {
    const p = STORE.CATALOG.find(x => x.id === e.detail.id); if (!p) return;
    if (tipShown && tipFor !== p.id) return;
    tipShown = true; tipFor = p.id;
    const anchor = $("#pd .info__desc"); if (!anchor) return;
    const T = BOT.productTip;
    const text = p.colors.length > 1 ? T.colors.replace("{n}", p.colors.length) : !STORE.Money.isPrice(p.price) ? T.ask : T.other;
    const msg = STORE.WA.product(p, e.detail.color);
    anchor.insertAdjacentHTML("afterend", `<div class="pdpal">
      <span class="pdpal__mascot" aria-hidden="true">${mascot()}</span>
      <div class="pdpal__bubble"><p>${esc(text)}</p>
        <a class="textlink" href="${waLink(msg)}" target="_blank" rel="noopener">${esc(T.button)}</a></div></div>`);
  });

  /* ---------- 6) Recordatorio de carrito (una vez por visita) ---------- */
  let reminded = store.get("vesta-remind") === "1", idleT;
  function remind() {
    if (reminded) return;
    const n = STORE.Cart.count(); if (!n) return;
    const pieces = `${n} ${n === 1 ? "pieza" : "piezas"}`;
    if (say({ text: BOT.remind.text.replace("{n}", pieces), options: [{ label: BOT.labels.myCart, cart: true }, { label: BOT.labels.keep, dismiss: true }] })) {
      reminded = true; store.set("vesta-remind", "1");
    }
  }
  // Escritorio: cuando el mouse sale por arriba de la ventana (intención de irse)
  document.addEventListener("mouseout", e => { if (!e.relatedTarget && e.clientY <= 0) remind(); });
  // Celular y escritorio: tras un rato sin moverse por la página
  function resetIdle() { clearTimeout(idleT); if (!reminded && BOT.remind.idleSeconds > 0) idleT = setTimeout(remind, BOT.remind.idleSeconds * 1000); }
  ["scroll", "pointerdown", "keydown"].forEach(ev => addEventListener(ev, resetIdle, { passive: true }));
  resetIdle();

  /* ---------- 7) Gracias después de enviar el pedido ---------- */
  document.addEventListener("vesta:ordersent", () => {
    if (!BOT.thanksPeek) return;   // por defecto basta con el aviso del pedido; Vesta no repite el mensaje
    setTimeout(() => say({ text: BOT.thanks, options: [{ label: BOT.labels.keep, dismiss: true }], hideAfter: 9000 }), 700);
  });

  window.VESTA_BOT_API = { open, close, answer, say };
})();
