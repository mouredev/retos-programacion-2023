package main


import (
    "fmt"
    "bufio"
    "log"
    "os"
    "strings"
)



/*
* Escribe un programa que reciba un texto y transforme lenguaje natural a
* "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
*  se caracteriza por sustituir caracteres alfanuméricos.
* - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
*   con el alfabeto y los números en "leet".
*   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
*/





// Creo pares de clave valor, para luego acceder a los respectivos valores de cada letra.
var diccionario map[string]string = map[string]string {
    "0": "o",
    "1": "L",
    "2": "R",
    "3": "E",
    "4": "A",
    "5": "S",
    "6": "b",
    "7": "T",
    "8": "B",
    "9": "g",
    "a": "4",
    "b": "I3",
    "c": "[",
    "d": ")",
    "e": "3",
    "f": "|=",
    "g": "&",
    "h": "#",
    "i": "1",
    "j": ",_|",
    "k": ">|",
    "l": "1",
    "m": "/\\/\\",
    "n": "^/",
    "o": "0",
    "p": "|*",
    "q": "(_,)",
    "r": "I2",
    "s": "5",
    "t": "7",
    "u": "(_)",
    "v": "\\/",
    "w": "\\/\\/",
    "x": "><",
    "y": "j",
    "z": "2",
}



func main() {
    fmt.Println("Escribe el texto que deseas traducir a LEET: ")
    reader := bufio.NewReader(os.Stdin)
    msg, err := reader.ReadString('\n')

    if err != nil {
        log.Fatalf("Error al leer el mensaje. Razon: %v", err)
    }
    fmt.Println(traductor(msg))

    cases()
}


// Funcion que traduce el texto ingresado por el usuario, recorriendo el rango del msg ingresado, pasandolo a lower text y retornando el mensaje ya traducido.
func traductor(msg string) string {
    traduccion := ""
    for _, letra := range msg {
        if l, found := diccionario[strings.ToLower(string(letra))]; 
        found {
            traduccion += l
        } else {
            traduccion += string(letra)
        }
    }
    return traduccion
} 


// Tests - (Realizado por @Lombervid)
func cases() {
    cases := map[string]string {
        "Me gusta este repositorio":    `/\/\3 &(_)574 3573 I23|*05170I210`,
        "Golang":                       `&014^/&`,
        "Hello World!":                 `#3110 \/\/0I21)!`,
        "Einstein":                     `31^/5731^/`,
    }

    for input, want := range cases {
        got := traductor(input)

        if want == got {
            fmt.Printf("Caso con exito ✅: ")
        } else {
            fmt.Printf("Caso fallido ❌: ")
        }

        fmt.Printf("\n\tinput:\t\"%s\"\n\twant:\t\"%s\"\n\tgot:\t\"%s\"\n\n", input, want, got)
    }
}
