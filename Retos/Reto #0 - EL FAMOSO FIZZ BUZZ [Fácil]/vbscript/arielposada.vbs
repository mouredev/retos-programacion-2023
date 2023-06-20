' Ejemplo de uso:
' cscript arielposada.vbs 

 ' Escribe un programa que muestre por consola (con un print) los
 ' números de 1 a 100 (ambos incluidos y con un salto de línea entre
 ' cada impresión), sustituyendo los siguientes:
 ' - Múltiplos de 3 por la palabra "fizz".
 ' - Múltiplos de 5 por la palabra "buzz".
 ' - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 ' 

Option Explicit

Dim i 
WScript.Echo "Fizz Buzz"

For i = 1 to 100
    If (i Mod 3) = 0 Then
        If (i Mod 5) = 0 Then
            WScript.Echo "fizzbuzz"
        Else
            WScript.Echo "fizz"
        End If
    ElseIf (i Mod 5) = 0 Then
        WScript.Echo "buzz"
    Else 
        WScript.Echo i
    End If
Next