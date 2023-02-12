#include <map>
#include <vector>
#include <iostream>

enum class Move {
    PIEDRA,
    PAPEL,
    TIJERA,
    LAGARTO,
    SPOCK
};

const std::map<Move, std::vector<int>> MOVES_MATRIX = {
        {Move::PIEDRA,  {0,  -1, 1,  1,  -1}},
        {Move::PAPEL,   {1,  0,  -1, -1, 1}},
        {Move::TIJERA,  {-1, 1,  0,  1,  -1}},
        {Move::LAGARTO, {-1, 1,  -1, 0,  1}},
        {Move::SPOCK,   {1,  -1, 1,  -1, 0}}
};

void processGame(std::vector<std::tuple<Move, Move>> const &moves) {
    int score = 0;
    for (auto [p1, p2]: moves) {
        const auto &movePoints = MOVES_MATRIX.at(p1);
        score += movePoints[(int) p2];
    }
    if (score == 0) {
        std::cout << "Empate" << std::endl;
    } else {
        std::cout << "Gana el Jugador " + (std::string) ((score > 0) ? "1" : "2") << std::endl;
    }
}

int main(int argc, char *argv[]) {
    using
    enum Move;
    std::vector<std::tuple<Move, Move>> moves = {
            std::make_tuple(PIEDRA, PAPEL),
            std::make_tuple(TIJERA, PAPEL),
            std::make_tuple(TIJERA, PAPEL)
    };
    processGame(moves);
}
