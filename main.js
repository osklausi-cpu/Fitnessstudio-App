const apiUrl = "https://jsonplaceholder.typicode.com/users";
const listGroup = document.getElementById("list-group");
users = [];

async function loadUsers() {
  const response = await fetch(apiUrl);
  return response.json();
}

function renderUsers() {
  users.forEach((element) => {
    let listItem = document.createElement("li");
    listItem.setAttribute("class", "list-item");
    listItem.innerHTML = `Mitglieder ID: ${element.id} Vorname: ${element.name} 
    <button class="btn btn-danger" onclick="deleteUser(${element.id})">Löschen</button> 
    <button class="btn btn-info" onclick="findUpdateUser(${element.id})">Bearbeiten</button>`;
    listGroup.appendChild(listItem);
  });
}

async function init() {
  users = await loadUsers();
  renderUsers();
}

function deleteUser(id) {
  if (confirm(`Willst du das Mitglied mit der ID ${id} wirklich löschen?`)) {
    const deletedUser = users.find((user) => user.id === id);
    users = users.filter((user) => user.id !== deletedUser.id);
    listGroup.innerHTML = "";
    renderUsers();
  }
}

function addMember(event) {
  event.preventDefault();
  const newNameInput = document.getElementById("new-name-input").value;
  const newMember = {
    id: users.length + 1,
    name: newNameInput,
  };
  users.push(newMember);
  listGroup.innerHTML = "";
  renderUsers();
  alert(`Das neue Mitglied ${newNameInput} wurde hinzugefügt`);
}

function findUpdateUser(id) {
  const updateSection = document.getElementById("update-section");
  updateSection.classList.remove("d-none");
  updateSection.classList.add("d-flex");

  user = users.find((user) => user.id === id);
  const userIdInput = document.getElementById("member-id");
  const userNameInput = document.getElementById("member-name");

  userIdInput.value = user.id;
  userNameInput.value = user.name;
}

function saveUpdateUser(event) {
  event.preventDefault();
  alert("Das Mitglied wurde erfolgreich aktualisiert");
  const updateSection = document.getElementById("update-section");
  updateSection.classList.remove("d-flex");
  updateSection.classList.add("d-none");

  const id = +document.getElementById("member-id").value;
  const updateUsername = document.getElementById("member-name").value;

  users = users.map((user) => {
    if (user.id === id) {
      return { ...users, name: updateUsername };
    }
    return users;
  });
  listGroup.innerHTML = "";
  renderUsers();
}

init();

 