//
//  juanjoseen.swift
//  
//
//  Created by Juan Jose Elias Navarro on 20/04/23.
//

import Foundation

func match(p1: String, p2: String) -> Int {
    switch p1 {
    case "🗿":
        switch p2 {
        case "🦎", "✂️":
            return 0
        case "🖖", "📄":
            return 1
        default:
            return -1
        }
    case "📄":
        switch p2 {
        case "🖖", "🗿":
            return 0
        case "🦎", "✂️":
            return 1
        default:
            return -1
        }
    case "✂️":
        switch p2 {
        case "🦎", "📄":
            return 0
        case "🗿", "🖖":
            return 1
        default:
            return -1
        }
    case "🦎":
        switch p2 {
        case "🖖", "📄":
            return 0
        case "🗿", "✂️":
            return 1
        default:
            return -1
        }
    case "🖖":
        switch p2 {
        case "🦎", "📄":
            return 0
        case "🗿", "✂️":
            return 1
        default:
            return -1
        }
    default:
        return -1
    }
}

func game(games: [(String, String)]) -> String {
    var score: [Int] = [0, 0]
    for game in games {
        let result: Int = match(p1: game.0, p2: game.1)
        if result >= 0 {
            let current: Int = score[result]
            score[result] = current + 1
        }
    }
    let p1Score: Int = score[0]
    let p2Score: Int = score[1]
    if p1Score == p2Score {
        return "Tie"
    } else if p1Score > p2Score {
        return "Player 1"
    }
    return "Player 2"
}

print(game(games: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]))
print(game(games: [("🗿","🖖"), ("✂️","🦎"), ("✂️","✂️")]))
print(game(games: [("📄","🖖"), ("✂️","🖖"), ("🦎","📄")]))
