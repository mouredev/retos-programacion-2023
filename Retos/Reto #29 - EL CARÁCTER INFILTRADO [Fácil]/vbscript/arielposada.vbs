' Ejemplo de uso: 
' cscript arielposada.vbs 
' Crea una función que reciba dos cadenas de texto casi iguales,
' a excepción de uno o varios caracteres. 
' La función debe encontrarlos y retornarlos en formato lista/array.
' - Ambas cadenas de texto deben ser iguales en longitud.
' - Las cadenas de texto son iguales elemento a elemento.
' - No se pueden utilizar operaciones propias del lenguaje
'   que lo resuelvan directamente.
' 
' Ejemplos:
' - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
' - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
Option Explicit

Dim str1, str2, result

str1 = "Me llamo mouredev"
str2 = "Me llemo mouredov"
result = FindDifferences(str1, str2)
WScript.Echo "Diferencias: " & Join(result, ", ")

str1 = "Me llamo.Brais Moure"
str2 = "Me llamo brais moure"
result = FindDifferences(str1, str2)
WScript.Echo "Diferencias: " & Join(result, ", ")

Function FindDifferences(str1, str2)
    Dim i, differences()
    Dim count

    count = 0
    For i = 1 To Len(str1)
        If Mid(str1, i, 1) <> Mid(str2, i, 1) Then
            ReDim Preserve differences(count)
            differences(count) = Mid(str2, i, 1)
            count = count + 1
        End If
    Next

    FindDifferences = differences
End Function
