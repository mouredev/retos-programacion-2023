class Tennis():
    def __init__(self):
        self.points = {
            0 : 'Love',
            1 : '15',
            2 : '30',
            3 : '40'
        }
        self.P1 = 0
        self.P2 = 0
        self.contador = 0

    def juego(self, partido : list):

        for player in partido:

            if len(partido) > 7:
                print('Partido invalido'); break

            else:
                self.P1 += 1 if player == 'P1' else 0 
                self.P2 += 1 if player == 'P2' else 0
                self.contador += 1
                
                try:
                    if self.P1 and self.P2 in self.points:
                        print(self.points[self.P1],  '-', self.points[self.P2])
                        
                    if self.contador == len(partido):
                        if self.P1 == self.P2:
                            print('Empate'); break
                        else:
                            print('Ventaja del P1\nHa ganado el jugador P1' if self.P1 > self.P2 else 
                                'Ventaja del P2\nHa ganado el jugador P2' ); break
                            
                except: 
                        print('Partida Invalida'); break
                
    def reset_game(self):
        self.P1 = 0
        self.P2 = 0
        self.contador = 0
                

p = Tennis() 
p.juego(["P1", "P1", "P1", "P2", "P2", "P1", 'P2'])
p.reset_game()
print('---------------------------------------------------')
p.juego(["P1", "P1", "P1", "P2", "P2", 'P2'])
p.reset_game()
print('---------------------------------------------------')
p.juego(["P1", "P1", "P1", "P2", "P2", "P1",])
p.reset_game()
print('---------------------------------------------------')
p.juego(["P1", "P1", "P2", "P2", 'P2'])          
