
$global:Marcaciones=@()
$Proceso = "Continuar"

function Marcador($jugador,$añadir){
    $Partida = "Continuar"
    clear
    $ValoresPuntuacion = @("Love", 15, 30, 40)
    $PuntuacionesExtras = @("Deuce","Ventaja ","Ha ganado ")
    if ($añadir -notlike "No Añadir"){
        $global:Marcaciones += $jugador
    }
    for($contador = 0; $contador -lt $marcaciones.Count;$contador++){
        $puntuacionP1 = ($Marcaciones[0..$contador] | Where-Object {$_ -like "P1"}).count
        $puntuacionP2 = ($Marcaciones[0..$contador] | Where-Object {$_ -like "P2"}).count
        if ($puntuacionP1 -gt 2 -and $puntuacionP2 -gt 2 ){
            switch ($puntuacionP1){
                {$PsItem -eq $puntuacionP2} {$textosalida = $PuntuacionesExtras[$puntuacionP1-$puntuacionP2]}
                {$PsItem -gt $puntuacionP2} {$textoSalida = $PuntuacionesExtras[$puntuacionP1-$puntuacionP2]+"P1"}
                {$PsItem -lt $puntuacionP2} {$textoSalida = $PuntuacionesExtras[$puntuacionP2-$puntuacionP1]+"P2"}
                default {}
            }
        }else{
            IF($puntuacionP1 -lt $ValoresPuntuacion.Count -and $puntuacionP2 -lt $ValoresPuntuacion.count){
                $textoSalida = [string]$ValoresPuntuacion[$puntuacionP1] +" - "+ $ValoresPuntuacion[$puntuacionP2]
            }else{
                If($puntuacionP1 -gt $puntuacionP2){
                    $JugadorMasPuntuacion = "P1"    
                }else{$JugadorMasPuntuacion = "P2"}
                $textoSalida = "Ha ganado "+$JugadorMasPuntuacion
            }
        }
        if ($textoSalida -match "Ha ganado"){$Partida = "Fin"}else{$Partida = "Continuar"}
        out-default -inputobject $textoSalida
    }
    return $Partida
}
Clear-Host
do {
    $RegistroPuntuacion = Read-Host -Prompt "Quién puntua? "
    switch($RegistroPuntuacion){
        "P1" {$Proceso = Marcador("P1")}
        "P2" {$Proceso = Marcador("P2")}
        default {Marcador($valor)("No Añadir"); out-default -inputobject "Introduzca P1 o P2"}
    }
    IF($Proceso -like "Fin"){break}
}while($RegistroPuntuacion -notlike "P1" -or $RegistroPuntuacion -notlike "P2")

