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

 Joaquín Ferrero. 20230117
]

use v6.c;

sub MAIN(
    Int $longitud! where 8 <= * <= 16,		#= longitud de la contraseña (entre 8 y 16)
    Bool :m($mayúsculas),			#= añadir mayúsculas
    Bool :n($números),				#= añadir números
    Bool :s($símbolos),				#= añadir símbolos
) {
    my @números    =  0  ..  9;
    my @letras     = 'a' .. 'z';
    my @mayúsculas = @letras.map: { .uc };
    my @símbolos   = ('!','$','%','&','*','+','-','.','/',':',';','<','>','=','_','@');

    my @caracteres-posibles =  |@letras;
    @caracteres-posibles.push: |@mayúsculas if $mayúsculas;
    @caracteres-posibles.push: |@números    if $números;
    @caracteres-posibles.push: |@símbolos   if $símbolos;

    my $contraseña = @caracteres-posibles.roll($longitud).join;

    say $contraseña;
}
