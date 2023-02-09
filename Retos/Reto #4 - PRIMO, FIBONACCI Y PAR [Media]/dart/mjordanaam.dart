/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

bool isPrime(number){
  if(number > 1){
    for(int i = 2; i < number; i++){
      if (number % i == 0){
        return false;
      }
    }
    return true;
  }
  else {
    return false;
  }
}

int fibonacci(number){
  if (number == 0){
    return 0;
  }
	else if (number == 1){
    return 1;
  } 
  else{
    return fibonacci(number-1) + fibonacci(number-2);
  }
}

bool isFibonacci(number){
  List<int> sequence = [fibonacci(0)];
  int counter = 0;
  
  while(sequence[counter] < number){
    counter++;
    sequence.add(fibonacci(counter));
  }
  
  if(sequence[counter] == number){
    return true;
  }
  
  return false;
}

bool isEven(number){
  if(number % 2 == 0){
    return true;
  }
  return false;
}


String checkNumber(number){
  late String text;
  if(number > -1){
    text = "$number is ";

    if(!isPrime(number)){
      text += "not ";
    }
    
    text += "prime, ";

    if(!isFibonacci(number)){
      text += "is not ";
    }
    text += "fibonacci and is ";

    if(isEven(number)){
      text += "even";
    }
    else{
      text += "odd";
    } 
  }
  else{
    text = "Negative number";
  }
	return text;	
}



void main() {
  print(checkNumber(2));
  print(checkNumber(7));
  print(checkNumber(8));
  print(checkNumber(16));
  print(checkNumber(17));
  print(checkNumber(0));
  print(checkNumber(89));
  print(checkNumber(97));
  print(checkNumber(100));
  print(checkNumber(1));
  print(checkNumber(-1));
}
