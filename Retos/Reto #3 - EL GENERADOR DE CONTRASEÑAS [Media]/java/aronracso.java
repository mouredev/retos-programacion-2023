import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;

/**
 * Reto #3: EL GENERADOR DE CONTRASEÑAS
 * MEDIA | Publicación: 16/01/23 | Resolución: 23/01/23
 * 
 * Enunciado:
 * 
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
public class aronracso
{
    protected static final String MINUSCULAS = "abcdefghijklmnñopqrstuvwxyz";
    protected static final String MAYUSCULAS = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ";
    protected static final String NUMEROS = "0123456789";
    protected static final String SIMBOLOS = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";
    
    public static void main(String[] args) throws NoSuchAlgorithmException
    {
        System.out.println(generarContraseña(8, false, false, false));
        System.out.println(generarContraseña(11, true, false, false));
        System.out.println(generarContraseña(14, false, true, false));
        System.out.println(generarContraseña(16, true, true, true));
    }

    public static String generarContraseña(int longitud, boolean mayusculas, boolean numeros, boolean simbolos) throws NoSuchAlgorithmException
    {
        if(longitud < 8 || longitud > 16)
            throw new IllegalArgumentException("El parámetro longitud debe estar entre 8 y 16");

        StringBuilder caracteres = new StringBuilder(MINUSCULAS);
        if(mayusculas)
            caracteres.append(MAYUSCULAS);
        if(numeros)
            caracteres.append(NUMEROS);
        if(simbolos)
            caracteres.append(SIMBOLOS);

        SecureRandom random = SecureRandom.getInstanceStrong();

        StringBuilder contraseña = new StringBuilder();
        for(int i = 0; i < longitud; ++i)
        {
            char c = caracteres.charAt(random.nextInt(caracteres.length()));
            contraseña.append(c);
        }

        return contraseña.toString();
    }
}
