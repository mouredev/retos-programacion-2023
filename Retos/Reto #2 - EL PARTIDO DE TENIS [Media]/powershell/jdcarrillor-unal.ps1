
<# Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 gane cada punto del juego. 
 - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
   15 - Love
   30 - Love
   30 - 15
   30 - 30
   40 - 30
   Deuce
   Ventaja P1
   Ha ganado el P1
- Si quieres, puedes controlar errores en la entrada de datos.   
- Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   #>

function tennisGame([Array]$arrayGame){
    [string]$player1 = "P1"
    [string]$player2 = "P2"
    [int]$p1_points = 0
    [int]$p2_points = 0 
    [Array]$game = @('Love', '15', '30', '40')
    [bool]$finished = $False 
    Write-Host $player1  "|" $player2
    do{
        foreach ($point in $arrayGame) {
            if($point -eq $player1){
                $p1_points += 1
            }else{
                $p2_points += 1 
            }
            if(($p1_points -ge $game.Length -1) -and ($p2_points -ge $game.Length -1) ){
                if([Math]::Abs($p1_points - $p2_points) -le 1){
                    if($p1_points -eq $p2_points){
                        Write-Host "Deuce"
                    }elseif ($p1_points -gt $p2_points) {
                        Write-Host "Ventaja" $player1
                    }else{
                        Write-Host "Ventaja" $player2
                    }   
                }else{
                    if($p1_points -gt $p2_points) {
                        Write-Host "Ha ganado" $player1
                    }else{
                        Write-Host "Ha ganado" $player2
                    } 
                    $finished = $True  
                    Write-Host "--------------------------------------" 
                }
            }else{
                if(($p1_points -lt 4 ) -and( $p2_points -lt 4)){
                    Write-Host $game[$p1_points] "|" $game[$p2_points]
                }else{
                    if($p1_points -gt $p2_points) {
                        Write-Host "Ha ganado" $player1
                    }else{
                        Write-Host "Ha ganado" $player2
                    } 
                    $finished = $True 
                    Write-Host "--------------------------------------"
                }
            }
        }
    }while(-not $finished)
}

tennisGame(@("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"))
tennisGame(@("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2","P2","P1","P1","P1"))