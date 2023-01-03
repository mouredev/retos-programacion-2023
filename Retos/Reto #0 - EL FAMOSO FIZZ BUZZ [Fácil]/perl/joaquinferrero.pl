#!/usr/bin/perl
#
# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
#  - Múltiplos de 3 por la palabra "fizz".
#  - Múltiplos de 5 por la palabra "buzz".
#  - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#
# Joaquin Ferrero, 20230102
#
use v5.24;
my $fizzbuzz;

for my $i (1 .. 100) {
    say							# decimos que 
        +(
            $fizzbuzz = (				# fizzbuz es
                      ($i % 3 == 0 ? "fizz" : "")	# "fizz" si es múltiplo de 3 y
                    . ($i % 5 == 0 ? "buzz" : "")	# "buzz" si es múltiplo de 5 o
            )						# "fizzbuzz" si es múltiplo de 15 (concatenación de los dos)
        )
        ? $fizzbuzz					# o tenemos el fizzbuzz
        : $i;						# o sacamos el número de línea
}
