' Ejemplo de uso: 
' cscript arielposada.vbs 14
' Crea un programa que encuentre y muestre todos los pares de números primos
' gemelos en un rango concreto.
' El programa recibirá el rango máximo como número entero positivo.
' 
' - Un par de números primos se considera gemelo si la diferencia entre
'   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
'
' - Ejemplo: Rango 14
'   (3, 5), (5, 7), (11, 13)

Option Explicit

Dim maxRange, i
Dim isPrime1, isPrime2

If WScript.Arguments.Count = 0 Then
    WScript.Quit
End If

maxRange = CInt(WScript.Arguments(0))

For i = 2 To maxRange - 2
    isPrime1 = IsPrime(i)
    isPrime2 = IsPrime(i + 2)
    If isPrime1 And isPrime2 Then
        WScript.Echo "(" & i & ", " & i + 2 & ")"
    End If
Next

Function IsPrime(num)
    Dim j
    If num < 2 Then
        IsPrime = False
        Exit Function
    End If
    For j = 2 To Sqr(num)
        If num Mod j = 0 Then
            IsPrime = False
            Exit Function
        End If
    Next
    IsPrime = True
End Function
