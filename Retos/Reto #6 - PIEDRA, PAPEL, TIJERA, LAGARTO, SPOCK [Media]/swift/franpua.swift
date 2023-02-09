import Foundation

func gamePPTLS(games:[(String,String)]) {
    
    let (sccisors, spock, lizard, paper, rock) = ("✂️", "🖖", "🦎", "📄", "🗿")

    var p1Score = 0
    var p2Score = 0
    
    for game in games{
                    
            switch game {
            case (rock,spock): p2Score += 1;
            case (rock,sccisors): p1Score += 1;
            case (rock,paper): p2Score += 1;
            case (rock,lizard): p2Score += 1;
            case (paper,rock): p1Score += 1;
            case (paper,sccisors): p2Score += 1;
            case (paper,lizard): p2Score += 1;
            case (paper,spock): p1Score += 1;
            case (sccisors,spock): p2Score += 1;
            case (sccisors,lizard): p1Score += 1;
            case (sccisors,rock): p2Score += 1;
            case (sccisors,paper): p1Score += 1;
            case (spock,paper): p2Score += 1;
            case (spock,lizard): p2Score += 1;
            case (spock,rock): p1Score += 1;
            case (spock,sccisors): p1Score += 1;
            case (lizard,sccisors): p2Score += 1;
            case (lizard,rock): p2Score += 1;
            case (lizard,paper): p1Score += 1;
            case (lizard,spock): p1Score += 1
                
            default: "error"
            }
    }
    let result = p1Score > p2Score ? "Player 1" : p2Score > p1Score ? "player 2" : "Tie"
    print(result)
}
gamePPTLS(games: [("🗿","🖖"),("🗿","✂️"), ("✂️","🗿"), ("🦎","📄")])
gamePPTLS(games: [("🗿","🖖"),("✂️","✂️"), ("✂️","🗿"), ("🦎","🦎")])
gamePPTLS(games: [("🗿","🗿")])
gamePPTLS(games: [("🦎","🖖"),("📄","✂️"), ("📄","🗿"), ("🦎","🗿"), ("🖖","🗿")])
gamePPTLS(games: [("👻","⚽️")])