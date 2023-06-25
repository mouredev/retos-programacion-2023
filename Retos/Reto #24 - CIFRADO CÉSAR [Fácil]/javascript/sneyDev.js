/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */

function cifradoCesar(mensaje, desplazamiento) {
  let mensajeCifrado = "";

  for (let i = 0; i < mensaje.length; i++) {
    let letra = mensaje[i];

    if (letra.match(/[a-z]/i)) {
      let codigo = letra.charCodeAt(0);
      // SI ? CARACTERES ESTAN EN MAYÚSCULA ENTONCES
      if (letra.match(/[A-Z]/)) {
        // VALOR UNICODE PARA LETRAS MAYÚSCULAS ES DE A-Z 65-90 DEL ALFABETO EN INGLÉS
        codigo = ((codigo - 65 + desplazamiento) % 26) + 65;
      } else {
        // VALOR UNICODE PARA LETRAS MINÚSCULAS ES DE a-z 97-122 DEL ALFABETO EN INGLÉS
        codigo = ((codigo - 97 + desplazamiento) % 26) + 97;
      }
      // POR CADA ITERACIÓN CONCATENAR CADA LETRA CIFRADA AL MENSAJE
      mensajeCifrado += String.fromCharCode(codigo);
    } else {
      mensajeCifrado += letra;
    }
  }

  return mensajeCifrado;
}

function descifrarCesar(mensajeCifrado, desplazamiento) {
  // LLAMAR A FUNCION CIFRADOCESAR PASANDOLE EL MENSAJE CIFRADO Y RESTANDO 26(CANTIDAD DE LETRAS EN EL ALFABETO) - N(NUMERO DE DESPLAZAMIENTO)
  return cifradoCesar(mensajeCifrado, 26 - desplazamiento);
}

let mensajeOriginal = "Me gusta la pizza!";
console.log("Mensaje a cifrar:", mensajeOriginal);
let desplazamiento = 1;

let mensajeCifrado = cifradoCesar(mensajeOriginal, desplazamiento);
console.log("Mensaje cifrado:", mensajeCifrado);

let mensajeDescifrado = descifrarCesar(mensajeCifrado, desplazamiento);
console.log("Mensaje descifrado:", mensajeDescifrado);
