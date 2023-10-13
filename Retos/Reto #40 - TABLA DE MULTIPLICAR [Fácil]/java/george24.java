import java.util.Scanner;

public class george24
{
    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        int num = 0;
        System.out.println("Ingrese el número: ");
        num = sc.nextInt();
        sc.close();
        System.out.println("Tabla de multiplicar del " + num + ": ");
        tabla_multip(num);

	}

    public static void tabla_multip(int num){
        for (int i= 1; i <=10; i++){
            int total = num *i;
            System.out.println(num + " x " + i + " = " + total );
        }
    }
}