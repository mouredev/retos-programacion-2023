import java.security.SecureRandom;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
/*
Reto 3: 
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

public class TaidaCR{

    private static Scanner scanner =new Scanner(System.in);

    private static final String MINUSCULAS = "abcdefghijklmnopqrstuvwxyz";
    private static final String MAYUSCULAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private static final String NUMEROS = "0123456789";
    private static final String SIMBOLOS = "!@#$%^&*()_-+=<>?";

    //STATIC: solo hay 1 instancia y se usa en toda la clase. Mejor que tener varias
    //FINAL: una vez creado random no se puede modificar, se convierte en una constante...
    //...si lo elimino funciona igual 
    private static final SecureRandom random = new SecureRandom ();

    public static String generatePass(int longitud, String may, String num, String simb){
        StringBuilder resultado=new StringBuilder();

        List <Integer> numerosPermitidos= new ArrayList<Integer>();
        numerosPermitidos.add(1);

            if (may.equalsIgnoreCase("Y")){
                numerosPermitidos.add(0);
            }

            if (simb.equalsIgnoreCase("Y")){
                numerosPermitidos.add(2);
            }

            if (num.equalsIgnoreCase("Y")){
                numerosPermitidos.add(3);
            }

            for (int i=0;i<longitud;i++){
            
            //devuelve el numero del tamaño de la lista: por ejemplo 3
            int tam=numerosPermitidos.size();
            
            //metemos el tamaño de la lista en random para que elija una posición
            int posicion=random.nextInt(tam);

            //coge el caracter de la posicion random elegida
            int indice=numerosPermitidos.get(posicion);

            //Para por elementoalAzar y resuelve para traer el caracter que lo añade al password
            resultado.append(elementoAlAzar(indice));
        }
        //devuelve la contraseña
        return resultado.toString();
    }

    //escoge el grupo seleccionado y de ahí un  caracter
    public static char elementoAlAzar (Integer agregarElemento){
        char caracter=1;
        int index=0;
        switch (agregarElemento){
            case 0:
                index= random.nextInt(MAYUSCULAS.length());
                caracter= MAYUSCULAS.charAt(index);
                break;
            case 1:
                index= random.nextInt(MINUSCULAS.length());
                caracter= MINUSCULAS.charAt(index);
                break;
            case 2:
                index= random.nextInt(SIMBOLOS.length());
                caracter= SIMBOLOS.charAt(index);
                break;
            case 3:
                index= random.nextInt(NUMEROS.length());
                caracter= NUMEROS.charAt(index);
                break;
        }
        return caracter;
    }

    //elige la longitud
    public static Integer generadorLongitud(String respuesta1){
        int longitud=0;
        boolean r=true;
        while(r){
            if (respuesta1.equalsIgnoreCase("R")){
                if (respuesta1.equalsIgnoreCase("R")){
                    longitud=random.nextInt(8) + 8;
                    r=false;
                }
            }else {
                try{
                    int num=Integer.parseInt(respuesta1);
                    if((num > 7) && (num <17)){
                        longitud=num;
                        r=false;
                    }else{
                        System.out.println("Por favor introduzca un numero del 8 al 16: ");
                        respuesta1=scanner.nextLine();
                    }
                }catch(NumberFormatException e){
                    System.out.println("Por favor introduzca un valor válido: ");
                    respuesta1=scanner.nextLine();
                }
            }
        
        }  
        return longitud;
    }

    //validador Y//N
    public static String validadorYoN (String respuesta){
        boolean r=true;
        while(r){
            if (respuesta.equalsIgnoreCase("Y")||respuesta.equalsIgnoreCase("N")){
                r=false;
            }else{
                System.out.println("Por favor introduzca un valor válido: ");
                respuesta=scanner.nextLine();
            }
        }
        return respuesta;
    }  

    //Donde comienza la ejecución del programa. Métodos fuera.
    public static void main(String[] args) {

        System.out.println("---GENERADOR DE CONTRASEÑAS---");
        System.out.println("Longitud: introduzca un número entre 8-16 o presione R para random");
        String longitud=scanner.nextLine();
        int longitudValidada=generadorLongitud(longitud);

        System.out.println("Mayusculas: Y(si)//N(no)");
        String may=scanner.nextLine();
        validadorYoN(may);
        System.out.println("Simbolo: Y(si)//N(no)");
        String simb=scanner.nextLine();
        validadorYoN(simb);
        System.out.println("Numero: Y(si)//N(no)");
        String num=scanner.nextLine();
        validadorYoN(num);

        System.out.println("TU CONTRASEÑA ES: ");
        System.out.println(generatePass(longitudValidada, may, num, simb));
    }
}
