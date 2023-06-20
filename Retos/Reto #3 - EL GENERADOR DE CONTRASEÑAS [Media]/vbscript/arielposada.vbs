' Ejemplo de uso:
'   cscript arielposada.vbs 8 12 True True True
' 
' Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
' Podrás configurar generar contraseñas con los siguientes parámetros:
' - Longitud: Entre 8 y 16.
' - Con o sin letras mayúsculas.
' - Con o sin números.
' - Con o sin símbolos.
' (Pudiendo combinar todos estos parámetros entre ellos)


Option Explicit

If WScript.Arguments.Count <> 5 Then
    WScript.Echo "La entrada debe tener el siguiente formato: minLength maxLength hasUpperCase hasNumbers hasSymbols"
    WScript.Echo "Ejemplo:"
    WScript.Echo "cscript arielposada.vbs 8 12 True True True"
    WScript.Quit
End If

Dim min_length, max_length, has_uppercase, has_number, has_special

min_length = WScript.Arguments(0)
max_length = WScript.Arguments(1)
has_uppercase = CBool(WScript.Arguments(2))
has_number = CBool(WScript.Arguments(3))
has_special = CBool(WScript.Arguments(4))

Dim has_uppercase_found, has_number_found, has_special_found

has_uppercase_found = False
has_number_found = False
has_special_found = False

Dim password, length, i 
Do 
    password = ""
    length = Int((max_length - min_length + 1) * Rnd + min_length)
    For i = 1 To length
        Randomize
        Select Case Int(3 * Rnd)
            Case 0  
                password = password & Chr(Int(26 * Rnd) + 97)
            Case 1  
                If has_uppercase And Not has_uppercase_found Then
                    password = password & Chr(Int(26 * Rnd) + 65)
                    has_uppercase_found = True
                Else
                    password = password & Chr(Int(26 * Rnd) + 97)
                End If
            Case 2  
                If has_number And Not has_number_found Then
                    password = password & Chr(Int(10 * Rnd) + 48)
                    has_number_found = True
                ElseIf has_special And Not has_special_found Then
                    password = password & Chr(Int(15 * Rnd) + 33)
                    has_special_found = True
                Else
                    password = password & Chr(Int(26 * Rnd) + 97)
                End If
        End Select
    Next
Loop Until has_uppercase = has_uppercase_found And has_number = has_number_found And has_special = has_special_found


WScript.Echo "Password generado: " 
WScript.Echo password

