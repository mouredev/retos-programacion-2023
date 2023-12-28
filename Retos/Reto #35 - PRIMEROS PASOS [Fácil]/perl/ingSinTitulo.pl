#!/usr/bin/perl

use strict;
use warnings;

# Punto 1: Hola, mundo!
print "Hola, mundo!\n";

# Punto 2: Crea una variable de texto o string
my $miTexto = "¡Hola desde Perl!\n";

# Punto 3: Crea una variable de número entero
my $miEntero = 42;

# Punto 4: Crea una variable de número con decimales
my $miDecimal = 3.14;

# Punto 5: Crea una variable de tipo booleano
my $miBooleano = 1;  # Verdadero

# Punto 6: Crea una constante (no aplicable en Perl)

# Punto 7: Usa un if, else if y else
if ($miEntero > 50) {
    print "El número es mayor que 50\n";
} elsif ($miEntero < 50) {
    print "El número es menor que 50\n";
} else {
    print "El número es igual a 50\n";
}

# Punto 8: Crea un Array (no aplicable en Perl)

# Punto 9: Crea una lista (no aplicable en Perl)

# Punto 10: Crea una tupla (no aplicable en Perl)

# Punto 11: Crea un set (no aplicable en Perl)

# Punto 12: Crea un diccionario (no aplicable en Perl)

# Punto 13: Usa un ciclo for
foreach my $elemento (1..5) {
    print "$elemento\n";
}

# Punto 14: Usa un ciclo foreach
foreach my $elemento ("Manzana", "Banana", "Naranja") {
    print "$elemento\n";
}

# Punto 15: Usa un ciclo while
my $contador = 0;
while ($contador < 3) {
    print "Contador: $contador\n";
    $contador++;
}

# Punto 16: Crea una función sin parámetros que no retorne nada
sub funcionSinParametros {
    print "Función sin parámetros\n";
}
funcionSinParametros();

# Punto 17: Crea una función con parámetros que no retorne nada
sub funcionConParametros {
    my ($param1, $param2) = @_;
    print "Parámetro 1: $param1\n";
    print "Parámetro 2: $param2\n";
}
funcionConParametros(1, "dos");

# Punto 18: Crea una función con parámetros que retorne valor
sub funcionConRetorno {
    my ($a, $b) = @_;
    return $a + $b;
}
my $resultado = funcionConRetorno(3, 4);
print "Resultado: $resultado\n";

# Punto 19: Crea una clase (no hay clases en Perl, se usan paquetes)

# Punto 20: Muestra control de excepciones (eval en Perl)
eval {
    my $division = $miEntero / 0;
    print "$division\n";
};
if ($@) {
    print "Error: $@\n";
}
