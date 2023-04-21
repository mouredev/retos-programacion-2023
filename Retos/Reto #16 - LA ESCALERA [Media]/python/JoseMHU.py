<<<<<<< HEAD
<<<<<<< HEAD
def ladder_builder(num):
    if num == 0:
        print("__")
    elif num < 0:
        count = 1
        print("_")
        for _ in range(0, abs(num)):
            print(" " * count + "|_")
            count += 2
    else:
        count = num - 1
        print("  " * (count + 1) + "_")
        for _ in range(0, num):
            print("  " * count + "_|")
            count -= 1


if __name__ == "__main__":
    ladder_builder(9)
=======
def ladder_builder(num):
    if num == 0:
        print("__")
    elif num < 0:
        count = 1
        print("_")
        for _ in range(0, abs(num)):
            print(" " * count + "|_")
            count += 2
    else:
        count = num - 1
        print("  " * (count + 1) + "_")
        for _ in range(0, num):
            print("  " * count + "_|")
            count -= 1


if __name__ == "__main__":
    ladder_builder(9)
>>>>>>> 4283955b820868d1d5cd8429791ea3d5a789bf2b
=======
def ladder_builder(num):
    if num == 0:
        print("__")
    elif num < 0:
        count = 1
        print("_")
        for _ in range(0, abs(num)):
            print(" " * count + "|_")
            count += 2
    else:
        count = num - 1
        print("  " * (count + 1) + "_")
        for _ in range(0, num):
            print("  " * count + "_|")
            count -= 1


if __name__ == "__main__":
    ladder_builder(9)
>>>>>>> 4283955b820868d1d5cd8429791ea3d5a789bf2b
