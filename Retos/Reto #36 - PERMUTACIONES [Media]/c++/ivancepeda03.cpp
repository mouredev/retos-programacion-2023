#include <iostream>
#include <vector>
using namespace std;

const string INPUT = "hola";

void print_permutations(string word, string sol, int k, vector<bool> used_letters) {
	for (int letter = 0; letter < word.size(); letter++) {
		sol.push_back(word[letter]);

		if (!used_letters[letter]) {

			used_letters[letter] = true;

			if (k == word.size() - 1)
				cout << sol << endl;
			else
				print_permutations(word, sol, k + 1, used_letters);

			used_letters[letter] = false;
		}
		sol.pop_back();
	}
}

void print_permutations(string word) {
	vector<bool> used_letters(word.size(), false);
	string sol;
	print_permutations(word, sol, 0, used_letters);
}

int main() {
	print_permutations(INPUT);

	return 0;
}