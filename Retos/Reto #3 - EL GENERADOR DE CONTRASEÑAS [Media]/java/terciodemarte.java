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
        String letras ="abcdefghijklmnopqrstuvwyz";
        char simbolos[] = new char[]{'º', '!', '@', '#', '%', '/', '^', '+', '-', '/', '/'};

        for (int i = 0; i <= longitud; i++) {
            byte aleatorio1 = (byte) (Math.random() * 4 + 1);
            byte aleatorio2 = (byte) (Math.random()*9);
            
            
            switch (aleatorio1) {
                case 1:
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
                    System.out.print(aleatorio2);
                    break;
                default:
                    System.out.println("Un error");
            }
        }
    }

}
