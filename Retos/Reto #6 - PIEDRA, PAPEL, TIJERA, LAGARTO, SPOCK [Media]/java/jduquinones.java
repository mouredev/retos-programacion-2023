/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */

import java.io.IOException;
import java.text.DecimalFormat;
import java.util.ArrayList;

public class jduquinones {

    public static void main(String[] args) throws IOException {
        Juego();
    }

   public static void Juego(){
       String tijera = "tijera";
       String piedra = "piedra";
       String papel = "papel";
       String spock = "spock";
       String lagarto = "lagarto";

       Integer plarer1 = 0;
       Integer plarer2 = 0;
       Integer tie = 0;

       ArrayList<String> iterar = new ArrayList<>();
       iterar.add(tijera);
       iterar.add(piedra);
       iterar.add(papel);
       iterar.add(spock);
       iterar.add(lagarto);

       DecimalFormat decimalFormat = new DecimalFormat("#");
       String  seleccionPlayer1 = iterar.get(Integer.parseInt(decimalFormat.format(Math.random() * 4)));
       String seleccionPlayer2 = iterar.get(Integer.parseInt(decimalFormat.format(Math.random() * 4)));

        //tijeras -> lagarto
        if (seleccionPlayer1.equals("tijeras") && seleccionPlayer2.equals("lagarto")){
            plarer1 ++;
        } else if (seleccionPlayer2.equals("tijeras") && seleccionPlayer1.equals("lagarto")) {
            plarer2 ++;
        }

       //tijeras -> papel
       if (seleccionPlayer1.equals("tijeras") && seleccionPlayer2.equals("papel")){
           plarer1 ++;
       }else if (seleccionPlayer2.equals("tijeras") && seleccionPlayer1.equals("papel")) {
           plarer2 ++;
       }

       //piedra -> lagarto
       if (seleccionPlayer1.equals("piedra") && seleccionPlayer2.equals("lagarto")){
           plarer1 ++;
       }else if (seleccionPlayer2.equals("piedra") && seleccionPlayer1.equals("lagarto")) {
           plarer2 ++;
       }

       //piedra -> tijeras
       if (seleccionPlayer1.equals("piedra") && seleccionPlayer2.equals("tijeras")){
           plarer1 ++;
       }else if (seleccionPlayer2.equals("piedra") && seleccionPlayer1.equals("tijeras")) {
           plarer2 ++;
       }

       //papel -> spock
       if (seleccionPlayer1.equals("papel") && seleccionPlayer2.equals("spock")){
           plarer1 ++;
       }else if (seleccionPlayer2.equals("papel") && seleccionPlayer1.equals("spock")) {
           plarer2 ++;
       }

       //papel -> piedra
       if (seleccionPlayer1.equals("papel") && seleccionPlayer2.equals("piedra")){
           plarer1 ++;
       }else if (seleccionPlayer2.equals("papel") && seleccionPlayer1.equals("piedra")) {
           plarer2 ++;
       }

       //spock -> tijeras
       if (seleccionPlayer1.equals("spock") && seleccionPlayer2.equals("tijeras")){
           plarer1 ++;
       }else if (seleccionPlayer2.equals("spock") && seleccionPlayer1.equals("tijeras")) {
           plarer2 ++;
       }

       //spock -> piedra
       if (seleccionPlayer1.equals("spock") && seleccionPlayer2.equals("piedra")){
           plarer1 ++;
       }else if (seleccionPlayer2.equals("spock") && seleccionPlayer1.equals("piedra")) {
           plarer2 ++;
       }

       //lagarto -> papel
       if (seleccionPlayer1.equals("lagarto") && seleccionPlayer2.equals("papel")){
           plarer1 ++;
       }else if (seleccionPlayer2.equals("lagarto") && seleccionPlayer1.equals("papel")) {
           plarer2 ++;
       }

       //lagarto -> spock
       if (seleccionPlayer1.equals("lagarto") && seleccionPlayer2.equals("spock")){
           plarer1 ++;
       }else if (seleccionPlayer2.equals("lagarto") && seleccionPlayer1.equals("spock")) {
           plarer2++;
       }

       if (seleccionPlayer1.equals("tijera") && seleccionPlayer2.equals("tijera")){
           tie ++;
       }else if (seleccionPlayer2.equals("piedra") && seleccionPlayer1.equals("piedra")) {
           tie++;
       }else if (seleccionPlayer2.equals("papel") && seleccionPlayer1.equals("papel")) {
           tie++;
       }else if (seleccionPlayer2.equals("spock") && seleccionPlayer1.equals("spock")) {
           tie++;
       }else if (seleccionPlayer1.equals("lagarto") && seleccionPlayer2.equals("lagarto")){
           tie ++;
       }

       System.out.println("score player 1:  " + plarer1);
       System.out.println("score player 2:  " + plarer2);
       System.out.println("score tie:  " + tie);

       System.out.println("select player 1 out if: " + seleccionPlayer1);
       System.out.println("select player 2: out if: " + seleccionPlayer2);
   }
}
