/* =========================================================
   VESTA BAGS — PEDIDOS A UNA SEMANA
   Catálogos completos de Tizza para encargar lo que aún no está en la tienda.
   Lista de encargo propia (no toca el carrito de la tienda).
   ========================================================= */
(function () {
  "use strict";
  const CONFIG = window.VESTA_CONFIG, E = window.VESTA_ENCARGOS, PAGES = window.VESTA_CATALOG_PAGES;
  const $ = s => document.querySelector(s), $$ = s => [...document.querySelectorAll(s)];
  const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const reduced = () => matchMedia("(prefers-reduced-motion: reduce)").matches;
  const store = {
    get(k, d) { try { const v = JSON.parse(localStorage.getItem(k)); return v ?? d; } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* sin almacenamiento */ } }
  };
  const CATS = E.catalogs.filter(c => PAGES[c.id] && PAGES[c.id].length);
  const catById = id => CATS.find(c => c.id === id);
  const pageOf = (cat, n) => PAGES[cat].find(p => p.n === n);
  const chapterOf = (cat, n) => { const ch = catById(cat).chapters.filter(c => c.from <= n); return ch.length ? ch[ch.length - 1].label : ""; };
  const priceText = p => !E.showPrices || !p.prices.length ? "" : p.prices.length === 1 ? `Bs ${p.prices[0]}` : `Bs ${Math.min(...p.prices)} a ${Math.max(...p.prices)}`;
  const ICON_WA = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20l1.3-3.9A8 8 0 1 1 8 18.8L4 20Z"/><path d="M9 9.5c0 3 2.5 5.5 5.5 5.5l1.2-1.4-1.9-.9-.8.8a4 4 0 0 1-2.4-2.4l.8-.8-.9-1.9L9 9.5Z"/></svg>';

  /* ---------- Lista de encargo ---------- */
  const List = {
    items: [],   // { cat, n, qty, note }
    load() {
      const raw = store.get(E.storageKey, []);
      this.items = (Array.isArray(raw) ? raw : []).filter(i => i && catById(i.cat) && pageOf(i.cat, i.n))
        .map(i => ({ cat: i.cat, n: i.n, qty: Math.min(Math.max(1, Math.floor(Number(i.qty)) || 1), 20), note: String(i.note || "").slice(0, 80) }));
      this.save();
    },
    save() { store.set(E.storageKey, this.items); },
    find(cat, n) { return this.items.find(i => i.cat === cat && i.n === n); },
    qtyOf(cat, n) { return this.items.filter(i => i.cat === cat && i.n === n).reduce((s, i) => s + i.qty, 0); },
    // Cada color o detalle distinto es una línea propia (así no se pierde «negro» si luego pides «rosado»)
    add(cat, n, note = "") {
      note = note.trim().slice(0, 80);
      const same = it => it.cat === cat && it.n === n && it.note.trim().toLowerCase() === note.toLowerCase();
      const it = this.items.find(same);
      if (it) it.qty = Math.min(it.qty + 1, 20);
      else this.items.push({ cat, n, qty: 1, note });
      this.save();
    },
    count() { return this.items.reduce((s, i) => s + i.qty, 0); }
  };
  const Customer = {
    key: CONFIG.storage.customer,
    get() { const d = store.get(this.key, {}); return { name: String(d.name || ""), city: String(d.city || ""), zone: String(d.zone || ""), ref: String(d.ref || "") }; },
    set(k, v) { const d = this.get(); d[k] = v.slice(0, 120); store.set(this.key, d); }
  };

  /* ---------- Mensaje de WhatsApp ---------- */
  function message() {
    const c = Customer.get();
    const o = [`${CONFIG.waHello} ${E.waGreeting}`, ""];
    List.items.forEach((it, i) => {
      const p = pageOf(it.cat, it.n), cat = catById(it.cat);
      o.push(`${i + 1}. ${cat.title}, página ${it.n}${chapterOf(it.cat, it.n) ? ` (${chapterOf(it.cat, it.n)})` : ""}`);
      if (p.codes.length) o.push(`   Código: ${p.codes.join(", ")}`);
      if (priceText(p)) o.push(`   Precio de catálogo: ${priceText(p)}`);
      o.push(`   Cantidad: ${it.qty}`);
      if (it.note.trim()) o.push(`   Detalle: ${it.note.trim()}`);
    });
    o.push("", `Nombre: ${c.name.trim() || "-"}`, `Ciudad: ${c.city.trim() || "-"}`, "", E.waClose, "", "¡Gracias!");
    return o.join("\n");
  }
  const waLink = () => `https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(message())}`;

  /* ---------- Estado de la vista ---------- */
  const S = { cat: CATS[0].id, chapter: "", q: "" };
  const thumb = p => p.thumb || p.img;
  const orderable = p => p.prices.length || p.codes.length || p.skus.length;   // portadas y separadores no se encargan
  const visible = () => {
    const q = S.q.replace(/\D/g, "");
    const cat = catById(S.cat), ch = cat.chapters, idx = ch.findIndex(c => c.label === S.chapter);
    const from = idx >= 0 ? ch[idx].from : 1, to = idx >= 0 && ch[idx + 1] ? ch[idx + 1].from - 1 : Infinity;
    return PAGES[S.cat].filter(p => (q ? [...p.codes, ...p.skus].some(c => c.includes(q)) : p.n >= from && p.n <= to));
  };

  function renderStatic() {
    const a = $("#announce"); if (CONFIG.announcement) a.textContent = CONFIG.announcement; else a.hidden = true;
    $("#encTitle").textContent = E.title;
    $("#encIntro").textContent = E.intro;
    $("#encSteps").innerHTML = E.steps.map(s => `<li>${esc(s)}</li>`).join("");
    $("#encVesta").textContent = E.vesta;
    $("#year").textContent = new Date().getFullYear();
    $("#encSwitch").innerHTML = CATS.map(c => `<button class="enc-tab" type="button" data-cat="${c.id}" aria-pressed="${c.id === S.cat}">
      <span class="enc-tab__cover"><img src="${esc(thumb(PAGES[c.id][0]))}" alt="" width="1000" height="1000" loading="lazy"></span>
      <span class="enc-tab__txt"><b>${esc(c.title)}</b><small>${esc(c.subtitle)}</small><em>${PAGES[c.id].length} páginas</em></span></button>`).join("");
  }
  function renderChips() {
    const cat = catById(S.cat);
    $("#encChips").innerHTML = [`<button class="chip" type="button" data-ch="" aria-pressed="${!S.chapter}">Todo</button>`,
      ...cat.chapters.map(c => `<button class="chip" type="button" data-ch="${esc(c.label)}" aria-pressed="${S.chapter === c.label}">${esc(c.label)}</button>`)].join("");
  }
  function renderGrid() {
    const list = visible();
    const digits = S.q.replace(/\D/g, "");
    if (S.q.trim() && !digits) { $("#encResults").textContent = "Escribe solo el número del código, por ejemplo 2141."; $("#encGrid").innerHTML = ""; return; }
    $("#encResults").textContent = S.q.trim()
      ? (list.length ? `${list.length} ${list.length === 1 ? "página tiene" : "páginas tienen"} el código «${digits}»` : "")
      : `${list.length} páginas${S.chapter ? ` de ${S.chapter}` : ""}`;
    $("#encGrid").innerHTML = list.length ? list.map(p => {
      const q = List.qtyOf(S.cat, p.n);
      return `<article class="enc-page">
        <button class="enc-page__img" type="button" data-view="${p.n}" aria-label="Ver página ${p.n} en grande"><img src="${esc(thumb(p))}" alt="Página ${p.n} del ${esc(catById(S.cat).title)}" width="1000" height="1000" loading="lazy" decoding="async"></button>
        <div class="enc-page__row"><span>Pág. ${p.n}${p.codes.length ? ` · Cód. ${esc(p.codes.slice(0, 2).join(", "))}` : ""}</span>${priceText(p) ? `<b>${priceText(p)}</b>` : ""}</div>
        ${orderable(p) ? `<button class="btn btn--sm ${q ? "" : "btn--line"} btn--block" type="button" data-add="${p.n}">${q ? `En tu encargo (${q})` : "Encargar"}</button>` : `<span class="enc-page__note">Portada de sección</span>`}
      </article>`;
    }).join("") : `<div class="empty"><h3>No encontramos ese código</h3><p class="muted">Revisa el número o búscalo en el otro catálogo. También puedes escribirnos por WhatsApp.</p><button class="btn" type="button" data-clearq>Ver todo el catálogo</button></div>`;
  }
  function renderCount() { const n = List.count(), c = $("#encCount"); c.textContent = n; c.dataset.n = n; }

  /* ---------- Visor ---------- */
  const V = { n: 1 };
  function openViewer(n) { V.n = n; renderViewer(); const d = $("#viewer"); if (!d.open) d.showModal(); }
  function viewerList() { return S.q.trim() ? visible() : PAGES[S.cat]; }
  function renderViewer() {
    const p = pageOf(S.cat, V.n), cat = catById(S.cat), list = viewerList(), i = list.findIndex(x => x.n === V.n);
    const q = List.qtyOf(S.cat, V.n);
    $("#vTitle").textContent = `${cat.title}, página ${p.n}`;
    $("#vSub").textContent = [chapterOf(S.cat, p.n), `${i + 1} de ${list.length}`].filter(Boolean).join(" · ");
    $("#vImg").src = p.img; $("#vImg").alt = `Página ${p.n} del ${cat.title}`;
    $("#vPrev").disabled = i <= 0; $("#vNext").disabled = i >= list.length - 1;
    $("#vPanel").innerHTML = `
      <div class="enc-viewer__info">${p.codes.length ? `<span>Cód. ${esc(p.codes.join(", "))}</span>` : ""}${priceText(p) ? `<b>${priceText(p)}</b>` : ""}</div>
      ${orderable(p) ? `<div class="fld enc-note"><label for="vNote">Color o detalle <span>(opcional)</span></label><input id="vNote" maxlength="80" placeholder="Ej. el modelo negro" enterkeyhint="done"></div>
      <button class="btn" type="button" data-vadd>${q ? `Añadir otra (${q} en tu encargo)` : "Encargar esta página"}</button>` : `<p class="muted">Esta página es una portada. Pasa a la siguiente para ver los modelos.</p>`}`;
  }
  function step(d) { const list = viewerList(), i = list.findIndex(x => x.n === V.n), t = list[i + d]; if (t) { V.n = t.n; renderViewer(); } }

  /* ---------- Lista ---------- */
  let sheetStep = 1;
  const LAST_KEY = "vesta-last-encargo";
  function lastEnc() {
    const o = store.get(LAST_KEY, null);
    if (!o || !Array.isArray(o.items) || !o.items.length || Date.now() - (o.at || 0) > 2 * 864e5) return null;
    return o.items.filter(i => i && catById(i.cat) && pageOf(i.cat, i.n));
  }
  function renderSheet() {
    renderCount();
    if (!List.items.length) {
      sheetStep = 1;
      const last = lastEnc();
      $("#encBody").innerHTML = `<div class="cart-empty"><h3>Tu encargo está vacío</h3><p class="muted">Abre un catálogo y toca «Encargar» en la página que te guste.</p><button class="btn" type="button" data-close>Ver catálogos</button>
        ${last ? `<button class="textlink" type="button" data-restore>Recuperar mi último encargo</button>` : ""}</div>`;
      $("#encFoot").hidden = true; return;
    }
    $("#encFoot").hidden = false;
    const n = List.count();
    if (sheetStep === 1) {
      $("#encSheetTitle").textContent = "Mi encargo";
      $("#encBody").innerHTML = List.items.map((it, k) => {
        const p = pageOf(it.cat, it.n), cat = catById(it.cat);
        return `<div class="line enc-line"><span class="enc-line__img"><img src="${esc(thumb(p))}" alt="" width="1000" height="1000" loading="lazy"></span>
          <div class="line__info">
            <div class="line__top"><b>${esc(cat.title.replace("Catálogo ", ""))}, pág. ${it.n}</b>${priceText(p) ? `<span class="price">${priceText(p)}</span>` : ""}</div>
            <span class="line__meta">${[chapterOf(it.cat, it.n), p.codes.length ? `Cód. ${p.codes.join(", ")}` : ""].filter(Boolean).join(" · ")}</span>
            <div class="fld enc-note"><label class="sr" for="note${k}">Color o detalle</label><input id="note${k}" data-note="${k}" maxlength="80" placeholder="Color o detalle (opcional)" value="${esc(it.note)}"></div>
            <div class="line__ctrl">
              <div class="qty" role="group" aria-label="Cantidad">
                <button type="button" data-q="-1" data-k="${k}" aria-label="Quitar una" ${it.qty <= 1 ? "disabled" : ""}><svg class="ico" viewBox="0 0 24 24"><path d="M6 12h12"/></svg></button>
                <output>${it.qty}</output>
                <button type="button" data-q="1" data-k="${k}" aria-label="Añadir una" ${it.qty >= 20 ? "disabled" : ""}><svg class="ico" viewBox="0 0 24 24"><path d="M6 12h12M12 6v12"/></svg></button>
              </div>
              <button class="rm" type="button" data-rm="${k}">Quitar</button>
            </div>
          </div></div>`;
      }).join("");
      $("#encFoot").innerHTML = `<div class="sum"><span>${n} ${n === 1 ? "pieza" : "piezas"} por encargo</span><span>Llega en ${esc(E.leadTime)}</span></div>
        <button class="btn btn--block" type="button" data-sstep="2">Continuar con mis datos</button>`;
      return;
    }
    const c = Customer.get();
    $("#encSheetTitle").textContent = "Tus datos";
    $("#encBody").innerHTML = `<button class="textlink back" type="button" data-sstep="1">Volver a mi encargo (${n} ${n === 1 ? "pieza" : "piezas"})</button>
      <form class="ship" id="encForm" novalidate>
        <p>Los usamos solo para preparar tu mensaje de WhatsApp.</p>
        <div class="fld"><label for="eName">Nombre</label><input id="eName" name="name" autocomplete="name" autocapitalize="words" enterkeyhint="next" value="${esc(c.name)}"><span class="err" id="eNameErr" hidden></span></div>
        <div class="fld"><label for="eCity">Ciudad</label><input id="eCity" name="city" autocomplete="address-level2" autocapitalize="words" enterkeyhint="done" value="${esc(c.city)}"><span class="err" id="eCityErr" hidden></span>
          <div class="chips">${CONFIG.cities.slice(0, 4).map(x => `<button type="button" class="chip" data-city="${esc(x)}" aria-pressed="${c.city === x}">${esc(x)}</button>`).join("")}</div></div>
      </form>`;
    $("#encFoot").innerHTML = `<a class="btn btn--block" id="encWa" target="_blank" rel="noopener" href="${waLink()}">${ICON_WA}Enviar encargo por WhatsApp</a>
      <p class="fine">Se abre WhatsApp con tu encargo escrito. Te confirmamos disponibilidad, precio y fecha de llegada antes de pedirlo a Tizza.</p>`;
  }
  function openSheet() { sheetStep = 1; renderSheet(); const d = $("#encSheet"); if (!d.open) d.showModal(); }
  function errors() {
    const c = Customer.get(), e = {};
    if (c.name.trim().length < 2) e.name = "Escribe tu nombre para saber a quién responder.";
    if (!c.city.trim()) e.city = "Indica tu ciudad para coordinar la entrega.";
    return e;
  }
  function showErrors(e) {
    [["name", "eName"], ["city", "eCity"]].forEach(([k, id]) => {
      const i = $("#" + id), m = $("#" + id + "Err"); if (!i) return;
      i.setAttribute("aria-invalid", e[k] ? "true" : "false"); m.hidden = !e[k]; m.textContent = e[k] || "";
    });
  }

  /* ---------- Avisos ---------- */
  let toastT, toastFn = null;
  function toast(msg, action) {
    $("#toastMsg").textContent = msg; toastFn = action ? action.fn : null;
    const b = $("#toastAct"); b.hidden = !action; if (action) b.textContent = action.label;
    const el = $("#toast");
    const host = [...document.querySelectorAll("dialog[open]")].pop() || document.body;   // visible también sobre el visor
    if (el.parentElement !== host) host.appendChild(el);
    el.classList.add("show"); clearTimeout(toastT); toastT = setTimeout(() => el.classList.remove("show"), action && action.long ? 7000 : 3400);
  }
  function added(n) {
    renderCount(); renderGrid();
    toast(`Página ${n} añadida a tu encargo.`, { label: "Ver encargo", fn: () => { if ($("#viewer").open) $("#viewer").close(); openSheet(); } });
  }

  /* ---------- Eventos ---------- */
  document.addEventListener("click", e => {
    const t = e.target.closest("button, a"); if (!t) return;
    const d = t.dataset;
    if ("close" in d) { const dl = t.closest("dialog"); if (dl) dl.close(); return; }
    if (d.cat) { S.cat = d.cat; S.chapter = ""; S.q = ""; $("#encQ").value = ""; $$(".enc-tab").forEach(b => b.setAttribute("aria-pressed", String(b.dataset.cat === S.cat))); renderChips(); renderGrid(); return; }
    if (d.ch !== undefined && t.classList.contains("chip") && t.closest("#encChips")) { S.chapter = d.ch; S.q = ""; $("#encQ").value = ""; renderChips(); renderGrid(); return; }
    if ("clearq" in d) { S.q = ""; $("#encQ").value = ""; renderGrid(); return; }
    if (d.view) { openViewer(Number(d.view)); return; }
    if (d.add) { List.add(S.cat, Number(d.add)); added(Number(d.add)); return; }
    if ("vadd" in d) { List.add(S.cat, V.n, ($("#vNote").value || "").trim()); renderViewer(); added(V.n); return; }
    if ("restore" in d) { const l = lastEnc(); if (l && l.length) { List.items = l; List.save(); store.set(LAST_KEY, null); renderSheet(); renderGrid(); } return; }
    if (d.sstep) { sheetStep = Number(d.sstep); renderSheet(); $("#encSheet .sheet__body").scrollTop = 0; return; }
    if (d.q && d.k !== undefined) { const it = List.items[Number(d.k)]; it.qty = Math.min(20, Math.max(1, it.qty + Number(d.q))); List.save(); renderSheet(); renderGrid(); return; }
    if (d.rm !== undefined) { List.items.splice(Number(d.rm), 1); List.save(); renderSheet(); renderGrid(); return; }
    if (d.city) { Customer.set("city", d.city); $("#eCity").value = d.city; $$("#encForm .chip").forEach(c => c.setAttribute("aria-pressed", String(c.dataset.city === d.city))); $("#encWa").href = waLink(); if ($("#encForm [aria-invalid=true]")) showErrors(errors()); return; }
    if (t.id === "encWa") {
      const er = errors();
      if (Object.keys(er).length) { e.preventDefault(); showErrors(er); $(er.name ? "#eName" : "#eCity").focus(); return; }
      t.href = waLink();
      const saved = List.items.map(i => ({ ...i }));
      store.set(LAST_KEY, { items: saved, at: Date.now() });
      setTimeout(() => {
        List.items = []; List.save(); renderSheet(); renderGrid(); $("#encSheet").close();
        toast("Abrimos WhatsApp con tu encargo. Tu lista quedó vacía.", { label: "Recuperar lista", long: true, fn: () => { List.items = saved; List.save(); renderCount(); renderGrid(); toast("Recuperamos tu lista."); } });
      }, 350);
    }
  });
  document.addEventListener("input", e => {
    const t = e.target;
    if (t.dataset.note !== undefined) { const it = List.items[Number(t.dataset.note)]; if (it) { it.note = t.value.slice(0, 80); List.save(); } }
    if (t.closest && t.closest("#encForm")) { Customer.set(t.name, t.value); const a = $("#encWa"); if (a) a.href = waLink(); if (t.getAttribute("aria-invalid") === "true") showErrors(errors()); }
  });
  document.addEventListener("keydown", e => {
    if ($("#viewer").open && (e.key === "ArrowLeft" || e.key === "ArrowRight") && e.target.tagName !== "INPUT") { e.preventDefault(); step(e.key === "ArrowLeft" ? -1 : 1); }
    if (e.key === "Enter" && e.target.closest && e.target.closest("#encForm")) { e.preventDefault(); const f = $$("#encForm input"), i = f.indexOf(e.target); if (f[i + 1]) f[i + 1].focus(); else e.target.blur(); }
  });
  $("#encQ").addEventListener("input", e => { S.q = e.target.value; if (S.q.trim()) S.chapter = ""; renderChips(); renderGrid(); });
  $("#encBtn").addEventListener("click", openSheet);
  $("#toastAct").addEventListener("click", () => { $("#toast").classList.remove("show"); const f = toastFn; toastFn = null; if (f) f(); });
  $("#vPrev").addEventListener("click", () => step(-1));
  $("#vNext").addEventListener("click", () => step(1));
  // Deslizar con el dedo en el visor
  let sx = null;
  $("#vStage").addEventListener("touchstart", e => { sx = e.touches[0].clientX; }, { passive: true });
  $("#vStage").addEventListener("touchend", e => { if (sx == null) return; const dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 50) step(dx < 0 ? 1 : -1); sx = null; });
  $$("dialog").forEach(dl => dl.addEventListener("click", e => { if (e.target === dl) dl.close(); }));
  const hdr = $("#header"); addEventListener("scroll", () => hdr.classList.toggle("is-scrolled", scrollY > 10), { passive: true });

  /* ---------- Inicio ---------- */
  if (CONFIG.palette) document.documentElement.dataset.palette = CONFIG.palette;
  List.load(); renderStatic(); renderChips(); renderGrid(); renderCount();
  window.VESTA_PEDIDOS = { List, message, S, PAGES };
})();
