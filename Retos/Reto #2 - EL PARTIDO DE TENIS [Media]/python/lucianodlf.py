#!/usr/bin/env python3
label_points = ["Love", "15", "30", "40", "Deuce", "Advantage", "All"]


def processGame(secuence_game):
    points_player_1 = 0
    points_player_2 = 0
    count_match = 0
    player_wins_match = '-'
    label_player_1 = label_points[0]
    label_player_2 = label_points[0]

    # Verify whether the amount of the match is adequate
    if (len(secuence_game) == 0 or len(secuence_game) % 2 != 0):
        print("Error in game secuence")
        exit()

    printResumePoints(count_match, player_wins_match,
                      label_player_1, label_player_2)

    for point in secuence_game:
        count_match += 1
        player_wins_match = point

        if player_wins_match == 'P1':
            points_player_1 += 1
        elif player_wins_match == 'P2':
            points_player_2 += 1
        else:
            print("Error in format of game secuence")
            exit()

        if points_player_1 > 2 or points_player_2 > 2:
            if points_player_1 - points_player_2 == 2:  # If win player 1
                printResumePoints(count_match, player_wins_match, "Wins!", "")
                break
            elif points_player_2 - points_player_1 == 2:  # If win player 2
                printResumePoints(count_match, player_wins_match, "", "Wins!")
                break
            elif points_player_1 - points_player_2 == 1:  # If Advantage player 1
                printResumePoints(
                    count_match, player_wins_match, label_points[5], "")
            elif points_player_2 - points_player_1 == 1:  # If Advantage player 2
                printResumePoints(
                    count_match, player_wins_match, "", label_points[5])
            elif points_player_1 == points_player_2:  # Deuce
                printResumePoints(
                    count_match, player_wins_match, label_points[4], label_points[4])
            else:
                print("Esto no tiene que salir!")
        else:
            if points_player_1 == 2 and points_player_2 == 2:  # All or 30 equals
                printResumePoints(count_match, player_wins_match,
                                  label_points[6], label_points[6])
            else:
                printResumePoints(count_match, player_wins_match,
                                  label_points[points_player_1], label_points[points_player_2])

    printResumePoints(None, None, None, None)


def printResumePoints(number_match, player_current_point, player1_label_point, player2_label_point):
    if number_match == 0:
        print('+' + '-'*45 + '+')
        print(
            f'|{"N° Match".center(10)}|{"Wins Match".center(12)}|{"P1".center(10)}|{"P2".center(10)}|')
        print('|' + '-'*45 + '|')
        print(f'|{"0".center(10)}|{player_current_point.center(12)}|{player1_label_point.center(10)}|{player2_label_point.center(10)}|')
    elif number_match == None:
        print('+' + '-'*45 + '+')
        # print(f'|{"_"*10}|{"_"*12}|{"_"*10}|{"_"*10}|')
    else:
        print(f'|{str(number_match).center(10)}|{player_current_point.center(12)}|{player1_label_point.center(10)}|{player2_label_point.center(10)}|')


print(processGame(['P1', 'P2', 'P1', 'P2', 'P2', 'P2']))
print(processGame(['P1', 'P2', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1']))
print(processGame(['P1', 'P2', 'P1', 'P2',
      'P2', 'P1', 'P2', 'P1', 'P1', 'P1']))
