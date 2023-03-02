public class LaijieJi{
    // Propuesta de solución para el reto
    public static void main(String[] args){
        long num = System.currentTimeMillis();
        num = num * num + num;
        System.out.println("El número aleatorio es: " + (num % 100));
    }
}
