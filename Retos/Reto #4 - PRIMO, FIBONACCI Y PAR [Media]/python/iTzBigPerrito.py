def main():
    try:
        while(True):
            evenFlag = False
            fibFlag = False
            primeFlag = False

            numberInput = int(input('Enter a number: '))
            fibCheckList = fibonacci(numberInput)

            if(numberInput != 1):
                for i in range(2, numberInput):
                    if(numberInput % i != 0):
                        primeFlag = True
                    else:
                        primeFlag = False
                        break

            if(numberInput in fibCheckList):
                fibFlag = True

            if(numberInput % 2 == 0):
                evenFlag = True
            break
        
        textEven = 'is even' if(evenFlag) else 'is not even'
        textFib = 'is fibonacci' if(fibFlag) else 'is not fibonacci'
        textPrime = 'is prime' if(primeFlag) else 'is not prime'

        print(f'The number {numberInput} {textEven}, {textFib}, and {textPrime}')

    except:
        print('Unexpected error, try again later');
        exit(0)

def fibonacci(len):    
    pos0 = 0
    pos1 = 1

    fibList = [0,1]
    


    for i in range(0, len):
        nextPos = pos0 + pos1
        fibList.append(nextPos)
        pos0 = pos1
        pos1 = nextPos    

    return fibList


if __name__ == '__main__':
    main()