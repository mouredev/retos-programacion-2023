void main() {
  // Punto 1: Hola, mundo!
  print("Hola, mundo!");

  // Punto 2: Crea una variable de texto o string
  String miTexto = "¡Hola desde Dart!";

  // Punto 3: Crea una variable de número entero
  int miEntero = 42;

  // Punto 4: Crea una variable de número con decimales
  double miDecimal = 3.14;

  // Punto 5: Crea una variable de tipo booleano
  bool miBooleano = true;

  // Punto 6: Crea una constante
  const MI_CONSTANTE = 10;

  // Punto 7: Usa un if, else if y else
  if (miEntero > 50) {
    print("El número es mayor que 50");
  } else if (miEntero < 50) {
    print("El número es menor que 50");
  } else {
    print("El número es igual a 50");
  }

  // Punto 8: Crea un Array (list en Dart)
  List<int> miArray = [1, 2, 3, 4, 5];

  // Punto 9: Crea una lista
  List<String> miLista = ["Manzana", "Banana", "Naranja"];

  // Punto 10: Crea una tupla (no aplicable en Dart)

  // Punto 11: Crea un set (set en Dart)
  Set<String> miSet = {"Rojo", "Verde", "Azul"};

  // Punto 12: Crea un diccionario (map en Dart)
  Map<String, String> miDiccionario = {
    "clave1": "valor1",
    "clave2": "valor2"
  };

  // Punto 13: Usa un ciclo for
  for (var elemento in miArray) {
    print(elemento);
  }

  // Punto 14: Usa un ciclo foreach
  for (var elemento in miLista) {
    print(elemento);
  }

  // Punto 15: Usa un ciclo while (no es común en Dart, se prefiere for o for-in)
  int contador = 0;
  while (contador < 3) {
    print("Contador: $contador");
    contador++;
  }

  // Punto 16: Crea una función sin parámetros que no retorne nada
  void funcionSinParametros() {
    print("Función sin parámetros");
  }

  // Punto 17: Crea una función con parámetros que no retorne nada
  void funcionConParametros(int param1, String param2) {
    print("Parámetro 1: $param1");
    print("Parámetro 2: $param2");
  }

  // Punto 18: Crea una función con parámetros que retorne valor
  int funcionConRetorno(int a, int b) {
    return a + b;
  }

  // Punto 19: Crea una clase (class en Dart)
  class Persona {
    String nombre;
    int edad;

    Persona(this.nombre, this.edad);
  }

  // Punto 20: Muestra control de excepciones (try-catch en Dart)
  try {
    var resultado = miEntero ~/ 0;
    print(resultado);
  } catch (e) {
    print("Error: $e");
  }
}
