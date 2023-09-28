/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */

public class AnNavNicolas {
    public static void main(String[] args) {
        System.out.println(findColumn("A"));
        System.out.println(findColumn("Z"));
        System.out.println(findColumn("AA"));
        System.out.println(findColumn("CA"));
        System.out.println(findColumn("zz"));
    }
    public static Integer findColumn(String column) {
        column = column.toUpperCase();
        Integer result = 0;
        for(char character : column.toCharArray()){
            int i = 1;
            for(char c = 'A'; c <= 'Z'; ++c){
                if(character == c){
                    result = result * 26 + i;
                }
                i++;
            }
        }
        return result;
    }
}