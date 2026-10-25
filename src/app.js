/* =========================================================
   VESTA BAGS — LÓGICA DE LA TIENDA
   1 utilidades · 2 dinero · 3 carrito · 4 cliente · 5 WhatsApp · 6 componentes · 7 secciones · 8 eventos
   ========================================================= */
(function () {
  "use strict";
  const CONFIG = window.VESTA_CONFIG, COLORS = window.VESTA_COLORS;
  const CATALOG = window.VESTA_CATALOG.filter(p => p.active !== false);
  // Solo se muestran colecciones y tipos que tienen productos
  const COLS = window.VESTA_COLLECTIONS.filter(c => CATALOG.some(p => p.collection === c.id));
  const CATS = window.VESTA_CATEGORIES.filter(c => CATALOG.some(p => p.category === c.id));

  /* ---------- 1. Utilidades ---------- */
  const $ = s => document.querySelector(s);
  const $$ = s => [...document.querySelectorAll(s)];
  const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const SRC = p => (window.VESTA_EMBED && window.VESTA_EMBED[p]) || p;
  const norm = s => String(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
  const reduced = () => matchMedia("(prefers-reduced-motion: reduce)").matches;
  const store = {
    get(k, d) { try { const v = JSON.parse(localStorage.getItem(k)); return v ?? d; } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* almacenamiento no disponible */ } }
  };
  const byId = id => CATALOG.find(p => p.id === id);
  const catOf = p => CATS.find(c => c.id === p.category) || { label: p.category };
  const colOf = p => COLS.find(c => c.id === p.collection) || null;
  const descOf = p => p.description || `${catOf(p).label.replace(/s$/, "")}${colOf(p) ? ` de la colección ${colOf(p).label}` : ""}, en ${p.colors.length > 1 ? p.colors.length + " colores" : "color " + colorLabel(p.colors[0]).toLowerCase()}.`;
  const colorLabel = c => (COLORS[c] || { label: c }).label;
  const imagesOf = (p, color) => (p.images && (p.images[color] || p.images[p.colors[0]])) || [];
  const isNewSort = (a, b) => String(b.addedAt || "").localeCompare(String(a.addedAt || ""));
  const ICON = {
    close: '<svg class="ico" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6 6 18"/></svg>',
    minus: '<svg class="ico" viewBox="0 0 24 24"><path d="M6 12h12"/></svg>',
    plus: '<svg class="ico" viewBox="0 0 24 24"><path d="M6 12h12M12 6v12"/></svg>',
    check: '<svg class="ico" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
    wa: '<svg class="ico" viewBox="0 0 24 24"><path d="M4 20l1.3-3.9A8 8 0 1 1 8 18.8L4 20Z"/><path d="M9 9.5c0 3 2.5 5.5 5.5 5.5l1.2-1.4-1.9-.9-.8.8a4 4 0 0 1-2.4-2.4l.8-.8-.9-1.9L9 9.5Z"/></svg>',
    go: '<svg class="ico" viewBox="0 0 24 24" style="width:16px;height:16px"><path d="M9 6l6 6-6 6"/></svg>'
  };

  /* ---------- 2. Dinero (en centavos) ---------- */
  const Money = {
    nf: new Intl.NumberFormat("es-BO", { minimumFractionDigits: 0, maximumFractionDigits: 2 }),
    isPrice: n => typeof n === "number" && isFinite(n) && n >= 0,
    cents: n => Math.round(Number(n) * 100),
    format(n) { return `${CONFIG.currencyLabel} ${this.nf.format(n)}`; }
  };
  const canBuy = p => !!p && p.availability !== "soldout";
  const maxQty = p => Number.isInteger(p.stock) && p.stock > 0 ? Math.min(p.stock, CONFIG.maxQtyPerItem) : CONFIG.maxQtyPerItem;

  /* ---------- 3. Carrito ---------- */
  const Cart = {
    items: [],
    load() {
      const raw = store.get(CONFIG.storage.cart, []);
      const map = new Map();
      (Array.isArray(raw) ? raw : []).forEach(it => {
        const p = it && byId(it.id);
        if (!canBuy(p)) return;
        const color = p.colors.includes(it.color) ? it.color : null;
        const q = Math.floor(Number(it.qty));
        if (!color || !Number.isFinite(q) || q < 1) return;
        const key = p.id + "|" + color, prev = map.get(key);
        map.set(key, { id: p.id, color, qty: Math.min((prev ? prev.qty : 0) + q, maxQty(p)) });
      });
      this.items = [...map.values()]; this.save();
    },
    save() { store.set(CONFIG.storage.cart, this.items); },
    find(id, color) { return this.items.find(i => i.id === id && i.color === color); },
    room(id, color) { const p = byId(id), l = this.find(id, color); return maxQty(p) - (l ? l.qty : 0); },
    add(id, color, qty = 1) {
      const p = byId(id);
      if (!canBuy(p) || !p.colors.includes(color)) return "invalid";
      qty = Math.floor(qty);
      if (!Number.isFinite(qty) || qty < 1) return "invalid";
      if (this.room(id, color) <= 0) return "max";
      const l = this.find(id, color);
      if (l) l.qty = Math.min(l.qty + qty, maxQty(p)); else this.items.push({ id, color, qty: Math.min(qty, maxQty(p)) });
      this.save(); return "ok";
    },
    setQty(id, color, qty) {
      const l = this.find(id, color); if (!l) return;
      qty = Math.floor(qty);
      if (!Number.isFinite(qty) || qty < 1) return this.remove(id, color);
      l.qty = Math.min(qty, maxQty(byId(id))); this.save();
    },
    remove(id, color) { this.items = this.items.filter(i => !(i.id === id && i.color === color)); this.save(); },
    count() { return this.items.reduce((s, i) => s + i.qty, 0); },
    totals() {
      const lines = this.items.map(i => {
        const p = byId(i.id), priced = Money.isPrice(p.price);
        return { ...i, product: p, priced, unit: priced ? p.price : null, subCents: priced ? Money.cents(p.price) * i.qty : 0 };
      });
      const pricedCents = lines.reduce((s, l) => s + l.subCents, 0);
      const allPriced = lines.length > 0 && lines.every(l => l.priced);
      const ship = Money.isPrice(CONFIG.shippingCost) ? CONFIG.shippingCost : null;
      return {
        lines, allPriced, pending: lines.filter(l => !l.priced).length,
        products: pricedCents / 100, shipping: ship,
        total: allPriced ? (pricedCents + (ship != null ? Money.cents(ship) : 0)) / 100 : null
      };
    }
  };

  /* ---------- 4. Datos del cliente ---------- */
  const Customer = {
    data: { name: "", city: "", zone: "", ref: "" },
    load() { const d = store.get(CONFIG.storage.customer, {}); for (const k in this.data) if (typeof d[k] === "string") this.data[k] = d[k].slice(0, 120); },
    save() { store.set(CONFIG.storage.customer, this.data); },
    errors() {
      const e = {};
      if (this.data.name.trim().length < 2) e.name = "Escribe tu nombre para saber a quién responder.";
      if (!this.data.city.trim()) e.city = "Indica tu ciudad para coordinar la entrega.";
      return e;
    }
  };

  /* ---------- 5. WhatsApp ---------- */
  const WA = {
    base: () => `https://wa.me/${CONFIG.whatsapp}`,
    link: t => `https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(t)}`,
    order(t, c) {
      const o = [];
      o.push(t.allPriced ? `${CONFIG.waHello} Quiero realizar un pedido en ${CONFIG.brand}.`
        : `${CONFIG.waHello} Quiero consultar un pedido en ${CONFIG.brand}. Hay productos con precio por consultar.`);
      o.push("", "Productos:");
      t.lines.forEach((l, i) => {
        o.push(`${i + 1}. ${l.product.name}`);
        o.push(`   Color: ${colorLabel(l.color)}`);
        o.push(`   Cantidad: ${l.qty}`);
        o.push(`   Precio unitario: ${l.priced ? Money.format(l.unit) : "por consultar"}`);
        o.push(`   Subtotal: ${l.priced ? Money.format(l.subCents / 100) : "por consultar"}`);
      });
      o.push("");
      if (t.allPriced) {
        o.push(`Total de productos: ${Money.format(t.products)}`);
        if (t.shipping != null) { o.push(`Envío: ${Money.format(t.shipping)}`); o.push(`Total: ${Money.format(t.total)}`); }
        else o.push("Envío: por coordinar");
      } else {
        if (t.products > 0) o.push(`Subtotal de productos con precio: ${Money.format(t.products)}`);
        o.push(`Productos con precio por consultar: ${t.pending}. El total queda pendiente.`);
        o.push("Envío: por coordinar");
      }
      o.push("", "Datos de entrega:");
      o.push(`Nombre: ${c.name.trim() || "-"}`);
      o.push(`Ciudad: ${c.city.trim() || "-"}`);
      o.push(`Zona: ${c.zone.trim() || "-"}`);
      o.push(`Referencia: ${c.ref.trim() || "-"}`);
      o.push("", "¿Me confirman la disponibilidad, el costo de envío y la forma de pago?", "", "¡Gracias!");
      return o.join("\n");
    },
    product(p, color) {
      return [`${CONFIG.waHello} Quiero consultar por este producto de ${CONFIG.brand}:`, "",
        `${p.name}`, `Color: ${colorLabel(color)}`,
        `Precio: ${Money.isPrice(p.price) ? Money.format(p.price) : "por consultar"}`, "",
        "¿Me confirman el precio y la disponibilidad?", "", "¡Gracias!"].join("\n");
    }
  };

  /* ---------- 6. Componentes ---------- */
  const priceHTML = p => Money.isPrice(p.price)
    ? `<span class="price">${Money.format(p.price)}${Money.isPrice(p.compareAtPrice) && p.compareAtPrice > p.price ? `<s>${Money.format(p.compareAtPrice)}</s>` : ""}</span>`
    : `<span class="price price--ask">Precio por consultar</span>`;
  const stockHTML = p => p.availability === "soldout" ? `<span class="stock stock--out">Agotado</span>`
    : p.availability === "available" ? `<span class="stock stock--ok">Disponible</span>` : `<span class="stock">Disponibilidad por confirmar</span>`;
  // Imagen con respaldo: si una foto no carga, prueba la siguiente; si ninguna carga, muestra un aviso.
  // Las fotos del CDN de Shopify se piden al tamaño que se muestran (mucho más livianas)
  const isCdn = u => /cdn\.shopify\.com/.test(u);
  const sized = (u, w) => isCdn(u) ? `${u}${u.includes("?") ? "&" : "?"}width=${w}` : u;
  const imgTag = (srcs, alt, cls = "", lazy = true, sizes = "(max-width:900px) 50vw, 30vw") => {
    const list = (Array.isArray(srcs) ? srcs : [srcs]).filter(Boolean);
    if (!list.length) return "";
    const first = SRC(list[0]);
    const srcset = isCdn(first) ? ` srcset="${[360, 540, 760, 1080].map(w => `${esc(sized(first, w))} ${w}w`).join(", ")}" sizes="${sizes}"` : "";
    return `<img ${cls ? `class="${cls}"` : ""} src="${esc(sized(first, 760))}"${srcset} data-fb="${esc(JSON.stringify(list.slice(1).map(u => sized(SRC(u), 760))))}" alt="${esc(alt)}" width="1000" height="1250" ${lazy ? 'loading="lazy" decoding="async"' : ""}>`;
  };
  const phHTML = p => `<span class="ph" aria-hidden="true"><b>${esc(p ? p.name : "VESTA BAGS")}</b>Foto pendiente</span>`;
  const plate = (p, color, opts = {}) => {
    const ims = imagesOf(p, color);
    const start = opts.index || 0;
    const main = ims.slice(start).concat(ims.slice(0, start));
    const alt = opts.hover && ims.length > 1 ? imgTag(ims.slice(1), "", "alt", true, opts.sizes) : "";
    return `${phHTML(p)}${imgTag(main, altOf(p, color, start ? ", otra vista" : ""), `main${alt ? " has-alt" : ""}`, opts.lazy !== false, opts.sizes)}${alt}`;
  };
  const altOf = (p, color, view = "") => `${p.name} en ${colorLabel(color).toLowerCase()}${view}`;
  const cardColor = {};

  function card(p) {
    const color = cardColor[p.id] || p.colors[0];
    const badge = p.availability === "soldout" ? `<span class="badge">Agotado</span>` : p.isNew ? `<span class="badge">Nuevo</span>` : "";
    // Siempre la misma acción: se añade al carrito y el pedido completo va en un solo WhatsApp
    const action = !canBuy(p) ? `<button class="btn btn--sm btn--block" disabled>Agotado</button>`
      : `<button class="btn btn--sm btn--line btn--block" data-add="${p.id}">Añadir al carrito</button>`;
    return `<article class="card" data-card="${p.id}">
      <button class="plate" data-open="${p.id}" aria-label="Ver ${esc(p.name)}">${badge}${plate(p, color, { hover: true })}</button>
      <div class="card__row"><h3 class="card__name">${esc(p.name)}</h3>${priceHTML(p)}</div>
      <div class="card__meta"><span>${colorLabel(color)}</span>
        <div class="swatches" role="group" aria-label="Color de ${esc(p.name)}">${p.colors.map(c =>
          `<button class="sw" style="background:${COLORS[c].hex}" data-sw="${p.id}" data-color="${c}" aria-pressed="${c === color}" aria-label="${colorLabel(c)}"></button>`).join("")}</div></div>
      ${action}
    </article>`;
  }
  function refreshCards(id) { $$(`[data-card="${id}"]`).forEach(el => { el.outerHTML = card(byId(id)); }); }

  /* ---------- 7. Secciones ---------- */
  // Estáticos
  function renderStatic() {
    const a = $("#announce"); if (CONFIG.announcement) a.textContent = CONFIG.announcement; else a.hidden = true;
    $("#demoNote").hidden = !CONFIG.isDemoCatalog;
    ["#footWa", "#helpWa", "#menuWa"].forEach(s => { $(s).href = WA.base(); });
    $("#footSeller").textContent = CONFIG.hours || CONFIG.seller;
    $("#footPhone").textContent = "+" + CONFIG.whatsapp.replace(/^(\d{3})(\d{8})$/, "$1 $2");
    $("#year").textContent = new Date().getFullYear();
    const soc = Object.entries(CONFIG.social || {}).filter(([, u]) => u);
    $("#social").innerHTML = soc.map(([k, u]) => `<li><a href="${esc(u)}" target="_blank" rel="noopener">${k[0].toUpperCase() + k.slice(1)}</a></li>`).join("");
    $("#social").hidden = !soc.length;
    $("#footCols").innerHTML = COLS.map(c => `<li><button class="flink" data-col="${c.id}">${esc(c.label)}</button></li>`).join("")
      + CATS.slice(0, 4).map(c => `<li><button class="flink" data-navcat="${c.id}">${esc(c.label)}</button></li>`).join("");
  }
  const productsOf = colId => CATALOG.filter(p => p.collection === colId).sort((a, b) => (b.featured - a.featured) || (b.isNew - a.isNew));
  const countLabel = n => `${n} ${n === 1 ? "modelo" : "modelos"}`;

  // Portada: logo de la marca y accesos a cada colección
  function renderSeal() {
    $("#sealNames").innerHTML = COLS.map(c => `<button data-col="${c.id}">${esc(c.label)}</button>`).join("");
    // Desplazamiento suave del contenido de la portada al hacer scroll
    const inner = $("#vitrine .seal__inner");
    if (reduced()) return;
    let ticking = false;
    addEventListener("scroll", () => {
      if (ticking) return; ticking = true;
      requestAnimationFrame(() => {
        const y = Math.min(scrollY, 700);
        inner.style.transform = y > 0 ? `translateY(${y * 0.28}px)` : "";
        inner.style.opacity = y > 0 ? String(Math.max(0, 1 - y / 620)) : "";
        ticking = false;
      });
    }, { passive: true });
  }

  // Colecciones en arcos
  function renderArches() {
    const list = $("#arches");
    list.innerHTML = COLS.map((c, i) => {
      const items = productsOf(c.id), a = items[0], b = items[1] || items[0];
      const ia = imagesOf(a, a.colors[0]), ib = imagesOf(b, b.colors[b.colors.length - 1]);
      return `<li style="--i:${i}"><button class="arch" data-col="${c.id}" aria-label="Ver colección ${esc(c.label)}, ${countLabel(items.length)}">
        <span class="arch__frame">${imgTag(ia, "", "a")}${imgTag(ib, "", "b")}</span>
        <span class="arch__name"><b>${esc(c.label)}</b><small>${countLabel(items.length)}</small></span>
        <span class="arch__go">Ver colección</span>
      </button></li>`;
    }).join("");
    // Revelado escalonado una sola vez, cuando la sección entra en pantalla
    if (reduced() || !("IntersectionObserver" in window)) return;
    const r = list.getBoundingClientRect();
    if (r.top < innerHeight * 0.9) return;
    list.classList.add("is-armed");
    const reveal = () => { list.classList.add("is-in"); setTimeout(() => list.classList.remove("is-armed", "is-in"), 1800); io.disconnect(); };
    const io = new IntersectionObserver(es => { if (es.some(e => e.isIntersecting)) reveal(); }, { threshold: 0.15 });
    io.observe(list);
  }

  // Tipos
  function renderCats() {
    const cover = id => CATALOG.find(p => p.category === id && p.featured) || CATALOG.find(p => p.category === id);
    $("#catList").innerHTML = CATS.map((c, i) => {
      const n = CATALOG.filter(p => p.category === c.id).length, p = cover(c.id);
      return `<li><button class="index__row${i === 0 ? " is-on" : ""}" data-cat="${c.id}">
        <span class="index__thumb"><span class="plate">${plate(p, p.colors[0])}</span></span>
        <b>${esc(c.label)}</b><small>${countLabel(n)}</small><span class="go">${ICON.go}</span></button></li>`;
    }).join("");
    $("#catPreview").innerHTML = `<div class="plate">${CATS.map((c, i) => { const p = cover(c.id); return imgTag(imagesOf(p, p.colors[0]), "", i === 0 ? "is-on" : "").replace("<img ", `<img data-prev="${c.id}" `); }).join("")}</div>
      <figcaption id="prevCap">${esc(cover(CATS[0].id).name)}</figcaption>`;
  }
  function previewCat(id) {
    $$(".index__row").forEach(r => r.classList.toggle("is-on", r.dataset.cat === id));
    $$("[data-prev]").forEach(im => im.classList.toggle("is-on", im.dataset.prev === id));
    const p = CATALOG.find(x => x.category === id && x.featured) || CATALOG.find(x => x.category === id);
    if (p && $("#prevCap")) $("#prevCap").textContent = p.name;
  }

  // Novedades
  function renderRail() {
    const list = CATALOG.filter(p => p.isNew || p.featured).sort((a, b) => (b.isNew - a.isNew) || (b.featured - a.featured)).slice(0, 8);
    $("#novedades").hidden = !list.length;
    $("#rail").innerHTML = list.map(card).join("");
    updateRail();
  }
  function updateRail() {
    const r = $("#rail"); const max = r.scrollWidth - r.clientWidth - 2;
    $("#railPrev").disabled = r.scrollLeft <= 2; $("#railNext").disabled = r.scrollLeft >= max;
    $(".rail-ctrl").hidden = max <= 2;
  }

  // Tienda
  const F = { q: "", cols: new Set(), cats: new Set(), colors: new Set(), onlyAvail: false, sort: "featured" };
  function match(p, q) {
    if (!q) return true;
    const hay = norm([p.name, p.description, catOf(p).label, colOf(p) ? colOf(p).label : "", ...p.colors.map(colorLabel), ...(p.tags || [])].join(" "));
    return norm(q).trim().split(/\s+/).every(w => hay.includes(w));
  }
  function filtered() {
    const list = CATALOG.filter(p =>
      (!F.cols.size || F.cols.has(p.collection)) &&
      (!F.cats.size || F.cats.has(p.category)) &&
      (!F.colors.size || p.colors.some(c => F.colors.has(c))) &&
      (!F.onlyAvail || p.availability === "available") && match(p, F.q));
    const pk = (p, hi) => Money.isPrice(p.price) ? p.price : hi;
    const S = {
      featured: (a, b) => (b.featured - a.featured) || (b.isNew - a.isNew) || CATALOG.indexOf(a) - CATALOG.indexOf(b),
      new: (a, b) => (b.isNew - a.isNew) || isNewSort(a, b) || CATALOG.indexOf(a) - CATALOG.indexOf(b),
      "price-asc": (a, b) => (pk(a, Infinity) - pk(b, Infinity)) || a.name.localeCompare(b.name, "es"),
      "price-desc": (a, b) => (pk(b, -Infinity) - pk(a, -Infinity)) || a.name.localeCompare(b.name, "es"),
      name: (a, b) => a.name.localeCompare(b.name, "es")
    };
    return list.sort(S[F.sort] || S.featured);
  }
  const countIn = (key, id) => CATALOG.filter(p => p[key] === id).length;
  function filtersHTML(prefix) {
    const usedColors = Object.keys(COLORS).filter(c => CATALOG.some(p => p.colors.includes(c)));
    const group = (title, key, list, set) => `<fieldset class="fgroup"><legend>${title}</legend>${list.map(c =>
      `<label class="check"><input type="checkbox" data-f${key}="${c.id}" id="${prefix}-${key}-${c.id}" ${set.has(c.id) ? "checked" : ""}>${esc(c.label)}<small>${countIn(key === "col" ? "collection" : "category", c.id)}</small></label>`).join("")}</fieldset>`;
    return `${group("Colección", "col", COLS, F.cols)}${group("Tipo", "cat", CATS, F.cats)}
      <fieldset class="fgroup"><legend>Color</legend><div class="colorset">${usedColors.map(c =>
        `<button class="sw" type="button" style="background:${COLORS[c].hex}" data-fcolor="${c}" aria-pressed="${F.colors.has(c)}" aria-label="${colorLabel(c)}" title="${colorLabel(c)}"></button>`).join("")}</div></fieldset>
      ${CATALOG.some(p => p.availability === "available") ? `<fieldset class="fgroup"><legend>Disponibilidad</legend>
        <label class="check"><input type="checkbox" data-favail id="${prefix}-avail" ${F.onlyAvail ? "checked" : ""}>Solo disponibles ahora</label></fieldset>` : ""}
      <button class="textlink" type="button" data-clear style="align-self:flex-start" ${activeCount() ? "" : "hidden"}>Limpiar filtros</button>`;
  }
  const activeCount = () => F.cols.size + F.cats.size + F.colors.size + (F.onlyAvail ? 1 : 0) + (F.q.trim() ? 1 : 0);
  function renderFilters() { $("#filtersDesk").innerHTML = filtersHTML("d"); $("#filtersMob").innerHTML = filtersHTML("m"); }
  function renderColHead() {
    const c = F.cols.size === 1 ? COLS.find(x => F.cols.has(x.id)) : null;
    $("#colHead").innerHTML = c ? `<div class="colhead"><div><b>${esc(c.label)}</b><p>${esc(c.note || "")} ${countLabel(productsOf(c.id).length)}.</p></div>
      <button class="btn btn--line btn--sm" data-clear>Ver toda la tienda</button></div>` : "";
  }
  function renderGrid() { renderGridInner(); emit("grid", { query: F.q.trim() }); }
  function renderGridInner() {
    const list = filtered();
    renderColHead();
    $("#grid").innerHTML = list.length ? list.map(card).join("")
      : `<div class="empty"><h3>No hay productos con estos filtros</h3><p class="muted">${F.q.trim() ? `Nada coincide con «${esc(F.q.trim())}». ` : ""}Quita algún filtro o vuelve a ver toda la tienda.</p><button class="btn" data-clear>Limpiar filtros</button></div>`;
    const pills = [
      ...[...F.cols].map(c => [`col:${c}`, COLS.find(x => x.id === c).label]),
      ...[...F.cats].map(c => [`cat:${c}`, CATS.find(x => x.id === c).label]),
      ...[...F.colors].map(c => [`color:${c}`, colorLabel(c)]),
      ...(F.onlyAvail ? [["avail", "Solo disponibles ahora"]] : []),
      ...(F.q.trim() ? [["q", `«${F.q.trim()}»`]] : [])];
    $("#pills").innerHTML = `<span class="muted num" id="resCount" aria-live="polite">${countLabel(list.length)}</span>`
      + pills.map(([k, l]) => `<button class="pill" data-unpill="${esc(k)}" aria-label="Quitar filtro ${esc(l)}">${esc(l)}${ICON.close}</button>`).join("");
    const n = activeCount() - (F.q.trim() ? 1 : 0);
    $("#filterBtnTxt").textContent = n ? `Filtros (${n})` : "Filtros";
    $("#fsApply").textContent = `Ver ${countLabel(list.length)}`;
    $$("[data-clear]").forEach(b => { if (b.closest(".filters")) b.hidden = !activeCount(); });
  }
  function clearFilters() {
    F.q = ""; F.cols.clear(); F.cats.clear(); F.colors.clear(); F.onlyAvail = false; F.sort = "featured";
    $("#q").value = ""; $("#sort").value = "featured"; renderFilters(); renderGrid();
  }
  function showOnly(kind, id) {
    F.cols.clear(); F.cats.clear(); F.colors.clear(); F.onlyAvail = false; F.q = ""; $("#q").value = "";
    (kind === "col" ? F.cols : F.cats).add(id);
    renderFilters(); renderGrid(); goCatalog();
  }
  function applyFilters({ cats = [], cols = [] } = {}) {
    F.cols = new Set(cols); F.cats = new Set(cats); F.colors.clear(); F.onlyAvail = false; F.q = ""; $("#q").value = "";
    renderFilters(); renderGrid(); goCatalog();
  }
  const goCatalog = () => $("#tienda").scrollIntoView({ behavior: reduced() ? "auto" : "smooth" });

  // Ayuda
  let tab = 0;
  function renderHelp() {
    $("#tabs").innerHTML = CONFIG.info.map((t, i) => `<button class="tab" role="tab" id="tab-${t.id}" aria-controls="tabPanel" aria-selected="${i === tab}" tabindex="${i === tab ? 0 : -1}" data-tab="${i}">${esc(t.title)}</button>`).join("");
    const t = CONFIG.info[tab];
    $("#tabPanel").setAttribute("aria-labelledby", `tab-${t.id}`);
    $("#tabPanel").innerHTML = `<h3>${esc(t.title)}</h3><p>${esc(t.pending || !t.body ? t.fallback : t.body)}</p>`;
    $("#faq").innerHTML = CONFIG.faq.map(f => `<details><summary>${esc(f.q)}<span class="pm" aria-hidden="true"></span></summary><p>${esc(f.a)}</p></details>`).join("");
  }

  // Carrito
  function renderCount() {
    const n = Cart.count(), c = $("#cartCount");
    c.textContent = n; c.dataset.n = n;
    $("#cartBtn").setAttribute("aria-label", n ? `Abrir carrito, ${n} ${n === 1 ? "artículo" : "artículos"}` : "Abrir carrito, vacío");
  }
  // Eventos para que la mascota acompañe (bot.js los escucha)
  const emit = (name, detail) => document.dispatchEvent(new CustomEvent("vesta:" + name, { detail }));
  function renderCart() { renderCartInner(); emit("cart", Cart.totals()); }
  // Último pedido enviado a WhatsApp (se puede recuperar durante 2 días)
  const LAST_KEY = "vesta-last-order";
  function lastOrder() {
    const o = store.get(LAST_KEY, null);
    if (!o || !Array.isArray(o.items) || !o.items.length || Date.now() - (o.at || 0) > 2 * 864e5) return null;
    const items = o.items.filter(i => byId(i.id) && canBuy(byId(i.id)));
    return items.length ? items : null;
  }
  // Carrito en dos pasos: 1) Tu pedido  2) Tus datos (más cómodo en celular, sin teclado tapando todo)
  let cartStep = 1;
  function totalsHTML(t) {
    return t.allPriced
      ? `<div class="sum sum--total"><span>Total de productos</span><span>${Money.format(t.products)}</span></div>
         ${t.shipping != null ? `<div class="sum"><span>Envío</span><span>${Money.format(t.shipping)}</span></div><div class="sum sum--total"><span>Total</span><span>${Money.format(t.total)}</span></div>` : `<div class="sum"><span>Envío</span><span>Por coordinar</span></div>`}`
      : `${t.products > 0 ? `<div class="sum"><span>Productos con precio</span><span>${Money.format(t.products)}</span></div>` : ""}
         <p class="warn">${t.pending === 1 ? "Un producto tiene" : `${t.pending} productos tienen`} precio por consultar. Tu pedido se enviará como consulta y te confirmaremos el total.</p>`;
  }
  function renderCartInner() {
    renderCount();
    const t = Cart.totals();
    const n = t.lines.reduce((s, l) => s + l.qty, 0);
    if (!t.lines.length) cartStep = 1;
    $("#cart").dataset.step = cartStep;
    $("#cartTitle").textContent = cartStep === 2 ? "Tus datos" : "Tu pedido";
    if (!t.lines.length) {
      const last = lastOrder();
      $("#cartBody").innerHTML = `<div class="cart-empty"><h3>Tu carrito está vacío</h3><p class="muted">Explora las colecciones y añade tus favoritas.</p><a class="btn" href="#tienda" data-close>Ir a la tienda</a>
        ${last ? `<button class="textlink" type="button" data-restore>Recuperar mi último pedido (${last.reduce((s, i) => s + i.qty, 0)} ${last.length === 1 && last[0].qty === 1 ? "pieza" : "piezas"})</button>` : ""}</div>`;
      $("#cartFoot").hidden = true; return;
    }
    $("#cartFoot").hidden = false;
    if (cartStep === 1) {
      $("#cartBody").innerHTML = t.lines.map(l => {
        const p = l.product, mx = maxQty(p);
        return `<div class="line"><span class="plate">${plate(p, l.color, { lazy: false, sizes: "88px" })}</span>
          <div class="line__info">
            <div class="line__top"><b>${esc(p.name)}</b>${l.priced ? `<span class="price">${Money.format(l.subCents / 100)}</span>` : `<span class="price price--ask">Por consultar</span>`}</div>
            <span class="line__meta">${colorLabel(l.color)}${l.priced ? `. ${Money.format(l.unit)} c/u` : ""}</span>
            <div class="line__ctrl">
              <div class="qty" role="group" aria-label="Cantidad de ${esc(p.name)} ${colorLabel(l.color)}">
                <button data-q="-1" data-id="${p.id}" data-color="${l.color}" aria-label="Quitar una unidad" ${l.qty <= 1 ? "disabled" : ""}>${ICON.minus}</button>
                <output aria-live="polite">${l.qty}</output>
                <button data-q="1" data-id="${p.id}" data-color="${l.color}" aria-label="Añadir una unidad" ${l.qty >= mx ? "disabled" : ""}>${ICON.plus}</button>
              </div>
              <button class="rm" data-rm="${p.id}" data-color="${l.color}">Eliminar</button>
            </div>
            ${l.qty >= mx && Number.isInteger(p.stock) ? `<span class="fine">Cantidad máxima disponible.</span>` : ""}
          </div></div>`;
      }).join("");
      $("#cartFoot").innerHTML = `${totalsHTML(t)}
        <button class="btn btn--block" type="button" data-cstep="2">Continuar con mis datos</button>`;
      return;
    }
    // Paso 2: datos de entrega
    const d = Customer.data;
    const quick = CONFIG.cities.slice(0, 4);
    $("#cartBody").innerHTML = `
      <button class="textlink back" type="button" data-cstep="1">Volver a mi pedido (${n} ${n === 1 ? "pieza" : "piezas"})</button>
      <form class="ship" id="shipForm" novalidate>
        <p>Los usamos solo para preparar tu mensaje de WhatsApp y quedan guardados únicamente en este dispositivo.</p>
        <div class="fld"><label for="cName">Nombre</label><input id="cName" name="name" autocomplete="name" autocapitalize="words" enterkeyhint="next" value="${esc(d.name)}" aria-describedby="eName"><span class="err" id="eName" hidden></span></div>
        <div class="fld"><label for="cCity">Ciudad</label><input id="cCity" name="city" autocomplete="address-level2" autocapitalize="words" enterkeyhint="next" value="${esc(d.city)}" aria-describedby="eCity"><span class="err" id="eCity" hidden></span>
          <div class="chips" role="group" aria-label="Ciudades frecuentes">${quick.map(c => `<button type="button" class="chip" data-city="${esc(c)}" aria-pressed="${d.city === c}">${esc(c)}</button>`).join("")}</div></div>
        <div class="fld"><label for="cZone">Zona o barrio <span>(opcional)</span></label><input id="cZone" name="zone" autocapitalize="words" enterkeyhint="next" value="${esc(d.zone)}"></div>
        <div class="fld"><label for="cRef">Referencia <span>(opcional)</span></label><input id="cRef" name="ref" enterkeyhint="done" value="${esc(d.ref)}" placeholder="Calle, edificio o punto de encuentro"></div>
      </form>`;
    $("#cartFoot").innerHTML = `
      <div class="sum"><span>${n} ${n === 1 ? "pieza" : "piezas"}</span><span>${t.allPriced ? Money.format(t.total ?? t.products) : "Total por confirmar"}</span></div>
      <a class="btn btn--block" id="waBtn" target="_blank" rel="noopener">${ICON.wa}Finalizar pedido por WhatsApp</a>
      <p class="fine">Se abre WhatsApp con tu pedido escrito. Envíalo desde el chat; tu pedido queda confirmado cuando te respondamos.</p>`;
    updateWa();
  }
  function updateWa() { const b = $("#waBtn"); if (b) b.href = WA.link(WA.order(Cart.totals(), Customer.data)); }
  function showErrors(e) {
    [["name", "cName", "eName"], ["city", "cCity", "eCity"]].forEach(([k, i, er]) => {
      const inp = $("#" + i), m = $("#" + er); if (!inp) return;
      inp.setAttribute("aria-invalid", e[k] ? "true" : "false"); m.hidden = !e[k]; m.textContent = e[k] || "";
    });
  }
  function openCart() { const d = $("#cart"); if (!d.open) cartStep = 1; renderCart(); if (!d.open) { d.showModal(); emit("cartopen", Cart.totals()); } }
  function goStep(n) { cartStep = n; renderCart(); const b = $("#cart .sheet__body"); if (b) b.scrollTop = 0; if (n === 2 && matchMedia("(hover:hover)").matches) { const i = $("#cName"); if (i && !i.value) i.focus(); } }

  // Ficha
  const PD = { id: null, color: null, qty: 1, img: 0 };
  function openProduct(id, color) {
    const p = byId(id); if (!p) return;
    Object.assign(PD, { id, color: color && p.colors.includes(color) ? color : (cardColor[id] || p.colors[0]), qty: 1, img: 0 });
    renderPD(); const d = $("#pd"); if (!d.open) d.showModal(); d.scrollTop = 0;
  }
  function renderPD() { renderPDInner(); emit("pd", { id: PD.id, color: PD.color }); }
  function renderPDInner() {
    const p = byId(PD.id), color = PD.color, ims = imagesOf(p, color);
    const priced = Money.isPrice(p.price), buy = canBuy(p), room = Cart.room(p.id, color);
    PD.qty = Math.max(1, Math.min(PD.qty, Math.max(room, 1)));
    const related = [...CATALOG.filter(x => x.id !== p.id && x.collection === p.collection && x.category !== p.category), ...CATALOG.filter(x => x.id !== p.id && x.category === p.category), ...CATALOG.filter(x => x.id !== p.id)]
      .filter((x, i, a) => a.indexOf(x) === i).slice(0, 4);
    $("#pd").innerHTML = `
      <div class="pd__bar"><img src="${SRC("assets/logo-dark.png")}" alt="VESTA BAGS" width="611" height="293"><button class="iconbtn" data-close aria-label="Cerrar ficha">${ICON.close}</button></div>
      <div class="wrap">
        <div class="pd__main">
          <div class="gallery">
            <div class="thumbs" role="group" aria-label="Fotografías">${ims.map((s, i) => `<button data-img="${i}" aria-current="${i === PD.img}" aria-label="Foto ${i + 1} de ${ims.length}"><span class="plate">${phHTML(null).replace("VESTA BAGS", String(i + 1))}${imgTag([s], "")}</span></button>`).join("")}</div>
            <div class="plate gallery__main">${plate(p, color, { index: PD.img, lazy: false, sizes: "(max-width:900px) 100vw, 55vw" })}</div>
            ${CONFIG.isDemoCatalog ? `<p class="gallery__note">Fotografía de referencia de Tizza.</p>` : ""}
          </div>
          <div class="info">
            <span class="muted">${colOf(p) ? `Colección ${colOf(p).label}, ` : ""}${catOf(p).label.toLowerCase()}${p.isNew ? ", nuevo" : ""}</span>
            <h2 id="pdName">${esc(p.name)}</h2>
            <div class="info__price">${priced ? Money.format(p.price) : `<span class="price--ask" style="font-size:16px">Precio por consultar</span>`}</div>
            <p class="info__desc">${esc(descOf(p))}</p>
            ${p.features && p.features.length ? `<ul class="feats">${p.features.map(f => `<li>${esc(f)}</li>`).join("")}</ul>` : ""}
            <div class="opt"><span class="opt__label" id="pdColorL">Color <span>${colorLabel(color)}</span></span>
              <div class="colors" role="group" aria-labelledby="pdColorL">${p.colors.map(c => `<button data-pdcolor="${c}" aria-pressed="${c === color}"><i style="background:${COLORS[c].hex}"></i>${colorLabel(c)}</button>`).join("")}</div></div>
            ${stockHTML(p)}
            ${buy ? `<div class="opt"><span class="opt__label">Cantidad</span>
              <div class="buy"><div class="qty"><button data-pdq="-1" aria-label="Quitar una unidad" ${PD.qty <= 1 ? "disabled" : ""}>${ICON.minus}</button><output aria-live="polite">${PD.qty}</output><button data-pdq="1" aria-label="Añadir una unidad" ${PD.qty >= room ? "disabled" : ""}>${ICON.plus}</button></div>
              <button class="btn" data-pdadd ${room <= 0 ? "disabled" : ""}>${room <= 0 ? "Máximo en tu carrito" : "Añadir al carrito"}</button></div></div>` : `<button class="btn" disabled>Agotado</button>`}
            <a class="btn btn--line" target="_blank" rel="noopener" href="${WA.link(WA.product(p, color))}">${ICON.wa}Consultar por WhatsApp</a>
            ${!priced && buy ? `<p class="warn">Este modelo no tiene precio publicado. Si lo añades, tu pedido se enviará como consulta y el total quedará pendiente.</p>` : ""}
            <div class="acc">${CONFIG.info.filter(i => i.id === "entregas" || i.id === "pagos").map(i => `<details><summary>${esc(i.title)}<span class="pm" aria-hidden="true"></span></summary><p>${esc(i.pending || !i.body ? i.fallback : i.body)}</p></details>`).join("")}</div>
          </div>
        </div>
        ${buy && room > 0 ? `<div class="pd__dock" aria-hidden="false"><div><b>${esc(p.name)}</b><span>${colorLabel(color)} · ${priced ? Money.format(p.price) : "Precio por consultar"}</span></div><button class="btn" data-pdadd>Añadir</button></div>` : ""}
        ${related.length ? `<section class="related" aria-labelledby="relT"><h3 id="relT">También te puede gustar</h3><div class="grid">${related.map(card).join("")}</div></section>` : ""}
      </div>`;
  }

  // Búsqueda rápida
  function renderSearch() {
    const q = $("#sq").value.trim();
    const list = q ? CATALOG.filter(p => match(p, q)) : CATALOG.filter(p => p.featured);
    $("#sres").innerHTML = list.slice(0, 6).map(p => `<button data-open="${p.id}"><span class="plate">${plate(p, p.colors[0])}</span><b>${esc(p.name)}</b><small>${Money.isPrice(p.price) ? Money.format(p.price) : "Precio por consultar"}</small></button>`).join("");
    $("#shint").innerHTML = q
      ? (list.length ? `<span>${list.length} ${list.length === 1 ? "resultado" : "resultados"}</span><button class="textlink" data-searchall>Ver todos en la tienda</button>` : `<span>No encontramos «${esc(q)}». Prueba con otro nombre o un color.</span>`)
      : `<span>Destacados</span>`;
  }

  // Feedback
  let toastT, toastAction = null;
  // action: true = "Ver carrito", false = sin botón, { label, fn } = acción propia
  function toast(msg, action = true) {
    toastAction = action === true ? { label: "Ver carrito", fn: () => { if ($("#pd").open) $("#pd").close(); openCart(); } } : action || null;
    $("#toastMsg").textContent = msg; $("#toastCart").hidden = !toastAction;
    if (toastAction) $("#toastCart").textContent = toastAction.label;
    const el = $("#toast");
    // Si hay un diálogo abierto (ficha, carrito…), el aviso va dentro para que se vea encima
    const host = [...document.querySelectorAll("dialog[open]")].pop() || document.body;
    if (el.parentElement !== host) host.appendChild(el);
    el.classList.add("show"); clearTimeout(toastT); toastT = setTimeout(() => el.classList.remove("show"), action && action !== true ? 7000 : 3400);
  }
  function added(res, p, color, btn) {
    if (res === "max") return toast(`Ya tienes la cantidad máxima disponible de ${p.name}.`, true);
    if (res !== "ok") return;
    renderCount(); renderCart();
    const c = $("#cartCount"); c.classList.remove("bump"); void c.offsetWidth; c.classList.add("bump");
    if (btn) { const txt = btn.innerHTML; btn.classList.add("is-done"); btn.innerHTML = `${ICON.check}Añadida`; setTimeout(() => { if (btn.isConnected) { btn.classList.remove("is-done"); btn.innerHTML = txt; } }, 1600); }
    toast(`${p.name} en ${colorLabel(color).toLowerCase()} está en tu carrito.`);
    emit("added", { id: p.id });
  }

  /* ---------- 8. Eventos ---------- */
  document.addEventListener("click", e => {
    const t = e.target.closest("button, a"); if (!t) return;
    const d = t.dataset;
    if ("close" in d) { const dl = t.closest("dialog"); if (dl) dl.close(); if (t.tagName === "BUTTON") return; }
    if (d.open) { if ($("#searchSheet").open) $("#searchSheet").close(); openProduct(d.open, d.opencolor); return; }
    if (d.add) { const p = byId(d.add), c = cardColor[p.id] || p.colors[0]; added(Cart.add(p.id, c, 1), p, c, t); return; }
    if (d.sw) { cardColor[d.sw] = d.color; refreshCards(d.sw); return; }
    if (d.col) { if (t.closest("dialog")) t.closest("dialog").close(); showOnly("col", d.col); return; }
    if (d.navcat) { e.preventDefault(); if (t.closest("dialog")) t.closest("dialog").close(); showOnly("cat", d.navcat); return; }
    if (d.cat && t.classList.contains("index__row")) { showOnly("cat", d.cat); return; }
    if (d.fcolor) { F.colors.has(d.fcolor) ? F.colors.delete(d.fcolor) : F.colors.add(d.fcolor); renderFilters(); renderGrid(); return; }
    if ("clear" in d) { clearFilters(); return; }
    if (d.unpill) {
      const [k, v] = d.unpill.split(":");
      if (k === "col") F.cols.delete(v); else if (k === "cat") F.cats.delete(v); else if (k === "color") F.colors.delete(v); else if (k === "avail") F.onlyAvail = false; else { F.q = ""; $("#q").value = ""; }
      renderFilters(); renderGrid(); return;
    }
    if (d.q) { const l = Cart.find(d.id, d.color); if (l) { Cart.setQty(d.id, d.color, l.qty + Number(d.q)); renderCart(); } return; }
    if (d.rm) { const p = byId(d.rm); Cart.remove(d.rm, d.color); renderCart(); toast(`${p.name} se eliminó del carrito.`, false); return; }
    if (d.img) { PD.img = Number(d.img); renderPD(); return; }
    if (d.pdcolor) { PD.color = d.pdcolor; PD.img = 0; PD.qty = 1; cardColor[PD.id] = d.pdcolor; renderPD(); refreshCards(PD.id); return; }
    if (d.pdq) { PD.qty += Number(d.pdq); renderPD(); return; }
    if ("pdadd" in d) {
      const p = byId(PD.id), inDock = !!t.closest(".pd__dock"); const res = Cart.add(p.id, PD.color, PD.qty); PD.qty = 1; renderPD();
      added(res, p, PD.color, $(inDock ? "#pd .pd__dock [data-pdadd]" : "#pd .info [data-pdadd]")); return;
    }
    if (d.tab) { tab = Number(d.tab); renderHelp(); $(`[data-tab="${tab}"]`).focus(); return; }
    if ("searchall" in d) { F.q = $("#sq").value; $("#q").value = F.q; $("#searchSheet").close(); renderFilters(); renderGrid(); goCatalog(); return; }
    if (d.cstep) { goStep(Number(d.cstep)); return; }
    if ("restore" in d) { const last = lastOrder(); if (last) { last.forEach(i => Cart.add(i.id, i.color, i.qty)); store.set(LAST_KEY, null); renderCart(); toast("Recuperamos tu último pedido.", false); } return; }
    if (d.city) {
      Customer.data.city = d.city; Customer.save(); $("#cCity").value = d.city;
      $$("#shipForm .chip").forEach(c => c.setAttribute("aria-pressed", String(c.dataset.city === d.city)));
      if ($("#shipForm [aria-invalid=true]")) showErrors(Customer.errors()); updateWa(); return;
    }
    if (t.id === "waBtn") {
      const errs = Customer.errors();
      if (Object.keys(errs).length) { e.preventDefault(); showErrors(errs); $(errs.name ? "#cName" : "#cCity").focus(); }
      else {
        updateWa();
        // El pedido ya va escrito en WhatsApp: vaciamos el carrito (se puede recuperar desde el aviso)
        const saved = Cart.items.map(i => ({ ...i }));
        store.set(LAST_KEY, { items: saved, at: Date.now() });   // por si vuelve de WhatsApp sin haber enviado
        setTimeout(() => {
          Cart.items = []; Cart.save(); cartStep = 1; renderCart(); emit("ordersent", {});
          if ($("#cart").open) $("#cart").close();
          toast("Abrimos WhatsApp con tu pedido. Tu carrito quedó vacío.", { label: "Recuperar carrito", fn: () => {
            Cart.items = saved; Cart.save(); renderCart(); toast("Recuperamos tu carrito.");
          } });
        }, 350);
      }
    }
  });
  document.addEventListener("change", e => {
    const t = e.target;
    if (t.dataset.fcat) { t.checked ? F.cats.add(t.dataset.fcat) : F.cats.delete(t.dataset.fcat); renderFilters(); renderGrid(); }
    if (t.dataset.fcol) { t.checked ? F.cols.add(t.dataset.fcol) : F.cols.delete(t.dataset.fcol); renderFilters(); renderGrid(); }
    if ("favail" in t.dataset) { F.onlyAvail = t.checked; renderFilters(); renderGrid(); }
  });
  document.addEventListener("input", e => {
    const t = e.target;
    if (t.closest && t.closest("#shipForm")) {
      Customer.data[t.name] = t.value.slice(0, 120); Customer.save(); updateWa();
      if (t.getAttribute("aria-invalid") === "true") showErrors(Customer.errors());
    }
  });
  document.addEventListener("keydown", e => {
    if (e.key !== "Enter" || !e.target.closest || !e.target.closest("#shipForm")) return;
    e.preventDefault();
    const f = [...document.querySelectorAll("#shipForm input")], i = f.indexOf(e.target);
    if (f[i + 1]) f[i + 1].focus(); else e.target.blur();
  });
  $("#tabs").addEventListener("keydown", e => {
    if (!["ArrowLeft", "ArrowRight", "Home", "End"].includes(e.key)) return;
    e.preventDefault(); const n = CONFIG.info.length;
    tab = e.key === "Home" ? 0 : e.key === "End" ? n - 1 : (tab + (e.key === "ArrowRight" ? 1 : -1) + n) % n;
    renderHelp(); $(`[data-tab="${tab}"]`).focus();
  });
  $("#catList").addEventListener("mouseover", e => { const r = e.target.closest(".index__row"); if (r) previewCat(r.dataset.cat); });
  $("#catList").addEventListener("focusin", e => { const r = e.target.closest(".index__row"); if (r) previewCat(r.dataset.cat); });
  $("#q").addEventListener("input", e => { F.q = e.target.value; renderGrid(); $$("[data-clear]").forEach(b => { if (b.closest(".filters")) b.hidden = !activeCount(); }); });
  $("#sort").addEventListener("change", e => { F.sort = e.target.value; renderGrid(); });
  $("#railPrev").addEventListener("click", () => $("#rail").scrollBy({ left: -$("#rail").clientWidth * .8, behavior: reduced() ? "auto" : "smooth" }));
  $("#railNext").addEventListener("click", () => $("#rail").scrollBy({ left: $("#rail").clientWidth * .8, behavior: reduced() ? "auto" : "smooth" }));
  $("#rail").addEventListener("scroll", updateRail, { passive: true });
  addEventListener("resize", updateRail, { passive: true });
  $("#cartBtn").addEventListener("click", openCart);
  $("#footCart").addEventListener("click", openCart);
  $("#toastCart").addEventListener("click", () => { $("#toast").classList.remove("show"); const a = toastAction; toastAction = null; if (a) a.fn(); });
  $("#menuBtn").addEventListener("click", () => $("#mmenu").showModal());
  $("#mmenu").addEventListener("click", e => { if (e.target.closest(".mnav a")) $("#mmenu").close(); });
  // Respaldo de imágenes: si una foto no carga, se prueba la siguiente; si no queda ninguna, se muestra el aviso
  document.addEventListener("error", e => {
    const im = e.target; if (!(im instanceof HTMLImageElement) || !im.dataset.fb) return;
    let rest = []; try { rest = JSON.parse(im.dataset.fb); } catch (err) { rest = []; }
    if (rest.length) { im.dataset.fb = JSON.stringify(rest.slice(1)); im.src = rest[0]; }
    else { im.hidden = true; im.dataset.failed = "1"; const box = im.closest(".plate, .vitrine__bag"); if (box && !box.querySelector("img:not([hidden]).main, .vitrine__bag > img:not([hidden])")) box.classList.add("is-failed"); }
  }, true);
  $("#filterBtn").addEventListener("click", () => $("#filterSheet").showModal());
  $("#searchBtn").addEventListener("click", () => { renderSearch(); $("#searchSheet").showModal(); $("#sq").focus(); });
  $("#sq").addEventListener("input", renderSearch);
  $("#sq").addEventListener("keydown", e => { if (e.key === "Enter") { e.preventDefault(); const b = $("[data-searchall]"); if (b) b.click(); } });
  $$("dialog").forEach(dl => dl.addEventListener("click", e => { if (e.target === dl) dl.close(); }));
  $("#copyPhone").addEventListener("click", async () => {
    try { await navigator.clipboard.writeText("+" + CONFIG.whatsapp); toast("Número copiado.", false); }
    catch (err) { const r = document.createRange(); r.selectNodeContents($("#footPhone")); const s = getSelection(); s.removeAllRanges(); s.addRange(r); toast("Número seleccionado. Cópialo con Ctrl+C.", false); }
  });
  addEventListener("storage", e => { if (e.key === CONFIG.storage.cart) { Cart.load(); renderCart(); } });
  const hdr = $("#header"); const onScroll = () => hdr.classList.toggle("is-scrolled", scrollY > 10);
  addEventListener("scroll", onScroll, { passive: true });

  /* ---------- Inicio ---------- */
  // Si ningún producto tiene precio, ordenar por precio no sirve: se ocultan esas opciones
  if (!CATALOG.some(p => Money.isPrice(p.price))) $$('#sort option[value^="price"]').forEach(o => o.remove());
  Cart.load(); Customer.load();
  renderStatic(); renderSeal(); renderArches(); renderCats(); renderRail(); renderFilters(); renderGrid(); renderHelp(); renderCart(); onScroll();
  window.VESTA = { CONFIG, CATALOG, COLS, CATS, Cart, Customer, Money, WA, F, showOnly, productsOf, catOf, colorLabel, plate, openProduct, openCart, applyFilters };   // pruebas y depuración
})();
