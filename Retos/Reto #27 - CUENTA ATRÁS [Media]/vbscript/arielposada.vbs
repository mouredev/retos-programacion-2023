' Ejemplo de uso: 
' cscript arielposada.vbs 5 2
' Crea una función que reciba dos parámetros para crear una cuenta atrás.
' - El primero, representa el número en el que comienza la cuenta.
' - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
' - Sólo se aceptan números enteros positivos.
' - El programa finaliza al llegar a cero.
' - Debes imprimir cada número de la cuenta atrás.
Option Explicit

Dim startNumber, delay, args

Set args = WScript.Arguments

If args.Count <> 2 Then
    WScript.Quit
End If

startNumber = CInt(args(0))
delay = CInt(args(1))

If startNumber <= 0 Or delay <= 0 Then
    WScript.Quit
End If

Do While startNumber >= 0
    WScript.Echo startNumber
    WScript.Sleep delay * 1000
    startNumber = startNumber - 1
Loop
