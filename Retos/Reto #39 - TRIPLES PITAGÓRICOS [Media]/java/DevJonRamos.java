import java.util.ArrayList;
import java.util.List;

public class DevJonRamos {

    public static List<List<Integer>> triplesPitagoricos(int limite){

        int m = 2;
        List<List<Integer>> ternas = new ArrayList<>();
            
        while (true) {

            for (int n = 1; n < m; n++) {
                
                int a = (m * m) - (n * n);
                int b = 2 * m * n;
                int c = (m * m) + (n * n);

                if(c > limite) return ternas;

                ternas.add(List.of(a, b, c));

            }

            m++;

        }

    }

    public static void main(String[] args) throws Exception {

        int limite = 50;

        System.out.println(triplesPitagoricos(limite));

    }
}
