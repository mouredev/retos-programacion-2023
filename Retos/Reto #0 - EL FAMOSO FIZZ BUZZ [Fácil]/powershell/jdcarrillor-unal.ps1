# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
[int]$repeat = 101 
for ($counter = 1; $counter -lt $repeat; $counter++){
    if($counter%3  -eq 0  -and $counter%5 -eq 0 ){
        Write-Host "fizzbuzz"
    }elseif($counter%5 -eq 0){
        Write-Host "buzz"
    }elseif($counter%3 -eq 0){
        Write-host "fizz"
    }else{
        Write-host $counter
    }
}
