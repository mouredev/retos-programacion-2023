#include <iostream>
#include <map>
#include <string>
#include <cctype>
#include <algorithm>

using namespace std;

int main() {

    map<char, string> leet_alphabet = {
        {    'a' ,"4",      },
        {    'b' ,"I3",     },
        {    'c' ,"[",      },
        {    'd' ,")",      },
        {    'e' ,"3",      },
        {    'f' ,"|=",     },
        {    'g' ,"&",      },
        {    'h' ,"#",      },
        {    'i' ,"1",      },
        {    'j' ,",_|",    },
        {    'k' ,">|",     },
        {    'l' ,"1",      },
        {    'm' ,"/\\/\\", },
        {    'n' ,"^/",     },
        {    'o' ,"0",      },
        {    'p' ,"|*",     },
        {    'q' ,"(_,)",   },
        {    'r' ,"I2",     },
        {    's' ,"5",      },
        {    't' ,"7",      },
        {    'u' ,"(_)",    },
        {    'v' ,"\\/",    },
        {    'w' ,"\\/\\/", },
        {    'x' ,"><",     },
        {    'y' ,"j",      },
        {    'z' ,"2",      },
        {    '1' ,"L"       },
        {    '2' ,"R",      },
        {    '3' ,"E",      },
        {    '4' ,"A",      },
        {    '5' ,"S",      },
        {    '6' ,"b",      },
        {    '7' ,"T",      },
        {    '8' ,"B"       },
        {    '9' ,"g",      },
        {    '0' ,"o"       },
        {    ' ' ," "       },
    };

    string text;
    cout << "Put in any normal text\n>";
    getline(cin, text);

    transform(text.begin(), text.end(), text.begin(), ::tolower);

    const char* c_text = text.c_str();

    for (int i = 0; i < text.length(); i++)
    {
        string word(1, c_text[i]);
        (leet_alphabet[c_text[i]] != "") ? cout << leet_alphabet[c_text[i]] : cout << word;
    }

	return 0;
}