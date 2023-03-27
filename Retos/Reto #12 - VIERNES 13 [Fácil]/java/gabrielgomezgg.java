public class RetoTrece {

    /*
     * Crea una función que sea capaz de detectar si existe un viernes 13
     * en el mes y el año indicados.
     * - La función recibirá el mes y el año y retornará verdadero o falso.
     */

    public static void main(String[] args) {

        var anio = 2023;
        var mes = 1;

        System.out.println(esViernesTrece(anio,mes));

    }
    
    private static boolean esViernesTrece(int anio, int mes) {
        var fecha = LocalDate.of(anio, mes, 13);
        if (fecha.getDayOfWeek() != DayOfWeek.FRIDAY){
            return false;
        }
        return true;
    }
}