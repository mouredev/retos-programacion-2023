/* Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 * - Tijera corta a papel, papel tapa a piedra, piedra aplasta a lagarto, lagarto envenena a Spock, Spock rompe a tijera, tijera decapita a lagarto, lagarto devora a papel, papel desautoriza a Spock, Spock vaporiza a piedra, y como siempre, piedra aplasta a tijera
 */
using System;
namespace piedra_papel_tijera_lagarto_spock{
    class Game
    {
        private string Username { get; set;} // para guardar el nombre del usuario
        private int roundCounter {get; set;}  // para guardar el numero de rondas que quieres jugar el usuario
        private int pointsUser {get; set;} //para guardar los puntos del usuario
        private int pointsPC {get; set;} // para guardar los puntos del pc
        private string[] Games = {"PIEDRA", "PAPEL", "TIJERA","LAGARTO", "SPOCK"};
        public void Start() // metodo que inicia el juego
            {
                Console.WriteLine("Bienvenido a PIEDRA - PAPEL - TIJERA - LAGARTO - SPOCK");
                Console.WriteLine("Ingresa tu nombre:");
                this.Username = Console.ReadLine();
                Console.WriteLine($"Tu nombre: { this.Username }");
                this.PlayController();
            }
        void PlayController() // metodo para saber cuantas rondas quiere jugar el usuario contra la máquina / Validacion de las jugadas / Fin del juego
        {
            Console.WriteLine("¿Cuántas rondas quieres jugar?");
            int option = int.Parse(Console.ReadLine());
            for (int i =1; i <= option; i++){
                this.roundCounter = i;
                this.ValidateRound(this.GetUserPlay(), this.GetUSerPC());
                this.PrintPointsPlayers(); // imprimimos los puntos que llevan los jugadores en cada ronda
            }
            this.PrintWinner(); // imprimimos el ganador del juego
        }

        void PrintPlays(int userPlay, int pcPlay)
        {
            Console.WriteLine ($"Jugada de  {this.Username}: {this.Games [userPlay - 1]}");
            Console.WriteLine ($"Jugada de  Robot: {this.Games [pcPlay - 1]}");
        }
        void PrintPointsPlayers()
        {
            Console.WriteLine("Puntuación de Robot: " + this.pointsPC);
            Console.WriteLine($"Puntuación de {this.Username}: " + this.pointsUser);
        }

        void PrintWinner()
        {
            // a ? b : (c ? d : e)
            // condicion ? true : false   operadores ternario---> simplifican el uso de if/else
            Console.WriteLine("END GAME");
            Console.WriteLine(
                this.pointsUser > this.pointsPC ? $"GANA {this.Username}" : 
                (this.pointsUser == this.pointsPC ? "EMPATE" : "GANA ROBOT")
            );
        }
        void ValidateRound(int userPlay, int pcPlay)
        {
            this.PrintPlays(userPlay,pcPlay);
            // pares de combinaciones que sale ganado el usuario   
            // 1 piedra -  3 tijera
            // 1 piedra - 4 lagarto
            // 2 papel - 1 piedra
            // 2 papel - 5 spock 
            // 3 tijera - 2 papel
            // 3 tijera - 4 lagarto
            // 4 lagarto - 5 spock
            // 4 lagarto - 2 papel
            // 5 spock - 3 tijera
            // 5 spock - 1 piedra

            if ((userPlay == 1 && pcPlay == 3) ||
            (userPlay == 1 && pcPlay == 4) ||
            (userPlay == 2 && pcPlay == 1) ||
            (userPlay == 2 && pcPlay == 5) ||
            (userPlay == 3 && pcPlay == 2) ||
            (userPlay == 3 && pcPlay == 4) ||
            (userPlay == 4 && pcPlay == 5) ||
            (userPlay == 4 && pcPlay == 2) ||
            (userPlay == 5 && pcPlay == 3) ||
            (userPlay == 5 && pcPlay == 1))
            {
                this.pointsUser++;
                Console.WriteLine($" ¡{this.Username} gana la ronda! ");
            }
            else
            {
                this.pointsPC++;
                Console.WriteLine("¡Robot gana la ronda!");
            }
            if((userPlay == pcPlay ))
            {
                Console.WriteLine("TIE");
            }
        }
        int GetUserPlay() // metodo para la jugada del usuario, en el que le mandamos elegir un numero al cual cada numero corresponde a una elección
        {
            Console.WriteLine($"RONDA Nº { this.roundCounter }");
            Console.WriteLine("Selecciona una opción: ");
            Console.WriteLine("1- PIEDRA");
            Console.WriteLine("2- PAPEL");
            Console.WriteLine("3- TIJERA");
            Console.WriteLine("4- LAGARTO");
            Console.WriteLine("5- SPOCK");
            int option = int.Parse(Console.ReadLine());
            return option;
        }
        int GetUSerPC() //metodo para la jugada del PC, como es aleatorio usamos el metodo random y le marcamos el numero mínimo y el numero máximo+1
        {
            return new Random().Next(1,6);
        }
        void Reset(){
            this.pointsPC = 0;
            this.pointsUser = 0;
        }
    }
}