let noppienMaara = Number(prompt("Anna noppien määrä:"));
let haluttuSumma = Number(prompt("Anna silmälukujen summa:"));

let kierrokset = 10000;
let onnistumiset = 0;

for (let i = 0; i < kierrokset; i++) {
  let summa = 0;

  for (let j = 0; j < noppienMaara; j++) {
    let heitto = Math.floor(Math.random() * 6) + 1;
    summa += heitto;
  }

  if (summa === haluttuSumma) {
    onnistumiset++;
  }
}

let todennakoisyys = (onnistumiset / kierrokset) * 100;

document.getElementById("tulos").textContent =
  `Todennäköisyys saada summa ${haluttuSumma} ${noppienMaara} nopalla on ${todennakoisyys.toFixed(2)} %`;