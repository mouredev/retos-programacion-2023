#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    // Solución al ejercicio #0
    for (int i = 0; i < 101; i++) {
        if (i %3 == 0 && i %5 == 0) {
            cout << "fizzbuzz\n" << endl;
        }

        else if (i %3 == 0) {
            cout << "fizz\n" << endl;
        }

        else if(i %5 == 0) {
            cout << "buzz\n" << endl;
        }

        else {
            cout << i << endl;
        }        
    }
    
    return 0;
}
