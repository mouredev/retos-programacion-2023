def main():
    multiplo3 = False
    multiplo5 = False

    for x in range(1, 101):
        multiplo3 = x % 3
        multiplo5 = x % 5

        if(multiplo3 == 0 and multiplo5 == 0):
            print('fizzbuzz')
            continue
        elif(multiplo3 == 0):
            print('fizz')
            continue
        elif(multiplo5 == 0):
            print('buzz')
            continue
        else:
            print(x)

if (__name__ == '__main__'):
    main()