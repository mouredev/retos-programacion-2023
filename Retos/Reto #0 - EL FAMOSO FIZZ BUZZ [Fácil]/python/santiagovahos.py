def main():
    n = list(range(1, 101))
    for i in n:
        if (i % 3 == 0) & (i % 5 == 0):
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:    
            print(f'{i}')
main()