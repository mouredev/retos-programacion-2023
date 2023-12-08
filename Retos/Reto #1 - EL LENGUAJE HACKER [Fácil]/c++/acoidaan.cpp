#include <iostream>
#include <string>
#include <map>
#include <cctype>
std::string toLower(const std::string& text) {
  std::string result;
  for (char c : text) {
    result += std::tolower(c);
  }
  return result;
}

int main() {
  const std::map<char, std::string> leet_alphabet = {
  {'a', "4",},
  {'b', "I3",},
  {'c', "[",},
  {'e', "3",},
  {'d', ")",},
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
  {' ', " "}
  };
  std::string input_text;
  std::cout << "Write some text to be translated to hacker language" << std::endl;
  std::getline(std::cin, input_text);
  std::string lower_text = toLower(input_text);
  for (char i : lower_text) {
    std::cout << leet_alphabet.at(i);
  }
}