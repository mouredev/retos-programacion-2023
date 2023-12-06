#!/usr/bin/env perl
#
# «Mostrar la sintaxis de los principales elementos de un lenguaje»
#
# Joaquín Ferrero, 20230905.
#
use v5.38;
use utf8;
use open IO => ':locale';			# E/S codificado según la terminal

# - Haz un "Hola, mundo!"
say "¡Hola, mundo!";


# - Crea variables de tipo String, numéricas (enteras y decimales)
my $var_de_cadena = "La casa de la abuela es verde";
my $número_de_balcones = 7;
my $temperatura_a_la_sombra = 25.7;


#   y Booleanas (o cualquier tipo de dato primitivo).
use builtin qw(true false);			# A partir de Perl v5.36
no warnings 'experimental::builtin';

my $es_de_noche = true;
say $es_de_noche;				# 1


# - Crea una constante.
use constant PI => 4 * atan2(1, 1);
say PI;						# 3.14159265358979


# - Usa un if, else if y else.
if ($es_de_noche) {
    say "Es de noche";
}
elsif ($temperatura_a_la_sombra > 30.0) {
    say "Hace calor";
}
else {
    say "Hace frío";
}


# - Crea estructuras como un array, lista, tupla, set y diccionario.
my @array = ('a'..'z');
my $lista = [ [ 'a', 3 ], [ 'b', 6 ], [ 'c', 9 ] ];

my %tupla = map { $_ => 1 } 2, 3, 4, 8, 64;
my %set; $set{$_}++ for 3, 3, 3, 4, 4, 5, 1, 1, 1;

my %diccionario = (
    'jefe'  => 'Antonio Pradera',
    'vice'  => 'Mar Pereira',
    'secr'  => 'Victor Hostos',
);


# - Usa un for, foreach y un while.
for my $tup (keys %tupla) {			# foreach es un alias de for
    say $tup;
}

while (!$es_de_noche) {
    say "Sigue siendo de dia";
    sleep 3600;					# una hora
}


# - Crea una clase.
use feature 'class';				# A partir de Perl v5.38
no warnings 'experimental::class';

class Point {
    field $x :param;
    field $y;

    method zero { $x = $y = 0; }
    method x    { $x }
}

my $punto = Point->new(x => 42);
say $punto->x;					# 42

## - Crea diferentes funciones (con/sin parámetros y con/sin retorno).
sub función_sin_parámetros { say "Sin parámetros" }

sub función_con_parámetros($parámetro1, $parámetro2) {
    say "Par1: $parámetro1";
    say "Par2: $parámetro2";
}

sub función_sin_retorno() { PI }
sub función_con_retorno() { return PI }

función_sin_parámetros;
función_con_parámetros(41, 2);
say función_sin_retorno;
say función_con_retorno;


# - Muestra el control de excepciones.
use feature 'try';				# A partir de Perl v5.34
no warnings 'experimental::try';

try {
    my $x = 200 + función_con_retorno();
    $x < 100 or die "Too big";
    say $x;
}
catch ($e) {
    warn "Unable to output a value; $e";
}
finally {
    print "Finished\n";
}


__END__

