package reto_36;

import java.util.ArrayList;
import java.util.Scanner;

class JesusWay69{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Introduzca cadena de caracteres: ");
        String chain = sc.nextLine().toUpperCase();
        if (chain.length() > 0) {
            ArrayList<String> letters = new ArrayList<>();
            letters.ensureCapacity(3000000);
            letters.add(String.valueOf(chain.charAt(0)));
            for (int i = 1; i < chain.length(); i++) {
                for (int j = letters.size() - 1; j >= 0; j--) {
                    String s = letters.remove(j);
                    for (int k = 0; k <= s.length(); k++) 
                        letters.add(s.substring(0, k) + chain.charAt(i) + s.substring(k));
                }
            }
            int chainx2=chain.length()*2;
            System.out.println("\n Cantidad de combinaciones: " + letters.size() + "\n");
            for (int l = 0; l < letters.size();) {
                System.out.print(letters.get(l) + "  ");
                l++;
                if (l % chainx2 == 0) System.out.println();
            }
        }
    }
}

