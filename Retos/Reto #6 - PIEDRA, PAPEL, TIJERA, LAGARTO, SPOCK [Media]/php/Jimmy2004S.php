<?php
# Reto #6: Piedra, Papel, Tijera, Lagarto, Spock
#### Dificultad: Media | Publicación: 06/02/23 | Corrección: 13/02/23

## Enunciado

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


$puntos_p1 = 0;
$puntos_p2 = 0;

function evaluate(array $jugada){
    $reglas = [
        "🗿" =>
        [
            ["🗿", "✂️"],
            ["🗿", "🦎"] 
        ],
        "✂️" =>
        [
            ["✂️", "🗿"],
            ["✂️", "📄"],
            ["✂️", "🦎"] 
        ],
        "📄" =>
        [
            ["📄", "🗿"],
            ["📄", "🖖"]
        ],
        "🦎" =>
        [
            ["🦎", "📄"],
            ["🦎", "🖖"]
        ],
        "🖖" =>
        [
            ["🖖", "✂️"] ,
            ["🖖", "🗿"] 
        ]
       
    ];
    

    foreach($reglas as $key => $regla) {
        foreach($regla as $jugada_regla) {
            if(empty(array_diff($jugada, $jugada_regla))) {
                return $key; // Imprime la clave si los arreglos son iguales
            }
        }
    }
}

 function game (array $array){
    global $puntos_p1;
    global $puntos_p2;

    $mensaje = "";
    foreach($array as $key => $element){
        $mensaje .= "     " .$element['P1'] . " - " .  $element['P2'] . "<br>";
        if($element['P1'] == $element['P2']){
            $mensaje .= "   Empate <br>";
        }else{
            $jugada_win = evaluate($element);
            if($element['P1'] == $jugada_win){
                $mensaje .= "  Player 1";
                $puntos_p1++;
            }else{
                $mensaje .= "  Player 2";
                $puntos_p2++;
            }
        }
        $mensaje .= "</br> -------------------------</br>";
    }
    return $mensaje;
 }


 $juegos = [
     "R1" => ["P1" => "🗿", "P2" => "📄"],
     "R2" => ["P1" => "🦎", "P2" => "✂️"],
     "R3" => ["P1" => "🖖", "P2" => "🗿"],
     "R4" => ["P1" => "🗿", "P2" => "✂️"],
     "R5" => ["P1" => "✂️", "P2" => "🦎"],
     "R6" => [ "P1" => "📄", "P2" => "🖖"],
     "R7" => [ "P1" => "📄", "P2" => "🦎"],
     "R8" => [ "P1" => "✂️", "P2" => "✂️"],
     "R9" => [ "P1" => "🖖", "P2" => "🦎"],
     "R10" => [ "P1" => "🖖", "P2" => "🖖"],
     "R11" => [ "P1" => "🖖", "P2" => "🦎"]
 ];



 
$result = game($juegos);
$gano = ($puntos_p1 == $puntos_p2) ? "Empate" : (($puntos_p1 > $puntos_p2) ? "Player 1" : "Player 2");
echo $result . "<b> Gano: $gano </b>";


