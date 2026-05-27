const memberInput = document.getElementById("memberInput");
const memberList = document.getElementById("memberList");

const members = [];

document.getElementById("addButton").addEventListener("click", function() {
  const name = memberInput.value;
  if (name === "") return alert("Bitte einen Namen eingeben!");
  
  members.push(name);

  memberList.innerHTML = "";
  members.forEach((member) => {
    const li = document.createElement("li");
    li.textContent = member;
    memberList.appendChild(li);
  });

  memberInput.value = "";
});

