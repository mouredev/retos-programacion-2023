import java.util.Scanner;
public class Program
{
    public static void main(String[] args) {
        Scanner numero = new Scanner(System.in);
    int num = numero.nextInt();
    int total = 0;
    String text= "";
        for(int i =1; i<=10; i++){
            total = num * i; 
        text =  num+" x "+i + " = "+total;
        System.out.println(text);    
        }
	}
}