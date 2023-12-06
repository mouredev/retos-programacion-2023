/*
 * Piedra, papel, tijera, lagarto, spock
 *
 * Reglas del juego:
 * Tijeras cortan a papel
 * Papel tapa a piedra
 * Piedra aplasta a lagarto
 * Lagarto envenena a Spock
 * Spock rompe a tijeras
 * Tijeras decapitan a lagarto
 * Lagarto devora a papel
 * Papel desautoriza a Spock
 * Spock vaporiza a piedra
 * Piedra aplasta a tijeras
 */

function piedraPapelTijeraLagartoSpock(jugadas) {
  const piedra = "🗿";
  const papel = "📄";
  const tijera = "✂️";
  const lagarto = "🦎";
  const spock = "🖖";
  const resultado = ["Player 1", "Player 2", "Tie"];
  let ganador = 0;
  let p1 = 0;
  let p2 = 0;
  let empate = 0;

  for (let i = 0; i < jugadas.length; i++) {
    if (jugadas[i][0] === tijera && jugadas[i][1] === papel) {
      p1++;
    } else if (jugadas[i][0] === papel && jugadas[i][1] === piedra) {
      p1++;
    } else if (jugadas[i][0] === piedra && jugadas[i][1] === lagarto) {
      p1++;
    } else if (jugadas[i][0] === lagarto && jugadas[i][1] === spock) {
      p1++;
    } else if (jugadas[i][0] === spock && jugadas[i][1] === tijera) {
      p1++;
    } else if (jugadas[i][0] === tijera && jugadas[i][1] === lagarto) {
      p1++;
    } else if (jugadas[i][0] === lagarto && jugadas[i][1] === papel) {
      p1++;
    } else if (jugadas[i][0] === papel && jugadas[i][1] === spock) {
      p1++;
    } else if (jugadas[i][0] === spock && jugadas[i][1] === piedra) {
      p1++;
    } else if (jugadas[i][0] === piedra && jugadas[i][1] === tijera) {
      p1++;
    } else if (jugadas[i][0] === jugadas[i][1]) {
      empate++;
    } else {
      p2++;
    }
  }

  if (p1 > p2) {
    ganador = 0;
  } else if (p1 < p2) {
    ganador = 1;
  } else {
    ganador = 2;
  }

  return resultado[ganador];
}

console.log(
  piedraPapelTijeraLagartoSpock([
    ["🗿", "✂️"],
    ["✂️", "🗿"],
    ["📄", "✂️"]
  ])
);

console.log(
  piedraPapelTijeraLagartoSpock([
    ["🗿", "🗿"],
    ["🦎", "🖖"],
    ["🖖", "✂️"]
  ])
);

console.log(
  piedraPapelTijeraLagartoSpock([
    ["🗿", "🗿"]
  ])
);