import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;


public class Herzogs {

	static class RetoSemanal {
        private Integer numero;

        public RetoSemanal (Integer n){
            this.numero = n;
        }

        public List<Character> convertHexadecimal(){
            List<Character> lista = new ArrayList<>();
            Map<Integer,Character> mapa = new HashMap<Integer,Character>();
            mapa.put(10,'A');
            mapa.put(11,'B');
            mapa.put(12,'C');
            mapa.put(13,'D');
            mapa.put(14,'E');
            mapa.put(15,'F');
            Integer ent = this.numero;
            while (ent != 0) {
                Integer rest = ent % 16;
                Character ch;
                if(rest >= 10)
                  ch = mapa.get(rest);
                else
                  ch = (char) (rest + '0');
                lista.add(ch);
                ent /= 16;
            }
            java.util.Collections.reverse(lista);
            return lista;
        }


        public List<Integer> convertOctal(){
            List<Integer> listaIntegers = new ArrayList<>();
            Integer ent = this.numero;
            while (ent != 0) {
                listaIntegers.add(ent % 8);
                ent /= 8;
            }
            java.util.Collections.reverse(listaIntegers);
            return listaIntegers;
        }
  }

  
  public static void main(String[] args) {
      RetoSemanal reto14 = new RetoSemanal(242);
      System.out.print("Hexa: ");
      reto14.convertHexadecimal().forEach(element -> System.out.print(element));
      System.out.print("\nOctal: ");
      reto14.convertOctal().forEach(element -> System.out.print(element));
    }
}
