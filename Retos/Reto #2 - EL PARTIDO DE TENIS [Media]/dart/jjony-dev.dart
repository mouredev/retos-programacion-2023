void main() {
  Match match = Match();

  match.addAllPoints(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']);
  print(match.processAll());
}

class Match {
  int _currentPoint = 0;
  List<String> _points = [];
  Map<String, int> _players = {'P1': 0, 'P2': 0};
  List<String> _secuence = ['Love', '15', '30', '40', 'Vent.'];
  bool _endedFlag = false;

  addPoint(String player) {
    if (!_players.containsKey(player.toUpperCase())) return;
    _points.add(player.toUpperCase());
  }

  removePoint(int index) {
    if (index >= _points.length && index < 0) return;
    _points.removeAt(index);
  }

  addAllPoints(List<String> points) {
    for (var point in points) {
      addPoint(point);
    }
  }

  clearPoints() {
    _points.clear();
  }

  bool hasWinner(int p1Points, int p2Points) {
    return (p1Points >= _secuence.length || p2Points >= _secuence.length) ||
        (p1Points == _secuence.length - 1 && (p1Points - p2Points).abs() > 1) ||
        (p2Points == _secuence.length - 1 && (p1Points - p2Points).abs() > 1);
  }

  String showScore() {
    late String output;
    int p1Points = _players['P1']!;
    int p2Points = _players['P2']!;
    if (hasWinner(p1Points, p2Points)) {
      String winner = p1Points > p2Points ? 'P1' : 'P2';
      output = 'El partido lo gano $winner';
    } else if (_secuence[p1Points] == '40' && _secuence[p2Points] == '40') {
      output = '\tDeuce\t';
    } else {
      output = '${_secuence[p1Points]}\t-\t${_secuence[p2Points]}';
    }
    return output;
  }

  String processOnce() {
    String currentScore;
    if (_currentPoint < _points.length && !_endedFlag) {
      switch (_points[_currentPoint]) {
        case 'P1':
          if (_players['P2'] == _secuence.length - 1) {
            // Si P2 está en Ventaja
            _players['P2'] = _players['P2']! - 1;
          } else {
            _players['P1'] = _players['P1']! + 1;
          }
          break;
        case 'P2':
          if (_players['P1'] == _secuence.length - 1) {
            // Si P1 está en Ventaja
            _players['P1'] = _players['P1']! - 1;
          } else {
            _players['P2'] = _players['P2']! + 1;
          }
          break;
      }
      _currentPoint++;
      currentScore = showScore();
      _endedFlag = hasWinner(_players['P1']!, _players['P2']!);
    } else {
      currentScore = 'el pardido ya terminó';
    }
    return currentScore;
  }

  String processAll({bool fromStart = false}) {
    String finalScore = '';
    if (fromStart) {
      _currentPoint = 0;
      _endedFlag = false;
      _players = _players.map((key, value) => MapEntry(key, 0));
    }

    while (_currentPoint < _points.length && !_endedFlag) {
      finalScore += processOnce() + '\n';
    }

    return finalScore;
  }
}
