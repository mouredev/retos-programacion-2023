#!/bin/bash

# Punto 1: Hola, mundo!
echo "Hola, mundo!"

# Punto 2: Crea una variable de texto o string
miTexto="¡Hola desde Bash!"

# Punto 3: Crea una variable de número entero
miEntero=42

# Punto 4: Crea una variable de número con decimales (Bash no maneja decimales directamente)
miDecimal=3.14

# Punto 5: Crea una variable de tipo booleano (Bash maneja booleanos como números)
miBooleano=true

# Punto 6: Crea una constante (no es común en Bash, se simula con variables en mayúsculas)
MI_CONSTANTE=10

# Punto 7: Usa un if, else if y else
if [ $miEntero -gt 50 ]; then
    echo "El número es mayor que 50"
elif [ $miEntero -lt 50 ]; then
    echo "El número es menor que 50"
else
    echo "El número es igual a 50"
fi

# Punto 8: Crea un Array (array en Bash)
miArray=(1 2 3 4 5)

# Punto 9: Crea una lista (array en Bash)
miLista=("Manzana" "Banana" "Naranja")

# Punto 10: Crea una tupla (no aplicable en Bash)

# Punto 11: Crea un set (no aplicable en Bash)

# Punto 12: Crea un diccionario (no aplicable en Bash)

# Punto 13: Usa un ciclo for
for elemento in "${miArray[@]}"; do
    echo $elemento
done

# Punto 14: Usa un ciclo foreach (no es común en Bash, se logra con ciclo for)

# Punto 15: Usa un ciclo while
contador=0
while [ $contador -lt 3 ]; do
    echo "Contador: $contador"
    contador=$((contador + 1))
done

# Punto 16: Crea una función sin parámetros que no retorne nada
funcionSinParametros() {
    echo "Función sin parámetros"
}

# Punto 17: Crea una función con parámetros que no retorne nada
funcionConParametros() {
    echo "Parámetro 1: $1"
    echo "Parámetro 2: $2"
}

# Punto 18: Crea una función con parámetros que retorne valor
funcionConRetorno() {
    suma=$((a + b))
    echo $suma
}

# Punto 19: Crea una clase (no hay clases en Bash, se trabaja principalmente con funciones y scripts)

# Punto 20: Muestra control de excepciones (Bash maneja errores con comandos y salidas de errores)
resultado=$(echo "scale=2; $miEntero / 0" | bc 2>&1)
if [ $? -ne 0 ]; then
    echo "Error: $resultado"
fi
