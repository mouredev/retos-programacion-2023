#include <iostream>
#include <stdio.h>
#include <string>
#include <map>


using namespace std;


map<char, string> leetDict = {
        {'a', "4",}, {'b', "I3",}, {'c', "[",}, {'d', ")",}, {'e', "3",},
        {'f', "|=",}, {'g', "&",}, {'h', "#",}, {'i', "1",}, {'j', ",_|",},
        {'k', ">|",}, {'l', "1",}, {'m', "/\\/\\",}, {'n', "^/",}, {'o', "0",},
        {'p', "|*",}, {'q', "(_,)",}, {'r', "I2",}, {'s', "5",}, {'t', "7",},
        {'u', "(_)",}, {'v', "\\/",}, {'w', "\\/\\/",}, {'x', "><",}, {'y', "j",},
        {'z', "2",}, {'1', "L"}, {'2', "R",}, {'3', "E",}, {'4', "A",},
        {'5', "S",}, {'6', "b",}, {'7', "T",}, {'8', "B"}, {'9', "g",}, {'0', "o"},
        {' ', " "},
};


string leetConverter(string word)
{
    string output = "";

    for (int i = 0; i < word.length(); i++)
    {
        output += leetDict[word[i]];
    }
    return output;
}

int main()
{
    string x;
    cout << "Please, type a word:" << endl;
    getline(std::cin, x);
    cout << "The converted word is: " + leetConverter(x) << endl;
}