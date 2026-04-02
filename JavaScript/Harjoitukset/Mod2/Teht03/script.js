let dogs = [];

for (let i = 0; i < 6; i++) {
    let input = prompt("Enter Dog Number " + (i + 1) + " Name:");
    dogs.push(input);
}

dogs.sort((a, b) => b.localeCompare(a));

let list = document.getElementById("lista");

for (let i = 0; i < dogs.length; i++) {
    let li = document.createElement("li");
    li.textContent = dogs[i];
    list.appendChild(li);
}