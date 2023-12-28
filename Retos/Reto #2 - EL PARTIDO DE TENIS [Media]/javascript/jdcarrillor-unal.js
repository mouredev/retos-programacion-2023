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
const tenis_game = (puntos) =>{
    const palyer1 = "P1"
    let p1_points = 0 
    let p2_points = 0 
    const player2 = "P2"
    const game = ["Love", "15", "30", "40"]
    finished = false
    do{
        console.log(palyer1, player2)
        for(let point in puntos){
            (puntos[point] == palyer1) ? p1_points++ : p2_points++ 
            if(p1_points >= game.length - 1 &&  p2_points >= game.length - 1){
                if (Math.abs( p1_points - p2_points <= 1)){
                    if(p1_points == p2_points){
                        console.log("Deuce")
                    }else if(p1_points > p2_points){
                        console.log("Ventaja " + palyer1)
                    }else{
                        console.log("Ventaja " + player2)
                    }
                }else{
                    if(p1_points > p2_points){
                        console.log("Ha ganado " + palyer1)
                    }else{
                        console.log("Ha ganado " + player2)
                    }
                    finished = true 
                }
            }else{  
                if (p1_points < 4 || p2_points < 4){
                    console.log(`${game[p1_points]}` + " " + `${game[p2_points]}`)
                }else{
                    if(p1_points > p2_points){
                        console.log("Ha ganado " + palyer1)
                    }else{
                        console.log("Ha ganado " + player2)
                    }
                    finished = true 
                }
            }
            }  
    }while(!finished)
    }

console.log(tenis_game(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]))
console.log(tenis_game(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2","P2","P1","P1","P1"]))