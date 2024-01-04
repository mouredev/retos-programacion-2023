function ConvertTo-Leet { # Creamos la función "ConvertTo-Leet"
    param ( # Definimos los parámetros que recibirá la función
        [Parameter(Mandatory=$true)] # Caracteristicas del parametro. En este caso, el parámetro de abajo es obligatorio
        [string]$Text # El parámetro "Text" es de tipo "string"
    )

    $LeetText = ""  # Creamos una variable vacía para almacenar el texto convertido

    foreach ($char in $Text) {  # Recorremos cada caracter del texto
                                              # $char es la variable que contiene el caracter actual
                                              # $Text es la variable que contiene el texto que recibimos como parámetro
        switch ($char.ToLower()) {  # Comparamos el caracter actual con cada uno de los caracteres que queremos reemplazar
            "a" { $LeetText += "4" } # Si el caracter actual es igual a alguno de los caracteres que queremos reemplazar, lo reemplazamos
            "e" { $LeetText += "3" }
            "i" { $LeetText += "1" }
            "o" { $LeetText += "0" }
            "s" { $LeetText += "5" }
            "t" { $LeetText += "7" }
            default { $LeetText += $char } # Si el caracter actual no es igual a ninguno de los caracteres que queremos reemplazar, lo dejamos igual
        }
    }

    return $LeetText # Retornamos el texto convertido
}

ConvertTo-Leet -text "Hola Mundo" # Llamamos a la función "ConvertTo-Leet" y le pasamos el texto que queremos convertir