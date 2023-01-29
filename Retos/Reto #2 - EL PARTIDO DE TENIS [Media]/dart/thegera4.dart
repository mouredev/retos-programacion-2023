void main() {
  var points = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'];
  print(playTennis(points));
}

String playTennis(List<String> points) {
  var score = {'P1': 0, 'P2': 0};
  var secuence = ['Love', '15', '30', '40', 'Ventaja'];
  var output = '';
  
  for (var point in points) {
    if (score[point] == secuence.length - 1) {
      String winner = score['P1']! > score['P2']! ? 'P1' : 'P2';
      output += 'Ha ganado el $winner';
      break;
    } else {
      score[point] = score[point]! + 1;
    }
    if (secuence[score['P1']!] == '40' && secuence[score['P2']!] == '40') {
      output += 'Deuce\n';
    } else {
      if(secuence[score['P1']!] == 'Ventaja'){
        output += 'Ventaja P1\n';
      } else if(secuence[score['P2']!] == 'Ventaja'){
        output += 'Ventaja P2\n';
      }else{
        output += '${secuence[score['P1']!]}\t-\t${secuence[score['P2']!]}\n';
      }
    }
  }
  return output;
}
