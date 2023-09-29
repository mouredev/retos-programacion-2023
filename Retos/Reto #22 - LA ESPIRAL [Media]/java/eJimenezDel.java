import java.util.Scanner;

/*
 * Crea una función que dibuje una espiral como la del ejemplo.
 * - Únicamente se indica de forma dinámica el tamaño del lado.
 * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
 *
 * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
 * ════╗
 * ╔══╗║
 * ║╔╗║║
 * ║╚═╝║
 * ╚═══╝
 */
public class eJimenezDel {
	
	public static void main(String[] args) {
		eJimenezDel reto22eJimenez = new eJimenezDel();
		try(Scanner input = new Scanner(System.in)){
			int max;
			
	        System.out.print("Ingresa el tamaño del lado: ");
	        max = input.nextInt();        
	        
            reto22eJimenez.printSpiral(max);	        
		}catch(Exception e) {
			e.printStackTrace();

			
		}        
    }
	
	private void printSpiral(int lado) {
		int iniRow = 1;
		int iniCol = 0;
		int endRow = lado;
		int endCol = lado+1;
		
		int nivel = lado-1;
		
		for (int i = 1; i <= lado; i++) {
			
			for (int j = 1; j <= lado; j++) {
												
				if(i==iniRow && j==endCol-1 && j>=i) 
					System.out.print( "╗");
				else if(j== iniCol && i==iniRow && j < endCol-1) 
					System.out.print("╔");
				else if(i==lado - nivel && j==1 + nivel) 
					System.out.print( "╚");
				else if(j==lado && i==lado || (j==lado-nivel && i==lado-nivel && i>endRow )) 
					System.out.print( "╝");				
				else if(j>=iniCol && j<endCol || j>=endCol && j<=iniCol ) 
					System.out.print("═");
				else
					System.out.print("║");
				             
			}		
			
			System.out.print( "\n");

			iniCol++;
			endCol--;
			iniRow++;			
			endRow--;
			nivel--;
			
			
        }
        
	}

}
