' Ejemplo de uso:
'   cscript arielposada.vbs
' 
' Crea una función que sea capaz de transformar Español al lenguaje básico del universo
' Star Wars: el "Aurebesh".
' - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
' - También tiene que ser capaz de traducir en sentido contrario.
'  
' ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
'
' ¡Que la fuerza os acompañe!

Option Explicit
Dim spaToAurebesh, aurebeshToSpa

Sub InitializeDictionaries()
    Set spaToAurebesh = CreateObject("Scripting.Dictionary")
    Set aurebeshToSpa = CreateObject("Scripting.Dictionary")

    Dim spaChars, aurebeshChars
    ' https://starwars.fandom.com/es/wiki/Aurebesh
    ' Se utilizó de referencia una solución en Python
    spaChars = Array("a", "b", "c", "d", "w", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z", "ch", "ae", "eo", "kh", "ng", "oo", "sh", "th")
    aurebeshChars = Array("aurek", "besh", "cresh", "dorn", "wesk", "esk", "forn", "grek", "herf", "isk", "jenth", "krill", "leth", "mern", "nern", "osk", "peth", "qek", "resh", "senth", "trill", "usk", "vev", "xesh", "yirt", "zerek", "cherek", "enth", "onith", "krenth", "nen", "orenth", "shen", "thesh")

    Dim i
    For i = LBound(spaChars) To UBound(spaChars)
        spaToAurebesh(spaChars(i)) = aurebeshChars(i)
        aurebeshToSpa(aurebeshChars(i)) = spaChars(i)
    Next
End Sub

Function TextToAurebesh(text)
    Dim result, i, found, key
    result = ""
    i = 1
    While i <= Len(text)
        found = False
        For Each key In spaToAurebesh.Keys
            If LCase(Mid(text, i, Len(key))) = key Then
                result = result & spaToAurebesh(key) 
                i = i + Len(key)
                found = True
                Exit For
            End If
        Next
        If Not found Then
            result = result & Mid(text, i, 1)
            i = i + 1
        End If
    Wend
    TextToAurebesh = result
End Function

Function TranslateAurebesh(text, start)
    Dim result, i, key
    If start > Len(text) Then
        TranslateAurebesh = ""
        Exit Function
    End If

    result = ""
    For i = 1 To Len(text) - start + 1
        Dim fragment, foundKey
        fragment = Mid(text, start, i)
        foundKey = ""

        For Each key In aurebeshToSpa.Keys
            If fragment = key Then
                foundKey = key
                Exit For
            End If
        Next

        If foundKey <> "" Then
            result = TranslateAurebesh(text, start + i)
            If result <> "FAIL" Then
                TranslateAurebesh = aurebeshToSpa(foundKey) & result
                Exit Function
            End If
        End If
    Next
    TranslateAurebesh = "FAIL"
End Function

Function AurebeshToText(aurebesh)
    Dim result
    result = TranslateAurebesh(aurebesh, 1)
    If result = "FAIL" Then
        result = ""
    End If
    AurebeshToText = result
End Function

' Ejemplo de uso
InitializeDictionaries()

Dim text, aurebesh 
text = "automatizado"
WScript.Echo "Texto original: " & text
aurebesh = TextToAurebesh(text)
WScript.Echo "Texto en Aurebesh: " & aurebesh
WScript.Echo "Texto original traducido nuevamente: " & AurebeshToText(aurebesh)