' Ejemplo de uso: 
' cscript arielposada.vbs "6-666-88-777-33-3-33-888"
' Los primeros dispositivos móviles tenían un teclado llamado T9
' con el que se podía escribir texto utilizando únicamente su
' teclado numérico (del 0 al 9).
' Crea una función que transforme las pulsaciones del T9 a su
' representación con letras.
' - Debes buscar cuál era su correspondencia original.
' - Cada bloque de pulsaciones va separado por un guión.
' - Si un bloque tiene más de un número, debe ser siempre el mismo.
' - Ejemplo:
'     Entrada: 6-666-88-777-33-3-33-888
'     Salida: MOUREDEV
Option Explicit

Dim inputStr, outputStr

inputStr = WScript.Arguments(0)
outputStr = T9toText(inputStr)
WScript.Echo outputStr

Function T9toText(inputStr)
    Dim t9Dict, blocks, i, block, key, timesPressed, charIndex, charToAdd
    Set t9Dict = CreateObject("Scripting.Dictionary")
    
    t9Dict.Add "2", "ABC"
    t9Dict.Add "3", "DEF"
    t9Dict.Add "4", "GHI"
    t9Dict.Add "5", "JKL"
    t9Dict.Add "6", "MNO"
    t9Dict.Add "7", "PQRS"
    t9Dict.Add "8", "TUV"
    t9Dict.Add "9", "WXYZ"
    
    blocks = Split(inputStr, "-")
    T9toText = ""
    
    For i = 0 To UBound(blocks)
        block = blocks(i)
        key = Left(block, 1)
        timesPressed = Len(block)
        charIndex = (timesPressed - 1) Mod Len(t9Dict(key))
        charToAdd = Mid(t9Dict(key), charIndex + 1, 1)
        T9toText = T9toText & charToAdd
    Next
End Function
