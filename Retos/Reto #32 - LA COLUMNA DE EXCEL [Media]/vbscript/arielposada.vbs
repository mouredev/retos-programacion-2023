' Ejemplo de uso: 
' cscript arielposada.vbs 
' Crea una función que calcule el número de la columna de una hoja de Excel
' teniendo en cuenta su nombre.
' - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
' - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
Option Explicit

Dim columnNames, i

WScript.Echo ColumnNameToNumber("A")
WScript.Echo ColumnNameToNumber("Z")
WScript.Echo ColumnNameToNumber("AA")
WScript.Echo ColumnNameToNumber("CA")

Function ColumnNameToNumber(columnName)
    Dim i, char, value
    value = 0
    
    For i = 1 To Len(columnName)
        char = Mid(columnName, i, 1)
        value = value * 26 + (Asc(char) - Asc("A") + 1)
    Next
    
    ColumnNameToNumber = value
End Function
