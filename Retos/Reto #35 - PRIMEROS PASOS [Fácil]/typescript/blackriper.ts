
/* hola mundo*/

// arrow funcion
const hello = () => console.log("Hello World")

// funcion tradicional
function Hello() {
  console.log("Hello World")
}

/* tipos de datos */
let numero: number = 10
let message: string = "Hola"
let send: boolean = false || true
let big: bigint = 100n;
let u: undefined = undefined;
let n: null = null;
let strictlyTyped: unknown = 4;
let looselyTyped: any = 4;

/* declaracion de variables*/

// constante 
const filename = "texto.txt"
// variable global 
var precio = 12.5
// variable local 
let tecnica = "Kaioken"

/* estructuras condicionales */
let warrior = "Goku"
if (warrior == "Goku") {
  console.log(`${warrior} uso el kamehame-ha`)
} else {
  console.log(`${warrior} uso vuelo`)
}

/* estructuras de datos*/
//array o list
let warriors = ["Goku", "Vegeta", "Kriin", "Gohan", "Picoro", "Trunks"]
// tupla 
let tecnicas: [string, number] = ["Kaioken", 20]
//set 
let villanos = new Set<string>(["Frezzer", "Cell", "MajinBoo"])

// object 
interface Warrior {
  name: string;
  race: string;
  age: number;
}

const goku: Warrior = {
  name: "SonGoku",
  race: "Sayan",
  age: 39
}

/* estructuras de repeticion*/

warriors.forEach((warrior) => console.log(warrior))

for (let index = 0; index < villanos.size; index++) {
  console.log(villanos[index])
}

let countdown = 10

while (countdown > 0) {
  console.log(countdown--)
}

/*funciones*/

function AttackWarrior(): string {
  return "Picoro utilizo el Makankossapo!!"
}

function Attack(name: string, tecnica: string) {
  console.log(`${name} utilizo el ${tecnica}`)
}

/* clases */
class Guerrero {
  private nombre: string;
  private ataque: string;

  constructor(nom: string, atk: string) {
    this.nombre = nom;
    this.ataque = atk;
  }

  Attack() {
    console.log(`${this.nombre} utilizo el ${this.ataque}`)
  }
}
// instanciar clase para crear un object warrior y acceder a sus metodos
let gotenks = new Guerrero("Gotenks", "Fantasmas Kamikaze!!")
gotenks.Attack()

// control de errores 
const cuentame_un_chiste = async () => {
  try {
    const res = await fetch("https://api.chucknorris.io/jokes/random")
    const data = await res.json()
    console.log(data.value)
  } catch (err) {
    console.log(err)
  }
}













