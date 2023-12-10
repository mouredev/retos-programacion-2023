/*
* Crea un programa que calcule quien gana más partidas al piedra,
* papel, tijera, lagarto, spock.
* - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
* - La función recibe un listado que contiene pares, representando cada jugada.
* - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
*   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
* - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
* - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

    Tijeras✂️ cortan papel📄
    Papel📄 cubre piedra🗿
    Piedra🗿 aplasta lagarto🦎
    Lagarto🦎 envenena Spock🖖
    Spock🖖 destruye tijeras✂️
    Tijeras✂️ decapitan lagarto🦎
    Lagarto🦎 come papel📄
    Papel📄 desaprueba Spock🖖
    Spock🖖 vaporiza piedra🗿
    Piedra🗿 aplasta tijeras✂️
*/

using System;

class Program
{
    public static void Main(String[] args)
    {
        Console.WriteLine(Game("✂️", "📄"));
        Console.WriteLine(Game("📄", "🖖"));
        Console.WriteLine(Game("🗿", "🦎"));
        Console.WriteLine(Game("🦎", "📄"));
        Console.WriteLine(Game("🦎", "🦎"));
        Console.WriteLine(Game("Error", "📄"));
    }

    public static string Game(string player1, string player2)
    {
        if(player1 == player2) { return "Tie"; }
        if((player1 == "✂️" || player1 == "📄" || player1 == "🗿" || player1 == "🦎" || player1 == "🖖") && (player2 == "✂️" || player2 == "📄" || player2 == "🗿" || player2 == "🦎" || player2 == "🖖")) {  
            // Tijeras ✂️
            if (player1.Equals("✂️") && player2.Equals("📄") || player2.Equals("🦎")){ return ("Player 1"); }
            if (player2.Equals("✂️") && player1.Equals("📄") || player1.Equals("🦎")) { return ("Player 2"); }
            // Papel 📄
            if (player1.Equals("📄") && player2.Equals("🗿") || player2.Equals("🖖")) { return ("Player 1"); }
            if (player2.Equals("📄") && player1.Equals("🗿") || player1.Equals("🖖")) { return ("Player 2"); }
            // Piedra 🗿
            if (player1.Equals("🗿") && player2.Equals("🦎") || player2.Equals("✂️")) { return ("Player 1"); }
            if (player2.Equals("🗿") && player1.Equals("🦎") || player1.Equals("✂️")) { return ("Player 2"); }
            // Lagarto 🦎
            if (player1.Equals("🦎") && player2.Equals("🖖") || player2.Equals("📄")) { return ("Player 1"); }
            if (player2.Equals("🦎") && player1.Equals("🖖") || player1.Equals("📄")) { return ("Player 2"); }
            // Spock 🖖
            if (player1.Equals("🖖") && player2.Equals("✂️") || player2.Equals("🗿")) { return ("Player 1"); }
            if (player2.Equals("🖖") && player1.Equals("✂️") || player1.Equals("🗿")) { return ("Player 2"); }
        }
        return "Introduce opciones válidas.";
    }
}