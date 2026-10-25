/* =========================================================
   VESTA BAGS — CATÁLOGO
   Productos de Tizza (tizza.pe) que VESTA importa a Bolivia.
   ⚠ Las FOTOS son de referencia y se cargan desde la web de Tizza.
     Reemplázalas por tus propias fotos cuando llegue la mercadería
     (ponlas en assets/products/ y cambia las rutas).
   ⚠ Los PRECIOS en Bs están pendientes: price: null = "Precio por consultar".
     refPEN es solo una nota interna con el precio de Tizza en soles; NO se muestra.
   - availability: "available" | "soldout" | "unknown"
   - stock: entero (límite de cantidad) o null
   ========================================================= */
window.VESTA_COLORS = {
  negro:   { label: "Negro",   hex: "#151515" },
  rosado:  { label: "Rosado",  hex: "#E7B3C1" },
  celeste: { label: "Celeste", hex: "#A8CDE6" },
  azul:    { label: "Azul",    hex: "#2E4A78" },
  dorado:  { label: "Dorado",  hex: "#C9A65A" },
  hueso:   { label: "Hueso",   hex: "#ECE4D3" },
  verde:   { label: "Verde",   hex: "#5D7A56" },
  unico:   { label: "Único",   hex: "#8E8E8E" }
};

/* Colecciones (como en Tizza). Las que no tienen productos no se muestran. */
window.VESTA_COLLECTIONS = [
  { id: "mafalda",     label: "Mafalda",     note: "Colaboración oficial Tizza x Mafalda." },
  { id: "garfield",    label: "Garfield",    note: "Colaboración oficial Tizza x Garfield." },
  { id: "hello-kitty", label: "Hello Kitty", note: "Colección Hello Kitty & Friends." },
  { id: "stitch",      label: "Stitch",      note: "Colección Disney Stitch." },
  { id: "snoopy",      label: "Snoopy",      note: "" },
  { id: "princesas",   label: "Princesas",   note: "" },
  { id: "toy-story",   label: "Toy Story",   note: "" }
];

/* Tipos de producto */
window.VESTA_CATEGORIES = [
  { id: "carteras",   label: "Carteras" },
  { id: "morrales",   label: "Morrales" },
  { id: "mochilas",   label: "Mochilas" },
  { id: "billeteras", label: "Billeteras" },
  { id: "maletas",    label: "Maletas" },
  { id: "accesorios", label: "Accesorios" }
];

(function () {
  const CDN = "https://cdn.shopify.com/s/files/1/0735/2804/9803/files/";
  // Fotos de referencia Tizza: varias opciones por color; la web salta a la siguiente si una falla.
  const tz = (...files) => files.map(f => CDN + f);
  const item = o => ({ price: null, compareAtPrice: null, availability: "unknown", stock: null, features: [], tags: [],
    active: true, featured: false, isNew: false, description: "", ...o });

  window.VESTA_CATALOG = [
    /* ---------- MAFALDA ---------- */
    item({ id: "maf-2128", slug: "cartera-mafalda-2128", name: "Cartera Mafalda 2128", collection: "mafalda", category: "carteras",
      colors: ["rosado", "celeste"], refPEN: 229, featured: true, isNew: true,
      images: {
        rosado: tz("2128-2074464-1_76a65f87-f2cb-4650-97a3-60a86ef70144.jpg", "2128-2074464-2.jpg", "2128-2074464-3.jpg", "2128-2074464-4.jpg", "2128-2074464-5.jpg"),
        celeste: tz("2128-2074463-1_681eff5f-813d-4334-b322-736deab51db0.jpg", "2128-2074463-2.jpg", "2128-2074463-3.jpg", "2128-2074463-4.jpg", "2128-2074463-5.jpg") } }),
    item({ id: "maf-2122", slug: "cartera-mafalda-2122", name: "Cartera Mafalda 2122", collection: "mafalda", category: "carteras",
      colors: ["dorado", "celeste"], refPEN: 239, featured: true, isNew: true,
      images: {
        dorado: tz("2122-2074454-1_8f622ce4-8b27-4782-85e5-853205838ed9.jpg", "2122-2074454-2.jpg", "2122-2074454-3.jpg", "2122-2074454-4.jpg", "2122-2074454-5.jpg"),
        celeste: tz("2122-2074455-1_21a0b3a0-98d8-48f5-8afb-8467e1a84e92.jpg", "2122-2074455-2.jpg", "2122-2074455-3.jpg", "2122-2074455-4.jpg", "2122-2074455-5.jpg") } }),
    item({ id: "maf-2125", slug: "cartera-mafalda-2125", name: "Cartera Mafalda 2125", collection: "mafalda", category: "carteras",
      colors: ["azul"], refPEN: 229, isNew: true,
      images: { azul: tz("2125-2074460-1_30827ee6-514e-48a3-a855-57f43c7e29eb.jpg", "2125-2074460-2.jpg", "2125-2074460-3.jpg") } }),
    item({ id: "maf-2132", slug: "morral-mafalda-2132", name: "Morral Mafalda 2132", collection: "mafalda", category: "morrales",
      colors: ["negro"], refPEN: 199,
      images: { negro: tz("2132-2074470-1_f6e85275-ce9a-4e75-8a3b-155f0b3bba52.jpg", "2132-2074470-2.jpg", "2132-2074470-3.jpg", "2132-2074470-4.jpg") } }),
    item({ id: "maf-2129", slug: "morral-mafalda-2129", name: "Morral Mafalda 2129", collection: "mafalda", category: "morrales",
      colors: ["rosado", "celeste"], refPEN: 199,
      images: {
        rosado: tz("2129-2074466-1_4fdab3ab-d625-46e4-b0f1-4b18cd453aaa.jpg", "2129-2074466-2.jpg", "2129-2074466-3.jpg", "2129-2074466-4.jpg"),
        celeste: tz("2129-2074465-1_63bef3ae-6df6-4672-b426-ee34ab7b65f4.jpg", "2129-2074465-2.jpg", "2129-2074465-3.jpg", "2129-2074465-4.jpg") } }),
    item({ id: "maf-2126", slug: "morral-mafalda-2126", name: "Morral Mafalda 2126", collection: "mafalda", category: "morrales",
      colors: ["azul"], refPEN: 189,
      images: { azul: tz("2126-2074461-1_cc400d7d-7d23-447e-a057-a2d5d3b2232d.jpg", "2126-2074461-2.jpg", "2126-2074461-3.jpg", "2126-2074461-4.jpg", "2126-2074461-5.jpg") } }),
    item({ id: "maf-2123", slug: "morral-mafalda-2123", name: "Morral Mafalda 2123", collection: "mafalda", category: "morrales",
      colors: ["dorado", "celeste"], refPEN: 229,
      images: {
        dorado: tz("2123-2074456-1_04c4c3c3-15f7-4d6a-bb92-8bc0315337e0.jpg", "2123-2074456-2.jpg", "2123-2074456-3.jpg", "2123-2074456-4.jpg", "2123-2074456-5.jpg"),
        celeste: tz("2123-2074457-1_270fc7d4-ced4-40a2-879b-f34641027289.jpg", "2123-2074457-2.jpg", "2123-2074457-3.jpg", "2123-2074457-4.jpg") } }),
    item({ id: "maf-2131", slug: "mochila-mafalda-2131", name: "Mochila Mafalda 2131", collection: "mafalda", category: "mochilas",
      colors: ["negro"], refPEN: 229,
      images: { negro: tz("2131-2074469-1_a7a6a456-4dce-4d7a-a1ac-6eb2a0f200d4.jpg", "2131-2074469-2.jpg", "2131-2074469-3.jpg", "2131-2074469-4.jpg") } }),
    item({ id: "maf-2121", slug: "mochila-mafalda-2121", name: "Mochila Mafalda 2121", collection: "mafalda", category: "mochilas",
      colors: ["dorado", "celeste"], refPEN: 229,
      images: {
        dorado: tz("2121-2074452-1_10b78e4a-468e-4488-8a1c-ebe6f2e2ec11.jpg", "2121-2074452-2.jpg", "2121-2074452-3.jpg"),
        celeste: tz("2121-2074453-1_c9c71343-c270-4559-a8d7-d313b9fa8306.jpg", "2121-2074453-2.jpg") } }),
    item({ id: "maf-2133", slug: "billetera-mafalda-2133", name: "Billetera Mafalda 2133", collection: "mafalda", category: "billeteras",
      colors: ["negro"], refPEN: 139,
      images: { negro: tz("2133-2074471-1_ee0c6f05-cf43-461b-86c6-f86e4cb162b4.jpg", "2133-2074471-2.jpg", "2133-2074471-3.jpg") } }),
    item({ id: "maf-2130", slug: "billetera-mafalda-2130", name: "Billetera Mafalda 2130", collection: "mafalda", category: "billeteras",
      colors: ["rosado", "celeste"], refPEN: 99,
      images: {
        rosado: tz("2130-2074468-1_ed67034e-2ba5-466a-aa9f-477509c38584.jpg", "2130-2074468-2.jpg", "2130-2074468-3.jpg"),
        celeste: tz("2130-2074467-1_dea1e9f2-b077-402a-8fab-768abfa7d330.jpg", "2130-2074467-2.jpg", "2130-2074467-3.jpg") } }),
    item({ id: "maf-2124", slug: "billetera-mafalda-2124", name: "Billetera Mafalda 2124", collection: "mafalda", category: "billeteras",
      colors: ["dorado", "celeste"], refPEN: 139,
      images: {
        dorado: tz("2124-2074458-1_a3ff1365-bf47-4c16-bdbe-57682986cab3.jpg", "2124-2074458-2.jpg", "2124-2074458-3.jpg", "2124-2074458-4.jpg"),
        celeste: tz("2124-2074459-1_4cd6a313-7993-4923-b85c-d5221c452641.jpg", "2124-2074459-2.jpg", "2124-2074459-3.jpg", "2124-2074459-4.jpg", "2124-2074459-5.jpg") } }),
    item({ id: "maf-2127", slug: "portacelular-mafalda-2127", name: "Portacelular Mafalda 2127", collection: "mafalda", category: "accesorios",
      colors: ["azul"], refPEN: 149,
      images: { azul: tz("2127-2074462-1_528dbf55-a994-4daa-8836-60d91fa51dac.jpg", "2127-2074462-2.jpg", "2127-2074462-3.jpg", "2127-2074462-4.jpg", "2127-2074462-5.jpg") } }),

    /* ---------- GARFIELD ---------- */
    item({ id: "gar-2141", slug: "cartera-garfield-2141", name: "Cartera Garfield 2141", collection: "garfield", category: "carteras",
      colors: ["negro", "verde"], featured: true,
      images: {
        negro: tz("2141-2074490-1_2825efde-a0b5-4445-bb99-f2231d26c91b.jpg", "2141-2074490-2.jpg", "2141-2074490-3.jpg", "2141-2074490-4.jpg", "2141-2074490-5.jpg"),
        verde: tz("2141-2074489-1_daf30784-7035-4c3b-8dd8-e9ee8e71b1a5.jpg", "2141-2074489-2.jpg", "2141-2074489-3.jpg", "2141-2074489-4.jpg", "2141-2074489-5.jpg") } }),
    item({ id: "gar-2144", slug: "cartera-garfield-2144", name: "Cartera Garfield 2144", collection: "garfield", category: "carteras",
      colors: ["hueso"],
      images: { hueso: tz("2144-2074494-1_5fd2cab7-7628-4c6c-b05e-2ca0570716fd.jpg", "2144-2074494-2.jpg", "2144-2074494-3.jpg", "2144-2074494-4.jpg") } }),
    item({ id: "gar-2145", slug: "morral-garfield-2145", name: "Morral Garfield 2145", collection: "garfield", category: "morrales",
      colors: ["hueso"],
      images: { hueso: tz("2145-2074495-1_8594f333-b09f-40ac-8da2-0026916b7e58.jpg", "2145-2074495-2.jpg", "2145-2074495-3.jpg", "2145-2074495-4.jpg", "2145-2074495-5.jpg") } }),
    item({ id: "gar-2143", slug: "mochila-garfield-2143", name: "Mochila Garfield 2143", collection: "garfield", category: "mochilas",
      colors: ["hueso"],
      images: { hueso: tz("2143-2074493-1_7437ad6e-83a5-44a8-97e8-4033f06e3f25.jpg", "2143-2074493-2.jpg", "2143-2074493-3.jpg", "2143-2074493-4.jpg") } }),
    item({ id: "gar-2142", slug: "billetera-garfield-2142", name: "Billetera Garfield 2142", collection: "garfield", category: "billeteras",
      colors: ["negro", "verde"],
      images: {
        negro: tz("2142-2074492-1_d013db63-c0e4-4014-a45d-04029d211c19.jpg", "2142-2074492-2.jpg", "2142-2074492-3.jpg", "2142-2074492-4.jpg"),
        verde: tz("2142-2074491-1_61aa3e69-b169-473b-9afd-9526036f4ade.jpg", "2142-2074491-2.jpg", "2142-2074491-3.jpg", "2142-2074491-4.jpg") } }),
    item({ id: "gar-2146", slug: "billetera-garfield-2146", name: "Billetera Garfield 2146", collection: "garfield", category: "billeteras",
      colors: ["hueso"],
      images: { hueso: tz("2146-2074496-1_15b2056b-d17f-4b2c-946a-a526f10bc6ea.jpg", "2146-2074496-2.jpg", "2146-2074496-3.jpg") } }),

    /* ---------- HELLO KITTY ---------- */
    item({ id: "hk-2056", slug: "cartera-hello-kitty-2056", name: "Cartera Hello Kitty & Friends 2056", collection: "hello-kitty", category: "carteras",
      colors: ["rosado"], featured: true,
      images: { rosado: tz("2056-2073912_2da55830-6568-448d-a02f-4800db59ac63.jpg", "2056-2073912-2_e726f49d-7e2b-46e8-a291-9e0d50a6cd52.jpg", "2056-2073912-3_5980b8d8-3007-418c-95c9-4723bdec5be9.jpg", "2056-2073912-4_7e0261a8-6867-4c3e-9a43-35d1ed6eca0f.jpg") } }),
    item({ id: "hk-2057", slug: "billetera-hello-kitty-2057", name: "Billetera Hello Kitty & Friends 2057", collection: "hello-kitty", category: "billeteras",
      colors: ["rosado"],
      images: { rosado: tz("2057-2073913.jpg", "2057-2073913-2_90ca7fdb-1142-47b4-96e7-af321bf91b6b.jpg", "2057-2073913-3_c2262b1d-af57-4e32-8199-27782fc69eaa.jpg") } }),

    /* ---------- STITCH ---------- */
    item({ id: "st-2100", slug: "mochila-stitch-2100", name: "Mochila Stitch 2100", collection: "stitch", category: "mochilas",
      colors: ["unico"],
      images: { unico: tz("2100-2073988-1_246d9ec9-9aca-4155-b09e-5ebab538f1af.jpg", "2100-2073988-2.jpg", "2100-2073988-3.jpg") } })
  ];
})();
