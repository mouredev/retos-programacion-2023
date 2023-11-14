import java.io.*;
import java.util.Scanner;

class Multiplicate {
    
   private int num=0;
   Scanner sc = new Scanner(System.in);
  
    public void read_number(){
      System.out.println("What multiplication table do you want to see?");  
      num=sc.nextInt();
        
    }
    
    public void print_table(){
      System.out.println("multiplication table "+num);        
      for (int n=1;n<=10 ;n++ ){
         System.out.println(num+"x"+n+"="+(num*n));
      }         
    }
  
    
	public static void main (String[] args) {
	   Multiplicate mult= new Multiplicate();
	   mult.read_number();
	   mult.print_table();
	}
}
