

function genera_contraseña($configuracion){
    $mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    $minusculas = "abcdefghijklmnopqrstuvwxyz"
    $numeros = "0123456789"
    $simbolos = '/!"#$%&()*+,-./:;<=>?[\]^_{|}~'

    [int]$longitud = ((($configuracion.replace("m","")).replace("n","")).replace("s","")).replace("l","")
    if ($configuracion -match "m"){
        $mayuscula = $true
    }else{
        $mayuscula = $false
    }
    if ($configuracion -match "n"){
        $numero = $true
    }else{
        $numero = $false
    }
    if ($configuracion -match "s"){
        $simbolo = $true
    }else{
        $simbolo = $false
    }
    if ($longitud -gt 9 -and $longitud -lt 17){
        $contador = 0
        do{
            $añadido = $false
            $opcion = Get-Random -Maximum 4
            switch($opcion){
                0   {if ($mayuscula){
                    $contraseña = $contraseña + $mayusculas[(get-random -maximum ($mayusculas.Length))]
                    $añadido = $true
                    }
                }
                1   {
                    $contraseña = $contraseña + $minusculas[(get-random -maximum ($minusculas.Length))]
                    $añadido = $true
                }
                2   {if ($numero){
                    $contraseña = $contraseña + $numeros[(get-random -maximum ($numeros.Length))]
                    $añadido = $true
                    }
                }
                3   {if ($simbolo){
                    $contraseña = $contraseña + $simbolos[(get-random -maximum ($simbolos.Length))]
                    $añadido = $true
                    }
                }
            }
            if ($añadido){
                $contador += 1
            }

        }while($contador -lt $longitud)
    }else{
        $contraseña = "Introduzca un número entre 10 y 16"
    }
    return $contraseña
    }

out-default -inputobject (genera_contraseña("l12mns"))    