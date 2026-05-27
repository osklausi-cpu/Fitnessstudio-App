const btn = document.getElementById('clickMe');
const output = document.getElementById('output');

btn.addEventListener('click', () => {
  output.textContent = "Du hast den Button geklickt! 🎉";
});