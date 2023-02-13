import random

char_dict = {
    "lower_case": ["abcdefghijklmnopqrstuvwxyz", True],
    "upper_case": ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", True],
    "number": ["0123456789", True],
    "symbol": ["~`!@#$%^&*()_-+={[}]|\\:;'<,>.?/" + '"', True]
}

type_dict = {
    0: "lower_case",
    1: "upper_case",
    2: "number",
    3: "symbol"
}


def generate_char() -> str:
    num = random.randint(0, 3)
    current = char_dict[type_dict[num]]
    if current[1]:
        return current[0][random.randint(0, len(current[0]) - 1)]
    else:
        return generate_char()


def generate_password(pass_len: int = 8) -> str:
    password = ""
    for cycle in range(password_length):
        password += generate_char()
    return password


def handle_input(inp: str) -> bool:
    if inp.lower() == "y":
        return True
    if inp.lower() == "n":
        return False


def menu(option: int):
    while True:
        if option == 1:
            selection = int(input("Longitud de la contraseña (8-16): "))
            if 8 <= selection <= 16:
                return selection
        if option == 2:
            selection = input("Incluir mayúsculas? (y/n): ")
            if selection.lower() in "yn":
                return handle_input(selection)
        if option == 3:
            selection = input("Incluir números? (y/n): ")
            if selection.lower() in "yn":
                return handle_input(selection)
        if option == 4:
            selection = input("Incluir símbolos? (y/n): ")
            if selection.lower() in "yn":
                return handle_input(selection)
        print("Debes ingresar una opción válida.")


password_length = menu(1)
char_dict["upper_case"][1] = menu(2)
char_dict["number"][1] = menu(3)
char_dict["symbol"][1] = menu(4)

# Generar varias opciones de contraseñas
for i in range(10):
    print(f"({i+1}) {generate_password(password_length)}")
