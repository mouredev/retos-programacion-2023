/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool is_prime(int number){
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

int fibonacci(int number){
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

bool is_fibonacci(int number){
  vector<int> sequence;
  sequence.push_back(fibonacci(0));
  int counter = 0;
  
  while(sequence[counter] < number){
    counter++;
    sequence.push_back(fibonacci(counter));
  }
  
  if(sequence[counter] == number){
    return true;
  }
  
  return false;
}

bool is_even(int number){
  if(number % 2 == 0){
    return true;
  }
  return false;
}

void check_number(int number){
    if(number > -1){
        cout << number << " is ";
        //text = string(number);

        if(is_prime(number) == false){
            cout << "not ";
        }

        cout << "prime, ";

        if(is_fibonacci(number) == false){
            cout << "is not ";
        }
        cout << "fibonacci and is ";

        if(is_even(number)){
            cout << "even";
        }
        else{
            cout << "odd";
        }
    }
    else{
        cout << "Negative number";
    }
    cout << endl;
}

int main(){
    check_number(2);
    check_number(7);
    check_number(8);
    check_number(16);
    check_number(17);
    check_number(0);
    check_number(89);
    check_number(97);
    check_number(100);
    check_number(1);
    check_number(-1);
    return 0;
}
