' Ejemplo de uso:
'   cscript arielposada.vbs
' 
' Crea un programa que calcule quien gana más partidas al piedra,
' papel, tijera, lagarto, spock.
' - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
' - La función recibe un listado que contiene pares, representando cada jugada.
' - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
'   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
' - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
' - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
'/

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

Dim player1Score
Dim player2Score
player1Score = 0
player2Score = 0

Call ForceConsole

WScript.Echo "Escriba los turnos de los jugadores con cada selección"
WScript.Echo "Ejemplo: Spock,Spock"
Do
    Dim input
    WScript.Echo "Escriba el siguiente turno, o espacio para terminar"
    input = WScript.StdIn.ReadLine()
    If input = "" Then
        Exit Do
    End If
    
    Dim round
    round = Split(input, ",")
    
    Dim player1
    Dim player2
    player1 = round(0)
    player2 = round(1)
    
    If player1 = player2 Then
        
    ElseIf player1 = "Rock" Then
        If player2 = "Scissors" Or player2 = "Lizard" Then
            player1Score = player1Score + 1 
        Else
            player2Score = player2Score + 1 
        End If
    ElseIf player1 = "Paper" Then
        If player2 = "Rock" Or player2 = "Spock" Then
            player1Score = player1Score + 1 
        Else
            player2Score = player2Score + 1 
        End If
    ElseIf player1 = "Scissors" Then
        If player2 = "Paper" Or player2 = "Lizard" Then
            player1Score = player1Score + 1 
        Else
            player2Score = player2Score + 1 
        End If
    ElseIf player1 = "Lizard" Then
        If player2 = "Paper" Or player2 = "Spock" Then
            player1Score = player1Score + 1 
        Else
            player2Score = player2Score + 1 
        End If
    ElseIf player1 = "Spock" Then
        If player2 = "Rock" Or player2 = "Scissors" Then
            player1Score = player1Score + 1 
        Else
            player2Score = player2Score + 1 
        End If 
    End If
Loop

WScript.Echo "Resultado: "

If player1Score > player2Score Then
    WScript.Echo "Player 1 wins"
ElseIf player1Score < player2Score Then
    WScript.Echo "Player 2 wins"
Else
    WScript.Echo "Tie"
End If