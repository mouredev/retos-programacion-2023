' Ejemplo de uso: 
' cscript arielposada.vbs 4
' Crea una función que dibuje una escalera según su número de escalones.
' - Si el número es positivo, será ascendente de izquiera a derecha.
' - Si el número es negativo, será descendente de izquiera a derecha.
' - Si el número es cero, se dibujarán dos guiones bajos (__).
' 
' Ejemplo: 4
'         _
'       _|       
'     _|
'   _|
' _|
' 
'

Option Explicit


Function DibujarEscalera(n)
    Dim i
    If n = 0 Then
        WScript.Echo "__"
        Exit Function
    End If

    If n > 0 Then
        WScript.Echo String(2 * (n), " ") & "_"
        For i = 1 To n
            WScript.Echo String(2 * (n - i), " ") & "_|"
        Next 
    Else
        n = Abs(n)
        WScript.Echo "_"
        For i = 1 To n 
            WScript.Echo String(2 * i - 1, " ") & "|_"
        Next
    End If
End Function

' Lee la cadena de la línea de comandos
Dim numero
numero = CInt(WScript.Arguments(0))

CALL DibujarEscalera(numero)
