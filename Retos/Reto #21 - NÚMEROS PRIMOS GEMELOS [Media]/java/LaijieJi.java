import java.util.*;
public class LaijieJi{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in).useLocale(Locale.US);
		boolean[] prime = new boolean[2000000];
		calculoPrimos(prime);
		System.out.println("Inserta un rango para encontrar primos gemelos");
		num = sc.nextInt();
		primosGemelos(prime, num);	

	}
	//precalculamos una serie de números primos
  public static void calculoPrimos (boolean [] prime){
		for (int a = 2; a < prime.length; a++){
			prime[a] = true;
		}
		for (int i = 3; i < prime.length; i++){
			if (prime[i]){
				for (int j = i + i; j < prime.length;j += i){
					prime[j] = false;
				}
			}
		}
		prime[4] = false;
		prime[1] = false;
	}
  //Comprobamos los primos gemelos que hayan en el array, con un límite superior especificado
	public static void primosGemelos(boolean[] prime, int bound){
		StringBuffer sol = new StringBuffer();
		for(int i = 3; i < bound - 2; i++){
			if(prime[i] && prime[i + 2]){
				sol.append("(" + i + ", " + (i + 2) + ") ");
			}
		}
		System.out.println(sol);
	}
}
