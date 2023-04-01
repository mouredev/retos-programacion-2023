' Ejemplo de uso:
' cscript arielposada.vbs "Candea de ejemplo"

 ' Crea 3 funciones, cada una encargada de detectar si una cadena de
 ' texto es un heterograma, un isograma o un pangrama.
 ' - Debes buscar la definición de cada uno de estos términos.
 ' 

Option Explicit

Function Heterograma(cadena)
    Dim letra, i
    Set letra = CreateObject("Scripting.Dictionary")
    For i = 97 To 122
        letra.Add CStr(i), 0
    Next
    For i = 1 To Len(cadena)
        letra(CStr(Asc(LCase(Mid(cadena, i, 1))))) = 1
    Next
    For i = 97 To 122
        If letra(CStr(i)) = 0 Then
            Heterograma = True
            Exit Function
        End If
    Next
    Heterograma = FAlse
End Function

Function Isograma(cadena)
    Dim letras, i
    letras = ""
    For i = 1 To Len(cadena)
        If InStr(1, letras, LCase(Mid(cadena, i, 1))) > 0 Then
            Isograma = False
            Exit Function
        End If
        letras = letras & LCase(Mid(cadena, i, 1))
    Next
    Isograma = True
End Function

Function Pangrama(cadena)
    Dim letra, i
    Set letra = CreateObject("Scripting.Dictionary")
    For i = 97 To 122
        letra.Add CStr(i), 0
    Next
    For i = 1 To Len(cadena)
        letra(CStr(Asc(LCase(Mid(cadena, i, 1))))) = 1
    Next
    For i = 97 To 122
        If letra(CStr(i)) = 0 Then
            Pangrama = False
            Exit Function
        End If
    Next
    Pangrama = True
End Function


' Lee la cadena de la línea de comandos
Dim cadena
cadena = WScript.Arguments(0)

' Verifica si es un heterograma
Dim esHeterograma
esHeterograma = Heterograma(cadena)
WScript.Echo "Heterograma: " & esHeterograma

' Verifica si es un isograma
Dim esIsograma
esIsograma = Isograma(cadena)
WScript.Echo "Isograma: " & esIsograma

' Verifica si es un pangrama
Dim esPangrama
esPangrama = Pangrama(cadena)
WScript.Echo "Pangrama: " & esPangrama