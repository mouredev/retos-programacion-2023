#include <string>
#include <vector>
#include <ranges>
#include <iostream>
#include <random>
#include <algorithm>

struct toChar {
    char operator()(int p) const { return (char) p; }
};


std::string generatePassword(int charactersNum,
                             bool upper,
                             bool lower,
                             bool number,
                             bool symbols) {
    // Use the ASCII table to select the characters to use
    std::vector<std::ranges::iota_view<int, int>> passElements;
    if (upper) {
        passElements.emplace_back(std::views::iota(65, 90));
    }
    if (lower) {
        passElements.emplace_back(std::views::iota(97, 122));
    }
    if (number) {
        passElements.emplace_back(std::views::iota(48, 57));
    }
    if (symbols) {
        passElements.emplace_back(std::views::iota(33, 47));
        passElements.emplace_back(std::views::iota(58, 64));
        passElements.emplace_back(std::views::iota(91, 96));
        passElements.emplace_back(std::views::iota(123, 126));
    }
    // Join the ranges and copy in a vector
    auto elementsToUseView = passElements | std::views::join;
    std::vector<int> elementsToUse{begin(elementsToUseView), end(elementsToUseView)};
    // Take random elements
    std::vector<int> intPassword;
    std::mt19937 rng{std::random_device{}()};
    std::ranges::sample(elementsToUse, std::back_inserter(intPassword), charactersNum, rng);
    // Transform to char
    std::string password;
    std::ranges::transform(intPassword, std::back_inserter(password), toChar());
    return password;
}

int main(int argc, char *argv[]) {
    int characterNum = 16;
    bool useUpper = true;
    bool useLower = true;
    bool useNumber = true;
    bool useSymbols = true;
    std::string password = generatePassword(characterNum, useUpper, useLower, useNumber, useSymbols);
    std::cout << password << std::endl;
}
