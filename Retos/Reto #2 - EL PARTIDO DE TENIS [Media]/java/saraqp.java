import java.util.Scanner;

public class saraqp {
    static int p1 = 0;
    static int p2 = 0;
    static boolean finalizado=false;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("escribe la secuencia deseada. Ej: P1,P1,P2,P2,P1,P2,P1,P1");
        String usuario=sc.nextLine().toUpperCase();
        String[] partido_usuario=(usuario.trim()).split(",");

        jugarPartido(partido_usuario);
        sc.close();
    }
    private static void jugarPartido(String[] partido){
        for(String jugada:partido){
            if(jugada.equals("P1")){
                if(p2>40){
                    p2-=15;
                }
                if(p1==30){
                    p1+=10;
                }else{
                    p1+=15;
                }
            }else{
                if(p1>40){
                    p1-=15;
                }
                if(p2==30){
                    p2+=10;
                }else{
                    p2+=15;
                }
            }
            mostrarPuntuacion(p1,p2);
            if(finalizado){
                break;
            }
        }
    }
    private static String mostrarPuntuacion(int p1, int p2) {
        String tablaPuntuacion="";

        if(p1>40 && p2<40){
            System.out.println("Ha ganado el P1");
            finalizado=true;
        }else if(p1<40 && p2>40){
            System.out.println("Ha ganado el P2");
            finalizado=true;
        }else if(p1>40 && p2==40){
            if(p1==70){
                System.out.println("Ha ganado el P1");
                finalizado=true;
            }else{
                System.out.println("Ventaja P1");
            }
        }else if(p2>40 && p1==40){
            if(p2==70){
                System.out.println("Ha ganado el P2");
                finalizado=true;
            }else{
                System.out.println("Ventaja P2");
            }
        }else if(p1==40 && p2==40){
            System.out.println("Deuce");
        }else if(p1!=40 && p2!=40) {
            if(p2==0){
                System.out.println(p1+" - Love");
            }else if(p1==0){
                System.out.println("Love - "+p2);
            }else{
                System.out.println(p1+" - "+p2);
            }

        }else if(p1==40 && p2!=40){
            if(p2==0){
                System.out.println(p1+" - Love");
            }else if(p1==0){
                System.out.println("Love - "+p2);
            }else{
                System.out.println(p1+" - "+p2);
            }
        }else{
            if(p2==0){
                System.out.println(p1+" - Love");
            }else if(p1==0){
                System.out.println("Love - "+p2);
            }else{
                System.out.println(p1+" - "+p2);
            }
        }
        return tablaPuntuacion;
    }
}
