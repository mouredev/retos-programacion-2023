#include <iostream>
#include <list>
#include <string>
#include <unordered_map>
#include <unordered_set>

std::unordered_map<std::string, std::unordered_set<std::string>> rules = {
    {"piedra", std::unordered_set<std::string>({"tijera", "lagarto"})},
    {"papel", std::unordered_set<std::string>({"piedra", "spock"})},
    {"tijera", std::unordered_set<std::string>({"papel", "lagarto"})},
    {"lagarto", std::unordered_set<std::string>({"spock", "papel" })},
    {"spock", std::unordered_set<std::string>({"tijera", "piedra"})},
};


std::string checkResult(const std::list<std::pair<std::string,std::string>> &l) {
    auto player1 = 0;
    auto player2 = 0;

    for (const auto &p : l) {
        if (rules[p.first].count(p.second))
            ++player1;
        else if (rules[p.second].count(p.first))
            ++player2;
    }

    std::string result;
    if (player1 > player2)
        result = "PLAYER1";
    else if (player2 > player1)
        result = "PLAYER2";
    else
        result = "TIE";

    return result;
}


int main()
{
    //MOUREDEV EXAMPLE
    std::list<std::pair<std::string, std::string>> input = { {"piedra", "tijera"}, {"tijera", "piedra"}, {"papel", "tijera"}};
    std::cout << checkResult(input) << "\n";

    //PLAYER1 WINNER
    input = { {"piedra", "tijera"}, {"papel", "piedra"}, {"spock", "piedra"} };
    std::cout << checkResult(input) << "\n";

    //PLAYER2 WINNER
    input = { {"piedra", "tijera"}, {"piedra", "papel"}, {"piedra", "spock"} };
    std::cout << checkResult(input) << "\n";

    //TIE
    input = { {"piedra", "tijera"}, {"spock", "piedra"}, {"spock", "lagarto"}, {"lagarto", "tijera"} };
    std::cout << checkResult(input) << "\n";
    //TIE
    input = { {"piedra", "piedra"}, {"spock", "spock"}, {"spock", "spock"}, {"lagarto", "lagarto"} };
    std::cout << checkResult(input) << "\n";
    
    return 0;
}