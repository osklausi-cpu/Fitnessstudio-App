document.addEventListener("DOMContentLoaded", async () => {
  const grid = document.getElementById("product-grid");
  const products = await getProducts();

  products.forEach(product => {
    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = `
      <h2>${product.name}</h2>
      <p>${product.description || "Keine Beschreibung"}</p>
      <p>Preis: €${product.price}</p>
      <a href="product.html?id=${product.id}">Details ansehen</a>
    `;
    grid.appendChild(card);
  });
});