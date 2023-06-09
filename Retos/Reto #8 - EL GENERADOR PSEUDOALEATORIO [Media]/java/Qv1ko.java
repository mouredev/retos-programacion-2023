public class Qv1ko {

    public static void main(String[] args) {
        System.out.println(random());
    }//main

    private static long random() {
        return System.nanoTime()%101;
    }//random

}//class