void main() {
  fizzBuzz();  
}

void fizzBuzz() {
  for ( int index=1; index<=100; index++ ) {
    String output = ( index % 3 ==0 ? "fizz" : "" ) + ( index % 5 ==0 ? "buzz" : "");
    print( output.isEmpty ? index : output );
  }
}