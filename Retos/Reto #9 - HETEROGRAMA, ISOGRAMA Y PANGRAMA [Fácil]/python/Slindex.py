import string as sg

def es_pangrama():
    frase = input('Por favor ingresa una palabra o frase ').lower()

    abecedario = []

    for letra in frase:
        if letra not in abecedario:
            abecedario.append(letra)

    for sym in sg.punctuation:
        if sym in abecedario:
            abecedario.remove(sym)
    if ' ' in abecedario:
        abecedario.remove(' ')

    if len(abecedario) == 33:
        return True
    else:
        return False

def es_heterograma():
    frase = input('Por favor ingresa una palabra o frase ').lower()
    resumen = []
    visto = []

    for sym in sg.punctuation:
        visto.append(sym)
    visto.append(' ')

    for letra in frase:
        if letra not in visto:
            visto.append(letra)
            cuenta = 0
            for i in range(len(frase)):
                if letra == frase[i]:
                    cuenta += 1
            resumen.append(cuenta)

    for num in resumen:
        if num != 1:
            return False
    
    return True

def es_isograma():
    frase = input('Por favor ingresa una palabra o frase ').lower()
    resumen = []
    visto = []

    for sym in sg.punctuation:
        visto.append(sym)
    visto.append(' ')

    for letra in frase:
        if letra not in visto:
            visto.append(letra)
            cuenta = 0
            for i in range(len(frase)):
                if letra == frase[i]:
                    cuenta += 1
            resumen.append(cuenta)

    for num in resumen:
        if num == 1 or num != resumen[0]:
            return False
    
    return True

opcion = int(input('''
Por favor elija una de las siguientes opciones:

(1) ¿Es pangrama?
(2) ¿Es heterograma?
(3) ¿Es isograma?
                   
'''))

if opcion == 1:
    if es_pangrama():
        print('True!')
    else:
        print('False!')
elif opcion == 2:
    if es_heterograma():
        print('True!')
    else:
        print('False!')
elif opcion == 3:
    if es_isograma():
        print('True!')
    else:
        print('False!')
else:
    print('Por favor escoja una opción valida!')