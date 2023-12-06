import std.stdio;

// Punto 1: Hola, mundo!
writeln("Hola, mundo!");

// Punto 2: Crea una variable de texto o string
string miTexto = "¡Hola desde D!";

// Punto 3: Crea una variable de número entero
int miEntero = 42;

// Punto 4: Crea una variable de número con decimales
double miDecimal = 3.14;

// Punto 5: Crea una variable de tipo booleano
bool miBooleano = true;

// Punto 6: Crea una constante (const en D)
const int MI_CONSTANTE = 10;

// Punto 7: Usa un if, else if y else
if (miEntero > 50) {
    writeln("El número es mayor que 50");
} else if (miEntero < 50) {
    writeln("El número es menor que 50");
} else {
    writeln("El número es igual a 50");
}

// Punto 8: Crea un Array (array en D)
int[] miArray = [1, 2, 3, 4, 5];

// Punto 9: Crea una lista (array en D)
string[] miLista = ["Manzana", "Banana", "Naranja"];

// Punto 10: Crea una tupla (tuple en D)
tuple(int, string) miTupla = tuple(1, "Tupla");

// Punto 11: Crea un set (no aplicable en D)

// Punto 12: Crea un diccionario (associative array en D)
string[string] miDiccionario = ["clave1": "valor1", "clave2": "valor2"];

// Punto 13: Usa un ciclo for
foreach (elemento; miArray) {
    writeln(elemento);
}

// Punto 14: Usa un ciclo foreach
foreach (elemento; miLista) {
    writeln(elemento);
}

// Punto 15: Usa un ciclo while
int contador = 0;
while (contador < 3) {
    writeln("Contador:", contador);
    contador++;
}

// Punto 16: Crea una función sin parámetros que no retorne nada
void funcionSinParametros() {
    writeln("Función sin parámetros");
}

// Punto 17: Crea una función con parámetros que no retorne nada
void funcionConParametros(int param1, string param2) {
    writeln("Parámetro 1:", param1);
    writeln("Parámetro 2:", param2);
}

// Punto 18: Crea una función con parámetros que retorne valor
int funcionConRetorno(int a, int b) {
    return a + b;
}

// Punto 19: Crea una clase (no aplicable en D)

// Punto 20: Muestra control de excepciones (try-catch en D)
try {
    int resultado = miEntero / 0;
} catch (Exception e) {
    writeln("Error:", e.msg);
}
