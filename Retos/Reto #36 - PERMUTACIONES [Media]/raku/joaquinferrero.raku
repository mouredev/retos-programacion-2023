#!/usr/bin/env raku
#`(
 «Permutaciones de las letras de una palabra»

 Crea un programa que sea capaz de generar e imprimir todas las
 permutaciones disponibles formadas por las letras de una palabra.
 - Las palabras generadas no tienen por qué existir.
 - Deben usarse todas las letras en cada permutación.
 - Ejemplo: sol, slo, ols, osl, los, lso

 Joaquín Ferrero, 20230913.
)
use v6.c;

my $word = prompt "Introduzca la palabra a permutar: ";

# .comb divide $word en letras
# .permutations crea una lista con las permutaciones,
#   cada una de ellas es otra lista de letras permutadas
# .map(*.join) une cada lista de letras permutadas
# .join(", ") une las nuevas palabras en una única cadena de caracteres
# .say imprimimos el resultado
$word.comb.permutations.map(*.join).join(", ").say;

