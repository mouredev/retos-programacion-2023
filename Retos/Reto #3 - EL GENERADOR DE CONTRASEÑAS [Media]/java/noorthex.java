/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
public class noorthex {
	
	public void passwordGenerator()
	{	
		char letrasM[] = {'a','b','c','d','e','f','g','h','i','j','k','l','ñ','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
		char letrasMn[] = {'A','B','C','D','E','F','G','H','I','J','K','L','Ñ','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
		char simbolos[] = {'!','#','$','%','&','/','(',')','=','?','¡'};
		int numeros[] = new int[100];
		for(int i=0;i<8;i++)
		{
			int letrasAM = (int)(Math.random()*27); 
			int letrasMN = (int)(Math.random()*27);
			int simbolosAM = (int)(Math.random()*11);
			int numerosAM = (int)(Math.random()*100);
			String cadena = String.valueOf(letrasM[letrasAM])+String.valueOf(letrasMn[letrasMN])+String.valueOf(simbolos[simbolosAM]+numeros[numerosAM]);
			System.out.print(cadena);
		}
	}
}