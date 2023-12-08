const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
console.log("🔢 Tabla de multiplicar 🔢");
function main() {
  rl.question("Ingresa un numero entero:", (answer) => {
      if (answer === "" || answer === null || isNaN(parseInt(answer))) {
         console.log("Porfavor ingresa un numero entero:");
         return main()
      }
      operation(parseInt(answer))
  });
}

function operation(value = 0) {
  console.log(`La tabla de multiplicacion de ${value} es:`);
  const number = value;
  for (let index = 1; index <= 10; index++) {
    console.log(`${number} x ${index} = ${index * value}`);
  }
}

main();
