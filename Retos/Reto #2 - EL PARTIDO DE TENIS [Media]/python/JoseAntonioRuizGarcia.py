POINTS = {
    0: 'Love',
    1: '15',
    2: '30',
    3: '40',
}

class GameTennis():
    def __init__(self, plays: list):
        self.__cleanSecuence__(plays)
        self.__is_deuce__ = False
        self.points = [0, 0]
    
    def __cleanSecuence__(self, plays: list):
        self.__plays__ = (
            plays.replace('[', '')
            .replace(']', '')
            .replace(' ', '')
            .split(',')
        )
    
    def __sumPoint__(self, player: str):
        if player == 'P1':
            self.points[0] += 1

        else:
            self.points[1] += 1

    def __printResultPartial__(self):
        p1 = POINTS.get(self.points[0])
        p2 = POINTS.get(self.points[1])

        print(f'{p1} - {p2}')

    def runGame(self):
        # Recorre todas las jugadas
        for p in self.__plays__:
            # Suma 1 punto al jugador correspondiente
            self.__sumPoint__(p)

            '''
                Comprueba si hay un ganador
                Siempre que ambos jugadores tengan más de 3 puntos
                Si la diferencia entre ambos es mayor que 1
            '''            
            if (any([self.points[0] > 3, self.points[1] > 3])) and abs(self.points[0] - self.points[1]) > 1:
                if self.points[0] > self.points[1]:
                    print('Ha gana el jugardor P1')
                    break

                else:
                    print('Ha gana el jugardor P2')
                    break
            
            '''
                Comprueba si entrar en modo Deuce
                Si hay empate a 3 puntos se pasa a puntación > 10 puntos
                Gana el primero que tenga más de un punto de diferencia con el otro jugador
            '''             
            if (self.points[0] == 3) and (self.points[1] == 3):
                self.points = [10, 10]
                self.__is_deuce__ = True
            
            # Imprime la puntación normal o del modo deuce
            if self.__is_deuce__:
                if self.points[0] == self.points[1]:
                    print('Deuce')
                else:
                    print(f'Ventaja {p}')
            else:
                self.__printResultPartial__()


if __name__ == '__main__':
    games = '[P1, P1, P2, P2, P1, P2, P1, P1]'
    gt = GameTennis(plays = games)
    gt.runGame()
