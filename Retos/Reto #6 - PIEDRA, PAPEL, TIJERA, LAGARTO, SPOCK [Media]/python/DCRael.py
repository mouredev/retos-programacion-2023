class Game():
    def __init__(self):
        self.jugadas_ganadoras = {
        "🗿" : ("✂️", "🦎"),
        "📄" : ("🗿", "🖖"),
        "✂️" : ("📄", "🦎"),
        "🦎" : ("📄", "🖖"),
        "🖖" : ("🗿", "✂️")
        }
        self.win1 = 0
        self.win2 = 0

    def historial_partida(self, partida : list) -> str:

        resultados = []
        for i, intento in enumerate(partida):
            j1, j2 = intento

            if j2 in self.jugadas_ganadoras[j1]:
                self.win1 += 1
                resultados.append(f"Partida {i+1}: Player 1 {j1}  vs{j2}")
            elif j1 == j2:
                resultados.append(f"Partida {i+1}: Empate {j1}  vs{j2}")
            else:
                self.win2 += 1
                resultados.append(f"Partida {i+1}: Player 2 {j1}  vs{j2}")

        resultados.append(f'Resultado final: {self.ganador()}')
        return resultados
        
    def ganador(self) -> str:
        return "Player 1" if self.win1 > self.win2 else "player 2" if self.win2 > self.win1 else 'Tie'
    

game = Game()
intentos = [("✂️", "✂️"), ("✂️", "🗿"), ("✂️", "📄")]
print("Historial de partidas:")
resultados = game.historial_partida(intentos)
for resultado in resultados:
    print(f"{resultado}")