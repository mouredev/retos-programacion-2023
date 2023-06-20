' Ejemplo de uso:
'   cscript arielposada.vbs 1 2023
'
' Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
' - La función recibirá el mes y el año y retornará verdadero o falso.

Option Explicit
Dim month, year

If WScript.Arguments.Count = 2 Then
    month = CInt(WScript.Arguments.Item(0))
    year = CInt(WScript.Arguments.Item(1))
Else
    WScript.Echo "La entrada debe especificar el mes y el año"
    WScript.Echo "Ejemplo:"
    WScript.Echo "cscript arielposada.vbs 1 2023"
    WScript.Quit
End If

Function Friday13(month, year)
    Dim date
    date = CDate("13/" & month & "/" & year)
    If Weekday(date) = 6 Then
        Friday13 = True
    Else
        Friday13 = False
    End If
End Function

WScript.Echo "Viernes 13: " & Friday13(month, year)