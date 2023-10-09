#include <iostream>


int main(){

    for(short i=0;i<=100;i++){

        if(i % 3  == 0 && i % 5 == 0) std::cout << "FizzBuzz" << std::endl;
        else if(i % 3 == 0) std::cout << "Fizz" << std::endl;
        else if(i % 5 == 0) std::cout << "Buzz" << std::endl;
        else std::cout << i << std::endl;
    }
    return 0;
}
