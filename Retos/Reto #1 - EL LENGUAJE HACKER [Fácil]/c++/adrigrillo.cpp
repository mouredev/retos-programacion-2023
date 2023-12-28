
#include <string>
#include <map>
#include <iostream>

const static std::map<char, std::string> LEET_ALPHABET = {
        {'a', "4",},
        {'b', "I3",},
        {'c', "[",},
        {'d', ")",},
        {'e', "3",},
        {'f', "|=",},
        {'g', "&",},
        {'h', "#",},
        {'i', "1",},
        {'j', ",_|",},
        {'k', ">|",},
        {'l', "1",},
        {'m', "/\\/\\",},
        {'n', "^/",},
        {'o', "0",},
        {'p', "|*",},
        {'q', "(_,)",},
        {'r', "I2",},
        {'s', "5",},
        {'t', "7",},
        {'u', "(_)",},
        {'v', "\\/",},
        {'w', "\\/\\/",},
        {'x', "><",},
        {'y', "j",},
        {'z', "2",},
        {'1', "L"},
        {'2', "R",},
        {'3', "E",},
        {'4', "A",},
        {'5', "S",},
        {'6', "b",},
        {'7', "T",},
        {'8', "B"},
        {'9', "g",},
        {'0', "o"},
        {' ', " "},
};

int main() {
    std::cout << "Write some text to be translated to hacker language" << std::endl;
    std::string text;
    if (!std::getline(std::cin, text)) {
        // Check for I/O errors
        return -1;
    }

    std::string finalText;
    for (auto character:text) {
        character = (char) std::tolower(character);
        auto leetCharacter = LEET_ALPHABET.find(character);
        if (leetCharacter != LEET_ALPHABET.end()){
            finalText += leetCharacter->second;
        } else {
            finalText += character;
        }
    }
    std::cout << "The result is:\n" + finalText << std::endl;
}