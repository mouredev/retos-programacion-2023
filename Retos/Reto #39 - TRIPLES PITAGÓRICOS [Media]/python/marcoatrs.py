from itertools import product


def triples_pitagoricos(max_number: int) -> list:
    result = []
    for combi in product(list(range(1, max_number+1)), list(range(1, max_number+1))):
        hipo = (combi[0] ** 2 + combi[1] ** 2) ** 0.5
        if (hipo != int(hipo)) or (hipo > max_number):
            continue
        res = sorted([combi[0], combi[1], int(hipo)])
        if res in result:
            continue
        result.append(res)
    return result


print(triples_pitagoricos(10))
