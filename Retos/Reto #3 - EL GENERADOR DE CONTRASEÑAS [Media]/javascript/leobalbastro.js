/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

/*
  Esto es un texto mas que nada para informar sobre fortalezas de contraseña y el por qué debe importarnos como programador el hecho de que se manejen
  fuertes contraseñas en lugar de unas debiles, si no te interesa el tema puedes ver directamente el algoritmo debajo que es mi solucion.
  
  Antes que nada debo definir los estandares de una contraseña y sus fortaleza o debilidad. Primero que nada necesitamos una contraseña para que no se 
  pueda "hackear" o mejor dicho que nos la puedan robar, para esto hay un estandar y se dice que una contraseña es fuerte cuando tiene letras minusculas,
  mayusculas, simbolos y numeros, además de longitud (cuan larga es la contraseña).
  Una contraseña debil tiende a serla por ser un dato personal, y aunque todos pensemos que estamos a salvo o que nuestros datos no son relevantes para
  las personas les invito a ver este video: https://www.youtube.com/watch?v=NPE7i8wuupk.
  normalmente una contraseña debil se compone de letras y numeros, mientras mas simbolos y variedad de letras agreguemos, mas dificil se hace de averiguar
  la contraseña.
  
  En orden de mas a menos debil:
  jose -> lo mas debil color: rojo
  pedro12 -> no tan debil color: naranja oscuro
  miguel1984 -> contraseñas estandar, nombres y apellidos con una fecha normalmente de nacimiento. color: naranja
  manu8405!! -> comienzo de contraseña fuerte , se puede mejorar, color: amarillo
  Jose#Pica#La#Piedrita#190525 -> esto deberia de ser una contraseña fuerte, color: verde
  
  Este algoritmo se penso para poder generar tanto la mas baja de ellas (aunque no con un significado particular) como la mas fuerte.  
*/

function randomPassword(long, mayus, num, sim) {
  let abc = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" "); //Array de caracteres de la A a la Z en minusculas
  let numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]; //Array de numeros
  let sym = [   //Array de simbolos
    "|",
    "#",
    "@",
    "~",
    "€",
    "¬",
    "/",
    "(",
    ")",
    "!",
    "·",
    "$",
    "%",
    "&",
  ];

  let generatedPass = ""; //Nuestra cadena de contraseña que luego vamos a mostrarsela al usuario

  for (let index = 0; index < long; index++) { //En este bloque de codigo hacemos un bucle para que genere los caracteres uno por uno dependiendo de las caracteristicas
    try {                                      //que le hayamos agregado cuando llamamos la funcion.
      if (long > 7 && long < 17) { // si la longitud ingresada es mayor a 7 o menor a 17 
        let randomizerString = Math.floor(Math.random() * 26); //generador de un caracter en minuscula
        let randomizerStringMayus = Math.floor(Math.random() * 26); //generador de un caracter en mayusculas
        let randomizerNum = Math.floor(Math.random() * 10); //generador de un caracter en formato numero del 0-9
        let randomizerSym = Math.floor(Math.random() * 14); //generador de un caracter simbolico
        generatedPass += abc[randomizerString]; //por defecto agregamos una letra minuscula ya que es lo mas bajo y lo unico que no le pedimos al usuario por parametro
        if (mayus && generatedPass.length < long) { //si el parametro "mayus" es true, y la longitud de la contraseña generada es menor a la longitud declarada
          generatedPass += abc[randomizerStringMayus].toUpperCase(); //agregar a la cadena de texto de la contraseña una letra random en mayuscula
          index += 1; //subir el indice en 1 porque agregamos un caracter
        }
        if (num && generatedPass.length < long) { //si el parametro "num" es true, y la longitud de la contraseña generada es menor a la longitud declarada
          generatedPass += numList[randomizerNum]; // agregamos un numero del 0-9 al string de la contraseña
          index += 1; //volvemos a subir el indice en 1.
        }
        if (sim && generatedPass.length < long) { //si el parametro "sim" es true, y la longitud de la contraseña generada es menor a la longitud declarada
          generatedPass += sym[randomizerSym]; //agregamos un simbolo de la lista de sym.
          index += 1; //volvemos a aumentar en 1 el index.
        }
      } else { //si el numero de long ingresado esta por fuera del if anterior entonces tiramos un error
        throw new Error(
          "La longitud ingresada no es correcta, debes ingresar una longitud entre 8 y 16 digitos"
        );
      }
    } catch (error) {
      console.log(error.message); //manejamos el error que lanzamos anteriormente dando información especifica al usuario
      break;
    }
    
    if (generatedPass.length===long) console.log(`tu password Generada es: ${generatedPass}`); // solo mostrara la contraseña generada si se hizo la password.
  }
}

randomPassword(15, true, true, true);
