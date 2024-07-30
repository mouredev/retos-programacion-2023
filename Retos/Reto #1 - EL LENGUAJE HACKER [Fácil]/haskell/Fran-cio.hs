module Fran_cio where
-- /*
--  * Escribe un programa que reciba un texto y transforme lenguaje natural a
--  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
--  *  se caracteriza por sustituir caracteres alfanuméricos.
--  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
--  *   con el alfabeto y los números en "leet".
--  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
--  */



toLeet :: Char -> String
toLeet 'a' = "4"
toLeet 'A' = "4"
toLeet 'b' = "I3"
toLeet 'B' = "I3"
toLeet 'c' = "["
toLeet 'C' = "["
toLeet 'd' = ")"
toLeet 'D' = ")"
toLeet 'e' = "3"
toLeet 'E' = "3"
toLeet 'f' = "|="
toLeet 'F' = "|="
toLeet 'g' = "&"
toLeet 'G' = "&"
toLeet 'h' = "#"
toLeet 'H' = "#"
toLeet 'i' = "1"
toLeet 'I' = "1"
toLeet 'j' = ",_|"
toLeet 'J' = ",_|"
toLeet 'k' = ">|"
toLeet 'K' = ">|"
toLeet 'l' = "1"
toLeet 'L' = "1"
toLeet 'm' = "/\\/\\"
toLeet 'M' = "/\\/\\"
toLeet 'n' = "^/"
toLeet 'N' = "^/"
toLeet 'o' = "0"
toLeet 'O' = "0"
toLeet 'p' = "|*"
toLeet 'P' = "|*"
toLeet 'q' = "(_,)"
toLeet 'Q' = "(_,)"
toLeet 'r' = "|2"
toLeet 'R' = "|2"
toLeet 's' = "5"
toLeet 'S' = "5"
toLeet 't' = "7"
toLeet 'T' = "7"
toLeet 'u' = "(_)"
toLeet 'U' = "(_)"
toLeet 'v' = "\\/"
toLeet 'V' = "\\/"
toLeet 'w' = "\\/\\/"
toLeet 'W' = "\\/\\/"
toLeet 'x' = "><"
toLeet 'X' = "><"
toLeet 'y' = "j"
toLeet 'Y' = "j"
toLeet 'z' = "2"
toLeet 'Z' = "2"
toLeet c   = [c]

main :: String
main = concatMap toLeet "/*\n  * Escribe un programa que reciba un texto y transforme lenguaje natural a\n  * \"lenguaje hacker\" (conocido realmente como \"leet\" o \"1337\"). Este lenguaje\n  *  se caracteriza por sustituir caracteres alfanuméricos.\n  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) \n  *   con el alfabeto y los números en \"leet\".\n  *   (Usa la primera opción de cada transformación. Por ejemplo \"4\" para la \"a\")\n  *"
