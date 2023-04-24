#!/usr/bin/env raku
#
# Translación de un texto a Leet Speek
#
# Joaquín Ferrero, 20220103
#

for @*ARGS -> $texto {
    say $texto.trans(
            "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
         => "OLREASbTBg@6¢>ëƒ9#1;<!m^Ø?&®27µvพ×¥s48[)3v6#|;<£MทQ?2Я5+บVพЖЧ%"
    );
}
