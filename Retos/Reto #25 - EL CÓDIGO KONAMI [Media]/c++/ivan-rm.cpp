// This program prompts reads the user input and detects if the "Konami" code
// has been pressed.
// The Konami code it's the following secuence of keys presses: ↑ ↑ ↓ ↓ ← → ← → B A
//
// As we are using the ncurses library, we have to tell the compiler to link it:
// g++ -o ivan-rm ivan-rm.cpp -lncurses
// @Author: Iván Ruiz Marcos


#include <iostream>
#include <ncurses.h>          // For detection of the arrow keys in Linux


class KonamiCode {
    private:
        // Arrow keys are not ASCII characters, they are special keys. There is no
        // standard or portable way to detect them, the implementation is OS specific.
        // When pressing an arrow key two values are received, the first one is 224
        // and the second one is the direction of the arrow key.

        int konamiCode[10] = {KEY_UP, KEY_UP,
                             KEY_DOWN, KEY_DOWN,
                             KEY_LEFT, KEY_RIGHT,
                             KEY_LEFT, KEY_RIGHT,
                             'B', 'A'};
        int konamiCodeIndex = 0;
    public:
        bool isKonamiCode(int key) {
            if (key == konamiCode[konamiCodeIndex]) {
                konamiCodeIndex++;
                if (konamiCodeIndex == 10) {
                    konamiCodeIndex = 0;
                    return true;
                }
            } else {
                konamiCodeIndex = 0;
            }
            return false;
        }
};

int main() {

    KonamiCode konamiCode;
    int keyPress;

    // curses initializations for detecting the arrow keys in Linux
    initscr();                  // curses initialization
    keypad(stdscr, TRUE);       // enable KEY_UP/KEY_DOWN/KEY_RIGHT/KEY_LEFT
    noecho();                   // do not echo the pressed key on the screen

    std::cout << "Keep pressing keys and the program will check if the Konami secuence has been pressed:" << std::endl;

    while (true) {
        keyPress = getch ();
        if (konamiCode.isKonamiCode(keyPress)) {
            clear();
            std::cout << "Konami code detected!" << std::endl;
            break;
        }
    }

    return 0;
}