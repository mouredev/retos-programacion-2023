#!/usr/bin/env python3

import random
from enum import Enum

class ResultRound(Enum):
    WIN = 1
    LOSE = 2
    DRAW = 3

values = ["rock", "scissors", "paper", "spock", "lizard"]

def play_round(player1, player2):
    game_matrix = {
        "rock" : ["scissors", "lizard"],
        "scissors" : ["paper", "lizard"],
        "paper" : ["rock", "spock"],
        "spock" : ["scissors", "rock"],
        "lizard" : ["spock", "paper"],
    }

    if player1 == player2:
        return ResultRound.DRAW

    if player2 in game_matrix[player1]:
        return ResultRound.WIN
    else:
        return ResultRound.LOSE

def play_game(rounds):
    score_p1 = 0
    score_p2 = 0

    for r in rounds:
        res = play_round(r[0], r[1])
        if res == ResultRound.WIN:
            score_p1 = score_p1 + 1
        elif res == ResultRound.LOSE:
            score_p2 = score_p2 + 1

    print("Final score:")
    print("Player 1: "+str(score_p1))
    print("Player 2: "+str(score_p2))
    print("Final result:")
    if score_p1 == score_p2:
        print("Tie")
    elif score_p1 > score_p2:
        print("Player 1")
    else:
        print("Player 2")

def play_vs_computer():
    rounds = []
    random.seed()
    print("Introduce "+str(values)+" or 'end' to finish")

    p1_round = input()
    while p1_round != "end":
        if p1_round in values:
            p2_round = random.choice(values)
            rounds.append([p1_round, p2_round])
        p1_round = input()

    print("Game with rounds: "+str(rounds))
    play_game(rounds)

if __name__ == "__main__":
    play_game([["rock", "scissors"], ["scissors", "rock"], ["paper", "scissors"]])
    play_vs_computer()
