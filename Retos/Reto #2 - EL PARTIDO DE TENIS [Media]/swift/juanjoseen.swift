//
//  juanjoseen.swift
//  
//
//  Created by Juan Jose Elias Navarro on 16/04/23.
//

import Foundation

enum Score: Int {
    case love = 0
    case fifteen = 1
    case thirty = 2
    case fourty = 3
    case deuce = 4
    case advantage = 5
    case win = 6
    
    var value: String {
        switch self {
        case .love:
            return "Love"
        case .fifteen:
            return "15"
        case .thirty:
            return "30"
        case .fourty:
            return "40"
        case .deuce:
            return "Deuce"
        case .advantage:
            return "Advantage"
        case .win:
            return "Win"
        }
    }
}

class Player {
    var name: String
    var score: Score = .love
    
    init(name: String) {
        self.name = name
    }
    
    func addScore() {
        if score != .win {
            if let newScore: Score = Score(rawValue: score.rawValue + 1) {
                score = newScore
            }
        } else {
            print("\(name) already win!")
        }
    }
    
    func scoreWith(_ other: Player) {
        
    }
}

class ScoreManager {
    
    var points: [Player]
    var p1: Player
    var p2: Player
    
    var winer: Player? = nil
    
    init(p1: Player, p2: Player) {
        self.points = []
        self.p1 = p1
        self.p2 = p2
        printScore()
    }
    
    func printScore() {
        if p1.score.rawValue < Score.fourty.rawValue && p2.score.rawValue < Score.fourty.rawValue {
            print(String(format: "%@ - %@", p1.score.value, p2.score.value))
        } else {
            if p1.score == p2.score {
                p1.score = .deuce
                p2.score = .deuce
                print("Deuce")
            } else {
                if p1.score == .win {
                    print("\(p1.name) win!")
                    winer = p1
                } else if p2.score == .win {
                    print("\(p2.name) win!")
                    winer = p2
                } else if p1.score == .advantage {
                    print("Advantage for \(p1.name)")
                } else if p2.score == .advantage {
                    print("Advantage for \(p2.name)")
                } else if p1.score.rawValue < p2.score.rawValue || p2.score.rawValue < p1.score.rawValue {
                    print(String(format: "%@ - %@", p1.score.value, p2.score.value))
                }
            }
        }
    }
    
    func addScore(to player: String) {
        if winer == nil {
            if p1.name == player {
                p1.addScore()
            } else if p2.name == player {
                p2.addScore()
            } else {
                print("Player \"\(player)\" not found!")
            }
            printScore()
        } else {
            print("\(winer!.name) already win!!")
        }
    }
    
    func analizeSecuence(_ secuence: [String]) {
        p1.score = .love
        p2.score = .love
        for player in secuence {
            addScore(to: player)
        }
    }
}

let p1: Player = Player(name: "P1")
let p2: Player = Player(name: "P2")

let manager: ScoreManager = ScoreManager(p1: p1, p2: p2)
manager.analizeSecuence(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])
