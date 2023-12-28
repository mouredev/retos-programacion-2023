/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */

//Inicialización de los puntos de juego
const pointsTable = {
  0: "Love", 1: "15", 2: "30", 3: "40"
}

function score(puntos1, puntos2, adv) {
  //Comprobación de si alguien ha ganado el juego y envía bandera para terminar
  if (adv === 2) {
    console.log("El jugador 1 ha ganado")
    return true
  } else if (adv === -2) {
    console.log("El jugador 2 ha ganado")
    return true
  }
  //Secuencia para mirar quien de los dos tiene la ventaja, si se tiene deuce o se imprimen los puntos
  if (puntos1 === 3 && puntos2 === 3) {
    if (adv > 0) {
      console.log("Ventaja P1")
    } else if (adv < 0) {
      console.log("ventaja P2")
    } else {
      console.log("Deuce")
    }
  } else {
    console.log(pointsTable[puntos1],"-",pointsTable[puntos2])
  }
  return false
}

function juegoTenis(arr) {
  //Inicialización de variables
  let jugador1 = 0
  let jugador2 = 0
  let ventaja = 0
  //Control de final de juego
  let exit = false
  arr.forEach( point => {
    //Si el juego no ha finalizado sigue contando puntos
	if (!exit) {
      //Por cada punto se sube el marcador, pero al llegar a 40, se deja de contar
	  if (point === "P1" && jugador1 < 3) {
        jugador1 += 1
      } else if (point === "P2" && jugador2 < 3) {
        jugador2 += 1
      //Si los dos jugadores llegan a 40, se pasa a los escenarios de ventaja
	  } else if (jugador1 === 3 && jugador2 === 3) {
        //Cuando el P1 tiene la ventaja se vuelve positivo y si repite, cumple la condición de victoria
		if (point == "P1") {
          ventaja += 1
        //Cuando el P2 tiene la ventaja se vuelve negativo y si repite, cumple la condición de victoria
		} else {
          ventaja -= 1
        }
      //Si el P1 ya tiene 40 puntos y el P2 dos no, cuando el P1 gana punto se cumple la condición de victoria
	  } else if (point === "P1") {
        ventaja += 2
      //Si el P2 ya tiene 40 puntos y el P1 dos no, cuando el P2 gana punto se cumple la condición de victoria
	  } else if (point === "P2") {
        ventaja -= 2
      //Mensaje cuando un valor no es valido
	  } else {
        console.log("Valor ingresado no valido")
      }
	  //Se envía la información de los puntajes al método de impresión
      exit = score(jugador1, jugador2, ventaja)
    //Mensaje especial cuando ya se termino el juego, pero siguen ingresando valores
	} else {
      console.log("El juego ya ha terminado")
    }
  })
}

//Secuencia de datos para enviar
juegoTenis(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P1", "P1",
             "P1", "P1", "P2", "P2", "P1", "P2", "P2"])