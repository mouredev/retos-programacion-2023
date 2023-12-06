 # Escribe un programa que reciba un texto y transforme lenguaje natural a
 # "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 #  se caracteriza por sustituir caracteres alfanuméricos.
 # - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 #  con el alfabeto y los números en "leet".
 #   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

$datos = Read-Host -Prompt "Escribe el texto que quieras traducir"
$resultado = '' 
for ($counter = 0; $counter -lt $datos.Length; $counter ++){
    Switch ($datos[$counter]){
        'a' { $resultado += '4'}
        'b' { $resultado += '8'}
        'c' { $resultado += '['}
        'd' { $resultado += '|)'}
        'e' { $resultado += '3'}
        'f' { $resultado += '|='}
        'g' { $resultado += '&'}
        'h' { $resultado += '#'}
        'i' { $resultado += '1'}
        'j' { $resultado += ']'}
        'k' { $resultado += '|<'}
        'l' { $resultado += '1'}
        'm' { $resultado += '/\/\'}
        'n' { $resultado += '|\|'}
        'o' { $resultado += '0'}
        'p' { $resultado += '|*'}
        'q' { $resultado += '9'}
        'r' { $resultado += '|2'}
        's' { $resultado += '5'}
        't' { $resultado += '7'}
        'u' { $resultado += '|_|'}
        'v' { $resultado += '\/'}
        'w' { $resultado += '\/\/'}
        'x' { $resultado += '><'}
        'y' { $resultado += 'j'}
        'z' { $resultado += '2'}
        '1' { $resultado += 'L'}
        '2' { $resultado += 'R'}
        '3' { $resultado += 'E'}
        '4' { $resultado += 'A'}
        '5' { $resultado += 'S'}
        '6' { $resultado += 'G'}
        '7' { $resultado += 'T'}
        '8' { $resultado += 'B'}
        '9' { $resultado += 'q'}
        '0' { $resultado += 'O'}
        default {$resultado += $datos[$counter]}
    }
}
Write-Host $resultado 