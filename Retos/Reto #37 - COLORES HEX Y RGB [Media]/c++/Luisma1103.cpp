#include <cmath>
#include <string>
#include <vector>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

unordered_map<char, int> hex_map = {
    {'0', 0}, {'1', 1}, {'2', 2}, {'3', 3},
    {'4', 4}, {'5', 5}, {'6', 6}, {'7', 7},
    {'8', 8}, {'9', 9}, {'A', 10}, {'B', 11},
    {'C', 12}, {'D', 13}, {'E', 14}, {'F', 15},
};

unordered_map<int, string> dec_map = {
    {0, "0"}, {1, "1"}, {2, "2"}, {3, "3"},
    {4, "4"}, {5, "5"}, {6, "6"}, {7, "7"},
    {8, "8"}, {9, "9"}, {10, "A"}, {11, "B"},
    {12, "C"}, {13, "D"}, {14, "E"}, {15, "F"},
};

string hex2dec(string hex) {
    
    int res = 0;

    for (int i = 0; i < hex.size(); i++) {
        char c = toupper(hex.at(i));
        int n = static_cast<int>(pow(16, i));
        res += n * hex_map[c];
    }

    string s = to_string(res);
    return s;
}

string dec2hex(int num) {

    string s;

    while (num != 0) {
        s += dec_map[num % 16];
        num /= 16;
    }

    reverse(s.begin(), s.end());
    return s;
}

string hex2rgb(string hex) {

    if (hex.empty()) { return ""; }
    if (hex.at(0) == '#') { hex.erase(0, 1); }

    string r, g, b;

    r = hex.substr(0, 2);
    r = hex2dec(r);
    g = hex.substr(2, 2);
    g = hex2dec(g);
    b = hex.substr(4, 2);
    b = hex2dec(b);

    return "(r: " + r + ", g: " + g + ", b: "+ b + ")";
}

string rgb2hex(int r, int g, int b) {

    string r_str, g_str, b_str;

    r_str = dec2hex(r);
    g_str = dec2hex(g);
    b_str = dec2hex(b);

    return "#" + r_str + g_str + b_str;
}

int main() {
    cout << hex2rgb("#FFEEAA") << endl;
    cout << rgb2hex(255, 238, 170) << endl;
    return 0;
}
