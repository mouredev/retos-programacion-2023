#!/usr/bin/perl -s
#
# Reto #3: EL GENERADOR DE CONTRASEÑAS
#### Dificultad: Media | Publicación: 16/01/23 | Corrección: 23/01/23
#
## Enunciado
#
# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
# - Longitud: Entre 8 y 16.
# - Con o sin letras mayúsculas.
# - Con o sin números.
# - Con o sin símbolos.
# (Pudiendo combinar todos estos parámetros entre ellos)
#
# Joaquín Ferrero. 20230117
#
use v5.28;
use utf8;
use open 'locale';

### Argumentos ##########################################
our ($l, $m, $n, $s);					# opciones por línea de comandos

if (length($l.$m.$n.$s) == 0				# si no se indicó ninguna opción,
    or not $l						# ni siquiera la obligatoria,
    or ($l < 8 or $l > 16)				# o no está entre 8 y 16,
) {							 
    die							# terminamos con el mensaje de ayuda
"Uso: $0 -l=<longitud> [-m] [-n] [-s]
    -l : longitud de la contraseña, entre 8 y 16 caracteres
    -m : incluir letras mayúsculas
    -n : incluir números
    -s : incluir símbolos\n";
}

### Caracteres posibles #################################
my @números    =  0  ..  9;
my @letras     = 'a' .. 'z';
my @mayúsculas = 'A' .. 'Z';
my @símbolos   = ('!','$','%','&','*','+','-','.','/',':',';','<','>','=','_','@');

my @caracteres_posibles = (
    @letras,
    ($m ? @mayúsculas : ()),
    ($n ? @números    : ()),
    ($s ? @símbolos   : ()),
);

### Generación de la contraseña #########################
my $contraseña = join "", map { $caracteres_posibles[ rand @caracteres_posibles ] } 1 .. $l;

say $contraseña;

__END__
