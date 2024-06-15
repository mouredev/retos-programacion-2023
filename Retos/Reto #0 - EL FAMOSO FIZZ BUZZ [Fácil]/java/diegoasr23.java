public class diegoasr23 {
    public static void main(String[] args) {
        new diegoasr23().reto01(1);
    }

    void reto01(int i) {
        if ((i % 3 == 0) && (i % 5 == 0))
            System.out.println("FlizzBuzz");
        else if (i % 5 == 0)
            System.out.println("Buzz");
        else if (i % 3 == 0)
            System.out.println("Flizz");
        if (i == 100)
            return;
        reto01(i + 1);
    }

}