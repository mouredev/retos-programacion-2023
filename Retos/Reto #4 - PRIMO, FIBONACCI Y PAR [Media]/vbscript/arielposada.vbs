' Ejemplo de uso:
'   cscript arielposada.vbs 7
' 
' Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
' Ejemplos:
' - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
' - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"


Option Explicit

If WScript.Arguments.Count <> 1 Then
    WScript.Echo "La entrada debe de tener un número"
    WScript.Echo "Ejemplo:"
    WScript.Echo "cscript arielposada.vbs 7"
    WScript.Quit
End If

Dim num, i, limite, fib1, fib2, fib, esPrimo, salida

num = CInt(WScript.Arguments.Item(0))

salida = num & ""

esPrimo = True
limite = Int(num/2) + 1
For i = 2 To limite
    If num Mod i = 0 Then
        esPrimo = False
        Exit For
    End If
Next
If esPrimo Or num = 2 Then
    salida = salida & " es primo"
Else
    salida = salida & " no es primo"
End If

fib1 = 0
fib2 = 1
fib = fib1 + fib2
While fib < num
    fib1 = fib2
    fib2 = fib
    fib = fib1 + fib2
Wend
If fib = num Then
    salida = salida & ", es fibonacci"
Else
    salida = salida & ", no es fibonacci"
End If

If num Mod 2 = 0 Then
    salida = salida & " y es par"
Else
    salida = salida & " y es impar"
End If

WScript.Echo salida