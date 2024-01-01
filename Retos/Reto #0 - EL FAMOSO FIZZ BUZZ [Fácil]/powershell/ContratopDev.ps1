

for ($i = 1; $i -le 100; $i++) {
# FOR: Permite ejecutar un bloque de código un número determinado de veces.
# $i = 1: Inicializa la variable $i en 1.
# $i -le 100: Mientras que $i sea menor o igual a 100, se repetirá el bloque de código.
# $i++: Incrementa en 1 el valor de $i cada vez que se repite el bloque de código.
    if ($i % 3 -eq 0 -and $i % 5 -eq 0) {
    # IF: Permite ejecutar un bloque de código si se cumple una condición.
    # $i % 3 -eq 0: Si el residuo de la división de $i entre 3 es igual a 0.
    # -and: Operador lógico que significa "y".
    # $i % 5 -eq 0: Si el residuo de la división de $i entre 5 es igual a 0.
        Write-Host "FizzBuzz"
        # Write-Host: Imprime en pantalla el texto que se le pase como parámetro.
    }
    elseif ($i % 3 -eq 0) {
    # ELSEIF: Permite ejecutar un bloque de código si no se cumple la condición del IF anterior y se cumple la condición del ELSEIF.
        Write-Host "Fizz"
    }
    elseif ($i % 5 -eq 0) {
        Write-Host "Buzz"
    }
    else {
    # ELSE: Permite ejecutar un bloque de código si no se cumple la condición del IF y del ELSEIF.
        Write-Host $i
        #Write-Host $i: Imprime en pantalla el valor de la variable $i.
    }
}
