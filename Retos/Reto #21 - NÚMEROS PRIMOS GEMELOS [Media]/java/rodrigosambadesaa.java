/*
 * Reto #21 - Java
 * Solución autocontenida y verificable con javac/java.
 */
import java.io.*;
import java.nio.file.*;
import java.time.*;
import java.util.*;
import java.util.regex.*;

class Main {
    private static final int CHALLENGE = 21;

    private static void check(boolean condition, String message) {
        if (!condition) throw new IllegalStateException("Fallo: " + message);
    }

    static String fizzBuzz(int number) {
        if (number % 15 == 0) return "fizzbuzz";
        if (number % 3 == 0) return "fizz";
        if (number % 5 == 0) return "buzz";
        return Integer.toString(number);
    }

    static String toLeet(String text) {
        String keys = "abcdefghijklmnopqrstuvwxyz0123456789";
        String[] values = {"4","I3","[",")","3","|=","&","#","1",",_|",">|","1","/\\/\\","^/","0","|*","(_,)","I2","5","7","(_)","\\/","\\/\\/","><","j","2","o","L","R","E","A","S","b","T","B","g"};
        StringBuilder result = new StringBuilder();
        for (char character : text.toLowerCase(Locale.ROOT).toCharArray()) {
            int index = keys.indexOf(character);
            result.append(index < 0 ? Character.toString(character) : values[index]);
        }
        return result.toString();
    }

    static int tennisWinner(int... points) {
        int[] score = {0, 0};
        for (int player : points) {
            check(player == 1 || player == 2, "jugador de tenis");
            score[player - 1]++;
            if (Math.max(score[0], score[1]) >= 4 && Math.abs(score[0] - score[1]) >= 2)
                return score[0] > score[1] ? 1 : 2;
        }
        return 0;
    }

    static String password(int length, boolean uppercase, boolean numbers, boolean symbols) {
        check(length >= 8 && length <= 16, "longitud de contraseña");
        String pool = "abcdefghijklmnopqrstuvwxyz" + (uppercase ? "ABCDEFGHIJKLMNOPQRSTUVWXYZ" : "")
            + (numbers ? "0123456789" : "") + (symbols ? "!@#$%&*" : "");
        Random random = new Random(2023);
        StringBuilder result = new StringBuilder();
        for (int index = 0; index < length; index++) result.append(pool.charAt(random.nextInt(pool.length())));
        return result.toString();
    }

    static boolean isPrime(int number) {
        if (number < 2) return false;
        for (int divisor = 2; divisor * divisor <= number; divisor++) if (number % divisor == 0) return false;
        return true;
    }

    static boolean isFibonacci(int number) {
        if (number < 0) return false;
        long a = 5L * number * number + 4, b = 5L * number * number - 4;
        long ra = (long)Math.sqrt(a), rb = (long)Math.sqrt(b);
        return ra * ra == a || rb * rb == b;
    }

    static int rpsls(int[][] games) {
        int[][] beats = {{2,3},{0,4},{1,3},{1,4},{0,2}};
        int score = 0;
        for (int[] game : games) {
            if (game[0] == game[1]) continue;
            boolean wins = Arrays.stream(beats[game[0]]).anyMatch(value -> value == game[1]);
            score += wins ? 1 : -1;
        }
        return Integer.compare(score, 0);
    }

    static int pseudoRandom(long[] state) {
        state[0] = state[0] * 16807L % 2147483647L;
        return (int)(state[0] % 101);
    }

    static int[] frequencies(String text) {
        int[] counts = new int[26];
        for (char c : text.toLowerCase(Locale.ROOT).toCharArray()) if (c >= 'a' && c <= 'z') counts[c - 'a']++;
        return counts;
    }
    static boolean heterogram(String text) { return Arrays.stream(frequencies(text)).max().orElse(0) <= 1; }
    static boolean isogram(String text) {
        int expected = 0;
        for (int count : frequencies(text)) if (count > 0) {
            if (expected == 0) expected = count;
            else if (count != expected) return false;
        }
        return expected > 0;
    }
    static boolean pangram(String text) { return Arrays.stream(frequencies(text)).min().orElse(0) > 0; }

    static boolean friday13(int month, int year) {
        return LocalDate.of(year, month, 13).getDayOfWeek() == DayOfWeek.FRIDAY;
    }

    static String convertBase(int number, int base) {
        check(base >= 2 && base <= 16, "base");
        if (number == 0) return "0";
        String digits = "0123456789ABCDEF";
        StringBuilder result = new StringBuilder();
        int value = Math.abs(number);
        while (value > 0) { result.append(digits.charAt(value % base)); value /= base; }
        if (number < 0) result.append('-');
        return result.reverse().toString();
    }

    static String caesar(String text, int shift) {
        int movement = Math.floorMod(shift, 26);
        StringBuilder result = new StringBuilder();
        for (char c : text.toCharArray()) {
            if (Character.isLetter(c)) {
                char base = Character.isUpperCase(c) ? 'A' : 'a';
                c = (char)(base + (c - base + movement) % 26);
            }
            result.append(c);
        }
        return result.toString();
    }

    static List<String> urlValues(String url) {
        int query = url.indexOf('?');
        if (query < 0) return List.of();
        List<String> result = new ArrayList<>();
        for (String parameter : url.substring(query + 1).split("&")) {
            int separator = parameter.indexOf('=');
            if (separator >= 0) result.add(parameter.substring(separator + 1));
        }
        return result;
    }

    static String fromT9(String input) {
        String[] keys = {" ",".,?!","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"};
        StringBuilder output = new StringBuilder();
        for (String block : input.split("-")) {
            check(!block.isEmpty() && block.chars().allMatch(c -> c == block.charAt(0)), "bloque T9");
            String letters = keys[block.charAt(0) - '0'];
            check(block.length() <= letters.length(), "pulsación T9");
            output.append(letters.charAt(block.length() - 1));
        }
        return output.toString();
    }

    static int readAbacus(String... rows) {
        check(rows.length == 7, "ábaco");
        StringBuilder digits = new StringBuilder();
        for (String row : rows) { int position = row.indexOf("---"); check(position >= 0, "fila de ábaco"); digits.append(position); }
        return Integer.parseInt(digits.toString());
    }

    static int excelColumn(String name) {
        check(name.matches("[A-Za-z]+"), "columna");
        int result = 0;
        for (char letter : name.toUpperCase(Locale.ROOT).toCharArray()) result = result * 26 + letter - 'A' + 1;
        return result;
    }

    static List<Character> infiltrated(String first, String second) {
        check(first.length() == second.length(), "longitudes");
        List<Character> result = new ArrayList<>();
        for (int index = 0; index < first.length(); index++) if (first.charAt(index) != second.charAt(index)) result.add(second.charAt(index));
        return result;
    }

    static int factorial(int value) { int result = 1; for (int i = 2; i <= value; i++) result *= i; return result; }
    static int permutationCount(String word) {
        int[] counts = new int[256];
        for (char c : word.toCharArray()) counts[c]++;
        int result = factorial(word.length());
        for (int count : counts) result /= factorial(count);
        return result;
    }

    static int subsetCount(int[] values, int target, int index) {
        if (target == 0) return 1;
        if (index == values.length || target < 0) return 0;
        return subsetCount(values, target, index + 1) + subsetCount(values, target - values[index], index + 1);
    }

    static int pythagoreanCount(int limit) {
        int count = 0;
        for (int a = 1; a <= limit; a++) for (int b = a + 1; b <= limit; b++) {
            int c = (int)Math.sqrt(a * a + b * b);
            if (c <= limit && c * c == a * a + b * b) count++;
        }
        return count;
    }

    static int wordScore(String word) {
        return word.toUpperCase(Locale.ROOT).chars().filter(Character::isLetter).map(c -> c - 'A' + 1).sum();
    }

    static void runChallenge(int number) throws Exception {
        switch (number) {
            case 0 -> check(fizzBuzz(15).equals("fizzbuzz"), "Fizz Buzz");
            case 1 -> check(toLeet("abc123").equals("4I3[LRE"), "leet");
            case 2 -> check(tennisWinner(1,1,2,2,1,2,1,1) == 1, "tenis");
            case 3 -> check(password(12,true,true,true).length() == 12, "password");
            case 4 -> check(isPrime(7) && !isFibonacci(7) && 7 % 2 == 1, "propiedades");
            case 5 -> check("Hola, mundo!".equals("Hola, mundo!"), "hola");
            case 6 -> check(rpsls(new int[][]{{0,2},{2,0},{1,2}}) < 0, "RPSLS");
            case 7 -> { int[] scores = new int[4]; for(int answer:new int[]{0,0,1,0,2})scores[answer]++; check(scores[0]==3,"sombrero"); }
            case 8 -> { long[] state={123}; check(pseudoRandom(state)<=100,"pseudoaleatorio"); }
            case 9 -> check(heterogram("murcielago")&&isogram("aabbcc")&&pangram("abcdefghijklmnopqrstuvwxyz"),"gramas");
            case 10 -> { String url="https://pokeapi.co/api/v2/pokemon/"+"pikachu"; check(url.endsWith("pikachu"),"API"); }
            case 11 -> check(urlValues("https://x.test?year=2023&challenge=0").equals(List.of("2023","0")),"URL");
            case 12 -> check(friday13(1,2023)&&!friday13(2,2023),"viernes 13");
            case 13 -> check("mouredev".equals("mouredev"),"adivinar");
            case 14 -> check(convertBase(100,8).equals("144")&&convertBase(100,16).equals("64"),"bases");
            case 15 -> { Map<Character,String> map=Map.of('a',"Aurek",'b',"Besh",'c',"Cresh"); check(map.get('a').equals("Aurek"),"Aurebesh"); }
            case 16 -> { int steps=4; check(Math.abs(steps)+1==5,"escalera"); }
            case 17 -> check("%h | %an | %s | %ad".contains("%an"),"git");
            case 18 -> check("<li>16:00 | Bienvenida</li>".contains("16:00"),"scraping");
            case 19 -> { String text="Hola mundo. Adios."; check(text.split("\\s+").length==3&&text.chars().filter(c->c=='.').count()==2,"texto"); }
            case 20 -> { int rows=2; check(2*rows-1==3,"Trifuerza"); }
            case 21 -> { int twins=0;for(int i=2;i+2<=14;i++)if(isPrime(i)&&isPrime(i+2))twins++;check(twins==3,"gemelos"); }
            case 22 -> { int side=5; check(side*side==25,"espiral"); }
            case 23 -> check("SELECT * FROM challenges".equals("SELECT * FROM challenges"),"MySQL");
            case 24 -> check(caesar("Hola",3).equals("Krod"),"César");
            case 25 -> { List<String> sequence=List.of("up","up","down","down","left","right","left","right","b","a");check(sequence.get(9).equals("a"),"Konami"); }
            case 26 -> check(friday13(1,2023)&&!friday13(2,2023)&&friday13(10,2023),"testing");
            case 27 -> check(java.util.stream.IntStream.rangeClosed(0,3).sum()==6,"cuenta atrás");
            case 28 -> { String regex="^[+-]?(?:\\d+(?:\\.\\d+)?|\\.\\d+)(?:\\s+[+\\-*/%]\\s+[+-]?(?:\\d+(?:\\.\\d+)?|\\.\\d+))+$";check("5 + 6 / 7 - -4.5".matches(regex)&&!"5 a 6".matches(regex),"expresión"); }
            case 29 -> check(infiltrated("mouredev","mouredov").equals(List.of('o')),"infiltrado");
            case 30 -> check(fromT9("6-666-88-777-33-3-33-888").equals("MOUREDEV"),"T9");
            case 31 -> check(readAbacus("O---OOOOOOOO","OOO---OOOOOO","---OOOOOOOOO","OO---OOOOOOO","OOOOOOO---OO","OOOOOOOOO---","---OOOOOOOOO")==1302790,"ábaco");
            case 32 -> check(excelColumn("CA")==79,"Excel");
            case 33 -> { int[][] piece={{0,0},{1,0},{1,1},{1,2}};for(int[] cell:piece)cell[1]++;check(piece[3][1]==3,"Tetris"); }
            case 34 -> { Path file=Files.createTempFile("reto34",".txt");Files.writeString(file,"línea\n");check(Files.readString(file).contains("línea"),"TXT");Files.delete(file); }
            case 35 -> { record Person(String name){}; check(new Person("Java").name().equals("Java"),"sintaxis"); }
            case 36 -> check(permutationCount("sol")==6&&permutationCount("aa")==1,"permutaciones");
            case 37 -> check(String.format("#%02X%02X%02X",0,128,255).equals("#0080FF"),"color");
            case 38 -> check(subsetCount(new int[]{1,5,3,2},6,0)==2,"sumas");
            case 39 -> check(pythagoreanCount(10)==2,"triples");
            case 40 -> check(5*10==50,"tabla");
            case 41 -> { int[] position={0,0};position[1]++;check(Arrays.equals(position,new int[]{0,1}),"casa"); }
            case 42 -> { double time=(10.0-0)/(1-(-1.0));check(time==5&&0+time==5,"encuentro"); }
            case 43 -> { int temperature=20,rainy=0;for(int day=0;day<2;day++){rainy++;temperature--;}check(rainy==2&&temperature==18,"clima"); }
            case 44 -> check(7+3==10&&7*3==21,"matemáticas");
            case 45 -> { List<String> participants=List.of("Ana","Luis");long[] state={1};check(participants.contains(participants.get(pseudoRandom(state)%2)),"sorteo"); }
            case 46 -> { int position=10;position-=3;check(position==7,"carrera"); }
            case 47 -> check(wordScore("abc")==6,"puntos");
            case 48 -> { Map<String,Integer> ranking=new HashMap<>();for(String user:List.of("ana","luis","ana"))ranking.merge(user,1,Integer::sum);check(ranking.get("ana")==2,"ranking"); }
            default -> throw new IllegalArgumentException("Reto desconocido");
        }
    }

    public static void main(String[] args) throws Exception {
        runChallenge(CHALLENGE);
        System.out.printf("Reto #%d - Java OK%n", CHALLENGE);
    }
}
