// Pruebas del bot (sin conexión a Meta): node bot-whatsapp/test.mjs
import { readFileSync } from "node:fs";
import { createHmac } from "node:crypto";
import assert from "node:assert/strict";
import test from "node:test";

const src = readFileSync(new URL("./worker.js", import.meta.url), "utf8")
  + "\nexport { CONFIG, intentOf, reply, isOpen };\n";
const W = await import("data:text/javascript;base64," + Buffer.from(src).toString("base64"));
const bot = W.default;
const env = { WHATSAPP_TOKEN: "tok", VERIFY_TOKEN: "vesta123", APP_SECRET: "secreto" };
const at = h => new Date(Date.UTC(2026, 9, 25, (h + 4) % 24));   // hora de Bolivia → UTC

test("intenciones por palabra clave", () => {
  const cases = {
    "Hola": "menu", "¿Cuánto cuesta la cartera Mafalda?": "precio", "hacen envíos a Santa Cruz?": "envios",
    "se puede pagar con QR": "pagos", "son originales?": "original", "quiero hablar con una persona": "equipo",
    "puedo encargar algo del catálogo": "encargo", "pedidos a una semana": "encargo", "aceptan cambios?": "devolucion",
    "tienen mochilas de Stitch": "catalogo", "muchas gracias": "gracias", "formas de pagos": "pagos", "tienen billeteras?": "catalogo", "asdfgh": "noEntiendo", "": "menu"
  };
  for (const [t, want] of Object.entries(cases)) assert.equal(W.intentOf(t), want, t);
});

test("horario de Bolivia", () => {
  assert.equal(W.isOpen(at(9)), true); assert.equal(W.isOpen(at(18)), true);
  assert.equal(W.isOpen(at(19)), false); assert.equal(W.isOpen(at(3)), false);
});

test("respuestas y límites de WhatsApp", () => {
  const menu = W.reply({ type: "text", text: { body: "hola" } })[0];
  assert.equal(menu.interactive.type, "list");
  const rows = menu.interactive.action.sections[0].rows;
  assert.ok(rows.length <= 10);
  for (const r of rows) { assert.ok(r.title.length <= 24, r.title); assert.ok(r.description.length <= 72); }
  for (const b of W.CONFIG.buttons) assert.ok(b.title.length <= 20, b.title);
  for (const [k, v] of Object.entries(W.CONFIG.answers)) assert.ok(v.length <= 1024, k);

  const env1 = W.reply({ type: "interactive", interactive: { type: "list_reply", list_reply: { id: "envios" } } })[0];
  assert.match(env1.interactive.body.text, /flota/);
  const eq = W.reply({ type: "text", text: { body: "quiero hablar con alguien" } }, at(10))[0];
  assert.match(eq.text.body, /wa\.me\/59176705942/); assert.doesNotMatch(eq.text.body, /fuera de horario/);
  const late = W.reply({ type: "image", image: {} }, at(22))[0];
  assert.match(late.text.body, /fuera de horario/);
  assert.equal(W.reply({ type: "audio" })[0].interactive.type, "list");
});

test("webhook: verificación, firma y envío", async () => {
  const ok = await bot.fetch(new Request("https://x/?hub.mode=subscribe&hub.verify_token=vesta123&hub.challenge=42"), env, {});
  assert.equal(await ok.text(), "42");
  const bad = await bot.fetch(new Request("https://x/?hub.mode=subscribe&hub.verify_token=otro&hub.challenge=42"), env, {});
  assert.equal(bad.status, 403);

  const body = JSON.stringify({ entry: [{ changes: [{ value: { metadata: { phone_number_id: "123" },
    messages: [{ from: "59170000000", type: "text", text: { body: "¿hacen delivery?" } }] } }] }] });
  const sig = "sha256=" + createHmac("sha256", "secreto").update(body).digest("hex");
  const sent = []; const realFetch = globalThis.fetch;
  globalThis.fetch = async (u, o) => { sent.push({ u, o }); return new Response("{}"); };
  const waits = []; const ctx = { waitUntil: p => waits.push(p) };
  try {
    const forged = await bot.fetch(new Request("https://x/", { method: "POST", body, headers: { "x-hub-signature-256": "sha256=00" } }), env, ctx);
    assert.equal(forged.status, 401);
    const r = await bot.fetch(new Request("https://x/", { method: "POST", body, headers: { "x-hub-signature-256": sig } }), env, ctx);
    assert.equal(r.status, 200); await Promise.all(waits);
  } finally { globalThis.fetch = realFetch; }
  assert.equal(sent.length, 1);
  assert.match(sent[0].u, /graph\.facebook\.com\/v\d+\.\d+\/123\/messages/);
  const p = JSON.parse(sent[0].o.body);
  assert.equal(p.to, "59170000000"); assert.equal(p.messaging_product, "whatsapp");
  assert.equal(sent[0].o.headers.Authorization, "Bearer tok");
});
