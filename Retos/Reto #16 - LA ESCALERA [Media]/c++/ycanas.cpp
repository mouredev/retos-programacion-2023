#include <iostream>

void drawStaircase(int steps);

int main() {
    std::cout << "Ascendente:" << std::endl;
    drawStaircase(4);

    std::cout << "Descendente:" << std::endl;
    drawStaircase(-4);

    std::cout << "0:" << std::endl;
    drawStaircase(0);

    return 0;
}

void drawStaircase(int steps) {
    if (steps > 0) {
        for (int i = 0; i < steps + 1; i++) {
            std::string draw = i == 0 ? "_" : "_|";
            int spaces = (steps * 2) - (2 * i);

            for (int j = 0; j < spaces; j++) {
                std::cout << " ";
            }

            std::cout << draw << std::endl;
        }
    }

    else if (steps < 0) {
        for (int i = 0; i < steps * (- 1) + 1; i++) {
            std::string draw = i == 0 ? " _" : "|_";

            for (int j = 0; j < 2 * i; j++) {
                std::cout << " ";
            }

            std::cout << draw << std::endl;
        }
    }

    else {
        std::cout << "__" << std::endl;
    }
}
