import datetime

def triple_pitagorico(maxNum: int)-> list:
    list_triple_pit = list()
    for i in range (1, maxNum + 1):
        for j in range(1, i + 1):
            for k in range(1, j + 1):
                if k ** 2 + j ** 2 == i ** 2:
                    list_triple_pit.append((k, j, i))

    return list_triple_pit

st = datetime.datetime.timestamp(datetime.datetime.now())
ns = triple_pitagorico(10)
print(datetime.datetime.timestamp(datetime.datetime.now()) - st)
for aux in ns:
    print(aux)