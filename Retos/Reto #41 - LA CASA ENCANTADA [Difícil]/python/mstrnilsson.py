import random, time, os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def intro():
    os.system('clear')
    txt1 = '👻 LA CASA ENCANTADA 👻'
    u = txt1.center(69, '#')
    print(f'\n\n\r{bcolors.HEADER}{bcolors.BOLD}{u}{bcolors.ENDC}\n\n', end='')
    time.sleep(1)
    txt2 = ' Te encuentas explorando las habitaciones de una 🏚️  mansión abandonada'
    v = txt2.center(69, '#')
    print(f'\r{bcolors.HEADER}{bcolors.BOLD}{v}{bcolors.ENDC}', end='')
    time.sleep(3)
    txt3 = ' Elige la dirección con las teclas N_orte 🔼 S_ur 🔽 E_ste ▶️  O_este ◀️ '
    w = txt3.center(69, '#')
    print(f'\r{bcolors.HEADER}{bcolors.BOLD}{w}{bcolors.ENDC}', end='')
    time.sleep(3)
    txt4 = ' Para entrar en cada habitación tendrás que resolver una pregunta '
    x = txt4.center(70, '#')
    print(f'\r{bcolors.HEADER}{bcolors.BOLD}{x}{bcolors.ENDC}', end='')
    time.sleep(3)
    txt5 = '¡¡¡¡ SUERTE !!!!'
    z = txt5.center(69, '#')
    print(f'\r{bcolors.HEADER}{bcolors.BOLD}{z}{bcolors.ENDC}\n', end='')
    os.system('clear')
    print('\r\r\r')
    time.sleep(1)


def random_targets():
    for i in range(1):
        random_row = random.randrange(0,4)
        random_column = random.randrange(0,4)
    return random_row, random_column

def targets(row, column):
    
    door_coor=[]
    lolli_coor=[]
    ghost_coor1 = []
    ghost_coor2 = []

    door_coor.extend([row, column])
    row, column = random_targets()
    while [row, column] == door_coor:
        row, column = random_targets()
    lolli_coor.extend([row, column])
    row, column = random_targets()
    while [row, column] == lolli_coor or [row, column] == door_coor:
        row, column = random_targets()
    ghost_coor1.extend([row, column])
    row, column = random_targets()
    while [row, column] == ghost_coor1 or [row, column] == lolli_coor or [row, column] == door_coor:
        row, column = random_targets()
    ghost_coor2.extend([row, column])

    return door_coor, lolli_coor, ghost_coor1, ghost_coor2
    

def paint_matrix(door_coor, now_coor, matrix):
    time.sleep(1)
    print('\r\r\r')
    for i in range(4):
        matrix.append([])
        for j in range(4):
            if [i, j] == door_coor:
                matrix[i].append('🚪')
                now_coor = door_coor.copy()
            else:
                matrix[i].append('🔳')
    for row in range(4):            
            for column in range(4):
                print(matrix[row][column], end = '')
            print()
    return now_coor, matrix

def course(now_coor):
    
    key = input('\nHacia que habitación quieres moverte?\n').lower()
    arrows = ['n', 's', 'e', 'o']

    if key == 'n':
        print('🔼')
    if key == 's':
        print('🔽')
    if key == 'e':
        print('▶️')
    if key == 'o':
        print('◀️')

    if key in arrows:
        if forbidden(key, now_coor) == key:
            return key
        else:
            return None
    else:
        return None
    
def forbidden(key, now_coor):
    
    if (now_coor[0] == 0 and key == 'n'):
        print(f'{bcolors.WARNING}\n ❌ No puedes moverte en esa dirección{bcolors.ENDC}')
        return None
    elif (now_coor[1] == 0 and key == 'o'):
        print(f'{bcolors.WARNING}\n ❌ No puedes moverte en esa dirección{bcolors.ENDC}')
        return None
    elif (now_coor[0] == 3 and key == 's'):
        print(f'{bcolors.WARNING}\n ❌ No puedes moverte en esa dirección{bcolors.ENDC}')
        return None
    elif (now_coor[1] == 3 and key == 'e'):
        print(f'{bcolors.WARNING}\n ❌ No puedes moverte en esa dirección{bcolors.ENDC}')
        return None
    else:
        return key

def next(key, now_coor):
   
    next_coor = now_coor.copy()
    
    if key == 'n':
        next_coor[0] -= 1
    if key == 's':
        next_coor[0] += 1
    if key == 'e':
        next_coor[1] += 1
    if key == 'o':
        next_coor[1] -= 1
    return next_coor
    

def wich_target(matrix, finish, next_coor, lolli_coor, ghost_coor1, ghost_coor2):
    
    if next_coor == ghost_coor1:
        print(f'\n{bcolors.WARNING}BUUUU !!! 👻 El fantasmico te retiene y debes superar 2 preguntas para entrar 👻{bcolors.ENDC}\n')
        time.sleep(1)
        enigma(2)
        print(f'\n{bcolors.OKGREEN}🔑 Puedes entrar en la habitación{bcolors.ENDC}\n')
        time.sleep(1)
        os.system('clear')
        matrix[ghost_coor1[0]][ghost_coor1[1]] = '👻'
        now_coor = next_coor.copy()
        return now_coor, finish

    elif next_coor == ghost_coor2:
        print(f'\n{bcolors.WARNING}BUUUU !!! 👻 El fantasmico te retiene y debes superar 2 preguntas para entrar 👻{bcolors.ENDC}\n')
        time.sleep(1)
        enigma(2)
        print(f'\n{bcolors.OKGREEN}🔑 Puedes entrar en la habitación{bcolors.ENDC}\n')
        time.sleep(1)
        os.system('clear')
        matrix[ghost_coor2[0]][ghost_coor2[1]] = '👻'
        now_coor = next_coor.copy()
        return now_coor, finish
        

    elif next_coor == lolli_coor:
        enigma(1)
        foo = '#'
        print(f'{bcolors.OKGREEN}\n{foo*9:68}{foo*9}{bcolors.ENDC}')
        print(f'{bcolors.OKGREEN}{foo*9:68}{foo*9}{bcolors.ENDC}')
        print(f'{bcolors.OKGREEN}{foo*9} 🍭 Genial!! Has encontrado la habitación de los dulces 🍭 {foo*9}{bcolors.ENDC}')
        print(f'{bcolors.OKGREEN}{foo*9:68}{foo*9}{bcolors.ENDC}')
        print(f'{bcolors.OKGREEN}{foo*9:68}{foo*9}\n{bcolors.ENDC}')
        time.sleep(1)
        matrix[lolli_coor[0]][lolli_coor[1]] = '🍭'
        now_coor = next_coor.copy()
        finish = 'lollipop'
        return now_coor, finish
        
    else:
        enigma(1)
        print(f'\n{bcolors.OKGREEN}🔑 Puedes entrar en la habitación{bcolors.ENDC}\n')
        time.sleep(1)
        os.system('clear')
        matrix[next_coor[0]][next_coor[1]] = '✅'
        now_coor = next_coor.copy()
        return now_coor, finish
        
def enigma(i:int):
    while i != 0:
        n1 = random.randrange(3,10)
        n2 = random.randrange(3,10)

        answer_input = input(f'\n{bcolors.OKBLUE}¿Cuánto es {n1} x {n2}? = {bcolors.ENDC}')
        answer = (n1*n2)

        if answer_input.isnumeric() and int(answer_input) == answer:
            print(f'\n{bcolors.OKGREEN}Correcto!!{bcolors.ENDC}')
        else: 
            print(f'\n{bcolors.FAIL} ❌ Lo siento respuesta incorrecta, es {bcolors.WARNING}{answer}{bcolors.ENDC}{bcolors.FAIL}, prueba otra vez{bcolors.ENDC}')
            enigma(1)
        i -= 1

def main():
    row=0
    column=0
    matrix = []
    next_coor = []
    now_coor = []
    key = ''
    finish = ''
    try:
        time.sleep(1)
        row, column = random_targets()
        door_coor, lolli_coor, ghost_coor1, ghost_coor2 = targets(row, column)
        now_coor, matrix = paint_matrix(door_coor, now_coor, matrix)
        while finish == '':
            key = course(now_coor)
            while key == None:
                key = course(now_coor)
            next_coor = next(key, now_coor)
            forbidden(key, now_coor)
            now_coor, finish = wich_target(matrix, finish, next_coor, lolli_coor, ghost_coor1, ghost_coor2)
            paint_matrix(door_coor, now_coor, matrix)
        menu()
    except KeyboardInterrupt:
        print('\nbye!!\n')    
        SystemExit

        
if __name__ == "__main__":
    
    def menu():
        
        try:            
            chosen_element = input(f"\n{bcolors.BOLD}{bcolors.OKBLUE}BIENVENIDO AL JUEGO, ELIGE UNA OPCIÓN: J_ugar C_ontinuar S_alir{bcolors.ENDC} \n")
            os.system('clear')
            if chosen_element.upper() == "J":
                intro()
                main()
            elif chosen_element.upper() == "C":
                main()
            elif chosen_element.upper() == "S":
                print('\nbye!!\n')
                time.sleep(1)   
                SystemExit
            else:
                print("\nOpción no válida, vuelve a intentarlo")
                menu()
        except KeyboardInterrupt:
            print('\nbye!!\n') 
            SystemExit
    menu()
    




    