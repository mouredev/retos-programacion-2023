import java.util.HashSet;

public class Elez95 {
   
    
	public static HashSet<String> permutar(String palabra) {

		if(palabra.length() > 6) {
			throw new IllegalArgumentException("Se recomienda escribir una palabra de longitud menor a 6 para evitar un exceso de trabajo al cpu");
		}
		else 
		{
			String palabraArmada = "";
			HashSet<String> permutaciones = new HashSet<>();
			generar_permutaciones(palabraArmada, palabra, permutaciones);
			return permutaciones;
		}
	}

    private static void generar_permutaciones(String palabraArmada, String palabra, HashSet<String> permutaciones) {
        
    	int n = palabra.length();
        if (n == 0) {
            permutaciones.add(palabraArmada);
        }
        else 
        {
            for (int i = 0; i < n; i++) {
                generar_permutaciones(palabraArmada + palabra.charAt(i), palabra.substring(0, i) + palabra.substring(i + 1), permutaciones);
            }
        }
    }
    
    
    
    public static void main(String[] args) {
    	
        String palabra = "SOL";
        HashSet<String> permutacionesDisponibles = permutar(palabra);
        
        for (String permutacion : permutacionesDisponibles) {
            System.out.println(permutacion);
        }
    }
}