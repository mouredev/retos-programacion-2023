#include <iostream>
#include <string>

using namespace std;

inline static bool isMultiplo(int value, int multiplo) {
	return ((value % multiplo) == 0);
}

int main()
{
	string str = "";
	for (int i = 1; i <= 100; i++) {
		str = "";
		if (isMultiplo(i, 3)) {
			str += "fizz";
		}
		if (isMultiplo(i, 5)) {
			str += "buzz";
		}
		if (str == "") {
			str = to_string(i);
		}
		cout << str << endl;
	}
}
