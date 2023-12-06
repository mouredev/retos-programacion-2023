#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

/**
*	Heterogram is a word or phrase without repeated letters
*/

bool isHeterogram(const std::string& s) {

	auto repited = false;
	auto i = 0;
	std::unordered_set<char> m;

	while (i < s.length()) {
		if (isalpha(s[i])) {
			if (m.count(tolower(s[i])))
				repited = true;
			else
				m.insert(tolower(s[i]));
		}
		++i;
	}

	return !repited;
}

/**
*	Isogram is a word or phrase with the same number of repeated letters
*/
bool isIsogram(const std::string& s) {

	std::unordered_map<char, int> m;

	for (const auto& c : s)
		if(isalpha(c))
			m[c]++;

	auto it = m.begin();
	auto c = it->second;
	auto equal = true;

	it++;
	while (it != m.end() && equal) {
		if (c != it->second)
			equal = false;
		else {
			c = it->second;
			it++;
		}
	}

	return equal;
}

/**
*	Panagram is a word or phrase that uses the entire alphabet
*/
bool isPangram(const std::string& s) {
	std::vector<bool> v(27);

	for (const auto& c : s) {
		if (tolower(c) == 'ñ' || isalpha(c)) {
			if (tolower(c) == 'ñ')
				v[26] = true;
			else
				v[tolower(c) - 'a'] = true;
		}
	}

	bool isValid = true;
	auto i = 0;
	while (i < v.size() && isValid) {
		isValid = v[i];
		++i;
	}

	return isValid;
}


int main() {

	std::string s1 = "yuxtaponer"; //heterogram
	std::string s12 = "yuxtaponerr"; //no heterogram

	std::string s2 = "UNCOPYRIGHTABLE"; //isogram
	std::string s22 = "UNCOPYRIGHTABLEE"; //no isogram

	std::string s3 = "abcdefghijklmnñopqrstuvwxyz"; //pangram
	std::string s32 = "abcdefghijklmnopqrstu"; //pangram


	
	std::cout << (isHeterogram(s1) ? "YES": "NO") << std::endl;
	std::cout << (isHeterogram(s12) ? "YES" : "NO") << std::endl;

	std::cout << (isIsogram(s2) ? "YES" : "NO") << std::endl;
	std::cout << (isIsogram(s22) ? "YES" : "NO") << std::endl;

	std::cout << (isPangram(s3) ? "YES" : "NO") << std::endl;
	std::cout << (isPangram(s32) ? "YES" : "NO") << std::endl;

	return 0;
}