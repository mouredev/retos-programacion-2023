' Ejemplo de uso:
'   cscript arielposada.vbs 128
' 
' Crea una función que reciba un número decimal y lo trasforme a Octal
' y Hexadecimal.
' - No está permitido usar funciones propias del lenguaje de programación que
' realicen esas operaciones directamente.
Option Explicit

Function DecimalToOctal(decimalParam)
    Dim octal, i, decimal
    decimal = decimalParam
    octal = ""
    Do While decimal <> 0
        i = decimal Mod 8
        octal = i & octal
        decimal = Int(decimal / 8)
    Loop
    DecimalToOctal = octal
End Function

Function DecimalToHexadecimal(decimalParam)
    Dim hexadecimal, i, decimal
    hexadecimal = ""
    decimal = decimalParam
    Do While decimal <> 0
        i = decimal Mod 16
        Select Case i
            Case 10
                hexadecimal = "A" & hexadecimal
            Case 11
                hexadecimal = "B" & hexadecimal
            Case 12
                hexadecimal = "C" & hexadecimal
            Case 13
                hexadecimal = "D" & hexadecimal
            Case 14
                hexadecimal = "E" & hexadecimal
            Case 15
                hexadecimal = "F" & hexadecimal
            Case Else
                hexadecimal = i & hexadecimal
        End Select
        decimal = Int(decimal / 16)
    Loop
    DecimalToHexadecimal = hexadecimal
End Function

Dim number
If WScript.Arguments.Count = 1 Then
    number = CInt(WScript.Arguments.Item(0))
Else
    WScript.Echo "Debe especificar el número como parámetro de entrada, ejemplo:"
    WScript.Echo "cscript arielposada.vbs 128"
    WScript.Quit
End If

WScript.Echo "Decimal: " & number
WScript.Echo "Octal: " & DecimalToOctal(number)
WScript.Echo "Hexadecimal: " & DecimalToHexadecimal(number)