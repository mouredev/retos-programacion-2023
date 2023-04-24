#!/usr/bin/env raku
#`[
 Reto #3: EL GENERADOR DE CONTRASEÑAS
 Dificultad: Media | Publicación: 16/01/23 | Corrección: 23/01/23

 Enunciado

 Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 Podrás configurar generar contraseñas con los siguientes parámetros:
     - Longitud: Entre 8 y 16.
     - Con o sin letras mayúsculas.
     - Con o sin números.
     - Con o sin símbolos.
 (Pudiendo combinar todos estos parámetros entre ellos)

 Joaquín Ferrero. 20230119

 Ejemplo de llamada:

    raku joaquinferrero.raku -m -n -s 8

]

use v6.c;

sub MAIN(
    Int $longitud! where 8 <= * <= 16,		#= longitud de la contraseña (entre 8 y 16)
    Bool :m($hay-que-poner-mayúsculas),		#= añadir mayúsculas
    Bool :n($hay-que-poner-números),		#= añadir números
    Bool :s($hay-que-poner-símbolos),		#= añadir símbolos
) {
    my Set $números    = set  0  ..  9;				# conjunto de números
    my Set $letras     = set 'a' .. 'z';			# conjunto de letras
    my Set $mayúsculas = set 'A' .. 'Z';			# conjunto de letras mayúsculas
    my Set $símbolos   = set '!$%&*+-.,/:;<>=_@'.comb;		# conjunto de símbolos

    my Set $caracteres-posibles					# creamos el conjunto de caracteres
        =  $letras						# a partir de las letras
        ∪ ($mayúsculas if $hay-que-poner-mayúsculas)		# y opcionalmente del resto de conjuntos
        ∪ ($números    if $hay-que-poner-números)
        ∪ ($símbolos   if $hay-que-poner-símbolos)
        ;

    # formamos la contraseña sacando caracteres al azar,
    # desde el conjunto de caracteres-posibles, tantos como indique $longitud,
    # y los unimos en una única cadena
    my Str $contraseña = $caracteres-posibles.roll($longitud).join;

    say $contraseña;
}

