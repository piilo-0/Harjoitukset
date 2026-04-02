let participants = [];
let participantsamount = parseInt(prompt("How many participants:"));

for (let i = 0; i < participantsamount; i++) {
    let input = prompt("Enter Participant " + (i + 1) + " Name:");
    participants.push(input);
}

participants.sort((a, b) => a.localeCompare(b));

let list = document.getElementById("lista");

for (let i = 0; i < participants.length; i++) {
    let li = document.createElement("li");
    li.textContent = participants[i];
    list.appendChild(li);
}