//
//  main.cpp
//  FizzBuzz
//
//  Created by Juan Carlos Bonilla on 12/15/23.
//

#include <iostream>

int main() {

    for(short i = 1; i <= 100; i++){
        if (i%3 == 0 && i%5 == 0) std::cout << "fizzbuzz" << std::endl;
        else if(i%3 == 0) std::cout << "fizz" << std::endl;
        else if(i%5 == 0) std::cout << "buzz" << std::endl;
        else std::cout << i << std::endl;
    }
    
    return 0;
}
