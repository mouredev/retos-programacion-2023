import java.util.Random;
import java.util.Scanner;

public class EspinoLeandroo {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int puntaje = 0;
        int operandoCifras = 1;

        for (int pregunta = 1; pregunta <= 20; pregunta++) {
            int operando1 = random.nextInt((int) Math.pow(10, operandoCifras));
            int operando2 = random.nextInt(10) + 1;
            char operacion = obtenerOperacionAleatoria();

            System.out.printf("Pregunta %d: %d %c %d\n", pregunta, operando1, operacion, operando2);

            // Guardar el tiempo de inicio
            long tiempoInicio = System.currentTimeMillis();

            // Esperar la respuesta del usuario
            String respuestaUsuario = scanner.nextLine();

            // Calcular el tiempo transcurrido
            long tiempoTranscurrido = System.currentTimeMillis() - tiempoInicio;

            // Verificar la respuesta y el tiempo transcurrido
            int resultado = calcularResultado(operando1, operando2, operacion);


            if(tiempoTranscurrido <= 3000){
                if (respuestaUsuario.equals(String.valueOf(resultado))) {
                    System.out.println("¡Correcto!");
                    puntaje++;
                }else{
                    System.out.println("Incorrecto. El resultado era: " + resultado);
                }
            }else{
                if (respuestaUsuario.equals(String.valueOf(resultado))) {
                System.out.println("Correcto, pero tardaste " + tiempoTranscurrido);
                    puntaje++;
                }else{
                System.out.println("Incorrecto y tardaste " + tiempoTranscurrido);
                }
                break;
            }

            // Actualizar el número de cifras cada 5 aciertos
            if (pregunta % 5 == 0) {
                operandoCifras++;
            }
        }

        System.out.println("Juego terminado. Puntaje final: " + puntaje);
    }

    private static char obtenerOperacionAleatoria() {
        char[] operaciones = {'+', '-', '*', '/'};
        return operaciones[new Random().nextInt(operaciones.length)];
    }

    private static int calcularResultado(int operando1, int operando2, char operacion) {
        switch (operacion) {
            case '+':
                return operando1 + operando2;
            case '-':
                return operando1 - operando2;
            case '*':
                return operando1 * operando2;
            case '/':
                return operando1 / operando2;
            default:
                throw new IllegalArgumentException("Operación no válida");
        }
    }
}
