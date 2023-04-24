
class Games:

    __who_wins_rules = {
        "🗿": ("✂️", "🦎"),
        "📄": ("🗿", "🖖"),
        "✂️":  ("📄", "🦎"),
        "🦎": ("🖖", "📄"),
        "🖖": ("🗿", "✂️")
    }
    __player_1: int
    __player_2: int 

    def piedra_papel_tijera_lagarto_spock(self, games: list[tuple]) -> None:

        self.__player_1 = 0
        self.__player_2 = 0
        for game in games:
            if self.verify_inputs(game):
                print(f"The game {game} contains incorrect entries, it will not be taken into account")
                continue
            if game[0] != game[1]: 
                if game[0] in self.__who_wins_rules[game[1]]:
                    self.__player_2 += 1
                elif game[1] in self.__who_wins_rules[game[0]]:
                    self.__player_1 += 1

        print(f"Result: {self.evaluate_who_wins(p1=self.__player_1, p2=self.__player_2)}")


    def evaluate_who_wins(self, p1:int, p2: int)->str:
        if p1 == p2:
            return "Tie"
        else:
            return "Player 1" if p1 > p2 else "Player 2"

    def verify_inputs(self, inputs:tuple)->bool:
        correct_vals = list(self.__who_wins_rules.keys())
        for inp in inputs:
            if inp not in correct_vals:
                return True
        return False


if __name__ == "__main__":

    game = Games()
    game.piedra_papel_tijera_lagarto_spock([("🗿", "✂️"), ("✂️", "🗿"), ("🖖", "✂️")])
    print("-"*10)
    game.piedra_papel_tijera_lagarto_spock([("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")])
    print("-"*10)
    game.piedra_papel_tijera_lagarto_spock([("✂️","✂️"), ("🦎","🦎")])
    print("-"*10)
    game.piedra_papel_tijera_lagarto_spock([("🗿", "✂️"), ("✂️", "🗿"), ("😀", "✂️")])