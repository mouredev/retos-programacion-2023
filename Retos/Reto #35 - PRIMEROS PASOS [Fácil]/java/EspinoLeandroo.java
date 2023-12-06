import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class EspinoLeandroo {

    // Constante
    static final int CONSTANT_VALUE = 11;

    public static void main(String[] args) {
        // Hola mundo
        System.out.println("Hola, mundo!");

        // Variables
        String text = "Soy Leandro";
        int integerValue = 26;
        double doubleValue = 3.14;
        boolean booleanValue = true;

        // if, else if y else
        if (integerValue > 50) {
            System.out.println("El valor es mayor que 50.");
        } else if (integerValue > 20) {
            System.out.println("El valor es mayor que 20 pero menor o igual que 50.");
        } else {
            System.out.println("El valor es menor o igual que 20.");
        }

        // Estructuras de datos
        // Array
        int[] array = { 1, 2, 3, 4, 5 };
        // Lista
        List<String> list = new ArrayList<>();
        list.add("item1");
        list.add("item2");

        // No hay tuplas en Java

        // Set
        Set<String> set = new HashSet<>();
        set.add("element1");
        set.add("element2");

        // Diccionario
        Map<String, Integer> dictionary = new HashMap<>();
        dictionary.put("key1", 100);
        dictionary.put("key2", 200);

        // for
        for (int num : array) {
            System.out.println("Número: " + num);
        }

        // foreach
        for (String item : list) {
            System.out.println("Item: " + item);
        }

        set.forEach(element -> System.out.println("Elemento: " + element));

        // while
        int counter = 0;
        while (counter < 5) {
            System.out.println("Contador: " + counter);
            counter++;
        }

        // Funciones
        System.out.println("Suma: " + sum(5, 7));
        subtraction(5, 7);
        System.out.println("PI: " + pi());
        constante();

        // Clase
        MyClass myObject = new MyClass();
        myObject.printMessage();

        // Control de excepciones
        try {
            int result = integerValue / 0; // Esto generará una excepción
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    // Funciones
    // con parametros y con retorno
    public static int sum(int a, int b) {
        return a + b;
    }

    // con parametros y sin retorno
    public static void subtraction(int a, int b) {
        System.out.println("Resta: " + (a - b));
    }

    // sin parametros y con retorno
    public static double pi() {
        return 3.1416;
    }

    // sin parametros y sin retorno
    public static void constante() {
        System.out.println(CONSTANT_VALUE);
    }

    // Clase
    static class MyClass {
        void printMessage() {
            System.out.println("Mensaje desde la clase.");
        }
    }
}
