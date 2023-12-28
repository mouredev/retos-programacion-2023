' Ejemplo de uso: 
' cscript arielposada.vbs
' Crea tres test sobre el reto 12: "Viernes 13".
' - Puedes copiar una solución ya creada por otro usuario en
'   el lenguaje que estés utilizando.
' - Debes emplear un mecanismo de ejecución de test que posea
'   el lenguaje de programación que hayas seleccionado.
' - Los tres test deben de funcionar y comprobar
'   diferentes situaciones (a tu elección).

Option Explicit
Dim month, year

' Tomando del código del reto 12 en VBScript
Function Friday13(month, year)
    Dim date
    date = CDate("13/" & month & "/" & year)
    If Weekday(date) = 6 Then
        Friday13 = True
    Else
        Friday13 = False
    End If
End Function

If Friday13(8, 2021) Then
    WScript.Echo "Test 1 Passed: 13 de agosto de 2021 fue un viernes 13."
Else
    WScript.Echo "Test 1 Failed: 13 de agosto de 2021 fue un viernes 13."
End If

If Friday13(9, 2019) Then
    WScript.Echo "Test 2 Passed: 13 de septiembre de 2019 fue un viernes 13."
Else
    WScript.Echo "Test 2 Failed: 13 de septiembre de 2019 fue un viernes 13."
End If

If Not Friday13(2, 2021) Then
    WScript.Echo "Test 3 Passed: 13 de febrero de 2021 no fue un viernes 13."
Else
    WScript.Echo "Test 3 Failed: 13 de febrero de 2021 no fue un viernes 13."
End If