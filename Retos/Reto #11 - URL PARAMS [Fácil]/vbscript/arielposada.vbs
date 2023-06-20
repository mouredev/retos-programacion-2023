' Ejemplo de uso:
'   cscript arielposada.vbs "https://retosdeprogramacion.com?year=2023&challenge=0"
'
' Dada una URL con parámetros, crea una función que obtenga sus valores.
' No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
'
' Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
' los parámetros serían ["2023", "0"]  

Option Explicit

Dim strUrl, objArgs, arrUrlParts, strParams, arrParamPairs, arrParamValues, strParamPair, strKey

If WScript.Arguments.Count = 1 Then
    strUrl = WScript.Arguments.Item(0)
Else
    WScript.Echo "Debe especificar una URL como parámetro de entrada."
    WScript.Quit
End If


Set objArgs = WScript.CreateObject("Scripting.Dictionary")
arrUrlParts = Split(strUrl, "?")
If UBound(arrUrlParts) > 0 Then
    strParams = arrUrlParts(1)
    arrParamPairs = Split(strParams, "&")
    For Each strParamPair In arrParamPairs
        arrParamValues = Split(strParamPair, "=")
        objArgs.Add arrParamValues(0), arrParamValues(1)
    Next
End If
For Each strKey in objArgs.Keys
    WScript.Echo strKey & " = " & objArgs.Item(strKey)
Next