let numbers = [];
while (true) {
    input = parseInt(prompt("Give number (existing number stops):"));

    if (numbers.includes(input)) {
        break;
    }

    numbers.push(input);
}

numbers.sort((a, b) => a - b);

console.log("Numbers in ascending order:");
for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}