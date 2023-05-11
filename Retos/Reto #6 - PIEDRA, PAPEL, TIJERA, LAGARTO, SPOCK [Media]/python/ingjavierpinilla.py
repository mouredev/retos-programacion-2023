from dataclasses import dataclass, field


@dataclass
class Game:
    score_p1: int = field(default=0, init=False)
    score_p2: int = field(default=0, init=False)
    wins_map: dict = field(default_factory=dict)

    def __post_init__(self):
        self.wins_map["🗿"] = ("✂️", "🦎")
        self.wins_map["📄"] = ("🗿", "🖖")
        self.wins_map["✂️"] = ("📄", "🦎")
        self.wins_map["🦎"] = ("📄", "🖖")
        self.wins_map["🖖"] = ("🗿", "✂️")

    def wins(self, p1: str, p2: str):
        return p2 in self.wins_map.get(p1)  # type: ignore

    def get_winner(self) -> str:
        if self.score_p1 == self.score_p2:
            return "Tie"
        return "Player1" if self.score_p1 > self.score_p2 else "Player2"

    def play(self, attempts: list):
        for attempt in attempts:
            p1, p2 = attempt
            if p1 == p2:
                continue
            if self.wins(p1, p2):
                self.score_p1 += 1
            else:
                self.score_p2 += 1
        return self.get_winner()


def main():
    intentos = [("🗿", "✂️"), ("✂️", "🗿"), ("✂️", "📄")]
    game = Game()
    print(game.play(intentos))


if __name__ == "__main__":
    main()
