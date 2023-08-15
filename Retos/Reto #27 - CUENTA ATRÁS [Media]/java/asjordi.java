public class Countdown {

    public static void main(String[] args) {
        execute(10, 6);
    }

    public static void execute(int start, int seconds) {
        if (start > 0 && seconds > 0){
            for (int i = start; i >= 0; i--) {
                System.out.println(i);
                if (i == 0) break;
                try{
                    Thread.sleep(seconds * 1000);
                } catch (Exception e){
                    System.out.println("There was an error: " + e.getMessage());
                }
            }
        } else{
            throw new RuntimeException("Los parámetros tienen que ser enteros positivos mayores a 0");
        }
    }

}
