' Ejemplo de uso:
'   cscript arielposada.vbs
' 
' Crea un programa que simule el comportamiento del sombrero selccionador del
' universo mágico de Harry Potter.
' - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
' - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
' - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
'   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
' - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
'   Por ejemplo, en Slytherin se premia la ambición y la astucia.

Option Explicit
Dim oWSH, vbsInterpreter
Set oWSH = CreateObject("WScript.Shell")
vbsInterpreter = "cscript.exe"

Function ForceConsole()
If InStr(LCase(WScript.FullName), vbsInterpreter) = 0 Then
    oWSH.Run vbsInterpreter & " //NoLogo " & Chr(34) & WScript.ScriptFullName & Chr(34)
    WScript.Quit
End If
End Function

Dim scores(4)
scores(0) = 0
scores(1) = 0
scores(2) = 0
scores(3) = 0

Dim houses(4)
houses(0) = "Gryffindor"
houses(1) = "Hufflepuff"
houses(2) = "Ravenclaw"
houses(3) = "Slytherin"

Dim questions(5,5)
questions(0,0) = "Hogwarts has just loosened the rules on pets allowed in the castle. You choose: "
questions(0,1) = "A lion"
questions(0,2) = "A badger"
questions(0,3) = "An eagle"
questions(0,4) = "A serpent" 

questions(1,0) = "Today’s Astrology lesson is all about the zodiac. Which element does Professor Trelawney match your zodiac sign to?"
questions(1,1) = "Fire"
questions(1,2) = "Earth"
questions(1,3) = "Air"
questions(1,4) = "Water"

questions(2,0) = "Hogwarts house colours run the gamut! But what combination do you like best? "
questions(2,1) = "Red and gold"
questions(2,2) = "Yellow and black"
questions(2,3) = "Blue and bronze"
questions(2,4) = "Green and silver"

questions(3,0) = "It’s spring again, and the Whomping Willow is in full bloom. How do you spend your Saturday afternoons? "
questions(3,1) = "Flying around the castle"
questions(3,2) = "In the gardens, with friends"
questions(3,3) = "At the library, reading"
questions(3,4) = "Experimenting with new potions"


questions(4,0) = "The wand chooses you! Which one of these materials is at the core of yours? "
questions(4,1) = "Phoenix Feather"
questions(4,2) = "Dittany Stock"
questions(4,3) = "Unicorn Tail Hair"
questions(4,4) = "Dragon Heartstring"


Dim i,j,o, house
WScript.Echo "Which Hogwarts House are you in? Answer the questions to find out..."
For i = 0 To 3
    WScript.Echo questions(i,0)
    For j = 1 to 4
        WScript.Echo j & " " & questions(i,j)
    Next
    o = CInt(WScript.StdIn.ReadLine())
    scores(o) = scores(o) = 1
Next

house = 0
For i = 1 To 3
    If scores(house) < scores(i) Then
        house = i
    End If
Next

WScript.Echo "Result:"
WScript.Echo houses(house)