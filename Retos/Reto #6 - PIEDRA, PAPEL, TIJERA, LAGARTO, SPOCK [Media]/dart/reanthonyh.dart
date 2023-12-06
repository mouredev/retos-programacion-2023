void main() {
  final resultOfTheGame = play([
    Pair(Element.piedra, Element.papel),
    Pair(Element.tijera, Element.piedra),
    Pair(Element.piedra, Element.lagarto),
    Pair(Element.papel, Element.spock),
    Pair(Element.tijera, Element.lagarto),
    Pair(Element.spock, Element.lagarto),
    Pair(Element.tijera, Element.spock),
  ]);

  print("The winner is : ${resultOfTheGame.niceName}");
}

enum Result {
  one('Player 1'),
  two('Player 2'),
  draw('Tie');

  final String niceName;
  const Result(this.niceName);
}

enum Element { piedra, papel, tijera, lagarto, spock }

class Pair {
  const Pair(this.one, this.two);

  final Element one, two;

  Result get winner {
    switch (one) {
      case Element.piedra:
        if (two == Element.lagarto) return Result.one;
        if (two == Element.tijera) return Result.one;
        if (two == Element.papel) return Result.two;
        if (two == Element.spock) return Result.two;
        break;
      case Element.papel:
        if (two == Element.piedra) return Result.one;
        if (two == Element.spock) return Result.one;
        if (two == Element.tijera) return Result.two;
        if (two == Element.lagarto) return Result.two;
        break;
      case Element.tijera:
        if (two == Element.papel) return Result.one;
        if (two == Element.lagarto) return Result.one;
        if (two == Element.spock) return Result.two;
        if (two == Element.piedra) return Result.two;
        break;
      case Element.lagarto:
        if (two == Element.spock) return Result.one;
        if (two == Element.papel) return Result.one;
        if (two == Element.piedra) return Result.two;
        if (two == Element.tijera) return Result.two;
        break;
      case Element.spock:
        if (two == Element.tijera) return Result.one;
        if (two == Element.piedra) return Result.one;
        if (two == Element.lagarto) return Result.two;
        if (two == Element.papel) return Result.two;
        break;
    }
    return Result.draw;
  }
}

Result play(List<Pair> pairs) {
  int countOne = 0, countTwo = 0;

  pairs.forEach((pair) {
    final winnner = pair.winner;
    if (winnner == Result.one) countOne++;
    if (winnner == Result.two) countTwo++;
  });

  if (countOne == countTwo) return Result.draw;

  if (countOne > countTwo)
    return Result.one;
  else
    return Result.two;
}
