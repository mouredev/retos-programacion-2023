import java.util.Scanner;

public class sergiolpzgmz {
    /*
     * Escribe un programa que, dado un número, compruebe y muestre si es primo,
     * fibonacci y par.
     * Ejemplos:
     * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
     * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
     */
    public static boolean esPar(int numUsuario){
        boolean resultado = false;

        if(numUsuario % 2 == 0) resultado = true;

        return resultado;
    }
    public static boolean esPrimo(int numUsuario){
        boolean primo = true;

        for (int i = 2; i < numUsuario; i++) {
            if(numUsuario%i==0){
                primo=false;
                break;
            }
        }
        if(numUsuario == 0 || numUsuario == 1) primo = false;
        return primo;
    }
    public static boolean esFibonacci(int numUsuario){
        int num1=0;
        int num2=1;
        int suma=0;

        boolean fibonacci = false;
        for (int i = 1; i <= numUsuario; i++) {
            suma = num1 + num2;
            num1 = num2;
            num2 = suma;
            if(numUsuario == suma) {
                fibonacci = true;
                break;
            }
        }
        return fibonacci;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Introduce un número: ");
        int numUsuario = sc.nextInt();

        String par = "";
        String primo = "";
        String fibonacci="";

        if(esPar(numUsuario)==true) par = "y es par";
        else par = "y es impar";
        if(esPrimo(numUsuario)==true) primo = "es primo";
        else primo = " no es primo";
        if (esFibonacci(numUsuario)==true) fibonacci = ", es fibonacci ";
        else fibonacci = ", no es fibonacci ";

        System.out.println(numUsuario + "" + primo + fibonacci + par);

        sc.close();
    }
}
