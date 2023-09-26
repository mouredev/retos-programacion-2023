void setup() {
    // Punto 1: Hola, mundo!
    Serial.begin(9600);  // Inicializa la comunicación serial
    Serial.println("Hola, mundo!");

    // Punto 2: Crea una variable de texto o string
    String miTexto = "¡Hola desde Arduino!";

    // Punto 3: Crea una variable de número entero
    int miEntero = 42;

    // Punto 4: Crea una variable de número con decimales
    float miDecimal = 3.14;

    // Punto 5: Crea una variable de tipo booleano
    boolean miBooleano = true;

    // Punto 6: Crea una constante
    const int MI_CONSTANTE = 10;

    // Punto 7: Usa un if, else if y else
    if (miEntero > 50) {
        Serial.println("El número es mayor que 50");
    } else if (miEntero < 50) {
        Serial.println("El número es menor que 50");
    } else {
        Serial.println("El número es igual a 50");
    }
}

void loop() {
    // Punto 8: Crea un Array
    int miArray[] = {1, 2, 3, 4, 5};

    // Punto 9: Crea una lista (Array en Arduino)
    String miLista[] = {"Manzana", "Banana", "Naranja"};

    // Punto 10: Crea una tupla (no aplicable en Arduino)

    // Punto 11: Crea un set (no aplicable en Arduino)

    // Punto 12: Crea un diccionario (no es directamente soportado en Arduino)

    // Punto 13: Usa un ciclo for
    for (int i = 0; i < sizeof(miArray) / sizeof(miArray[0]); i++) {
        Serial.println(miArray[i]);
    }

    // Punto 14: Usa un ciclo foreach (no es soportado directamente en Arduino)

    // Punto 15: Usa un ciclo while
    int contador = 0;
    while (contador < 3) {
        Serial.println("Contador: " + String(contador));
        contador++;
    }

    // Punto 16: Crea una función sin parámetros que no retorne nada (no es aplicable en Arduino)

    // Punto 17: Crea una función con parámetros que no retorne nada (no es aplicable en Arduino)

    // Punto 18: Crea una función con parámetros que retorne valor (no es aplicable en Arduino)

    // Punto 19: Crea una clase (no es directamente soportado en Arduino)

    // Punto 20: Muestra control de excepciones (no es soportado en Arduino)
}
