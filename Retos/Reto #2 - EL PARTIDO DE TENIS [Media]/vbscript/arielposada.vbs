' Ejemplo de uso:
'   cscript arielposada.vbs "P1,P1,P2,P2,P1,P2,P1,P1"
' 
' Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
' El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
' gane cada punto del juego.
' 
' - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
' - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
'   15 - Love
'   30 - Love
'   30 - 15
'   30 - 30
'   40 - 30
'   Deuce
'   Ventaja P1
'   Ha ganado el P1
' - Si quieres, puedes controlar errores en la entrada de datos.   
' - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
' 

Option Explicit

Dim input
If WScript.Arguments.Count = 1 Then
    input = WScript.Arguments(0)
Else
    WScript.Echo "Error: Debe ingresar una cadena de jugadores separada por coma (Ej: P1,P2)."
    WScript.Quit
End If

'Inicializar variables
Dim player1, player2
Dim score1, score2
player1 = "P1"
player2 = "P2"
score1 = 0
score2 = 0

Function PrintScore()
    Select Case score1
        Case 0
            WScript.Echo "Love - " & ScoreText(score2)
        Case 15
            WScript.Echo "15 - " & ScoreText(score2)
        Case 30
            WScript.Echo "30 - " & ScoreText(score2)
        Case 40
            If score2 = 40 Then
                WScript.Echo "Deuce"
            ElseIf score2 < 40 Then
                WScript.Echo "40 - " & ScoreText(score2)
            Else
                WScript.Echo "Ventaja " & player2
            End If
        Case Else
            If score2 = 40 Then
                WScript.Echo "Ventaja " & player1
            Else
                WScript.Echo player1 & " ha ganado."
            End If
    End Select
End Function

Function ScoreText(score)
    Select Case score
        Case 0
            ScoreText = "Love"
        Case 15
            ScoreText = "15"
        Case 30
            ScoreText = "30"
        Case 40
            ScoreText = "40"
        Case Else
            ScoreText = ""
    End Select
End Function

Dim plays, play
plays = Split(input, ",")
For Each play In plays
    Select Case play
        Case player1
            score1 = score1 + 15
        Case player2
            score2 = score2 + 15
        Case Else
            WScript.Echo "Error: La cadena de jugadas es inválida."
            WScript.Quit
    End Select
    If (score1 = 45 And score2 < 40) Or (score2 = 45 And score1 < 40) Then
        score1 = 40
        score2 = 40
    ElseIf score1 = 60 Or score2 = 60 Then
        Exit For
    End If
    PrintScore()
Next