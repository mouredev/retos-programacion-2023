' Ejemplo de uso: 
' cscript arielposada.vbs 
' Crea un programa que analice texto y obtenga:
' - Número total de palabras.
' - Longitud media de las palabras.
' - Número de oraciones del texto (cada vez que aparecen un punto).
' - Encuentre la palabra más larga.
' Todo esto utilizando un único bucle.

Option Explicit

Dim texto, palabras, i, numPalabras, longitudTotal, numOraciones, palabra, palabraMasLarga

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

numPalabras = 0
longitudTotal = 0
numOraciones = 0
palabraMasLarga = ""

palabras = Split(texto, " ")

For i = 0 To UBound(palabras)
    palabra = palabras(i)
    numPalabras = numPalabras + 1
    longitudTotal = longitudTotal + Len(palabra)
    
    If InStr(palabra, ".") > 0 Then
        numOraciones = numOraciones + 1
    End If
    
    If Len(palabra) > Len(palabraMasLarga) Then
        palabraMasLarga = palabra
    End If
Next

WScript.Echo "Numero total de palabras: " & numPalabras
WScript.Echo "Longitud media de las palabras: " & (longitudTotal / numPalabras)
WScript.Echo "Numero de oraciones: " & numOraciones
WScript.Echo "Palabra mas larga: " & palabraMasLarga