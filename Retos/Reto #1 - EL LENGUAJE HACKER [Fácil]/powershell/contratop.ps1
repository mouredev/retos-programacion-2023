function ConvertTo-Leet { # Definir la funcion "ConvertTo-Leet"
    param( # Definir los parametros de la funcion
        [Parameter(Mandatory=$true)] # Se establece el parametro como obligatorio
        [string]$texto # El parametro es de tipo string, se llama -texto y se almacena en la variable $texto
    )

    # Definir un hash table con las conversiones leet
    $leetTable = @{
        'a' = '4'
        'e' = '3'
        'i' = '1'
        'o' = '0'
        's' = '5'
        't' = '7'
    }

    # Convertir el texto a minusculas
    $texto = $texto.ToLower()

    # Recorrer el hash table y reemplazar las letras
    foreach ($letra in $leetTable.Keys) { # por cada $letra en las llaves del hash table
        $texto = $texto.Replace($letra, $leetTable[$letra]) # reemplazar la letra por el valor del hash table
    }

    # Devolver el texto convertido
    return $texto
}

# Ejemplo de uso ###

# Definir el texto a convert
$miTexto = "Hola, esto es un ejemplo de lenguaje leet."

# Llamamos a la funcion ConvertTo-Leet y le especificamos el parametro -texto con el valor de $miTexto
# que posteriormente se almacena en la variable $textoLeet el resultado
$textoLeet = ConvertTo-Leet -Texto $miTexto

# Mostramos el resultado con Write-Host
Write-Host $textoLeet
