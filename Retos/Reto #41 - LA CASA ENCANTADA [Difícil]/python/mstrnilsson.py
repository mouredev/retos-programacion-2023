import random, time

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

print_matrix = []
door_coor = []
ghost_coor1 = []
ghost_coor2 = []
lolli_coor = []
next_coor = []
now_coor = []

row=0
column=0
row_door=0
column_door=0
square = "🔳"
door = "🚪"
ghost = "👻"
up_arrow = "🔼" 
down_arrow = "🔽"
left_arrow = "◀️"
right_arrow = "▶️"
lollipop = "🍭"
ok = "✅"
up = 'n'
down = 's'
left = 'o'
right = 'e'
arrows = ['n', 's', 'e', 'o']

key = ''
finish = ''

def intro():
    txt1 = '👻 LA CASA ENCANTADA 👻'
    u = txt1.center(67, '#')
    print(f'\n{bcolors.HEADER}{bcolors.BOLD}{u}{bcolors.ENDC}\n')
    time.sleep(1)
    txt2 = 'Te encuentas explorando las habitaciones de una 🏚️  mansión abandonada'
    v = txt2.center(66, '#')
    print(f'\n{bcolors.HEADER}{bcolors.BOLD}{v}{bcolors.ENDC}\n')
    time.sleep(4)
    txt6 = 'Elige la dirección con las teclas N_orte 🔼 S_ur 🔽 E_ste ▶️  O_este ◀️ '
    w = txt6.center(66, '#')
    print(f'\n{bcolors.HEADER}{bcolors.BOLD}{w}{bcolors.ENDC}\n')
    time.sleep(4)
    txt5 = '  Para entrar en cada habitación tendrás que resolver una pregunta '
    x = txt5.center(66, '#')
    print(f'\n{bcolors.HEADER}{bcolors.BOLD}{x}{bcolors.ENDC}\n')
    time.sleep(4)
    txt3 = ' Tu misión es encontrar la habitación de los dulces 🍭  '
    y = txt3.center(66, '#')
    print(f'\n{bcolors.HEADER}{bcolors.BOLD}{y}{bcolors.ENDC}\n')
    time.sleep(4)
    txt4 = ' ¡¡¡¡ 🎃 SUERTE 🎃 !!!! '
    z = txt4.center(66, '#')
    print(f'\n{bcolors.HEADER}{bcolors.BOLD}{z}{bcolors.ENDC}\n')
    time.sleep(2)


def random_room():
    for i in range(1):
        random_row = random.randrange(0,4)
        random_column = random.randrange(0,4)
    return random_row, random_column

def paint_game(row, column):
    door_coor.extend([row, column])
    row, column = random_room()
    while [row, column] == door_coor:
        row, column = random_room()
    lolli_coor.extend([row, column])
    row, column = random_room()
    while [row, column] == lolli_coor or [row, column] == door_coor:
        row, column = random_room()
    ghost_coor1.extend([row, column])
    row, column = random_room()
    while [row, column] == ghost_coor1 or [row, column] == lolli_coor or [row, column] == door_coor:
        row, column = random_room()
    ghost_coor2.extend([row, column])

    return door_coor, lolli_coor, ghost_coor1, ghost_coor2
    

def paint_matrix(door_coor):
    
    for i in range(4):
        print_matrix.append([])
        for j in range(4):
            if [i, j] == door_coor:
                print_matrix[i].append(door)
                now_coor = door_coor.copy()
            else:
                print_matrix[i].append(square)
    for row in range(4):
            for column in range(4):
                print(print_matrix[row][column], end = '')
            print()
    return now_coor    

        

def status():
    
    key = input('\nHacia que habitación quieres moverte?\n').lower()

    if key == up:
        print(f'{up_arrow}')
    if key == down:
        print(f'{down_arrow}')
    if key == right:
        print(f'{right_arrow}')
    if key == left:
        print(f'{left_arrow}')


    if key in arrows:
        if forbidden(key) == key:
            return key
        else:
            return None
    else:
        return None
    
def forbidden(key):
    

    if (now_coor[0] == 0 and key == up):
        print(f'{bcolors.WARNING}\n ❌ No puedes moverte en esa dirección{bcolors.ENDC}')
        return None
        
    elif (now_coor[1] == 0 and key == left):
        print(f'{bcolors.WARNING}\n ❌ No puedes moverte en esa dirección{bcolors.ENDC}')
        return None
        
    elif (now_coor[0] == 3 and key == down):
        print(f'{bcolors.WARNING}\n ❌ No puedes moverte en esa dirección{bcolors.ENDC}')
        return None
        
    elif (now_coor[1] == 3 and key == right):
        print(f'{bcolors.WARNING}\n ❌ No puedes moverte en esa dirección{bcolors.ENDC}')
        return None
    else:
        return key

def move_status(key):
   
    next_coor = now_coor.copy()
    
    if key == up:
        next_coor[0] -= 1
        
    if key == down:
        next_coor[0] += 1
        
    if key == right:
        next_coor[1] += 1
        
    if key == left:
        next_coor[1] -= 1
    return next_coor
    

def wich_question(finish):
    
    if next_coor == ghost_coor1:
        print(f'\n{bcolors.WARNING}BUUUU !!! 👻 El fantasmico te retiene y debes superar 2 preguntas para entrar 👻{bcolors.ENDC}\n')
        time.sleep(2)
        times(2)
        print(f'\n{bcolors.OKGREEN}Puedes entrar en la habitación{bcolors.ENDC}\n')
        time.sleep(2)
        print_matrix[ghost_coor1[0]][ghost_coor1[1]] = ghost
        now_coor = next_coor.copy()
        return now_coor, finish

    elif next_coor == ghost_coor2:
        print(f'\n{bcolors.WARNING}BUUUU !!! 👻 El fantasmico te retiene y debes superar 2 preguntas para entrar 👻{bcolors.ENDC}\n')
        time.sleep(2)
        times(2)
        print(f'\n{bcolors.OKGREEN}Puedes entrar en la habitación{bcolors.ENDC}\n')
        time.sleep(2)
        print_matrix[ghost_coor2[0]][ghost_coor2[1]] = ghost
        now_coor = next_coor.copy()
        return now_coor, finish
        

    elif next_coor == lolli_coor:
        times(1)
        foo = '#'
        print(f'{bcolors.OKGREEN}{foo*9:68}{foo*9}{bcolors.ENDC}')
        print(f'{bcolors.OKGREEN}{foo*9:68}{foo*9}{bcolors.ENDC}')
        print(f'{bcolors.OKGREEN}{foo*9} 🍭 Genial!! Has encontrado la habitación de los dulces 🍭 {foo*9}{bcolors.ENDC}')
        print(f'{bcolors.OKGREEN}{foo*9:68}{foo*9}{bcolors.ENDC}')
        print(f'{bcolors.OKGREEN}{foo*9:68}{foo*9}{bcolors.ENDC}')
        time.sleep(2)
        print_matrix[lolli_coor[0]][lolli_coor[1]] = lollipop
        now_coor = next_coor.copy()
        finish = 'lollipop'
        return now_coor, finish
        
    else:
        times(1)
        print(f'\n{bcolors.OKGREEN}Puedes entrar en la habitación{bcolors.ENDC}\n')
        time.sleep(2)
        print_matrix[next_coor[0]][next_coor[1]] = ok
        now_coor = next_coor.copy()
        return now_coor, finish
        

def times(i:int):
    while i != 0:
        eval_question()
        i -= 1

def eval_question():
    n1 = random.randrange(3,10)
    n2 = random.randrange(3,10)

    answer_input = input(f'\n{bcolors.OKBLUE}¿Cuánto es {n1} x {n2}? = {bcolors.ENDC}')
    answer = (n1*n2)
    
    if answer_input.isnumeric() and int(answer_input) == answer:
        print(f'\n{bcolors.OKGREEN}Correcto!!\n {bcolors.ENDC}')
    else: 
        print(f'\n{bcolors.FAIL} ❌ Lo siento respuesta incorrecta, es {answer}, prueba otra vez{bcolors.ENDC}')
        times(1)


try:
    intro()
    row, column = random_room()
    door_coor, lolli_coor, ghost_coor1, ghost_coor2 = paint_game(row, column)
    now_coor = paint_matrix(door_coor)
    while finish == '':
        key = status()
        while key == None:
            key = status()
        next_coor = move_status(key)
        forbidden(key)
        now_coor, finish = wich_question(finish)
        paint_matrix(door_coor)
    
except KeyboardInterrupt:
    print('\nbye!!\n')    
    SystemExit

    