let numbers = [];
let input = 1;

while (input !== 0) {
    input = parseInt(prompt("Give number (0 stops):"));
    
    if (input !== 0) {
        numbers.push(input);
    }
}

numbers.sort((a, b) => b - a);

console.log("Numbers from largest to smallest:");
for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}