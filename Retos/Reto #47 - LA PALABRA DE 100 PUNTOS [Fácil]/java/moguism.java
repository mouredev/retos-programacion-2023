import java.util.Scanner;

public class moguism {

    public static void main(String[] args){

        Scanner leer = new Scanner(System.in);

        int puntos = 0;

        String palabra = "";

        while (puntos != 100) {

            System.out.print("Introduce una palabra: ");
            palabra = leer.next();

            String copiaPalabra = palabra.toUpperCase();

            for(int i = 0; i < copiaPalabra.length(); i++){

                int puntosLetra = 0;

                for(int j = 65; j <= 90; j++){ // Empieza en la A y termina en la Z (en ASCII)

                    puntosLetra++;

                    if(copiaPalabra.charAt(i) == j){

                        puntos = puntos + puntosLetra;
                        break;

                    } else if(copiaPalabra.charAt(i) == 'Ñ'){

                        puntos = puntos + 15;
                        break;

                    }

                    if(j == 78){ // Cuando llega a la Ñ

                        puntosLetra++;

                    }

                }

            }

            System.out.println("La palabra "+palabra+" vale "+puntos+" puntos");

            if(puntos != 100){

                puntos = 0;

            }

            
        }

        System.out.println("¡ENHORABUENA!");

        leer.close();

    }
}
