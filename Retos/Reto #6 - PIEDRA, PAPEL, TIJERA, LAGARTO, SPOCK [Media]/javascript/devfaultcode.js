/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */

const prompt = require('prompt-sync')();

function getComputerChoice() {
    let ranumber = Math.floor(Math.random() * 5)
    let array = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    for (let counter = 0; counter <= ranumber; counter++) {
        if (counter === ranumber) {
            let answer = array[counter]
            return answer
        }
    }

}

function playRound(playerSelection, computerSelection) {
    let result = ''
    let playerScore = 0
    let computerScore = 0

    if (playerSelection === 'rock') {
        if (computerSelection === 'rock') {
            result = 'Is a tie!'

        } else if (computerSelection === 'paper') {
            result = 'You Lose! Paper covers Rock'
            computerScore = 1

        } else if (computerSelection === 'scissors') {
            result = 'You Win! Rock breaks Scissors'
            playerScore = 1

        } else if (computerSelection === 'lizard') {
            result = 'You Win! Rock crushes Lizard'
            playerScore = 1

        } else if (computerSelection === 'spock') {
            result = 'You Lose! Spock vaporizes Rock'
            computerScore = 1

        }

    } else if (playerSelection === 'paper') {

        if (computerSelection === 'rock') {
            result = 'You Win! Paper cover Rock'
            playerScore = 1

        } else if (computerSelection === 'paper') {
            result = 'Is a tie!'

        } else if (computerSelection === 'scissors') {
            result = 'You Lose! Scissors cut Paper'
            computerScore = 1

        } else if (computerSelection === 'lizard') {
            result = 'You Lose! Lizard eats paper'
            computerScore = 1

        } else if (computerSelection === 'spock') {
            result = 'You Win! Paper disproves Spock'
            playerScore = 1

        }

    } else if (playerSelection === 'scissors') {

        if (computerSelection === 'rock') {
            result = 'You Lose! Rock breaks Scissors'
            computerScore = 1

        } else if (computerSelection === 'paper') {
            result = 'You Win! Scissors cut Paper'
            playerScore = 1

        } else if (computerSelection === 'scissors') {
            result = 'Is a tie!'

        } else if (computerSelection === 'lizard') {
            result = 'You Win! Scissors decapitate Lizard'
            playerScore = 1

        } else if (computerSelection === 'spock') {
            result = 'You Lose! Spock melt Scissors'
            computerScore = 1

        }

    } else if (playerSelection === 'lizard') {

        if (computerSelection === 'rock') {
            result = 'You Lose! Rock crushes Lizard'
            computerScore = 1

        } else if (computerSelection === 'paper') {
            result = 'You Win! Lizard eats paper'
            playerScore = 1

        } else if (computerSelection === 'scissors') {
            result = 'You Lose! Scissors decapitate Lizard'
            computerScore = 1

        } else if (computerSelection === 'lizard') {
            result = 'Is a tie!'

        } else if (computerSelection === 'spock') {
            result = 'Yuo Win! Lizard poisons Spock'
            playerScore = 1

        }

    } else if (playerSelection === 'spock') {

        if (computerSelection === 'rock') {
            result = 'You Win! Spock vaporizes Rock'
            playerScore = 1

        } else if (computerSelection === 'paper') {
            result = 'You Lose! Paper disproves Spock'
            computerScore = 1

        } else if (computerSelection === 'scissors') {
            result = 'You Win! Spock melt Scissors'
            playerScore = 1

        } else if (computerSelection === 'lizard') {
            result = 'Yuo Lose! Lizard poisons Spock'
            computerScore = 1

        } else if (computerSelection === 'spock') {
            result = 'Is a tie!'

        }

    }


    return [result, playerScore, computerScore]
}

function Menu() {
    let playerScore = 0
    let computerScore = 0
    while(1 === 1){
        let answer = prompt('Do yo Want to play? (y/n): ')
        answer = answer.toLowerCase()

        if(answer === 'y') {
            while(1 === 1){

                let numberRounds = prompt('Enter how many Rounds: ')
                numberRounds = parseInt(numberRounds)

                if (isNaN(numberRounds)) {
                    console.log('\nPlease enter a number\n');
                } else {

                    for (let counter = 0; counter < numberRounds; counter++) {
                        while (1 === 1) {
                            let playerSelection = prompt('Enter an option (Rock, Paper, Scissors, Lizard or Spock): ');
                            playerSelection = playerSelection.toLowerCase()
                            if (playerSelection !== 'rock' && playerSelection !== 'paper' && playerSelection !== 'scissors' && playerSelection !== 'lizard' && playerSelection !== 'spock') {
                                console.log('\nPlease select a valid option: Rock, Paper, Scissors, Lizard or Spock\n')
                            } else {
                                const computerSelection = getComputerChoice();
                                score = playRound(playerSelection, computerSelection)
                                playerScore += score[1]
                                computerScore += score[2]
                                console.log('\n' + score[0]);
                                console.log('\nPlayer: ' + playerScore);
                                console.log('Computer: ' + computerScore + '\n');
                                break
                            }
                        }
                    }
                    console.log('\nThe game is over, the final socre is:');
                    console.log('\nPlayer: ' + playerScore);
                    console.log('Computer: ' + computerScore + '\n\n');

                    if (playerScore > computerScore) {
                        console.log('Let\'s go! You win against the computer\n');
                    } else if (computerScore > playerScore) {
                        console.log('So sad! You lose against the computer\n');
                    } else {
                        console.log('It\'s tie\n');
                    }

                    break

                }
            }
        } else if (answer === 'n'){
            console.log('\nGoodbye!\n');
            break
        } else {
            console.log('\nSelect a valid option (y/n)\n');
        }
    }
}

Menu()