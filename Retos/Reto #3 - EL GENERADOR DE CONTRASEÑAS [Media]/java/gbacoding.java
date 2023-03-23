import java.util.Scanner;

public class Reto3GeneradorDeContraseñas {

	public static void main(String[] args) { 
		// TODO Auto-generated method stub
		
		// ---------------------------
		//   DECLARACION DE VARIABLES
		// ----------------------------

		

		// Variables de Entrada
		int longitudContraseñaIntroducida;
		String codigoSiMayuscula, codigoSiMinuscula, codigoSiNumero, codigoSiSimbolos;
		
		// Variables de Salida
		String contraseñaGenerada = "";
		
		// Variables Auxiliares
		boolean mayusculasContinuar = false, minusculasContinuar = false, numerosContinuar = false, simbolosContinuar = false;
		int longitudContraseñaGenerada = 0, numeroAleatorio, posicionMayusculas, posicionMinusculas, posicionNumeros, posicionSimbolos;
		
		// Constructor clase Scanner
		Scanner src = new Scanner (System.in);
		
		// Arrays
		String [] configuracionesContraseña  = new String [4];
		
		String [] mayusculas =  {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"};
		String [] minusculas =  {"a","b","c","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"};
		String [] numeros =  {"0","1","2","3","4","5","6","7","8","9"};
		String [] simbolos =  {"-","*",".","¿",",",";","!","@","#","$","%","&","/","(",")","=","?","+","¡"};
		
		// ---------------------------
		//       ENTRADA DE DATOS
		// ----------------------------
		// Pedimos a usuario la longitud de la contraseña
		do { 
			System.out.println("Por favor, introduzca la longitud deseada para su contraseña (mínimo de 8, máximo 16).");
			longitudContraseñaIntroducida = src.nextInt();
			if (longitudContraseñaIntroducida < 8 || longitudContraseñaIntroducida > 16)
				System.out.print("Longitud introducida no válida. ");
			
		} while (longitudContraseñaIntroducida < 8 || longitudContraseñaIntroducida > 16);
		src.nextLine();
		
		// incluir MAYUSCULAS en  contraseña
		do {
			System.out.println("Pulse 1 si quiere introducir MAYUSCULAS en su contraseña. Si no marque 0.");
			codigoSiMayuscula = src.nextLine();
			if (codigoSiMayuscula.equals("0") || codigoSiMayuscula.equals("1")) 
				mayusculasContinuar = true; 
				configuracionesContraseña[0] = codigoSiMayuscula;
		} while (mayusculasContinuar = false);
		
		
		// incluir MINUSCULAS en  contraseña
		do {
			System.out.println("Pulse 1 si quiere introducir MINISCULAS en su contraseña. Si no marque 0.");
			codigoSiMinuscula = src.nextLine();
			if (codigoSiMinuscula.equals("0") || codigoSiMinuscula.equals("1")) 
				minusculasContinuar = true; 
				configuracionesContraseña[1]=codigoSiMinuscula;
					
		} while (minusculasContinuar = false);
		
		// incluir NUMEROS en  contraseña
		do {
			System.out.println("Pulse 1 si quiere introducir NUMEROS en su contraseña. Si no marque 0.");
			codigoSiNumero = src.nextLine();
			if (codigoSiNumero.equals("0") || codigoSiNumero.equals("1")) 
				numerosContinuar = true; 
				configuracionesContraseña[2]=codigoSiNumero;
					
		} while (numerosContinuar = false);
		
		// incluir SIMBOLOS en contraseña
		do {
			System.out.println("Pulse 1 si quiere introducir SIMBOLOS en su contraseña. Si no marque 0.");
			codigoSiSimbolos = src.nextLine();
			if (codigoSiSimbolos.equals("0") || codigoSiSimbolos.equals("1")) 
				simbolosContinuar = true; 
				configuracionesContraseña[3]=codigoSiSimbolos;
					
		} while (simbolosContinuar = false);
		
		System.out.println();
		System.out.print("Array configuración contraseña: {" +configuracionesContraseña[0] + ", " +configuracionesContraseña[1] + ", " +configuracionesContraseña[2] + ", " +
				configuracionesContraseña[3] + "}. ");
		
    // ---------------------------
		//        PROCESAMIENTO
		// ----------------------------
		
		System.out.println();
		
		while (contraseñaGenerada.length() <= longitudContraseñaIntroducida) {
				numeroAleatorio =(int)(Math.random()*(4-0)+0);// nº aleatorio entre 2 valores Math.random() * (max - min) + min
		
					if (numeroAleatorio == 0 && configuracionesContraseña[0].equals("1")) {
						posicionMayusculas =(int)(Math.random()*(27-0)+0);
						contraseñaGenerada += mayusculas[posicionMayusculas];
					 } else if (numeroAleatorio == 1 && configuracionesContraseña[1].equals("1")) {
						posicionMinusculas =(int)(Math.random()*(27-0)+0);
						contraseñaGenerada += minusculas[posicionMinusculas];
					 } else if (numeroAleatorio == 2 && configuracionesContraseña[2].equals("1")) {
						posicionNumeros =(int)(Math.random()*(10-0)+0);
						contraseñaGenerada += numeros[posicionNumeros];
					 } else if (numeroAleatorio == 3 && configuracionesContraseña[3].equals("1")) {
						posicionSimbolos =(int)(Math.random()*(19-0)+0);
						contraseñaGenerada += simbolos[posicionSimbolos];
					 }

		}
		
		// ---------------------------
		//        SALIDA DE DATOS
		// ----------------------------

		System.out.print(contraseñaGenerada);

	}

}
