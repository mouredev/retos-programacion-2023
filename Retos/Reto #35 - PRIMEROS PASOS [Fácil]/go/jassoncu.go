/*
 * Como cada año, el día 256 se celebra el "Día de la Programación".
 * En nuestra comunidad siempre hacemos una gran fiesta donde repartirmos 
 * 256 regalos para seguir aprendiendo programación:
 * https://diadelaprogramacion.com
 *
 * Para seguir ayudando, te propongo este reto:
 * Mostrar la sintaxis de los principales elementos de un lenguaje
 * en TODOS los lenguajes de programación que podamos. ¿Llegaremos a 50?
 *
 * En un fichero, haz lo siguiente (si el lenguaje lo soporta),
 * y comenta cada bloque para identificar con qué se corresponde:
 * - Haz un "Hola, mundo!"
 * - Crea variables de tipo String, numéricas (enteras y decimales)
 *   y Booleanas (o cualquier tipo de dato primitivo).
 * - Crea una constante.
 * - Usa un if, else if y else.
 * - Crea estructuras como un array, lista, tupla, set y diccionario.
 * - Usa un for, foreach y un while.
 * - Crea diferentes funciones (con/sin parámetros y con/sin retorno).
 * - Crea una clase.
 * - Muestra el control de excepciones.
 *
 * Así, cualquier persona podrá consultar rápidamente diferentes ejemplos
 * de sintaxis básica de muchos lenguajes.
 *
 * ¡Muchas gracias!
 */

package main

import (
    "fmt"
)

func main() {
    // Hola, Mundo!
    fmt.Println("Hola, Mundo!")

    // Variables
    cadena := "Hola, Mundo!"
    numeroEntero := 42
    numeroDecimal := 3.14
    booleano := true

    fmt.Println(cadena)
    fmt.Println(numeroEntero)
    fmt.Println(numeroDecimal)
    fmt.Println(booleano)

    // Constante
    const miConstante = 100
    fmt.Println(miConstante)

    // Condicionales
    valor := 42
    if valor > 50 {
        fmt.Println("Mayor que 50")
    } else if valor == 50 {
        fmt.Println("Igual a 50")
    } else {
        fmt.Println("Menor que 50")
    }

    // Estructuras de datos
    array := [3]int{1, 2, 3}
    lista := []int{4, 5, 6}
    diccionario := map[string]string{"clave1": "valor1", "clave2": "valor2"}

    fmt.Println(array)
    fmt.Println(lista)
    fmt.Println(diccionario)

    // Bucles
    for i := 0; i < 5; i++ {
        fmt.Println(i)
    }

    lista2 := []string{"uno", "dos", "tres"}
    for _, elemento := range lista2 {
        fmt.Println(elemento)
    }

    j := 0
    for j < 5 {
        fmt.Println(j)
        j++
    }

    // Funciones
    saludar("Juan")
    resultado := sumar(10, 20)
    fmt.Println("Resultado:", resultado)

    // Clases (Structs en Go)
    miObjeto := MiStruct{miVariable: 42}
    fmt.Println(miObjeto.miVariable)
    miObjeto.miMetodo()

    // Control de excepciones (Errores en Go)
    resultado2, err := dividir(10, 2)
    if err != nil {
        fmt.Println("Error:", err)
    } else {
        fmt.Println("Resultado:", resultado2)
    }
}

func saludar(nombre string) {
    fmt.Println("Hola, " + nombre + "!")
}

func sumar(a, b int) int {
    return a + b
}

type MiStruct struct {
    miVariable int
}

func (ms MiStruct) miMetodo() {
    fmt.Println("Mi Método")
}

func dividir(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("No se puede dividir por cero")
    }
    return a / b, nil
}
