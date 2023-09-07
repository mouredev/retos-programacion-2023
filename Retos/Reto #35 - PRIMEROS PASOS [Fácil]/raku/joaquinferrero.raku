#!/usr/bin/env raku
#`(
 «Primeros pasos»

 Mostrar la sintaxis de los principales elementos de un lenguaje.

 Joaquín Ferrero, 20230907.
)
use v6.c;

# Haz un "Hola, mundo!"
say "¡Hola, Mundo!";

# Crea variables de tipo String, numéricas (enteras y decimales) y Booleanas
my $cadena  = "La casa de la abuela es de color verde";
my $capital = 1200;
my $hay-que-invertir = True;

# Crea una constante
constant Pi = π;
say Pi;					# 3.141592653589793

# Usa un if, else if y else
if Pi > 3 {
    say "Suficiente";
}
elsif $capital > 1000 {
    say "Suficiente";
}
else {
    say "Insuficiente";
}

# Crea estructuras como un array, lista, tupla, set y diccionario
my @array = 1, 3, 5, "Hola";		# un array
say @array.elems;			# 4 (elementos)

my $lista = (1, 2, 4, 8);		# las listas son inmutables
say $lista[2];				# 4

my $tupla = (1, "two");			# las tuplas son listas inmutables
say $tupla[1];				# "two"

my $frutas =				# un set
    set <limón manzana naranja manzana manzana>;
say $frutas;				# set(manzana naranja limón)

my %capitales =				# un diccionario
    España => 'Madrid', 'Estados Unidos' => 'Washington DC';
say %capitales{'España'};		# Madrid

# Usa un for, foreach y un while
for @array -> $x { say $x }		# for, foreach
loop (my $i = 5; $i > 0; $i--) {	# loop
    print $i;
    NEXT {
        print ";";
    }
}
my $x = 1;				# while
while $x < 4 {
    print $x++;
}
print "\n";

# Crea diferentes funciones (con/sin parámetros y con/sin retorno)
my &func = sub { say "Sin parámetros" }
func;					# Sin parámetros

sub sumar($a, $b) { return $a+$b }
say sumar(32, 10);			# 42

# Crea una clase
class Rectángulo {
    has Int $.longitud = 1;
    has Int $.ancho    = 1;

    method área(--> Int) {
        return $!longitud * $!ancho;
    }
}

my $r1 = Rectángulo.new(longitud => 2, ancho => 3);
say $r1.área();				# 6 

# Muestra el control de excepciones
try die "Sucedió algo malo";
if $! {
    say $!.message;			# Sucedió algo malo
}


