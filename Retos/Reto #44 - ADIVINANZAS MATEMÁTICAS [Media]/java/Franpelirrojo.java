import java.util.Scanner;

/*
 * https://github.com/franpelirrojo
 */

public class Franpelirrojo {
    private static int resultado;
    private static double vuelta = 0;
    private static int nX = 1;
    private static int nY = 1;

    private enum Estado {SIN_TIMEPO, INCORRECTO};
    private static Estado estado;

    public static void main(String[] args) throws InterruptedException {
        Thread main = Thread.currentThread();

        System.out.println("¡Responde rápido!");
        while (true){
            Thread crono = new Thread(() -> { //bucle del tiempo de juego
                try {
                    while (true){
                        Thread.sleep(3000);
                        if (!Thread.interrupted()){
                            estado = Estado.SIN_TIMEPO;
                            main.interrupt();
                            break;
                        }
                    }
                } catch (InterruptedException e) {
                    System.out.println("¡3 segundos!");
                }
            });

            Thread juego = new Thread(() ->{ //bucle de juego
                Scanner usuario = new Scanner(System.in);
                generarOperacion();

                int respuesta = usuario.nextInt();
                if (respuesta != resultado){
                    estado = Estado.INCORRECTO;
                    main.interrupt();
                }else {
                    crono.interrupt();
                }

                vuelta ++;
                comprobarVueltas();
            });
            juego.setDaemon(true);

            juego.start();
            crono.start();
            try {
                juego.join();
            } catch (InterruptedException e) {
                break;
            }
        }

        if (estado.equals(Estado.INCORRECTO)){ //Diferenciamos fin de juego
            System.out.println("¡FIN DEL JUEGO!");
            System.out.println("Acertaste " + (vuelta!=0 ? (int)(vuelta - 1) : vuelta) + " operaciones.");
            System.out.println("La respuesta correcta era: " + resultado);
        } else if (estado.equals(Estado.SIN_TIMEPO)) {
            System.out.println("¡FIN DEL JUEGO!");
            System.out.println("Te quedaste sin tiempo");
            System.out.println("Acertaste " + (vuelta!=0 ? (int)(vuelta - 1) : vuelta) + " operaciones.");
        }
    }

    /*
    * Generamos aleatoriamente una de las cuatro cuentas posibles.
    * La longitud de los operandos depende del exponente de 10.
    * */
    private static void generarOperacion(){
        int operandoX;
        int operandoY;
        int operador = (int) (Math.random() * 3.9);
        do {
            operandoX = (int) (Math.random() * Math.pow(10, nX));
            operandoY = (int) (Math.random() * Math.pow(10, nY));
        } while (operador == 2 && operandoY == 0 || operandoX<operandoY); //Evitamos divisiones incómodas y entre 0

        switch (operador){
            case 0 -> { //suma
                System.out.println(operandoX + " + " + operandoY);
                resultado = operandoX + operandoY;
            }
            case 1 -> { //multiplicación
                System.out.println(operandoX + " * " + operandoY);
                resultado = operandoX * operandoY;
            }
            case 2 -> { //división
                System.out.println(operandoX + " / " + operandoY);
                resultado = operandoX / operandoY;
            }
            case 3 -> { //resta
                System.out.println(operandoX + " - " + operandoY);
                resultado = operandoX - operandoY;
            }
        }
    }

    /*
    * Aumenta los operadores dependiendo de en qué momento de juego estamos.
    * Si el numero de vueltas que hemos dado al bucle de juego es divisible entre 5
    * aumenta el operador X. En cambio si también lo es entre 2 aumenta el operador Y.
    * */
    private static void comprobarVueltas(){
        if (vuelta%5 == 0 ){
            if (vuelta%2 == 0){
                nY++;
            }else {
                nX++;
            }
        }
    }
}
