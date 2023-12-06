' Ejemplo de uso: 
' cscript arielposada.vbs
' Crea un programa que realize el cifrado César de un texto y lo imprima.
' También debe ser capaz de descifrarlo cuando así se lo indiquemos.
'
' Te recomiendo que busques información para conocer en profundidad cómo
' realizar el cifrado. Esto también forma parte del reto.
Option Explicit

Dim strText, intShift, strResult

strText = "hola mundo"
intShift = 5

strResult = CaesarCipher(strText, intShift)
WScript.Echo "Texto cifrado: " & strResult

strResult = CaesarCipher(strResult, -intShift)
WScript.Echo "Texto descifrado: " & strResult

Function CaesarCipher(text, shift)
    Dim i, char, cipheredText
    cipheredText = ""
    For i = 1 To Len(text)
        char = Mid(text, i, 1)
        If IsLetter(char) Then
            cipheredText = cipheredText & ShiftLetter(char, shift)
        Else
            cipheredText = cipheredText & char
        End If
    Next
    CaesarCipher = cipheredText
End Function

Function IsLetter(c)
    IsLetter = InStr("abcdefghijklmnopqrstuvwxyz", c) > 0
End Function

Function ShiftLetter(letter, shift)
    Dim charCode
    charCode = Asc(letter)
    If charCode >= 97 And charCode <= 122 Then 
        ShiftLetter = Chr(((charCode - 97 + shift) Mod 26) + 97)
    Else
        ShiftLetter = letter
    End If
End Function
