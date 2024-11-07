#include <iostream>
using namespace std;

void fizzbuzz() {
    for (int x = 1; x <= 100; ++x) {
        if (x % 15 == 0) {
            cout << "fizzbuzz" << endl;
        } else if (x % 3 == 0) {
            cout << "fizz" << endl;
        } else if (x % 5 == 0) {
            cout << "buzz" << endl;
        } else {
            cout << x << endl;
        }
    }
}

int main() {
    fizzbuzz();
    return 0;
} 
