#!/usr/bin/env raku
#
# Terna pitagórica
#
# Crea una función que encuentre todos las ternas pitagóricas
# menores o iguales a un número dado.
#
# - Una terna pitagórica es un conjunto ordenado de tres números enteros positivos
#   a, b, c, y son solución de la ecuación diofántica cuadrática
#   a² + b² = c²
# - La función recibe el número máximo que puede aparecer en la terna.
#
# Ejemplo:
#   Las ternas menores o iguales a 10 son (3, 4, 5) y (6, 8, 10).
#
# Joaquín Ferrero, 20231005
#
use v6;


my @ternas = ternas(100);

for @ternas -> @terna {
    my ($a, $b, $c) = @terna;

    say "($a, $b, $c):\t", $a², " + ", $b², " = ", $c²;
}
say "Total ", @ternas.elems, " ternas";

sub ternas($máximo) {
    my %ternas_vistas;

    # Búsqueda exhaustiva, de todas las combinaciones
    my @ternas = gather {
        for 1 .. $máximo -> $m {
            for $m .. $máximo -> $n {
                next if %ternas_vistas{"$m;$n"};	# sólo ternas únicas

                my $o = ($m² + $n²).sqrt;

                next if $o > $máximo;			# fuera del límite
                next if $o.Int != $o;			# no es terna

                # generación de ternas no primitivas
                for 1 .. $máximo -> $d {
                    my $m2 = $d * $m;
                    my $n2 = $d * $n;
                    my $o2 = $d * $o;
                    last if $o2 > $máximo or $m2 > $máximo or $n2 > $máximo;

                    take [ $m2, $n2, $o2 ];

                    %ternas_vistas{"$m2;$n2"}++;
                }
            }
        }
    }

    return @ternas;
}

=finish

sub ternas_pitagóricas_babilónicas($máximo) {

    # Método babilónico
    # a = m²-n²
    # b = 2mn
    # c = m²+n²
    # siendo m>n

    # Doble bucle para los valores de m y n
    my @ternas = gather {
        for 1 ..^ $máximo -> $n {
            for $n ^.. $máximo -> $m {
                my $a = $m² - $n²;
                my $b = 2 × $m × $n;
                my $c = $m² + $n²;

                next if $a > $máximo  or  $b > $máximo  or  $c > $máximo;
                
                take [ $a, $b, $c ];
            }
        }
    }

    return @ternas;
}

