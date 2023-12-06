#include <iostream>

using namespace std;

bool isDivisibleBy(int i, int j);
string checkerFun(int i);

int main()
{

    for (int i = 1; i <= 100; i++)
    {
        cout << (checkerFun(i)) << endl;
    }

    return 0;
}

string checkerFun(int i)
{
    if (isDivisibleBy(i, 15))
    {

        return "Fizz Buzz";
    }

    else if (isDivisibleBy(i, 3))
    {
        return "Fizz";
    }
    else if (isDivisibleBy(i, 5))
    {
        return "Buzz";
    }
    else
    {
        return to_string(i);
    }
}

bool isDivisibleBy(int i, int j)
{
    if (i % j == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}