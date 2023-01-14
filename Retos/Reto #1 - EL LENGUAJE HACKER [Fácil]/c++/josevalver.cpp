#include <stdio.h>
#include <string>
#include <map>
#include <iostream>

std::map<char, std::string> leetmap = {
    {'A', "4"}, {'B', "I3"}, {'C', "["}, {'D', ")"}, {'E', "3"}, {'F', "|="}, {'G', "&"}, {'H', "#"}, {'I', "1"},
    {'J', ",_|"}, {'K', ">|"}, {'L', "1"}, {'M', "|\\/|"}, {'N', "^/"}, {'O', "0"}, {'P', "|*"}, {'Q', "(_,)"},
    {'R', "I2"}, {'S', "5"}, {'T', "7"}, {'U', "(_)"}, {'V', "\\/"}, {'W', "\\/\\/"}, {'X', "><"}, {'Y', "j"}, {'Z', "2"},
    {'1', "L"}, {'2', "R"}, {'3', "E"}, {'4', "A"}, {'5', "S"}, {'6', "b"}, {'7', "T"}, {'8', "B"}, {'9', "g"}, {'0', "o"}
};

std::string textToLeet(std::string text) {
    std::string leet = "";
    std::map<char, std::string>::iterator it;
    for (char c : text) {
        it = leetmap.find(toupper(c));
        if (it != leetmap.end()) {
            leet += it->second;
        } else {
            leet += c;
        }
    }
    return leet;
}

int main() {
    std::cout << "Enter text to convert to leet: " << std::endl;
    std::string text;
    std::getline(std::cin, text);
    std::cout << textToLeet(text) << std::endl;
}