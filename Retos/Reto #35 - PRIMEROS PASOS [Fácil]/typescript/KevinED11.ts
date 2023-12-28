// hello world
console.log("hello world");

// Variables
let name2: string = "kevin asael";
let age2: number = 22;
let money: number = 1.0;

// Constants
const pi: number = 3.1416;

// Conditionals
if (age2 >= 18) {
  console.log("eres mayor de edad");
} else {
  console.log("no eres mayor de edad");
}

if (name2 == "kevin") {
  console.log("eres kevin");
} else if (name2 == "kevin asael") {
  console.log("eres kevin asael");
}

// Structures
let names4: string[] = ["kevin", "juan", "dario", "julian"];
let personInformation: [string, number] = ["kevin", 22];
let values: Set<string> = new Set(["kevin", "kevin"]);
let newValues: Map<string, number> = new Map<string, number>([["kevin", 22]]);

// Loops
for (let name of names4) console.log(name);
names4.forEach((name) => console.log(name));

let counter = 1;
while (counter <= 10) {
  console.log(counter);
  counter++;
}

// Functions
function greet(): void {
  console.log("hello kevin");
}

const greet2 = (name: string): void => console.log(`hello ${name}`);

// Class
class Person {
  constructor(public name: string, public age: number) {}
}

const kevincin = new Person("kevin", 22);

// Exceptions
const raiseException = (): never => {
  throw new Error("prueba de lanzamiento de error");
};

try {
  raiseException();
} catch (err) {
  console.log(err);
}
