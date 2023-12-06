
import java.util.Scanner;

/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 * Hecho por Albano Díez de Paulino el 15/02/2023
 */
public class reto6 {

    public static void main(String[] args) {
         //DECLARACIÓN DE VARIABLES Y OBJETOS
        Scanner lecturaString = new Scanner(System.in);
        
        String palabra="";
        
        int numero=0;
        int numeropalabra=0;
        
        boolean condicion=false;
        
        //INICIO DEL JUEGO
        System.out.println("JUEGO DE PIEDRA/PAPEL/TIJERA/LAGARTO/SPOOK");
        do {
            System.out.println("Elige que quieres sacar");
        
            System.out.println("PIEDRA/PAPEL/TIJERA/LAGARTO/SPOOK");
        
            
            //DEFINIR JUGADA DEL ORDENADOR
            numero=(int)(Math.random()*5+1);
            
            //COMPROBAR LO QUE EL USUARIO A INTRODUCIDO
            do {
                palabra=lecturaString.nextLine();
                palabra=palabra.toUpperCase();
                switch (palabra) {
                   case "PIEDRA":
                       Roca();
                       condicion=false;
                       numeropalabra=1;
                       break;
                   case "PAPEL":
                       Papel();
                       condicion=false;
                       numeropalabra=2;
                       break;
                   case "TIJERA":
                       Tijeras();
                       condicion=false;
                       numeropalabra=3;
                       break;
                   case "LAGARTO":
                       Lagarto();
                       condicion=false;
                       numeropalabra=4;
                       break;
                   case "SPOOK":
                       Spock();
                       condicion=false;
                       numeropalabra=5;
                       break;
                   default:
                       System.out.println("Opcion no valida,vuelve a introducir");
                       System.out.println("Opciones");
                       System.out.println("PIEDRA/PAPEL/TIJERA/LAGARTO/SPOOK");
                       condicion=true;
               } 
            } while (condicion);
            
            //COMPROBAR JUGADA DEL ORDENADOR
            switch (numero) {
                    case 1:
                       System.out.println("SACO PIEDRA");
                       Roca();
                       break;
                   case 2:
                       System.out.println("SACO PAPEL");
                       Papel();
                       break;
                   case 3:
                       System.out.println("SACO TIJERAS");
                       Tijeras();
                       break;
                   case 4:
                       System.out.println("SACO LAGARTO");
                       Lagarto();
                       break;
                   case 5:
                       System.out.println("SACO SPOOK");
                       Spock();
                       break;
            }
            //METODO PARA COMPROBAR QUIEN HA GANADO PERSONA Y MAQUINA
            Marcador(numeropalabra, numero);
            
            
        } while (Final());
       
    }
     //DEFINIR ATRIBUTOS PRIVADOS A USAR
    private static int marcador1=0,marcador2=0;
    
    //METODOS PARA MOSTRAR LAS MANOS
    public static void Roca(){
         System.out.println("'''\n"
                + "    _______\n"
                + "---'   ____)\n"
                + "          _)\n"
                + "       ____)\n"
                + "      _____)\n"
                + "---._______)\n"
                + "");
        
    }
    public static void Tijeras(){
         System.out.println("'''\n"
                + "    _______\n"
                + "---'   ____)____\n"
                + "          ______)\n"
                + "       __________)\n"
                + "      (____)\n"
                + "---.__(___)\n"
                + "");
        
    }
    public static void Papel(){
        System.out.println("\n"
                + "    _______\n"
                + "---'   ____)____\n"
                + "          ______)\n"
                + "       __________)\n"
                + "      _________)\n"
                + "---._________)\n"
                + "");
        
    }
    public static void Lagarto(){
        System.out.println("\n"
               + "    _____________\n"
               + "---'   __________)\n"
               + "       __)\n"
               + "       __)\n"
               + "       __)___\n"
               + "---._________)\n"
               + "");
    
    }
    public static void Spock(){
           System.out.println("\n"
                + "    _______\n"
                + "---'   ____)____\n"
                + "          ______)\n"
                + "       __________)\n"
                + "      |_______\n"
                + "      ________)\n"
                + "---._________)\n"
                + "");
        
    }
    //METODO PARA SABER QUIEN A GANADO
    public static void Marcador(int x,int y){
        if (x==1&&(y==4||y==3)) {
            marcador1++;
            System.out.println("ME HAS GANADO");
        }else if(x==2&&(y==1||y==5)){
            System.out.println("ME HAS GANADO");
            marcador1++;
        }else if(x==3&&(y==2||y==4)){
            System.out.println("ME HAS GANADO");
            marcador1++;
        }else if(x==4&&(y==5||y==2)){
            System.out.println("ME HAS GANADO");
            marcador1++;
        }else if(x==5&&(y==3||y==1)){
            System.out.println("ME HAS GANADO");
            marcador1++;
        }else if(x==y){
            System.out.println("EMPATE");
        }else{
            System.out.println("TE HE GANADO");
            marcador2++;
        }
        System.out.println("VAMOS "+marcador1+" A "+marcador2);  
    }
    //METODO PARA DEFINIR EL GANADOR
    public static boolean Final(){
        if(marcador1>=3||marcador2>=3){
            return false;
        }else{
            return true;
        }
    }
    }



