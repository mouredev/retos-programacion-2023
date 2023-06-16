#include <iostream>
using namespace std;

int main(){
    for (int i = 0; i <= 100; i++){
        if (i % 3 == 0 && i % 5 == 0) cout << "fizzbuzz" << endl;
        else if (i % 3 == 0) cout << "fizz" << endl;
        else if (i % 5 == 0) cout << "buzz" << endl;
        else cout << i << endl;
    }
}
