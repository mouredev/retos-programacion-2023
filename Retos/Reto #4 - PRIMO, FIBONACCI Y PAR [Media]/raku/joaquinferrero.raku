#!/usr/bin/env raku
#`[
  Reto #4: PRIMO, FIBONACCI Y PAR
  Dificultad: Media | Publicación: 23/01/23 | Corrección: 30/01/23
 
  Enunciado
 
  Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
  Ejemplos:
  - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
  - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 
  Joaquín Ferrero. 20230127
]

use v6.c;

sub postfix:<②>( $número ) { $número %% 2 }

sub postfix:<Ⓟ>( $número ) { $número.is-prime }

sub postfix:<Ⓕ>( $número ) {
    my @fib = 1, 1, * + * ... * >= $número;
    @fib[*-1] == $número;
}

sub MAIN(
    Int $número where * >= 0			#= número a analizar
) {
    say "$número { 'no ' if not $númeroⓅ  }es primo, { 'no ' if not $númeroⒻ  }es fibonacci y es { $número② ?? 'par' !! 'impar' }";
}
