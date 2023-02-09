# La manera más normal y lógica

def solution_one():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print('fizzbuzz')
        elif num % 3 == 0:
            print('fizz')
        elif num % 5 == 0:
            print('buzz')
        else:
            print(num)


# La manera kamikaze, no me importa PEP8 a tomar por saco
def solution_two():
    for num in range(1, 101):
        print('fizzbuz') if num % 3 == 0 and num % 5 == 0 else print('fizz') if num % 3 == 0 else print('buzz') if num % 5 == 0 else print(num)


if __name__ == '__main__':
    solution_one()
    solution_two()
    
