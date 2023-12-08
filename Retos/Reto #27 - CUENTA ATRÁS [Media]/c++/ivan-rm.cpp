// This program creates a function that implements a countdown and
// prints it on the screen.
// The function accepts two parameters, the first it's the number where
// the countdown starts and the second it's the number of seconds slapsed
// between counts.
// @author: Iván Ruiz Marcos
// @version: 1.0

#include <iostream>
#include <unistd.h>     // Use the operating system as the clock source

bool countdown(int number, int delay)
{
    if (number < 0 || delay <= 0)
    {
        return false;
    }

    while (number >= 0)
    {
        std::cout << number << std::endl;
        if (number != 0) { sleep(delay); }  // Don't wait if we reached 0
        number--;
    }
    return true;
}

int main()
{
    std::cout << "The final countdown!" << std::endl;
    if (!countdown(10, 5)) { std::cout << "Illegal function parameters!"; };
    return 0;
}