
def run():
    print('Bienvenidos a mi FizzBuzz\n')
    for number in range(1, 101):
        string = ''
        string += 'fizz' if (number % 3 == 0) else ''
        string += 'buzz' if (number % 5 == 0) else ''
        print(string) if string != '' else print(number)


if __name__ == '__main__':
    run()