' Ejemplo de uso: 
' cscript arielposada.vbs 
' Crea una función que reciba una expresión matemática (String)
' y compruebe si es correcta. Retornará true o false.
' - Para que una expresión matemática sea correcta debe poseer
'   un número, una operación y otro número separados por espacios.
'   Tantos números y operaciones como queramos.
' - Números positivos, negativos, enteros o decimales.
' - Operaciones soportadas: + - * / % 
' Ejemplos:
' "5 + 6 / 7 - 4" -> true
' "5 a 6" -> false
Option Explicit

Function IsMathExpressionValid(expression)
    Dim regexPattern
    Dim objRegEx
    Dim objMatches

    regexPattern = "^(\s*-?\d+(\.\d+)?\s*[\+\-\*\/\%]\s*)*-?\d+(\.\d+)?\s*$"

    Set objRegEx = New RegExp
    objRegEx.Pattern = regexPattern
    objRegEx.Global = True

    Set objMatches = objRegEx.Execute(expression)

    If objMatches.Count >= 1 Then
        IsMathExpressionValid = True
    Else
        IsMathExpressionValid = False
    End If

    Set objMatches = Nothing
    Set objRegEx = Nothing
End Function

Dim testExpression1, testExpression2
testExpression1 = "5 + 6 / 7 - 4"
testExpression2 = "5 a 6"

WScript.Echo testExpression1 & " -> " & IsMathExpressionValid(testExpression1)
WScript.Echo testExpression2 & " -> " & IsMathExpressionValid(testExpression2)


