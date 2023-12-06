"""
Reto 6: Piedra, Papel, Tijeras, Lagarto, Spock

Crea un programa que calcule quien gana más partidas al piedra,
papel, tijera, lagarto, spock.
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La función recibe un listado que contiene pares, representando cada jugada.
- El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
  "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
- Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")].
  Resultado: "Player 2".
- Debes buscar información sobre cómo se juega con estas 5 posibilidades.
"""

class Game:
    """
    Clase que representa al juego de Piedra, Papel, Tijeras, Lagarto, Spock
    visto en la serie The Big Bang Theory.
    """
    def __init__(self):
        self.__score_1 = 0
        self.__score_2 = 0
        self.__options_set = {
            '🗿',
            '📄',
            '✂️',
            '🦎',
            '🖖'
        }
        self.__winner_combinations = {
            '🗿': ('✂️', '🦎'),
            '📄': ('🗿', '🖖'),
            '✂️': ('📄', '🦎'),
            '🦎': ('📄', '🖖'),
            '🖖': ('🗿', '✂️')
        }
    
    def round_winner(self, players_choice):
        """Determina el ganador de una partida del juego.""" 
        
        try:
            self.__check_input(players_choice)
        except ValueError as e:
            print(e)
        else:
            p1_choice, p2_choice = players_choice
            
            if p2_choice in self.__winner_combinations[p1_choice]:
                self.__score_1 += 1
            else:
                self.__score_2 += 1
        
        # Se imprime el marcador actual
        print(f'P1: {self.__score_1} -- P2: {self.__score_2}\n')
        
    def overall_winner(self, rounds_sequence):
        """Determina el ganador de una secuencia de jugadas."""
        # Reinicio del marcador
        self.reset_scoreboard()
        
        # Asignacion de puntuaciones
        for n, round in enumerate(rounds_sequence, start=1):
            print(f'Round {n}: ')
            self.round_winner(round)
        
        # Mensaje de jugador ganador o empate
        if self.__score_1 == self.__score_2:
            print('TIE\n')
        elif self.__score_1 > self.__score_2:
            print('PLAYER 1 WINS!\n')
        else:
            print('PLAYER 2 WINS!\n')

    def reset_scoreboard(self):
        """Reinicia el marcador del juego."""
        self.__score_1 = 0
        self.__score_2 = 0
    
    def __check_input(self, players_choice):
        """
        Verifica si las opciones escogidas por los jugadores son válidas.
        
        Condiciones de jugada válida:
        - Solo deben haber 2 opciones (es un juego de dos jugadores.)
        - Las opciones escogidas deben ser alguna de las siguientes:
        🗿, 📄, ✂️, 🦎, 🖖. 
        """
        
        if len(players_choice) != 2:
            raise ValueError('Only 2 players are allowed!')
        
        if not set(players_choice).issubset(self.__options_set):
            raise ValueError('The only avalaible options are: 🗿, 📄, ✂️, 🦎, 🖖.')

if __name__ == '__main__':
    game = Game()
    game.overall_winner([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")])
