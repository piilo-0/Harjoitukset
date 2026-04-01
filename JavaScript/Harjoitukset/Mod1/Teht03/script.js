let numero1 = parseInt(prompt("Anna Numero 1"))
let numero2 = parseInt(prompt("Anna Numero 2"))
let numero3 = parseInt(prompt("Anna Numero 3"))


document.getElementById("summa").textContent = "Summa: " + (numero1 + numero2 + numero3)
document.getElementById("tulo").textContent = "Tulo: " + numero1 * numero2 * numero3
document.getElementById("keskiarvo").textContent = "Keskiarvo: " + ((numero1 + numero2 + numero3) / 3)