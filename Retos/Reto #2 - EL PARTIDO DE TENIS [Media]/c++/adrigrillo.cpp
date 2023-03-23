
#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <span>

const std::map<int, std::string> POINTS = {
        {0, "Love"},
        {1, "15"},
        {2, "30"},
        {3, "40"}
};

std::vector<std::string> processInput(std::span<char*> arguments) {
    std::vector<std::string> sequence;
    if (arguments.size() > 1) {
        // argv[0] path to the script
        for (int i = 1; i < arguments.size(); ++i) {
            std::string elem = arguments[i];
            std::ranges::transform(elem.begin(), elem.end(), elem.begin(), toupper);
            if (elem == "P1" || elem == "P2") {
                sequence.emplace_back(elem);
            } else {
                std::cout << R"(Invalid sequence element. Only "P1" or "P2" are valid values.)" << std::endl;
            }
        }
    } else {
        std::cout << "Please, include the sequence as an argument in the command line. "
                     "Example: ./reto2 P1 P2 P1 P1 P1" << std::endl;
    }
    return sequence;
}

int main(int argc, char *argv[]) {
    std::vector<std::string> sequence = processInput(std::span(argv, argc));

    int pointsP1 = 0;
    int pointsP2 = 0;
    bool finished = false;
    for (auto const &action: sequence) {
        // update the punctuation
        (action == "P1") ? pointsP1++ : pointsP2++;

        // Print punctuation
        if (pointsP1 >= 3 && pointsP2 >= 3) {
            if (std::abs(pointsP1 - pointsP2) > 1) {
                finished = true;
            } else if (pointsP1 == pointsP2) {
                std::cout << "Deuce" << std::endl;
            } else {
                std::string text = "Ventaja para el ";
                text += (pointsP1 > pointsP2) ? "P1" : "P2";
                std::cout << text << std::endl;
            }
        } else if (pointsP1 < 4 && pointsP2 < 4) {
            auto text = POINTS.at(pointsP1);
            text += " - ";
            text += POINTS.at(pointsP2);
            std::cout << text << std::endl;
        } else {
            finished = true;
        }

        if (finished) {
            std::string text = "Ha ganado el ";
            text += (pointsP1 > pointsP2) ? "P1" : "P2";
            std::cout << text << std::endl;
            break;
        }
    }

    return 0;
}