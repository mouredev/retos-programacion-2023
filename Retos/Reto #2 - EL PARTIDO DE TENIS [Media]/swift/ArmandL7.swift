//
//  armando.swift
//  
//
//  Created by Armando Herrera on 1/12/23.
//

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

import Foundation
import UIKit

var player1Points = 0
var player2Points = 0
var player1Result = "Love"
var player2Result = "Love"

let getGame = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

for round in getGame {
    //print(round)
    switch round {
    case "P1":
        if player1Points == 0 || player1Points == 15 {
            player1Points += 15
            player1Result = String(player1Points)
        } else if player1Points == 30 {
            player1Points = 40
            player1Result = String(player1Points)
        } else if player1Points >= 40 {
            player1Points += 1
        }
    case "P2":
        if player2Points == 0 || player2Points == 15 {
            player2Points += 15
            player2Result = String(player2Points)
        } else if player2Points == 30 {
            player2Points = 40
            player2Result = String(player2Points)
        } else if player2Points >= 40 {
            player2Points += 1
        }
    default:
        ""
    }
    if (player1Points == 15 || player1Points == 30)  && player2Points == 0 {
        print("\(player1Result) - \(player2Result)")
    } else if player1Points >= 40 && player2Points >= 40 {
        if player1Points == 40 && player2Points == 40 {
            print("Deuce")
        } else if player1Points == 41 && player2Points == 40 {
            print("Ventaja 1")
        } else if player1Points > 41 && player2Points == 40 {
            print("Ha Ganado P1")
        }
    } else if player1Points == 40 && player2Points < 40 {
        print("\(player1Result) - \(player2Result)")
    } else {
        print("\(player1Result) - \(player2Result)")
    }
}


