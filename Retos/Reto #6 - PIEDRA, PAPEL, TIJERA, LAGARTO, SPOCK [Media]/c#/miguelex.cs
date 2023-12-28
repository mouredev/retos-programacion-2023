using System;
using System.Collections.Generic;

enum Jugada
{
    PIEDRA,
    PAPEL,
    TIJERAS,
    LAGARTO,
    SPOCK
}

class miguelex
{
    static string PiedraPapelTijerasLagartoSpock(List<Tuple<Jugada, Jugada>> juegos)
    {
        int p1Points = 0;
        int p2Points = 0;
        Dictionary<Jugada, List<Jugada>> ganador = new Dictionary<Jugada, List<Jugada>>()
        {
            { Jugada.PIEDRA, new List<Jugada>() { Jugada.TIJERAS, Jugada.LAGARTO } },
            { Jugada.PAPEL, new List<Jugada>() { Jugada.PIEDRA, Jugada.SPOCK } },
            { Jugada.TIJERAS, new List<Jugada>() { Jugada.PAPEL, Jugada.LAGARTO } },
            { Jugada.LAGARTO, new List<Jugada>() { Jugada.PAPEL, Jugada.SPOCK } },
            { Jugada.SPOCK, new List<Jugada>() { Jugada.TIJERAS, Jugada.PIEDRA } }
        };

        foreach (var juego in juegos)
        {
            Jugada jugador1 = juego.Item1;
            Jugada jugador2 = juego.Item2;
            if (jugador1 == jugador2)
            {
                p1Points++;
                p2Points++;
            }
            else if (ganador[jugador2].Contains(jugador1))
            {
                p1Points++;
            }
            else
            {
                p2Points++;
            }
        }

        if (p1Points == p2Points)
        {
            return $"Empate a {p1Points} puntos";
        }
        else if (p1Points > p2Points)
        {
            return $"Gana el jugador 1 por {p1Points} a {p2Points} puntos";
        }
        else
        {
            return $"Gana el jugador 2 por {p2Points} a {p1Points} puntos";
        }
    }

    static void Main(string[] args)
    {
        Console.WriteLine(PiedraPapelTijerasLagartoSpock(new List<Tuple<Jugada, Jugada>>()
        {
            Tuple.Create(Jugada.PIEDRA, Jugada.TIJERAS),
            Tuple.Create(Jugada.PIEDRA, Jugada.PAPEL),
            Tuple.Create(Jugada.LAGARTO, Jugada.SPOCK)
        }));

        Console.WriteLine(PiedraPapelTijerasLagartoSpock(new List<Tuple<Jugada, Jugada>>()
        {
            Tuple.Create(Jugada.TIJERAS, Jugada.TIJERAS),
            Tuple.Create(Jugada.PIEDRA, Jugada.PAPEL),
            Tuple.Create(Jugada.LAGARTO, Jugada.SPOCK),
            Tuple.Create(Jugada.PIEDRA, Jugada.PAPEL),
            Tuple.Create(Jugada.LAGARTO, Jugada.SPOCK),
            Tuple.Create(Jugada.PIEDRA, Jugada.PAPEL),
            Tuple.Create(Jugada.SPOCK, Jugada.PAPEL),
            Tuple.Create(Jugada.LAGARTO, Jugada.LAGARTO),
            Tuple.Create(Jugada.SPOCK, Jugada.LAGARTO)
        }));

    }
}