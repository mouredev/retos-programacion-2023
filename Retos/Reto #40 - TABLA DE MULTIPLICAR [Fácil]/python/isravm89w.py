
if __name__ == "__main__":

    while True:
        try:
            number = int(input("Enter a number between 1 and 10: \n"))
            if number < 1 or number > 10:
                raise ValueError 

            for index in range(1, 11):
                print(f"{number} x {index} = {number * index}")
        except ValueError:
            continue
        else:
            break