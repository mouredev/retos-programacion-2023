import java.util.*;
public class LaijieJi {
    //Solución propuesta para el reto #4
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in).useLocale(Locale.US);
        int n;
        while(sc.hasNext()){
            n = sc.nextInt();
            System.out.print(n + isPrime(n) + isFibonacci(n));
            if (isEven(n) == true) {
                System.out.print(" y es par\n");
            } else {
                System.out.print(" y es impar\n");
            }
        }
        sc.close();
    }

    public static String isPrime(int n){
        if (n == 2){
            return " es primo,";
        }
        if (n == 1 || isEven(n)){
            return " no es primo,";
        } else {
            for (int i = 3; i < Math.sqrt(n); i += 2){
			    if (n % i == 0){
				    return " no es primo,";
			    }   
		    }
            return " es primo,";
        }
    }

    public static boolean isEven(int n){
        if (n % 2 == 0){
            return true;
        } else {
            return false;
        }
    }

    public static String isFibonacci(int n){
        if(isPerfectSquare(5 * n * n + 4) || isPerfectSquare(5 * n * n - 4)){
            return " fibonacci,";
        } else {
            return " no es fibonacci,";
        }
    }

    public static boolean isPerfectSquare(int n){
        int aux = (int) Math.sqrt(n);
        return (aux * aux == n); 
    }
}
