INITIAL_NUMBERS_LIST = [1, 5, 3, 2]
GOAL = 6


def combinations(c: list) -> list:
    """
        Calcula y devuelve el conjunto potencia del conjunto c.
    """
    if len(c) == 0:
        return [[]]

    r = combinations(c[:-1])

    return r + [s + [c[-1]] for s in r]


def check_goal(numbers: list, goal: int) -> bool:

    if sum(numbers) == goal:
        return True

    return False


def print_solutions(solutions_list: list):

    for solution in solutions_list:
        print(solution)


def main():

    combinations_list = combinations(INITIAL_NUMBERS_LIST)
    solutions_list = [
        solution for solution in combinations_list if check_goal(solution, GOAL)]
    print_solutions(solutions_list)


if __name__ == '__main__':
    main()
