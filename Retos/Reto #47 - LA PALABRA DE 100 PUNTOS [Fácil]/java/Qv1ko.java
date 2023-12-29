import java.util.HashMap;
import java.util.Scanner;

class Qv1ko {

    public static void main(String[] args) {
        wordPoints();
    }

    private static void wordPoints() {

        HashMap<Character, Integer> letterPoints = new HashMap<Character, Integer>() {{ put('a', 1);put('b', 2); put('c', 3); put('d', 4); put('e', 5); put('f', 6); put('g', 7); put('h', 8); put('i', 9); put('j', 10); put('k', 11); put('l', 12); put('m', 13); put('n', 14); put('ñ', 15); put('o', 16); put('p', 17); put('q', 18); put('r', 19); put('s',  20); put('t', 21); put('u', 22); put('v', 23); put('w', 24); put('x', 25); put('y', 26); put('z', 27); }};
        String word = "";
        int points = 0;
        Scanner sc = new Scanner(System.in);
        
        while (points != 100) {

            points = 0;
            
            System.out.print("Type a word: ");
            word = sc.nextLine().toLowerCase();

            for (char letter : word.toCharArray()) {
                points += letterPoints.get(letter);
            }

            System.out.println("The word " + word + " has " + points + " points");

        }


        sc.close();

    }

}
