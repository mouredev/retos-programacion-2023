//
//  fjvgallego.swift
//  
//
//  Created by Francisco Javier Gallego Lahera on 11/1/23.
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

// MARK: DATA

enum TennisPlayer: String {
    case P1, P2
    
    var name: String { self.rawValue }
}

enum Score: CaseIterable {
    case love, fifteen, thirty, forty, adv, matchPoint
    
    var value: String {
        switch self {
        case .love: return "Love"
        case .fifteen: return "15"
        case .thirty: return "30"
        case .forty: return "40"
        case .adv: return "adv"
        case .matchPoint: return "matchPoint"
        }
    }
    
    func winPoint(rivalScore: Score) -> (newCurrentScore: Score, newRivalScore: Score) {
        switch self {
        case .love: return (.fifteen, rivalScore)
        case .fifteen: return (.thirty, rivalScore)
        case .thirty: return (.forty, rivalScore)
        case .forty: return
            rivalScore == .adv
                ? (.forty, .forty) // Remove the rival's advantage when the current player wins the point.
                
                : rivalScore == .forty
                    ? (.adv, .forty) // Set the current player's advantage when the rival has 40 points and the current player wins the point.
                    : (.matchPoint, rivalScore) //
        case .adv: return (.matchPoint, rivalScore)
        case .matchPoint: return (.matchPoint, rivalScore)
        }
    }
    
    static func getScoreTitle(player1Score: Score, player2Score: Score) -> String {
        var score = ""
        
        if player1Score == .forty && player1Score == player2Score {
            score = "deuce"
        } else if player1Score == .adv {
            score = "Ventaja \(TennisPlayer.P1)"
        } else if player2Score == .adv {
            score = "Ventaja \(TennisPlayer.P2)"
        } else if player1Score == .matchPoint {
            score = "Ha ganado el \(TennisPlayer.P1)"
        } else if player2Score == .matchPoint {
            score = "Ha ganado el \(TennisPlayer.P2)"
            
        } else {
            score = "\(player1Score.value) - \(player2Score.value)"
        }
        
        return score
    }
}

enum ScoreError: Error {
    case invalidSequence
    
    var description: String {
        switch self {
        case .invalidSequence: return "La secuencia de puntos NO es válida."
        }
    }
}

func playMatch(withSequence pointsSequence: [TennisPlayer]) {
    
    print()
    
    var finalScore = """
    ----------------
     MATCH SEQUENCE
    ----------------
    """
    
    // Match Start
    
    let initialScore: Score = .love
    
    var p1Score: Score = initialScore
    var p2Score: Score = initialScore
    
    // Match Sequence
    
    for point in pointsSequence {
        switch point {
        case .P1:
            let newScores = p1Score.winPoint(rivalScore: p2Score)
            p1Score = newScores.newCurrentScore
            p2Score = newScores.newRivalScore
        case .P2:
            let newScores = p2Score.winPoint(rivalScore: p1Score)
            p1Score = newScores.newRivalScore
            p2Score = newScores.newCurrentScore
        }
        
        finalScore.append("\n")
        finalScore.append(Score.getScoreTitle(player1Score: p1Score, player2Score: p2Score))
    }
    
    do {
        try errorCheck(forScore1: p1Score, andScore2: p2Score)
    } catch let error as ScoreError {
        print("ERROR: \(error.description)")
        return
    } catch {
        print("ERROR: Error desconocido.")
    }
    
    print(finalScore)
}

func errorCheck(forScore1 p1Score: Score, andScore2 p2Score: Score) throws {
    let p1IsWinner = p1Score == .matchPoint
    let p2IsWinner = p2Score == .matchPoint
    let uniqueWinnerExists = p1IsWinner && !p2IsWinner || !p1IsWinner && p2IsWinner
    
    guard uniqueWinnerExists else {
        throw ScoreError.invalidSequence
    }
}

// MARK: RESULTS

// Results that should print the score sequence.
playMatch(withSequence: [.P1, .P1, .P2, .P2, .P1, .P2, .P1, .P1])
playMatch(withSequence: [.P1, .P1, .P1, .P2, .P2, .P2, .P1, .P2, .P1, .P2, .P1, .P1])
playMatch(withSequence: [.P2, .P2, .P2, .P1, .P1, .P1, .P2, .P1, .P2, .P1, .P2, .P2])

// Results that should print an error.
playMatch(withSequence: [.P2, .P2])
playMatch(withSequence: [.P2, .P2, .P2, .P1, .P1, .P1, .P2, .P1, .P2, .P1, .P2])
