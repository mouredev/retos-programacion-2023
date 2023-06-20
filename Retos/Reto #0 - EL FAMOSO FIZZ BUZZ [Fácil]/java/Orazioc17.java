public class Orazioc17 {
    public static void main(String[] args) {
        for (int i = 1; i < 101; i++) {
            String palabra = "";

            palabra = (i % 3 == 0)?palabra+"fizz":palabra;
            palabra = (i % 5 == 0)?palabra+"buzz":palabra;

            palabra = (palabra.equals(""))?palabra+i:palabra;

            System.out.println(palabra);
        }
    }
}