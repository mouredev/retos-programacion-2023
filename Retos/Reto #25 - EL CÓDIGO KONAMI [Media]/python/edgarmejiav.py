codigo_konami = ['arriba', 'arriba', 'abajo', 'abajo', 'izquierda', 'derecha', 'izquierda', 'derecha', 'B', 'A']

def validar_codigo_konami(entrada_usuario):
    return entrada_usuario == codigo_konami

def recibir_entrada_usuario():
    entrada = input("Ingrese el código Konami completo (separado por espacios): ").split()
    print(entrada)
    if validar_codigo_konami(entrada):
        print("¡Código Konami válido!")
    else:
        print("Código Konami inválido.")

recibir_entrada_usuario()

# input test: arriba arriba abajo abajo izquierda derecha izquierda derecha B A