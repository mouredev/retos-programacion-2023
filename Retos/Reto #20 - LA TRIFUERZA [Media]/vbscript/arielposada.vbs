' Ejemplos de uso: 
' cscript arielposada.vbs 2
' cscript arielposada.vbs 5
'	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
'
' Crea un programa que dibuje una Trifuerza de "Zelda"
' formada por asteriscos.
' - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
' - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
'
' Ejemplo: Trifuerza 2
' 
'   *
'  ***
' *   *
'*** ***

Option Explicit

Dim n, i, j, espacio

If WScript.Arguments.Count = 0 Then
    WScript.Quit
End If

n = CInt(WScript.Arguments(0))

For i = 1 To n
    For espacio = 1 To n + n - i
        WScript.StdOut.Write " "
    Next
    For j = 1 To 2 * i - 1
        WScript.StdOut.Write "*"
    Next
    WScript.Echo ""
Next

For i = 1 To n
    For espacio = 1 To n - i
        WScript.StdOut.Write " "
    Next
    For j = 1 To 2 * i - 1
        WScript.StdOut.Write "*"
    Next
    For espacio = 1 To 2 * (n - i) + 1
        WScript.StdOut.Write " "
    Next
    For j = 1 To 2 * i - 1
        WScript.StdOut.Write "*"
    Next
    WScript.Echo ""
Next