' Ejemplo de uso: 
' cscript arielposada.vbs 
' Crea una función que sea capaz de leer el número representado por el ábaco.
' - El ábaco se representa por un array con 7 elementos.
' - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
'   para las cuentas y una secuencia de "---" para el alambre.
' - El primer elemento del array representa los millones, y el último las unidades.
' - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
' Ejemplo de array y resultado:
' ["O---OOOOOOOO",
'  "OOO---OOOOOO",
'  "---OOOOOOOOO",
'  "OO---OOOOOOO",
'  "OOOOOOO---OO",
'  "OOOOOOOOO---",
'  "---OOOOOOOOO"]
'  
'  Resultado: 1.302.790

Option Explicit

Dim abacus, result

abacus = Array( _
    "O---OOOOOOOO", _
    "OOO---OOOOOO", _
    "---OOOOOOOOO", _
    "OO---OOOOOOO", _
    "OOOOOOO---OO", _
    "OOOOOOOOO---", _
    "---OOOOOOOOO" _
)

result = AbacusToNumber(abacus)
WScript.Echo result

Function AbacusToNumber(abacus)
    Dim i, line, count, number
    number = ""
    
    For i = 0 To UBound(abacus)
        line = abacus(i)
        count = InStr(line, "---") - 1
        number = number & CStr(count)
    Next
    
    AbacusToNumber = FormatNumber(number, 0, -1, -1, -1)
End Function
