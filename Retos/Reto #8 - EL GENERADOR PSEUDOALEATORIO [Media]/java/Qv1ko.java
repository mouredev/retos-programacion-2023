public class Qv1ko {

    public static void main(String[] args) {
        System.out.println(randomNumber());
    }//main

    private static int randomNumber() {
        double num1=((double)System.currentTimeMillis())/1000;
        double num2=Math.floor(num1);
        return (int)(((num1)-num2)*101);
    }//randomNumber

}//class
