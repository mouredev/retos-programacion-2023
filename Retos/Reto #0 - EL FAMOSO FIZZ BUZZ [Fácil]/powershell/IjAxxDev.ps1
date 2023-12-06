Clear-Host

for ($i = 0; $i -lt 101; $i++){
    if($i % 3 -eq 0 -and $i % 5 -eq 0){
        write-host "buzzfizz"
    }
    elseif($i % 3 -eq 0){
        write-host "buzz"
    }
    elseif($i % 5 -eq 0){
        write-host "fizz"
    }
    else{
        write-host $i
    }
}
