// Reto #2: EL PARTIDO DE TENIS

function check_if_winner(P1, P2) {
    return (P1 > 3) && (P1 - P2 >= 2)
    
}

function score_tenis(sequence) {
   
    if (sequence.some(element => element !== "P1" && element !== "P2")) {
        return ['Entrada invalida - La secuencia tiene palabras distintas a P1 y P2']
    }

    let players = {
        P1: 0,
        P2: 0,
    }

    let score = []
    let final_game = false
    let deuce = false

    const notation = {
        0: "Love",
        1: "15",
        2: "30",
        3: "40",
    }

    let i = 0

    while (!final_game) {
        final_game = (check_if_winner(players.P1, players.P2) || check_if_winner(players.P2, players.P1))    
        players[sequence[i]] += 1

        if (check_if_winner(players.P1, players.P2)) {
            score.push("Ha ganado el P1")
            return score
        } else if (check_if_winner(players.P2, players.P1)) {
            score.push("Ha ganado el P2")
            return score
        } else if (players.P1 === players.P2 && players.P1 >= 3) {
            if (score.at(-1) === "Deuce") {
                score.push("Error en la entrada - No se encontró ganador en la secuencia")
                return score
            }
            deuce = true
            score.push("Deuce")
        } else if (deuce) {
            score.push("Ventaja " + sequence[i]);
        }
        else {
            score.push(notation[players.P1] + " - " + notation[players.P2]);
        }
        if (i === sequence.length) {
            score.push("No fue posible hallar un ganador con la secuencia ingresada")
            return score
        }
        i += 1
    }
    
    return score
}

// let res = score_tenis(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])
// let res = score_tenis(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2"])
// let res = score_tenis(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P2"])
// let res = score_tenis(["P1", "P1", "P1", "P2", "P1", "P2", "P1", "P1"])
// let res = score_tenis(["P1", "P3", "P2", "P2", "P1", "P2", "P1", "P1"])
let res = score_tenis(["P1", "P1", "P2"])

res.forEach(element => console.log(element))