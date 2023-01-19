/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
*Hecho por Albano Díez 16/01/2023
 */
public class reto3 {

    public static void main(String[] args) {
        byte longitud = (byte) (Math.random() * (16 - 8 + 1) + 8);
<<<<<<< HEAD
        char letras[] = new char[]{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'z'};
        char simbolos[] = new char[]{'º', '!', '@', '#', '%', '/', '^', '+', '-', '/', '/'};

        for (int i = 0; i <= longitud; i++) {
            byte aleatorio1 = (byte) (Math.random() * 3 + 1);
=======
        String letras ="abcdefghijklmnopqrstuvwyz";
        char simbolos[] = new char[]{'º', '!', '@', '#', '%', '/', '^', '+', '-', '/', '/'};

        for (int i = 0; i <= longitud; i++) {
            byte aleatorio1 = (byte) (Math.random() * 4 + 1);
>>>>>>> 98d6bc6b5d47ace7eef619e6eb658aeaeae4fb65
            byte aleatorio2 = (byte) (Math.random()*9);
            
            
            switch (aleatorio1) {
                case 1:
<<<<<<< HEAD
                    System.out.print(letras[(byte) (Math.random() * letras.length)]);
                    break;
                case 2:
                    System.out.print(simbolos[(byte) (Math.random() * simbolos.length)]);
                    break;
                case 3:
=======
                    letras=letras.toLowerCase();
                    System.out.print(letras.charAt((byte) (Math.random() * letras.length())));
                    break;
                case 2:
                    letras=letras.toUpperCase();
                    System.out.print(letras.charAt((byte) (Math.random() * letras.length())));
                    break;
                case 3:
                    System.out.print(simbolos[(byte) (Math.random() * simbolos.length)]);
                    break;
                case 4:
>>>>>>> 98d6bc6b5d47ace7eef619e6eb658aeaeae4fb65
                    System.out.print(aleatorio2);
                    break;
                default:
                    System.out.println("Un error");
            }
        }
    }

}
