/*
player 1
player 2
tie
*/

/*
===== Lógica del juego =====
    🖖 rompe        ✂️ [✅]
    🖖 vaporiza     🗿 [✅]

    ✂️ decapita     🦎 [✅]
    ✂️ corta        📄 [✅]

    📄 desautoriza  🖖 [✅]
    📄 envuelve     🗿 [✅]

    🗿 aplasta      ✂️ [✅]
    🗿 aplasta      🦎 [✅]

    🦎 envenena     🖖 [✅]
    🦎 devora       📄 [✅]
*/

const input = [
    ["🗿","✂️"],  // 0
    ["✂️","🗿"],  // 1
    ["📄","✂️"]   // 2
];


/**
 * Calcula e imprime qué jugador gana más partidas
 * @param {Array} input - Arreglo de arreglos con las jugadas de cada jugador
 */
function firstPlace(input){
    let player1 = 0;
    let player2 = 0;
    let tie = 0;

    for(let i = 0; i < input.length; i++){
        if(input[i][0] === input[i][1]){
            tie++;
        }
        else if(input[i][0] === "🖖" && input[i][1] === "✂️"){
            player1++;

        }
        else if(input[i][0] === "🖖" && input[i][1] === "🗿"){
            player1++;
        }
        else if(input[i][0] === "✂️" && input[i][1] === "🦎"){
            player1++;
        }
        else if(input[i][0] === "✂️" && input[i][1] === "📄"){
            player1++;
        }
        else if(input[i][0] === "📄" && input[i][1] === "🖖"){
            player1++;
        }
        else if(input[i][0] === "📄" && input[i][1] === "🗿"){
            player1++;
        }
        else if(input[i][0] === "🗿" && input[i][1] === "✂️"){
            player1++;
        }
        else if(input[i][0] === "🗿" && input[i][1] === "🦎"){
            player1++;
        }
        else if(input[i][0] === "🦎" && input[i][1] === "🖖"){
            player1++;
        }
        else if(input[i][0] === "🦎" && input[i][1] === "📄"){
            player1++;
        }
        else{
            player2++;
        }
    }
    
    if(tie > player1 && tie > player2){
        console.log("tie");
    }
    else if(player1 > player2){
        console.log(`Player 1: ${player1} wins`);
    }
    else{
        console.log(`Player 2: ${player2} wins`);
    }
}

firstPlace(input);
