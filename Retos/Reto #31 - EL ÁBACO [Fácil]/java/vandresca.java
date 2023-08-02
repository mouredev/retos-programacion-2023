package vandresca;

/*
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar
 *   operaciones) para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a
 *   la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *  
 *  Resultado: 1.302.790
 */
public class vandresca {
    
    static String[] abaco={
        "O---OOOOOOOO",
         "OOO---OOOOOO",
        "---OOOOOOOOO",
        "OO---OOOOOOO",
        "OOOOOOO---OO",
        "OOOOOOOO0---",
        "---OOOOOOOOO"
    }; 
    
    public static void main(String[] args) {

       StringBuilder stringBuilder = new StringBuilder();
       for(String cipher: abaco ){
            String[] cipherArray = cipher.split("---");
            int cipherNumeric = Integer.valueOf(cipherArray[0].length());
            stringBuilder.append(cipherNumeric);
       };
       System.out.println("Este es el ábaco: ");
       for(String cipher: abaco){
            System.out.println("\t"+cipher);
       }
       System.out.println();
       int number = Integer.valueOf(stringBuilder.toString());
       String formattedNumber = String.format("%,d", number);
       formattedNumber = formattedNumber.replace(",",".");
       System.out.println("Resultado: "+ formattedNumber);
       
    }
}
