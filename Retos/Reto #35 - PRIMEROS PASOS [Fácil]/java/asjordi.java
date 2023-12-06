import java.util.*;

public class FirstStepsInJava {

    public static void main(String[] args) {

        // Hola mundo

        System.out.println("Hola, mundo!");

        // Tipos de variables

        int numeroEntero = 10;
        byte byteEntero = 127;
        short shortEntero = 32767;
        long longEntero = 1000000000L;
        float numeroFlotante = 3.14f;
        double numeroDoble = 3.14159265359;
        char caracter = 'A';
        boolean esVerdadero = true;
        boolean esFalso = false;
        String texto = "Hola, Mundo!";

        // Constante

        final double PI = Math.PI;

        // Condicionales

        if (esVerdadero) System.out.println("Es verdadero");
        else if (esFalso) System.out.println("Es falo");
        else System.out.println("No se si es verdadero o falso");

        // Array

        String[] letras = new String[3];
        letras[0] = "A";
        letras[1] = "B";
        letras[2] = "C";

        int[] numeros = {1, 2, 3, 4, 5};

        // Listas

        ArrayList<Integer> numerosPositivos = new ArrayList<>();
        numerosPositivos.add(2);
        numerosPositivos.add(10);
        numerosPositivos.add(45);

        List<Character> vocales = new ArrayList<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));

        LinkedList<String> nombres = new LinkedList<>(Arrays.asList("Maria", "Guadalupe", "Pedro", "Raul"));

        // Set
        Set<Integer> numerosUnicos = new HashSet<>();
        numerosPositivos.add(1);
        numerosPositivos.add(3);
        numerosPositivos.add(1);

        // Map

        Map<String, Integer> alumnos = new HashMap<>();
        alumnos.put("Maria", 9);
        alumnos.put("Guadalupe", 10);
        alumnos.put("Pedro", 10);
        alumnos.put("Raul", 8);

        // for

        for (int i = 0; i < numeros.length; i++) {
            System.out.println(numeros[i]);
        }

        // foreach

        for (char vocal : vocales){
            System.out.println(vocal);
        }

        nombres.forEach(nombre -> System.out.println(nombre));

        // while

        while (numeroEntero > 0){
            System.out.println(numeroEntero);
            numeroEntero--;
        }

        // Ejecutar Funciones

        imprimirMensaje();
        saludar("Jordi");
        int edad = edadAlCuadrado(20);
        String nombreCompleto = nombreCompleto("Juan", "Gonzales");

        // Crear instancia de clase

        Persona persona1 = new Persona();
        persona1.setNombre("Jorge");
        persona1.setApellido("Delgado");
        persona1.setEdad(34);

        Persona persona2 = new Persona("Jimena", "Sanchez", 24);

        // Control de excepciones

        int numerador = 10;
        int divisor = 0;
        int resultado;

        try {
            resultado = numerador / divisor;
            System.out.println("El resultado de la división es: " + resultado);
        } catch (ArithmeticException e){
            System.err.println("Error: División por cero no permitida.");
        } finally {
            resultado = 0;
        }

    }

    // Ejemplos de funciones

    public static void imprimirMensaje(){
        System.out.println("Hola!");
    }

    public static void saludar(String nombre){
        System.out.println("Hola " + nombre);
    }

    public static int edadAlCuadrado(int edad){
        return edad * edad;
    }

    public static String nombreCompleto(String nombre, String apellido){
        return nombre + " " + apellido;
    }

    // Clase

    public static class Persona {
        private String nombre;
        private String apellido;
        private int edad;

        public Persona() {}

        public Persona(String nombre, String apellido, int edad) {
            this.nombre = nombre;
            this.apellido = apellido;
            this.edad = edad;
        }

        public String getNombre() {
            return nombre;
        }

        public void setNombre(String nombre) {
            this.nombre = nombre;
        }

        public String getApellido() {
            return apellido;
        }

        public void setApellido(String apellido) {
            this.apellido = apellido;
        }

        public int getEdad() {
            return edad;
        }

        public void setEdad(int edad) {
            this.edad = edad;
        }

        @Override
        public String toString() {
            return "Persona{" +
                    "nombre='" + nombre + '\'' +
                    ", apellido='" + apellido + '\'' +
                    ", edad=" + edad +
                    '}';
        }
    }

}
