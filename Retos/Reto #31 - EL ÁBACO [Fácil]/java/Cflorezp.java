package Reto31Abaco;

/*
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
 *   para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *
 *  Resultado: 1.302.790
 */
public class Cflorezp {

    public static void main(String[] args) {

        String[] abaco = {"0---OOOOOOOO", "OOO---OOOOOO", "---OOOOOOOOO",
                "OO---OOOOOOO","OOOOOOO---OO", "OOOOOOOOO---", "---OOOOOOOOO"};

        System.out.println("\nRepresentacion numerica: " + muestraNumeroDelAbaco(abaco));

        String numero = "5964";
        System.out.println("\nRepresentacion en el abaco de: " + numero);
        imprimeAbaco(numero);


    }

    public static String muestraNumeroDelAbaco(String[] abaco){
        StringBuilder numero = new StringBuilder();
        int count = 0;
        for(String e: abaco){
            for(int i = 0; i < e.length(); i++){
                if(e.charAt(i) == '-'){
                    break;
                }
                count++;
            }
            numero.append(count);
            count = 0;
        }
        return numero.toString();
    }

    /**
     *Esta funcion imprime la representacion de un numero en el abaco
     * @param input
     */
    public static void imprimeAbaco(String input){
        if(!verificaLimiteDelNumero(input)){
            System.out.println("El numero debe estar entre 0 y 7 cifras");
        }else{
            if(input.length() < 7){
                input = String.format("%07d", Integer.parseInt(input));
            }
            for(int i = 0; i < input.length(); i++){
                System.out.print("|");
                int num = 0;
                if(Character.isDigit(input.charAt(i))){
                    num = Integer.parseInt(String.valueOf(input.charAt(i)));
                }
                for(int j = 0; j < num; j++){
                    System.out.print("o");
                }
                System.out.print("---");
                if(num < 9){
                    for(int k = 0; k < (9 - num); k++){
                        System.out.print("o");
                    }
                }
                System.out.println("|");
            }
        }
    }

    public static boolean verificaLimiteDelNumero(String input){
        if(input.length() < 0 || input.length() > 7){
            return false;
        }
        return true;
    }
}
