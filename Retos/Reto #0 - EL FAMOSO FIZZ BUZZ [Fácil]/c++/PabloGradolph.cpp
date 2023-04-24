#include <iostream>

using namespace std;

void fizzbuzz(){

    for (int i=1; i<=100; i++){
        if (i%3 == 0 && i%5 == 0){
            cout<<"fizzbuzz"<<endl;
        } else if (i%3 == 0){
            cout<<"fizz"<<endl;
        } else if (i%5 == 0){
            cout<<"buzz"<<endl;
        } else {
            cout<<i<<endl;
        }
    }
}

int main(){
    fizzbuzz();

    return 0;
}