public class EspinoLeandroo {

    public static void main(String[] args) {

        long semilla = System.currentTimeMillis();
        for (int i = 0; i < 11; i++) {
            semilla = (1103515245 * semilla + 12345) % 2147483648L;
            int randomNum = (int) (semilla % 101);
            System.out.println(randomNum);
          }
    }
}
