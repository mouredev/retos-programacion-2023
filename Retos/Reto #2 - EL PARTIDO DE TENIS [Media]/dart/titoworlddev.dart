List<String> sequence = ['P1', 'P1', 'P2', 'P3', 'P2', 'P1', 'P2', 'P1', 'P1'];

void solution(List<String> seq) {
  int p1 = 0;
  int p2 = 0;

  for (String player in seq) {
    if (player != 'P1' && player != 'P2') {
      print('El jugador $player no es valido, debe ser P1 o P2');
    } else {
      if (p1 < 30 || p2 < 30) {
        player == 'P1' ? p1 += 15 : p2 += 15;
      } else {
        player == 'P1' ? p1 += 10 : p2 += 10;
      }

      if (p1 == 0 || p2 == 0) {
        print(p1 == 0 ? 'Love - $p2' : '$p1 - Love');
      } else if (p1 >= 40 && p1 == p2) {
        print('Deuce');
      } else if (p1 > 40 && p1 != p2 || p2 > 40 && p1 != p2) {
        p1 - 10 > p2
            ? print('Ha ganado el P1')
            : p2 - 10 > p1
                ? print('Ha ganado el P2')
                : print(p1 > p2 ? 'Ventaja P1' : 'Ventaja P2');
      } else {
        print('$p1 - $p2');
      }
    }
  }
}

void main() {
  solution(sequence);
}
