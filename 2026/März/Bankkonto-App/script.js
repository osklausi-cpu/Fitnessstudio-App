let balance = 0;

const balanceEl = document.getElementById("balance");
const amountEl = document.getElementById("amount");
const depositBtn = document.getElementById("deposit");
const withdrawBtn = document.getElementById("withdraw");
const messageEl = document.getElementById("message");

depositBtn.addEventListener("click", () => {
    const amount = parseFloat(amountEl.value);
    if (amount > 0) {
        balance += amount;
        balanceEl.textContent = balance.toFixed(2);
        messageEl.textContent = `✅ ${amount.toFixed(2)} € eingezahlt`;
    } else {
        messageEl.textContent = "❌ Bitte einen gültigen Betrag eingeben";
    }
    amountEl.value = "";
});

withdrawBtn.addEventListener("click", () => {
    const amount = parseFloat(amountEl.value);
    if (amount > 0 && amount <= balance) {
        balance -= amount;
        balanceEl.textContent = balance.toFixed(2);
        messageEl.textContent = `✅ ${amount.toFixed(2)} € abgehoben`;
    } else if (amount > balance) {
        messageEl.textContent = "❌ Nicht genügend Guthaben";
    } else {
        messageEl.textContent = "❌ Bitte einen gültigen Betrag eingeben";
    }
    amountEl.value = "";
});