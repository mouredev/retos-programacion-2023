/*
 * La última semana de 2021 comenzamos la actividad de retos de programación,
 * con la intención de resolver un ejercicio cada semana para mejorar
 * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
 *
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
 */
const abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

function reto_100(){
    let suma = 0

    let respuesta = prompt("Introduce una palabra: ")
    suma = contar_palabras(respuesta)
    console.log(respuesta+" suma "+suma)
    if(suma == 100){
        console.log("Enhorabuena, has introducido una palabra de 100 puntos")
    }
    else{
        console.log("La palabra no suma 100 puntos. Sigue intentadolo")
        reto_100()
    }    
}

function contar_palabras(respuesta){
    let aux = 0
    respuesta = respuesta.toUpperCase()
    for(let i= 0; i < respuesta.length; i++){
        aux += abecedario.indexOf(respuesta[i])+1
    }
    return aux
}

reto_100()