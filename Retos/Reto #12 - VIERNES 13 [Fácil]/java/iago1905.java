import java.sql.Date;
import java.time.LocalDate;

class iago1905 {
    public static void main(String[] args) {
        System.out.println(viernes_trece(2023, 10));
    }   
    
    private static boolean viernes_trece(int year,int month){
        LocalDate fecha = LocalDate.of(year, month, 13);
        return fecha.getDayOfWeek().getValue() == 5;
    }
}
