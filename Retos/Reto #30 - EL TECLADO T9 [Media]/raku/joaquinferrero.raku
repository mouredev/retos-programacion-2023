#!/usr/bin/env raku
#
# El teclado T9
#
# Los primeros dispositivos móviles tenían un teclado llamado T9
# con el que se podía escribir texto utilizando únicamente su
# teclado numérico (del 0 al 9).
#
# Crea una función que transforme las pulsaciones del T9 a su
# representación con letras.
# - Debes buscar cuál era su correspondencia original.
# - Si un bloque tiene más de un número, debe ser siempre el mismo.
#
# Ejemplo:
#   Entrada: 6-666-88-777-33-3-33-888
#   Salida: MOUREDEV
#
# Joaquín Ferrero, 20230927
#
use v6;

my $secuencia;

$secuencia = '6-666-88-777-33-3-33-888';
say $secuencia;
say T9($secuencia);

$secuencia = '555-2-0-222-2-7777-2-0-3-33-0-555-2-0-2-22-88-33-555-2-000-0-66-00-0-77777-99999-0-***-7-444-7777-666-0-1-****';
say $secuencia;
say T9($secuencia);

sub T9 ($secuencia) {
    my %keys = (
        1   => '1£$¥¤',
        2   => 'abc2äáàâãç',
        3   => 'def3ëéèê',
        4   => 'ghi4ïíìî',
        5   => 'jkl5',
        6   => 'mno6öñóòôõ',
        7   => 'pqrs7ß',
        8   => 'tuv8üúùû',
        9   => 'wxyz9ÿýæøå',
        0   => ' .,?!0+-:¿¡"´;_',
        '*' => '*/()<=>%',
        '#' => '  #@\&§',
    );

#    my $salida = [~] gather {
#        for split(/<[-]>/, $secuencia) -> $parte {
#            my $largo = $parte.chars;
#            my $tecla = substr $parte, 0, 1;
#            my $letra = substr %keys{$tecla}, $largo-1, 1;
#            take $letra;
#        }
#    };
#    return $salida;

    return [~] $secuencia.split(/\-/).map({ %keys{.substr(0, 1)}.substr(.chars-1, 1) });
}

