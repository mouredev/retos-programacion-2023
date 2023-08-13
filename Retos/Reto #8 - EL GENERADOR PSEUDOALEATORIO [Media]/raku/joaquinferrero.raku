#!/usr/bin/env raku
#`(
    Reto #8. «El generador pseudoaleatorio»
    
    Programa:
    
      Crea un generador de números pseudoaleatorios entre 0 y 100.
      * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
    
    Solución:
      Se puede usar funciones de tiempo y alguna operación matemática
    
    Joaquín Ferrero, 20230813
)
use v6.c;

say 1 + ((time * $*PID) +^ ($*PID * 2)) % 99;
