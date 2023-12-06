/**
 * @author lukaku
 */


/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */
public class Tenis {
 
    public String puntoGanador(){
        String punto="";
        Integer op;
        
        op = (int)(Math.random()*2)+1;
        switch(op){
            case 1:
                punto = "P1";
                break;
            case 2: 
                punto = "P2";
                break;
        }
        return punto;   
    }
    public int suma(int posicion){
        return posicion+1;
    }
    public void juego(){
        int posP1=0;
        int posP2=0;
        String punto="";
        boolean ganador=false;
        String[] p1;
        p1 = new String[]{"love","15","30","40","deuce","ventaja"};
        String[] p2;
        p2 = new String[]{"love","15","30","40","deuce","ventaja"};
        
        while(!ganador){
            punto=puntoGanador();
            switch(punto){
                case "P1":
                    
                    System.out.print(p1[posP1=suma(posP1)]+ " - ") ;
                    System.out.print(p2[posP2]);
                    System.out.println(" ");
                    break;
                    
                case "P2":
                    System.out.print(p1[posP1]+ " - ") ;
                    System.out.print(p2[posP2=suma(posP2)]);
                    System.out.println(" ");
                    break;
            }
            
            if(posP1==3 && punto.contains("P1")){
                ganador = true;
                System.out.println("P1 ha ganado");
            } else if (posP1==5 && punto.contains("P1")){
                ganador = true;
                System.out.println("P1 ha ganado");
            } else if (posP2==5 && punto.contains("P2")){
                ganador = true;
                System.out.println("P2 ha ganado"); 
            } else if(posP2==3 && punto.contains("P2")){
                ganador = true;
                System.out.println("P2 ha ganado");
            } else{
               
            }
        }   
    }
}
 public static void main(String[] args) {
    System.out.println("\nJuego de Tenis");
        Tenis tn = new Tenis();
        tn.juego();
 }
//the end
