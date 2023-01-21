#!usr/bin/env raku
#`[
 Escribe un programa que muestre por consola (con un print) los
 números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

 Joaquín Ferrero, 20230102
]

for 1..100 -> $i {
    say (
        my $fizzbuzz                        # "fizzbuzz" es la concatenación de dos casos posibles:
            = ($i %% 3 ?? "fizz" !! "")     # "fizz" si es múltiplo de 3
            ~ ($i %% 5 ?? "buzz" !! "")     # "buzz" si es múltiplo de 5
        )
        ?? $fizzbuzz                        # O tenemos un fizzbuzz,
        !! $i;                              # o sacamos el número de línea
}
