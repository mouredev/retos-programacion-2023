#!/usr/bin/perl
#
# Translación de un texto a Leet Speek
#
# Joaquín Ferrero, 20220102
#
use v5.24;
use utf8;
use open IO => qw<:utf8 :std>;

while (my $línea = <>) {                                                    # el texto llega por la entrada estándar
    $línea =~ tr                                                            # transliteración
        {0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ}    
        {OLREASbTBg@6¢>ëƒ9#1;<!m^Ø?&®27µvพ×¥s48[)3v6#|;<£MทQ?2Я5+บVพЖЧ%};

    print $línea;                                                           # Impresión
}

