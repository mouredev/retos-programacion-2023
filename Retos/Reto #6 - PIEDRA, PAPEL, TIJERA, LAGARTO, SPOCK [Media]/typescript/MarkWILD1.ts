
/*
    PIEDRA - PAPEL - TIJERA - LAGARTO - SPOCK
<--- PEQUEÑA ALTERACIÓN: PEDIR POR CONSOLA A LOS PLAYERS QUE ELIJAN SU OPCIÓN ------>

 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
*/

import { resolve } from "path";

const readline = require('readline');

//Elecciones
enum Choice {
    Piedra = 'piedra',
    Papel = 'papel',
    Tijera = 'tijera',
    Lagarto = 'lagarto',
    Spock = 'spock' 
}

// Mapa que define al ganador

const rules: { [key in Choice]: Choice[] } = {
    [Choice.Piedra]: [Choice.Tijera, Choice.Lagarto],
    [Choice.Papel]: [Choice.Piedra, Choice.Spock],
    [Choice.Tijera]: [Choice.Papel, Choice.Lagarto],
    [Choice.Lagarto]: [Choice.Papel, Choice.Spock],
    [Choice.Spock]: [Choice.Piedra, Choice.Tijera]
}

//Interfaz para una jugada

interface Play {
    p1: Choice,
    p2: Choice
}

const winnerOrTie = (play: Play): 'Player 1' | 'Player 2' | 'Tie' => {
    const { p1, p2 }  =  play;

    if (p1 === p2) {
        return 'Tie'
    }

    if (rules[p1].includes(p2)) {
        return 'Player 1'
    } else {
        return 'Player 2'
    }
}

//Lectura en consola
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let numOfGames: number = 10;

//Pedir eleccion del usuario
const askPlayers = (player: number): Promise<Choice> => {
    return new Promise((resolve) => {
        rl.question(`Player ${player}, make your choice: piedra, papel, tijera, lagarto, spock `, (answer: string) => {
            const choice = answer.trim().toLowerCase()
            if (Object.values(Choice).includes(choice as Choice)) {
                resolve(choice as Choice)
            } else {
                console.log("Eleccion invalida, elije entre: piedra, papel, tijera, lagarto, spock");
                askPlayers(player).then(resolve)
                
            }
        });
    });
}

//Ejecutar partida
const playRound = async (): Promise<Play> => {
    const p1Choice  = await askPlayers(1)
    const p2Choice  = await askPlayers(2)
    return { p1: p1Choice, p2: p2Choice}
}

const startGame = async () => {
    console.log("Let's PLAY. Make your choice: Piedra, Papel, Tijera, Lagarto, Spock!");
    const totalGames = numOfGames;

    let p1Wins: number = 0;
    let p2Wins: number = 0;
    let tie: number = 0;

    for (let i = 1; i < totalGames; i++) {
        console.log(`\n---Game ${i} ---`);
        
        const play = await playRound();
        const result = await winnerOrTie(play)

        switch (result) {
            case 'Player 1':
                p1Wins++;
                console.log("Player 1 wins this game!");
                break;
            
            case 'Player 2': 
                p2Wins++;
                console.log("Player 2 wins this game!");
                break;
            case 'Tie':
                tie++
                console.log("Tie Game!")
                break;   
        }
        
    }

    console.log("\n---Final Results---");
    console.log(`\n---Player 1 wins: ${p1Wins} games`);
    console.log(`\n---Player 2 wins: ${p2Wins} games`);
    console.log(`\n---Ties: ${tie} games`);

    if (p1Wins > p2Wins) {
        console.log("Player 1 is the WINNER!");
    } else if (p2Wins > p1Wins) {
        console.log("Player 2 is the Winner!!!");
    } else {
        console.log("It's a TIE!");
        
    }

    rl.close();
}

//Begin the game
startGame();
