
/*
 * Como cada año, el día 256 se celebra el "Día de la Programación".
 * En nuestra comunidad siempre hacemos una gran fiesta donde repartirmos 
 * 256 regalos para seguir aprendiendo programación:
 * https://diadelaprogramacion.com
 *
 * Para seguir ayudando, te propongo este reto:
 * Mostrar la sintaxis de los principales elementos de un lenguaje
 * en TODOS los lenguajes de programación que podamos. ¿Llegaremos a 50?
 *
 * En un fichero, haz lo siguiente (si el lenguaje lo soporta),
 * y comenta cada bloque para identificar con qué se corresponde:
 * - Haz un "Hola, mundo!"
 * - Crea variables de tipo String, numéricas (enteras y decimales)
 *   y Booleanas (o cualquier tipo de dato primitivo).
 * - Crea una constante.
 * - Usa un if, else if y else.
 * - Crea estructuras como un array, lista, tupla, set y diccionario.
 * - Usa un for, foreach y un while.
 * - Crea diferentes funciones (con/sin parámetros y con/sin retorno).
 * - Crea una clase.
 * - Muestra el control de excepciones.
 *
 * Así, cualquier persona podrá consultar rápidamente diferentes ejemplos
 * de sintaxis básica de muchos lenguajes.
 *
 * ¡Muchas gracias!
 */

// 1.- Muestra en la consola el mensaje Hola, mundo!
console.log("Hola, mundo!");

// 2.-Crea variables de tipo String, numéricas (enteras y decimales)
let name="gio" //String
let age=28  //number
let precio=999.9 // number
let casado=false //boolean
let resumen={
    name:"gio",
    age:28,
    pet:true,
    salary:99.9

}
// 3.-Crea una constante.
const myName="Giovany Arturo Osorio Torres"

// 4.- Usa un if, else if y else.

if(soyDisciplinado){
    return "Puede alcanzar mis metas"
}else{
    return "Enfrentare dificultades en mi camino"
}

// 5. - Crea estructuras como un array, lista, tupla, set y diccionario.

const generosMusicales=["rock","punk","ska","reggae"];
const miTupla = ['manzana', 3, false];
let miSet = new Set([1, 2, 3, 4, 5]);
const myObject={
    clave1: 'valor1',
    clave2: 2,
    clave3: true
}
// 6.- Usa un for, foreach y un while.

for(let i=0;i<10;i++){
    return i
}
foreach((item)=>item.price*0.5)

while (age>18) {
    return "puede ir a los antros de tu ciudad"
}

// 7- Crea diferentes funciones (con/sin parámetros y con/sin retorno).

function suma(num1,num2){
    return num1+num2
}
function saludo(){
    return "hello world"
}

// 8-Crea una clase.

class Pet{
    constructor(breed){
      this.breed=breed
    }
  
  saludar(breed){
    return `hello world i am a ${breed}`
  }
}

const mascota1=new Pet()
mascota1.saludar("Cat")
mascota1.saludar("Dog")

// 9-  - Muestra el control de excepciones.

try{
    fetch("https://dog.ceo/api/breeds/list/all")
    .then(data=>data.json())
    .then(result=>console.log(result.message))
  
  }
  catch(e){
    console.log(e)
  }