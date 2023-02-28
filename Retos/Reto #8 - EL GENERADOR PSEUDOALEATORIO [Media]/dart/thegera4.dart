void main() {
  int randomNum = 0;
  for( int i = 0; i < 100; i++ ) {
    randomNum = int.parse(DateTime.now().millisecond.toString().substring(1, 3));
    if (randomNum < 100) { break; }
  }
  print (randomNum);
}