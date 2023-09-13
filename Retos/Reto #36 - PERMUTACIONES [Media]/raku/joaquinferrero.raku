#!/usr/bin/env raku
#`(
 «Permutaciones de las letras de una palabra»

 Crea un programa que sea capaz de generar e imprimir todas las
 permutaciones disponibles formadas por las letras de una palabra.
 - Las palabras generadas no tienen por qué existir.
 - Deben usarse todas las letras en cada permutación.
 - Ejemplo: sol, slo, ols, osl, los, lso

 Joaquín Ferrero, 20230907.
)
use v6.c;

my $word = "sol";
say $word.comb.permutations.map(*.join).join(", ")

