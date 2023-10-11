import java.util.Scanner;
public class Program
{
    public static void main(String[] args) {
        Scanner numero = new Scanner(System.in);
    int num = numero.nextInt();    
        for(int i =1; i<=10; i++){        
        System.out.println(num+" x "+ i+" = "+num * i);
        }
	}
}
