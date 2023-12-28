const esPrimo = (n) => {
  if (n < 2) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}

const esFibonacci = (n) => {
  let a = 0, b = 1;
  while (b < n) {
    let c = a;
    a = b;
    b = a + c;
  }
  return b === n;
}

const esPar = (n) => {
  return n % 2 === 0;
}

const resultado = (n) => {
  const resultado = [];
  if (esPrimo(n)) {
    resultado.push("primo");
  }
  if (esFibonacci(n)) {
    resultado.push("fibonacci");
  }
  if (esPar(n)) {
    resultado.push("par");
  } else {
    resultado.push("impar");
  }
  return resultado;
}

const numero = parseInt(Math.floor(Math.random() * 100));
const resultados = resultado(numero);

if (resultados.includes("primo")) {
  console.log(numero + " es primo", end = ", ");
} else {
  console.log(numero + " no es primo", end = ", ");
}

if (resultados.includes("fibonacci")) {
  console.log("es fibonacci", end = ", ");
} else {
  console.log("no es fibonacci", end = ", ");
}

if (resultados.includes("par")) {
  console.log("es par.");
} else {
  console.log("es impar.");
}
