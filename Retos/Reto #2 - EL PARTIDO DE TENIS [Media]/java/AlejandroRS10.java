package Reto_2;

import javax.swing.*;
import java.util.HashMap;
public class AlejandroRS10 {
    public static void main(String[] args) {
        // TODO Auto-generated method stub

        //Creamos el diccionario de puntos
        HashMap <Integer,String> diccionario = new HashMap<>();
        diccionario.put(0,"Love");diccionario.put(1,"15");diccionario.put(2,"30");
        diccionario.put(3,"40");

        //Creamos los contadores de cada jugador.
        Integer player1=0;
        Integer player2=0;
        String p1="Nadal";
        String p2="Alcaraz";

        //------------------ SISTEMA CONTADOR PUNTOS -------------------

        int v=0;//Variable que marca si un jugador ha conseguido la victoria

        while (v==0){

            //A quién atribuimos el punto
            String punto=JOptionPane.showInputDialog("Punto para Nadal (1) o Alcaraz (2):");
            if (punto.equals("1")) {
                player1++;
            } else{
                player2++;
            }
            //Aplicamos las posibles combinatorias de victoria, ventaja y empate con condicionales
            if (player1-2>=player2 && player1>=4){
                System.out.println(p1+":VICTORIA"+"\n"+p2+":DERROTA"+"\n");
                v++;//Cumplir el while
                } else if (player1<=player2-2 && player2>=4) {
                System.out.println(p1+":DERROTA"+"\n"+p2+":VICTORIA" + "\n");
                v++;//Cumplir el while
                } else if (player1-1>=player2 && player1>=3 && player2>=3) {
                System.out.println(p1+":Ventaja"+"\n"+p2+":"+"\n");
                } else if (player1<=player2-1 && player2>=3 && player1>=3) {
                System.out.println(p1+":"+"\n"+p2+":Ventaja" + "\n");
                } else if (player1==player2 && player2>=4 && player1>=4) {
                System.out.println(p1+":Deuce"+"\n"+p2+":Deuce"+"\n");
                } else{
                System.out.println(p1+":"+diccionario.get(player1)+"\n"+p2+":"+diccionario.get(player2)+"\n");
                }
    }
        System.out.println("¡FIN DEL JUEGO!");
    }
}