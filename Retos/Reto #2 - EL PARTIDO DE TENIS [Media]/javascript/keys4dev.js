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

points = ['P2', 'P1', 'P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P2', 'P2']
tenisPoints = {'0':'Love', '1':'15', '2':'30', '3':'40', '4':'  Wins ','5':'Ventaja', '6':'       ', '7':'  Lose ', '8':'Deuce'}

game = {'P1':0, 'P2':0}


async function setPlayerPoint(player){
    let otherPlayer = (player === "P1") ? "P2" : "P1";
    //console.log("if "+player+':'+game[player]+'/'+otherPlayer+':'+game[otherPlayer])
    //Si el jugador tiene ventaja se lee asigna wins.
    if (game[player]==5){
        game[player] = 4;
        game[otherPlayer] = 7;
        //console.log(game)
    }
    //Si el jugador esta en desventaja se le asigna Deuce a cada jugador
    else if (game[player]==6) {
        game[player]=8;
        game[otherPlayer]=8;
        //console.log(game)
    } 
    //Si el jugador se pone 40:40 se le asigna Deuce a cada jugador
    else if (game[player]+1 == 3 && game[otherPlayer]==3){
        game[player]=8;
        game[otherPlayer]=8;
    }
    //Si el jugador esta en Deuce se le asigna ventaja y al contrincante desventaja
    else if (game[player]==8){
        game[player]=5;
        game[otherPlayer]=6;
        //console.log(game)
    }
    //Si los jugadores van 40:40 se le asigna ventaja al jugador y desventaja al otro
    else if (game[player]== 3 && game[otherPlayer]==3){
        game[player]=5;
        game[otherPlayer]=6;
       
    }
    //Si no es ningún caso de los anteriores se le suma un punto al jugador
    else{
        game[player] +=1;
    } 
}
        

function calculateGame(points){
    console.log('----------------------')
    console.log("      P1   :   P2       ")
    console.log('----------------------')
    points.forEach(point => {
        setPlayerPoint(point)
        //Formateo si love P1
        if (game['P1'] == 0){
            console.log('    '+tenisPoints[game['P1']]+'   :   '+tenisPoints[game['P2']] + '  ')
        }
        //Formateo si love P2
        else if(game['P2'] == 0){
            console.log('    '+tenisPoints[game['P1']]+' : '+tenisPoints[game['P2']] + '  ')
        }
        //Formateo si estan Deuce
        else if(game['P1'] == 8 || game['P2'] == 8){
            console.log('         Deuce   ')
        }
        //Formateo si estan cpn puntuación Normal
        else if(game['P1'] <= 3 && game['P2'] <= 3){
            console.log('     '+tenisPoints[game['P1']]+'    :   '+tenisPoints[game['P2']] + '  ')
        }   
        //Formateo si Ventaja o gana/pierde
        else{
            console.log('  ' + tenisPoints[game['P1']]+'  :   '+tenisPoints[game['P2']])
        }
    });
}
    

        
calculateGame(points)
//Retorna el juego asi:
/*
----------------------
      P1   :   P2       
----------------------
    Love   :   15  
     15    :   15  
     30    :   15  
     40    :   15  
     40    :   30  
     40    :   40  
         Deuce   
         Deuce   
           :  Ventaja
    Lose   :    Wins 
*/