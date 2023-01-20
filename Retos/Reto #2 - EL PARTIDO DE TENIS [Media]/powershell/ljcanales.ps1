$Finished = $false
$PointNames = @("Love", 15, 30, 40)

$PointsP1 = 0
$PointsP2 = 0

while (-not $Finished) {
    $Point = Read-Host -Prompt 'Point (P1 or P2)'
    if ($Point -eq 'P1') {
        $PointsP1 += 1
    } elseif ($Point -eq 'P2') {
        $PointsP2 += 1
    } else {}

    if ($PointsP1 -eq $PointsP2 -and $PointsP1 -ge 3) {
        Write-Host "Deuce"
    } elseif ($PointsP1 -lt 4 -and $PointsP2 -lt 4) {
        Write-Host "$($PointNames[$PointsP1]) - $($PointNames[$PointsP2])"
    } else {
        if ([Math]::Abs($PointsP1 - $PointsP2) -ge 2) {
            $Finished = $true
        }
        Write-Host "$(if ($Finished) {"Ha ganado"} else {"Ventaja"}) $(if ($PointsP1 -gt $PointsP2) {"P1"} else {"P2"})"
    }
}
