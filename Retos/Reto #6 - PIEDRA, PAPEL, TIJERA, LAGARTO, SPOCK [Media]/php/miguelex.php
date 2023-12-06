<?php

define("PIEDRA", "🗿");
define("PAPEL", "📄");
define("TIJERAS", "✂️");
define("LAGARTO", "🦎");
define("SPOCK", "🖖");

function PiedraPapelTijerasLagartoSpock($juegos) {
  $p1Points = 0;
  $p2Points = 0;

  $ganador = array(
    PIEDRA => array(TIJERAS, LAGARTO),
    PAPEL => array(PIEDRA, SPOCK),
    TIJERAS => array(PAPEL, LAGARTO),
    LAGARTO => array(PAPEL, SPOCK),
    SPOCK => array(TIJERAS, PIEDRA)
  );

  foreach ($juegos as $juego) {
    list($jugador1, $jugador2) = $juego;
    if ($jugador1 === $jugador2) {
      $p1Points++;
      $p2Points++;
    } else if (in_array($jugador2, $ganador[$jugador1])) {
      $p1Points++;
    } else {
      $p2Points++;
    }
  }

  if ($p1Points === $p2Points)
    return "Empate a " . $p1Points . " puntos";
  else if ($p1Points > $p2Points)
    return "Gana el jugador 1 por " . $p1Points . " a " . $p2Points . " puntos";
  else
    return "Gana el jugador 2 por " . $p2Points . " a " . $p1Points . " puntos";
}

echo PiedraPapelTijerasLagartoSpock(array(
  array(PIEDRA, TIJERAS),
  array(PIEDRA, PAPEL),
  array(LAGARTO, SPOCK)
)) . "\n";

echo PiedraPapelTijerasLagartoSpock(array(
  array(TIJERAS, TIJERAS),
  array(PIEDRA, PAPEL),
  array(LAGARTO, SPOCK),
  array(PIEDRA, PAPEL),
  array(SPOCK, PAPEL),
  array(LAGARTO, LAGARTO),
  array(SPOCK, LAGARTO),
)) . "\n";