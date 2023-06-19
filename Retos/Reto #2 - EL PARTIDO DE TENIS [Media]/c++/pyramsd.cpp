#include <iostream>
#include <vector>
using namespace std;

void finalMatch(const vector<string>& lista);

int main(){
    vector<string> lista {"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"};
    finalMatch(lista);
}

vector<string> scores {"love", "15", "30", "40"};

void finalMatch(const vector<string>& lista){
    int p1 = 0, p2 = 0;

    for (string p : lista){
        if (p == "P1") p1 += 1;
        else if (p == "P2") p2 += 1;

        if (p1 == 3 && p2 == 3) cout << "Deuce" << endl;
        else if (p1 >= 4 || p2 >= 4){
            int diff = p1 - p2;
            if (diff == 0) cout << "Deuce" << endl;
            else if (diff == 1) cout << "Ventaja P1" << endl;
            else if (diff == -1) cout << "Ventaja P2" << endl;
            else if (diff >= 2) cout << "Ha ganado el P1" << endl;
            else cout << "Ha ganado P2";
        }else cout << scores[p1] << "-" << scores[p2] << endl;
    }
}
