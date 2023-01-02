def run ():

    for i in range(1, 101):
        three_div = i % 3==0
        five_div =i % 5 ==0
        if (three_div & five_div):
            print("fizzbuzz")

        elif (three_div):
            print("fizz")

        elif (five_div):
            print("buzz")

        else:
            print(i)

if __name__== '__main__':
    run()