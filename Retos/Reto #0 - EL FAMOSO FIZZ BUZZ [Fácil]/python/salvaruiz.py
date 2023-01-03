def fizz_buzz(n1,n2):

    i = 1

    while  i <= 100 :
        if  i%n1 == 0:
            if i%n2 == 0:
                print('fizzbuzz')
            else:
                print('fizz')
        elif i%n2 == 0:
            print('buzz')
        else:
            print(i)
        i = i + 1


fizz_buzz(3,5)
