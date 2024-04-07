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

#include <stdio.h>
#include <stdbool.h>

static void sinParametros();
static int conParametros(int a, int b);

// Crea una clase.
typedef struct{
    char *name;
    char *surname;
    int id;
}Student;

int main()
{
    // Haz un "Hola, mundo!
    printf("Hola, mundo!");

    // Crea variables de tipo String, numéricas (enteras y decimales) y Booleanas (o cualquier tipo de dato primitivo).
    char string[] = "This is a string";
    int num = 10;
    float decim = 2.71;
    bool state = false;

    // Crea una constante.
    const int unchanged = 22;

    // Usa un if, else if y else.
    if (unchanged > num)
    {
        state = true;
    }
    else if (unchanged == num)
    {
        state = true;
    }
    else
    {
        state = false;
    }

    // Crea estructuras como un array, lista, tupla, set y diccionario.
    char array[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    // Usa un for, foreach y un while.
    for (int i = 0; i < 10; i++)
    {
        printf("%d ", array[i]);
    }

    int count = 0;
    while (count < 10)
    {
        printf("%d ", array[count]);
        count++;
    }

    // Crea diferentes funciones (con/sin parámetros y con/sin retorno).
    sinParametros();
    int result = conParametros(10,20);

    return 0;
}

static void sinParametros()
{
    printf("Sin parametros!\n");
}
static int conParametros(int a, int b)
{
    return a + b;
}
