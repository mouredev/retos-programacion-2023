public class SoleSasia {
  
    public static void main(String[] args) {
        System.out.println(esExpresionMatematica("5 + 6 / 7 - 4"));
    }

    private static boolean esExpresionMatematica(String expresionMatematica) {
        return expresionMatematica.matches("(-*\\d+.*\\d*\\s+[-+*/%]\\s+-*\\d+.*\\d*\\s*)+");
    }

}
