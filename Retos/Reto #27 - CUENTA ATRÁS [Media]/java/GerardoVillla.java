
package retos;

public class GerardoVillla {
    public static void main(String[] args) {
        countdown(12, 1);
        countdown(3, 2);
    }
    
    public static void countdown(int start, int duration){
        for (int i = start; i >= 0; i--){
            System.out.println("Countdown = " + i);
            try{
                Thread.sleep(duration * 1000);
            }catch(InterruptedException e){
                e.printStackTrace();
            }
        }
    }
}
