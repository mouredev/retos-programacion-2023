package reto3GeneradorDeContrasenas;

public class cflorezp {

    public static void main(String[] args){
        System.out.println(generaPasword(generaAletaorio8a16()));
    }

    public static int generaAletaorio8a16() {
        int numero = (int) (Math.random() * (16 - 8 + 1) + 8);
        return numero;
    }

    public static String generaPasword(int longitud) {
        char[] caracteres = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                '*', '/', '*', '.', '?', '¿', '!', '¡', '-', '_', '+'};

        char[] result = new char[longitud];
        for (int i = 0; i < longitud; i++) {
            int position = (int) (Math.random() * caracteres.length);
            result[i] = caracteres[position];
        }
        return new String(result);

    }
}
