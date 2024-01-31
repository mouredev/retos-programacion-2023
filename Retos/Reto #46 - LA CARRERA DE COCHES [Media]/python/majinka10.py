import random, time

def pre_carrera(longitud: int):
    pista_uno = ['🏁']
    pista_dos = ['🏁']

    for _ in range(longitud):
        pista_uno.append('_')
        pista_dos.append('_')

    pistas = [pista_uno, pista_dos]
    
    for pista in pistas:
        numero_arboles = random.choice(range(1,4))
        while numero_arboles > 0:
            posicion_aleatoria = random.randint(1, len(pista))
            pista.insert(posicion_aleatoria, '🌲')
            numero_arboles -= 1

    pista_uno.append('🚙')
    pista_dos.append('🚗')

    return pista_uno, pista_dos


def carrera(pista_uno, pista_dos):

    chocado_uno = False
    chocado_dos = False
    print(''.join(pista_uno))
    print(''.join(pista_dos))
    time.sleep(2)


    while True:
        try:
            posicion_uno = pista_uno.index('🚙')
        except:
            posicion_uno = pista_uno.index('💥')
        pos_final_uno = posicion_uno - random.choice(range(1,4))
        try:
            posicion_dos = pista_dos.index('🚗')
        except:
            posicion_dos = pista_dos.index('💥')
        pos_final_dos = posicion_dos - random.choice(range(1,4))

        if pos_final_uno <= 0 and pos_final_dos <= 0 and not (chocado_dos and chocado_uno):
            pista_uno.pop(posicion_uno)
            pista_uno.insert(posicion_uno, '_')
            pista_uno.pop(0)
            pista_uno.insert(0, '🚙')
            pista_dos.pop(posicion_dos)
            pista_dos.insert(posicion_dos, '_')
            pista_dos.pop(0)
            pista_dos.insert(0, '🚗')
            print(''.join(pista_uno))
            print(''.join(pista_dos))
            return 'Empate!'
        else:
            if pos_final_uno <= 0 and not chocado_uno:
                pista_uno.pop(posicion_uno)
                pista_uno.insert(posicion_uno, '_')
                pista_uno.pop(0)
                pista_uno.insert(0, '🚙')
                print(''.join(pista_uno))
                print(''.join(pista_dos))
                return 'El auto 🚙 ha ganado.'
            elif pista_uno[pos_final_uno] != '🌲' and not chocado_uno:
                pista_uno.pop(posicion_uno)
                pista_uno.insert(posicion_uno, '_')
                pista_uno.pop(pos_final_uno)
                pista_uno.insert(pos_final_uno, '🚙')
            elif pista_uno[pos_final_uno] == '🌲' and not chocado_uno:
                pista_uno.pop(posicion_uno)
                pista_uno.insert(posicion_uno, '_')
                pista_uno.pop(pos_final_uno)
                pista_uno.insert(pos_final_uno, '💥')
                chocado_uno = True
            else:
                pista_uno.pop(posicion_uno)
                pista_uno.insert(posicion_uno, '🚙')
                chocado_uno = False

            if pos_final_dos <= 0 and not chocado_dos:
                pista_dos.pop(posicion_dos)
                pista_dos.insert(posicion_dos, '_')
                pista_dos.pop(0)
                pista_dos.insert(0, '🚗')
                print(''.join(pista_uno))
                print(''.join(pista_dos))
                return 'El auto 🚗 ha ganado.'
            elif pista_dos[pos_final_dos] != '🌲' and not chocado_dos:
                pista_dos.pop(posicion_dos)
                pista_dos.insert(posicion_dos, '_')
                pista_dos.pop(pos_final_dos)
                pista_dos.insert(pos_final_dos, '🚗')
            elif pista_dos[pos_final_dos] == '🌲' and not chocado_dos:
                pista_dos.pop(posicion_dos)
                pista_dos.insert(posicion_dos, '_')
                pista_dos.pop(pos_final_dos)
                pista_dos.insert(pos_final_dos, '💥')
                chocado_dos = True
            else:
                pista_dos.pop(posicion_dos)
                pista_dos.insert(posicion_dos, '🚗')
                chocado_dos = False
        
        print(''.join(pista_uno))
        print(''.join(pista_dos))
        time.sleep(2)

pista_uno, pista_dos = pre_carrera(4)
print(carrera(pista_uno, pista_dos))