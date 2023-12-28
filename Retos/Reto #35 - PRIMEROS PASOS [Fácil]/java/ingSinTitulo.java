public class Main {
    public static void main(String[] args) {
        // Punto 1: Hola, mundo!
        System.out.println("Hola, mundo!");

        // Punto 2: Crea una variable de texto o string
        String miTexto = "¡Hola desde Java!";

        // Punto 3: Crea una variable de número entero
        int miEntero = 42;

        // Punto 4: Crea una variable de número con decimales
        double miDecimal = 3.14;

        // Punto 5: Crea una variable de tipo booleano
        boolean miBooleano = true;

        // Punto 6: Crea una constante
        final int MI_CONSTANTE = 10;

        // Punto 7: Usa un if, else if y else
        if (miEntero > 50) {
            System.out.println("El número es mayor que 50");
        } else if (miEntero < 50) {
            System.out.println("El número es menor que 50");
        } else {
            System.out.println("El número es igual a 50");
        }

        // Punto 8: Crea un Array
        int[] miArray = {1, 2, 3, 4, 5};

        // Punto 9: Crea una lista (ArrayList en Java)
        java.util.List<String> miLista = new java.util.ArrayList<>();
        miLista.add("Manzana");
        miLista.add("Banana");
        miLista.add("Naranja");

        // Punto 10: Crea una tupla (no aplicable en Java)

        // Punto 11: Crea un set (HashSet en Java)
        java.util.Set<String> miSet = new java.util.HashSet<>();
        miSet.add("Rojo");
        miSet.add("Verde");
        miSet.add("Azul");

        // Punto 12: Crea un diccionario (HashMap en Java)
        java.util.Map<String, String> miDiccionario = new java.util.HashMap<>();
        miDiccionario.put("clave1", "valor1");
        miDiccionario.put("clave2", "valor2");

        // Punto 13: Usa un ciclo for
        for (int elemento : miArray) {
            System.out.println(elemento);
        }

        // Punto 14: Usa un ciclo foreach
        for (String elemento : miLista) {
            System.out.println(elemento);
        }

        // Punto 15: Usa un ciclo while
        int contador = 0;
        while (contador < 3) {
            System.out.println("Contador: " + contador);
            contador++;
        }

        // Punto 16: Crea una función sin parámetros que no retorne nada
        funcionSinParametros();

        // Punto 17: Crea una función con parámetros que no retorne nada
        funcionConParametros(1, "dos");

        // Punto 18: Crea una función con parámetros que retorne valor
        int resultado = funcionConRetorno(3, 4);
        System.out.println("Resultado: " + resultado);

        // Punto 19: Crea una clase
        class Persona {
            String nombre;
            int edad;

            Persona(String nombre, int edad) {
                this.nombre = nombre;
                this.edad = edad;
            }
        }

        // Punto 20: Muestra control de excepciones (try-catch en Java)
        try {
            int division = miEntero / 0;
            System.out.println(division);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    // Punto 16: Crea una función sin parámetros que no retorne nada
    static void funcionSinParametros() {
        System.out.println("Función sin parámetros");
    }

    // Punto 17: Crea una función con parámetros que no retorne nada
    static void funcionConParametros(int param1, String param2) {
        System.out.println("Parámetro 1: " + param1);
        System.out.println("Parámetro 2: " + param2);
    }

    // Punto 18: Crea una función con parámetros que retorne valor
    static int funcionConRetorno(int a, int b) {
        return a + b;
    }
}
