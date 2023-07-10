import java.util.Scanner;

public class EspinoLeandroo {
    
    public static void main(String[] args) {
        EspinoLeandroo espinoLeandroo = new EspinoLeandroo();

        Scanner sc = new Scanner(System.in);

        System.out.println("Texto que deseas cifrar ");
        String texto = sc.nextLine();
        System.out.println("Con cuanto desplazamiento deseas cifrar ");
        int desplazamiento = sc.nextInt();

        String textoCifrado = espinoLeandroo.cifrarCesar(texto, desplazamiento);
        String textoDescifrado = espinoLeandroo.descifrarCesar(textoCifrado, desplazamiento);
        System.out.println("Texto cifrado: " + textoCifrado);
        System.out.println("Texto descifrado: " + textoDescifrado);
    }


    private String cifrarCesar(String texto, int desplazamiento){
        String resultado = "";

        for(int i = 0; i<texto.length(); i++){
            char letra = texto.charAt(i);
            if(esAlfanumerico(letra + "")){
                int codigo = (int) letra;
                int codigoCifrado = (codigo - 97 + desplazamiento) % 26 + 97;
                char letraCifrada = (char) codigoCifrado;
                resultado += letraCifrada;
            }else{
                resultado += letra;
            }
        }
        return resultado;
    }
    
    private String descifrarCesar(String texto, int desplazamiento){
        String resultado = "";

        for(int i = 0; i<texto.length(); i++){
            char letra = texto.charAt(i);
            if(esAlfanumerico(letra + "")){
                int codigo = (int) letra;
                int codigoCifrado = (codigo - 97 - desplazamiento) % 26 + 97;
                char letraCifrada = (char) codigoCifrado;
                resultado += letraCifrada;
            }else{
                resultado += letra;
            }
        }
        return resultado;
    }

    public static boolean esAlfanumerico(String s) {
        return s != null && s.matches("^[a-zA-Z0-9]*$");
    }
}
