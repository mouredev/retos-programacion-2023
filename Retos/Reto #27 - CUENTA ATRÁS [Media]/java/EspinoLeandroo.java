import java.util.Scanner;

public class EspinoLeandroo {

    public static void main(String[] args) {
        EspinoLeandroo espinoLeandroo = new EspinoLeandroo();

        Scanner sc = new Scanner(System.in);

        System.out.println("¿Desde que numero iniciara la cuenta regresiva? ");
        int start = sc.nextInt();
        System.out.println("¿Cuantos segundos seran de pausa entre cada numero? ");
        int pause = sc.nextInt();

        while (start >= 0) {
            System.out.println(start--);
            try {
                Thread.sleep(pause * 1000);
            } catch (InterruptedException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }

    }

}