const API_BASE = "http://localhost:8000/api"; // Beispiel-URL, anpassen an Backend

/**
 * Holt alle Produkte vom Backend
 * @returns {Promise<Array>}
 */
async function getProducts() {
  try {
    const res = await fetch(`${API_BASE}/products/`);
    if (!res.ok) throw new Error("Fehler beim Laden der Produkte");
    return await res.json();
  } catch (err) {
    console.error(err);
    alert("Produkte konnten nicht geladen werden.");
    return [];
  }
}

/**
 * Holt ein Produkt nach ID
 * @param {number} id 
 * @returns {Promise<Object>}
 */
async function getProductById(id) {
  try {
    const res = await fetch(`${API_BASE}/products/${id}/`);
    if (!res.ok) throw new Error("Produkt nicht gefunden");
    return await res.json();
  } catch (err) {
    console.error(err);
    alert("Produkt konnte nicht geladen werden.");
    return null;
  }
}