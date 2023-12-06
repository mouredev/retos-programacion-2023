def dif(str1, str2):
    arr = []
    if not len(str1) == len(str2): print("The strings have different lenght")
    for n in range(0, int(len(str1) - 1)):
        if not str1[n] == str2[n]: arr.append(str2[n])
    return arr


dif("Me llamo mouredev", "Me llemo mouredo")
