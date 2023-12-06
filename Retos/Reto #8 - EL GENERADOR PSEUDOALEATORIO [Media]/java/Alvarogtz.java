import java.util.ArrayList;

public class Alvarogtz {
    public static void main(String[] args) {
        System.out.println("----- GENERADOR DE NUMEROS ALEATORIOS -----");
        long base = Long.valueOf(System.currentTimeMillis());
        long hash = Long.valueOf(System.currentTimeMillis()).hashCode() * base;
        long numbers = base * hash;
        String number = String.valueOf(numbers).replace("-", "");
        int result = 0;

        for(int i = 0; i< number.toCharArray().length;i++){
            int numero = number.toCharArray()[i];
            if(result + numero < 100)
                result += numero;
            else if (result - numero > 0)
                result -= numero;
        }

        System.out.println("Numero : " + result);
    }
    
}