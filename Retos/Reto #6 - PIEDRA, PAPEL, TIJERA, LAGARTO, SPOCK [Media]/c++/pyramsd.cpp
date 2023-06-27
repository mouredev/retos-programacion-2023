#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
using namespace std;

string game(const vector<pair<string, string>>& players){
    int p1 = 0;
    int p2 = 0;
    int tie = 0;

    unordered_map<string, vector<string>> dic_moves_win{
        {"piedra", {"tijeras", "lagarto"}},
        {"papel", {"piedra", "spock"}},
        {"tijeras", {"papel", "lagarto"}},
        {"lagarto", {"papel", "spock"}},
        {"spock", {"tijeras", "piedra"}}
    };

    for (const auto& i : players){
        if (i.first == i.second) tie++;
        else if (find(dic_moves_win[i.second].begin(), dic_moves_win[i.second].end(), i.first) != dic_moves_win[i.second].end()) p2++;
        else p1++;
    }

    string r;
    if (p1 > p2) r = "Player 1";
    else if (p1 == p2) r = "Tie";
    else r = "Player 2";

    return r;

}

int main(){
    
    vector<pair<string, string>> game1 = {{"piedra", "spock"}, {"lagarto", "piedra"}, {"lagarto", "tijeras"}};
    vector<pair<string, string>> game2 = {{"lagarto", "papel"}, {"tijeras", "papel"}, {"papel", "spock"}};
    vector<pair<string, string>> game3 = {{"tijeras", "lagarto"}, {"papel", "tijeras"}};

    cout << game(game1) << endl;
    cout << game(game2) << endl;
    cout << game(game3) << endl;

}
