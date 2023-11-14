// See https://aka.ms/new-console-template for more information

using System.Diagnostics;
using System.Numerics;
using System.Runtime.CompilerServices;

class Program{
    static void Main(string[] args){
        Console.WriteLine("Empezamos el juego.");

        // Se crea el tablero
        Tablero tablero = new Tablero(4,4);
        int meta = tablero.Get_Pos(Tablero.dulce);

        // Se crea el jugador
        Jugador jugador = new Jugador(tablero.Get_Pos(Tablero.puerta));
        Console.WriteLine($"El jugador esta en la pos {jugador.pos}");

        // Empieza el juego
        do{
            tablero.Print();
            // Movimiento del jugador
            Console.WriteLine("¿Dónde quieres desplazarte? [norte|sur|este|oeste]");
            string respuestaJugador = Console.ReadLine();
            if(!jugador.ValidaRespuesta(respuestaJugador)){
                Console.WriteLine("La respuesta no está entre las opciones disponibles." + Environment.NewLine + "Pulsa para continuar.");
                Console.ReadKey();
                continue;
            }
            int newPos = -1;
            tablero.Move(respuestaJugador, jugador.pos, out newPos);
            jugador.pos = newPos;

            if(jugador.pos != meta){
                Console.Clear();
                tablero.Print();

                // Lógica casilla
                tablero.AbreCasilla(jugador.pos);
                tablero.Print();

                Console.WriteLine("Pulsa para continuar.");
                Console.ReadLine();
                Console.Clear();
            }

            
        }while(jugador.pos != meta);

        Console.WriteLine("Eu salido del jogo");
    }
}


class Jugador{

    public static string player = "🧭";

    public int pos{get;set;}

    public Jugador(int pos){
        this.pos = pos;
    }

    /// <summary>
    /// Verifica si respuesta del jugador esta entre las opciones validas
    /// </summary>
    public bool ValidaRespuesta(string respuesta){
        return Enum.IsDefined(typeof(Tablero.Movimientos), respuesta);
    }

    
}

class Casilla{
    public string Tipo{get;set;}
    public bool Activa{get;set;}

    public Casilla(string tipo, bool activa = false){
        this.Tipo = tipo;
        this.Activa = activa;
    }

    public void Print(){
        if(Activa){
            Console.Write(Jugador.player);
        }else{
            Console.Write(Tipo);
        }
    }
}

class Tablero{

    #region Preguntas

    Dictionary<string,string> preguntas = new Dictionary<string, string>() {
        {"¿El agua moja?","si"},
        {"Plata no es ¿dime que es?","platano"},
        {"Si un objeto imparable choca con un objeto inamovible que pasa", "nada"},
        {"Si tengo 3 peces y se ahoga 1 cuantos tengo","3"},
        {"Napoleon tenia un caballo blanco, de que color era el caballo de Napoleon","blanco"},
        {"Siempre paso helada y prima es la hielera","nevera"},
        {"¿Que le paso a la gallina cuando cruzo la calle?","llego al otro lado"},
        {"Sostengo muchas perlas blancas unas arriba unas abajo", "dentadura"}
    };

    #endregion Preguntas

    #region  Propiedades

    public enum Movimientos{
        norte,
        sur,
        este,
        oeste
    }

    public static string casilla = "⬜️";
    public static string puerta = "🚪";
    public static string fantasma = "👻";
    public static string dulce = "🍭";
    public static string enigma = "❓";

    int alto;
    int ancho;

    int probabilidadFantasmas = 10;

    public Casilla[] casillas{get;set;}

    #endregion Propiedades

    public Tablero(int alto, int ancho){
        this.alto = alto;
        this.ancho = ancho; 

        Init();
    }

    private void Init(){
        // Establecemos el total de casillas
        casillas = new Casilla[alto * ancho];

        // Rellenamos todo con [Casillas]
        for(int i = 0; i < casillas.Length; i++){
            casillas[i] = new Casilla(casilla);
        }

        // Insertamos la [Puerta] de entrada
        // La puerta estará obligatoriamente en un borde del tablero
        BuscaEntrada();

        // Insertamos el [Dulce] de salida
        // La salida puede estar en cualquier posicion
        BuscaSalida();
    }

    /// <summary>
    /// Busca una casilla en el brode del tablero para posicionar la salida
    /// </summary>
    private void BuscaEntrada(){
        Random random = new Random();
        int borde = random.Next(4);
        int fila = (borde < 2) ? (borde == 0 ? 0 : alto - 1) : random.Next(alto);
        int columna = (borde >= 2) ? (borde == 2 ? 0 : ancho - 1) : random.Next(ancho);
        int indice = (fila * ancho) + columna;
        casillas[indice].Tipo = puerta;
        casillas[indice].Activa = true;
    }

    private void BuscaSalida(){
        Random random = new Random();
        int casilla = random.Next(casillas.Length);
        if(casillas[casilla].Tipo == puerta){
            BuscaSalida();
            return;
        }
        casillas[casilla].Tipo = dulce;
    }

    public void Print(){
        for(int i = 0; i < casillas.Length; i++){
            casillas[i].Print();
            int col = i % ancho; // Columna
            if(col == ancho - 1){
                Console.Write(Environment.NewLine);
            }
        }
    }

    public int Get_Pos(string tipo){
        int? pos = casillas.Select((x, index) => new {E = x, Indice = index}).Where(x => x.E.Tipo == tipo).Select(x => x.Indice).First();
        if(pos != null && pos > -1){
            return (int)pos;
        }
        return -1;
    }

    public void Move(string movimiento, int playerPos, out int playerNewPos){
        Movimientos mov;
        if(!Enum.TryParse<Movimientos>(movimiento, out mov)){
            Console.WriteLine($"El movimeinto {movimiento} no está permitido.");
            playerNewPos = playerPos;
            return;
        }

        int fila = playerPos / ancho;
        int col = playerPos % ancho;

        switch(mov){
            case Movimientos.norte:
                fila = (fila > 0)? fila-1 : fila = 0;
            break;
            case Movimientos.sur:
                fila = (fila < alto)? fila+1 : fila = alto;
            break;
            case Movimientos.este:
                col = (col < ancho)? col+1 : col = ancho;
            break;
            case Movimientos.oeste:
                col = (col > 0)? col-1 : col = 0;
            break;
        }

        playerNewPos = fila * ancho + col;

        casillas[playerPos].Activa = false;
        casillas[playerNewPos].Activa = true;

        if(casillas[playerPos].Tipo == enigma){
            casillas[playerPos].Tipo = casilla;
        }
        if(casillas[playerNewPos].Tipo == casilla){
            casillas[playerNewPos].Tipo = enigma;
        }
    }

    public void AbreCasilla(int posCasilla){
        bool isFantasma = false;
        int numPreguntas = 1;
        int numRespuestas = 0;

        // Comprobamos la posibilidad de que haya un fantasma
        Random random = new Random();
        int numeroAleatorio = random.Next(1, 101);
        if(numeroAleatorio <= probabilidadFantasmas){
            isFantasma = true;
        }

        if(isFantasma){
            Console.WriteLine("¡Ha aparecido un fantasma!");
            casillas[posCasilla].Tipo = fantasma;
            numPreguntas = 2;
        }

        do{
            // Ronda Preguntas
            if(RondaPregunta()){
                numRespuestas++;
            }

        }while(numRespuestas < numPreguntas);
    }

    private bool RondaPregunta(){
        Random random = new Random();
        int numeroAleatorio = random.Next(0, preguntas.Count);
        KeyValuePair<string,string> pregunta = preguntas.ElementAt(numeroAleatorio);
        Console.WriteLine($"Preguta: {pregunta.Key}");
        Console.Write("Respuesta: ");
        string respuesta = Console.ReadLine().Trim().ToLower();

        if(respuesta != pregunta.Value){
            Console.WriteLine("Te has equivocado jeje.");
            return false;
        }

        Console.WriteLine("Correcto!!.");
        return true;
    }
}