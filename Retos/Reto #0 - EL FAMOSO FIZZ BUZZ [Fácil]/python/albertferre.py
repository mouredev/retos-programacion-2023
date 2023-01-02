def is_multiple(num, div):
    ret = (num%div) == 0
    return ret

def fizzbuzz(i):
    multiple3 = is_multiple(i, 3)
    multiple5 = is_multiple(i, 5)

    if multiple3 & multiple5:
        ret = "fizzbuzz"
    elif multiple3:
        ret = "fizz"
    elif multiple5:
        ret = "buzz"
    else:
        ret = i

    return ret

if __name__ == "__main__":
    for i in range(1,101):
        print(fizzbuzz(i))
