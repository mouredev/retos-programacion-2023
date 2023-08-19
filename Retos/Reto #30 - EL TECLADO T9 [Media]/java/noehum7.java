import java.util.HashMap;
import java.util.Map;

public class TecladoT9 {
    public static void main(String[] args) {
        String[] letras = {"ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"};
        String texto = "6-666-88-777-33-3-33-888", resultado = "";

        Map<Integer, String> equivalencias = new HashMap<>();

        for(int i = 0; i < letras.length; i++) {
            equivalencias.put(i + 2, letras[i]);
        }

        String[] cadenaArray = texto.split("-");
        for (String cadena: cadenaArray) {
            int numero = cadena.charAt(0) - '0';
            if(equivalencias.containsKey(numero)) {
                resultado += equivalencias.get(numero).charAt(cadena.length() - 1);
            }
        }
        System.out.println(resultado);
  }
}
