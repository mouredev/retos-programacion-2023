// Punto 1: Hola, mundo!
console.log("Hola, mundo!");

// Punto 2: Crea una variable de texto o string
const miTexto: string = "¡Hola desde TypeScript!";

// Punto 3: Crea una variable de número entero
const miEntero: number = 42;

// Punto 4: Crea una variable de número con decimales
const miDecimal: number = 3.14;

// Punto 5: Crea una variable de tipo booleano
const miBooleano: boolean = true;

// Punto 6: Crea una constante
const MI_CONSTANTE: number = 10;

// Punto 7: Usa un if, else if y else
if (miEntero > 50) {
  console.log("El número es mayor que 50");
} else if (miEntero < 50) {
  console.log("El número es menor que 50");
} else {
  console.log("El número es igual a 50");
}

// Punto 8: Crea un Array
const miArray: number[] = [1, 2, 3, 4, 5];

// Punto 9: Crea una lista (array en TypeScript)
const miLista: string[] = ["Manzana", "Banana", "Naranja"];

// Punto 10: Crea una tupla
const miTupla: [number, string, number] = [1, "dos", 3.14];

// Punto 11: Crea un set
const miSet: Set<string> = new Set(["Rojo", "Verde", "Azul"]);

// Punto 12: Crea un diccionario (objeto en TypeScript)
const miDiccionario: { [key: string]: string } = {
  clave1: "valor1",
  clave2: "valor2",
};

// Punto 13: Usa un ciclo for
for (const elemento of miArray) {
  console.log(elemento);
}

// Punto 14: Usa un ciclo foreach
for (const elemento of miLista) {
  console.log(elemento);
}

// Punto 15: Usa un ciclo while
let contador: number = 0;
while (contador < 3) {
  console.log(`Contador: ${contador}`);
  contador++;
}

// Punto 16: Crea una función sin parámetros que no retorne nada
function funcionSinParametros(): void {
  console.log("Función sin parámetros");
}
funcionSinParametros();

// Punto 17: Crea una función con parámetros que no retorne nada
function funcionConParametros(param1: number, param2: string): void {
  console.log(`Parámetro 1: ${param1}`);
  console.log(`Parámetro 2: ${param2}`);
}
funcionConParametros(1, "dos");

// Punto 18: Crea una función con parámetros que retorne valor
function funcionConRetorno(a: number, b: number): number {
  return a + b;
}
const resultado: number = funcionConRetorno(3, 4);
console.log(`Resultado: ${resultado}`);

// Punto 19: Crea una clase
class Persona {
  constructor(public nombre: string, public edad: number) {}
}
const persona: Persona = new Persona("Juan", 30);
console.log(`Nombre: ${persona.nombre}, Edad: ${persona.edad}`);

// Punto 20: Muestra control de excepciones (try-catch en TypeScript)
try {
  const division: number = miEntero / 0;
  console.log(`Resultado de la división: ${division}`);
} catch (error) {
  console.log(`Error: ${error}`);
}
