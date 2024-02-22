#include <iostream>
#include <fstream>
using namespace std;

string change_line(string line)
{
    for (int i = 0; i < line.length(); i++)
    {
        if (line[i] == 'a')
            line[i] = '4';
        if (line[i] == 'e')
            line[i] = '3';
        if (line[i] == 'i')
            line[i] = '1';
        if (line[i] == 'o')
            line[i] = '0';
    }
    return line;
}

void read(string txt)
{
    ifstream archivo(txt.c_str());
    string line;
    while (getline(archivo, line))
    {
        string newLine = change_line(line);
        cout << newLine << endl;
    }
}
int main()
{
    read("txt.txt");
    return 0;
}