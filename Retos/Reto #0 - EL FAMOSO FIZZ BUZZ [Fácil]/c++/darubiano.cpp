#include <iostream>
#include <string>
using namespace std;

void fizz_buzz_junior()
{
    for (int number = 1; number < 101; number++)
    {
        if (number % 3 == 0 && number % 5 == 0)
        {
            cout << "fizzbuzz\n";
        }
        else if (number % 3 == 0)
        {
            cout << "fizz\n";
        }
        else if (number % 5 == 0)
        {
            cout << "buzz\n";
        }
        else
        {
            cout << number << endl;
        }
    }
}

void fizz_buzz_senior()
{
    for (int number = 1; number <= 100; number++)
    {
        string output;
        if (number % 3 == 0)
            output += "fizz";
        if (number % 5 == 0)
            output += "buzz";
        cout << (output.empty() ? to_string(number) : output) << endl;
    }
}

void fizz_buzz_chatgpt()
{
    for (int number = 1; number <= 100; number++)
    {
        string output = (number % 3 == 0 ? "fizz" : "");
        output += (number % 5 == 0 ? "buzz" : "");
        cout << (output.empty() ? to_string(number) : output) << endl;
    }
}

int main()
{
    //* Solucion junior
    fizz_buzz_junior();

    //* Solucion senior
    fizz_buzz_senior();

    //* Solucion chatgpt 👀
    fizz_buzz_chatgpt();
    return 0;
}
