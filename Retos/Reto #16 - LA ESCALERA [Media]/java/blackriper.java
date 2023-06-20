
import java.util.Scanner;



/**
 *
 * @author blackriper
 */
class Stair {
    
    private int numberOfStairs=0;
    private  final ShowStair s = new ShowStair();
    
    public Stair( int numSta){
        this.numberOfStairs=numSta;
    }
    
    private void printStair(){
       //cuando es un numero positivo 
       if(this.numberOfStairs>0){
           s.setNumberstairs(this.numberOfStairs);
           s.printPositiveNumber();
          
       }
       // cuando es un numero negativo lo convierto a positivo solo uso esa referencia para imprimir el orden descendente
       if(this.numberOfStairs<0){
           s.setNumberstairs(this.numberOfStairs*-1);
           s.printNegativeNumber();
       }
       // cuando el numero es cero
       if(this.numberOfStairs==0){
          System.out.print("__\n");  
       }
    }
    
    //clase para leer datos de consola
    static Scanner sc = new Scanner(System.in);
    
    public static void main(String args[]){
        System.out.println("Introduce un numero de escalones: ");
        int numStair  = sc.nextInt();
        
        Stair st= new Stair(numStair);
        st.printStair();
        
    }
}


class ShowStair{
    
    private int numberOfStairs=0;
    
    public ShowStair(){}  
    
    //setter para obtener numero de escalones
    protected void setNumberstairs(int num){
        this.numberOfStairs=num;
    }
    
    // imprimir un numero negativo se imprime la base _ y luego se incrementan los espacios de dos en dos 
    protected void printNegativeNumber(){
        System.out.print("_\n");
        int numberSpaces=2;
        for(int i=0;i<this.numberOfStairs;i++){
            // clase para agregar los espacios a un cierto string
            String textWithSpc = String.format("%{num}s".replace("{num}",String.valueOf(numberSpaces)), "|_\n"); 
            System.out.print(textWithSpc);
            numberSpaces=numberSpaces+2;
            
         }
    }   
    
    // imprimir un numero positivo la base se imprime con un espaciado de veinte y se disminuye de dos en dos 
    protected void printPositiveNumber(){
         System.out.print(String.format("%20s", "_\n"));
         int numberSpaces=19;
         for(int i=0;i<this.numberOfStairs;i++){
            String textWithSpc = String.format("%{num}s".replace("{num}",String.valueOf(numberSpaces)), "_|\n"); 
            System.out.print(textWithSpc);
            numberSpaces=numberSpaces-2;
            
         }
         
    }

}