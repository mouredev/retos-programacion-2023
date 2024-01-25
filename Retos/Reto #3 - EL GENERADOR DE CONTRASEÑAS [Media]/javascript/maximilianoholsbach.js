/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

const crypto = require("crypto"); // Requerimos la libreria cypto para realizar las combinaciones

const valido = ["si", "no", 8, 9, 10, 11, 12, 13, 14, 15, 16]; // Colocamos en un array cuales seran los valores validos para el tratamiento de errores. Los valores numéricos se solicitan para establecer la cantidad de caracteres del password

// Generamos los distintos strings para las diferentes opciones de password

const ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
const completo =
  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+=<>?/";
const sNumero =
  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_-+=<>?/";
const sSimbolo =
  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

let tuPassword = ""; // Inicializamos un string vacio para poder concatenar los caracteres que nos ira entrgando Crypto

function newPass(data) {
  let mayuscula = data.mayuscula;
  let numero = data.numero || "si";
  let longitud = data.longitud || 12;
  let simbolo = data.simbolo || "si";
  try {
    if (
      !valido.includes(mayuscula) ||
      !valido.includes(numero) ||
      !valido.includes(longitud) ||
      !valido.includes(simbolo)
    ) {
      // Tratamiento de errores
      throw new Error(
        `Ingrese valores validos, los datos ingresados son: ${mayuscula}, ${numero}, ${longitud}, ${simbolo}`
      );
    }
    // Script de analisis de cada opción que pueda a llegar a requerir el usuario
    if (mayuscula == "si" && simbolo == "si" && numero == "si") {
      for (let i = 0; i < longitud; i++) {
        let index = crypto.randomInt(completo.length);
        let caracter = completo.charAt(index);
        tuPassword += caracter;
      }
      return tuPassword;
    } else if (mayuscula == "si" && simbolo == "si" && numero == "no") {
      for (let i = 0; i < longitud; i++) {
        let index = crypto.randomInt(sNumero.length);
        let caracter = sNumero.charAt(index);
        tuPassword += caracter;
      }
      return tuPassword;
    } else if (mayuscula == "si" && simbolo == "no" && numero == "si") {
      for (let i = 0; i < longitud; i++) {
        let index = crypto.randomInt(sSimbolo.length);
        let caracter = sSimbolo.charAt(index);
        tuPassword += caracter;
      }
      return tuPassword;
    } else if (mayuscula == "si" && simbolo == "no" && numero == "no") {
      for (let i = 0; i < longitud; i++) {
        let index = crypto.randomInt(ABC.length);
        let caracter = ABC.charAt(index);
        tuPassword += caracter;
      }
      return tuPassword;
    } else if (mayuscula == "no" && simbolo == "si" && numero == "si") {
      for (let i = 0; i < longitud; i++) {
        let index = crypto.randomInt(completo.length);
        let caracter = completo.charAt(index);
        tuPassword += caracter.toLocaleLowerCase();
      }
      return tuPassword;
    } else if (mayuscula == "no" && simbolo == "si" && numero == "no") {
      for (let i = 0; i < longitud; i++) {
        let index = crypto.randomInt(sNumero.length);
        let caracter = sNumero.charAt(index);
        tuPassword += caracter.toLocaleLowerCase();
      }
      return tuPassword;
    } else if (mayuscula == "no" && simbolo == "no" && numero == "si") {
      for (let i = 0; i < longitud; i++) {
        let index = crypto.randomInt(sSimbolo.length);
        let caracter = sSimbolo.charAt(index);
        tuPassword += caracter.toLocaleLowerCase();
      }
      return tuPassword;
    } else if (mayuscula == "no" && simbolo == "no" && numero == "no") {
      for (let i = 0; i < longitud; i++) {
        let index = crypto.randomInt(ABC.length);
        let caracter = ABC.charAt(index);
        tuPassword += caracter.toLocaleLowerCase();
      }
      return tuPassword;
    }
  } catch (error) {
    return error.message;
  }
  //console.log(`Los datos son: ${mayuscula}, ${numero}, ${longitud}, ${simbolo}`);
}

/** TABLA DE VERDAD CON LA QUE SE PROBARON 
 * LAS OPCIONES DE CONTRASEÑA
  | Mayúscula | Símbolo | Número | 
|-------------|---------|--------|
|  Verdadero | Verdadero| Verdadero
|  Verdadero | Verdadero| Falso   |
|  Verdadero |  Falso   | Verdadero
|  Verdadero |  Falso   | Falso   |
|   Falso   | Verdadero | Verdadero
|   Falso   | Verdadero | Falso   |
|   Falso   |   Falso   | Verdadero
|   Falso   |   Falso   | Falso   |

 */

console.log(
  newPass({ mayuscula: "no", numero: "no", longitud: 16, simbolo: "no" })
);
