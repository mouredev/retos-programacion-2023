import string
import random


def generate_password():
    password_length = get_password_length()
    password_letters = get_password_letters()
    password_numbers = get_password_numbers()
    password_symbols = get_password_symbols()
    password_characters = (
        password_letters + password_letters + password_numbers + password_symbols
    )

    password = "".join(
        generate_random_character(password_characters) for i in range(password_length)
    )

    return password


def get_password_length():
    SHOWN_USER_PHRASE = (
        "Introduce la longitud de la contraseña (longitud entre 8 y 16): "
    )
    password_length = 8
    user_enter_value = get_user_enter_value(SHOWN_USER_PHRASE)

    while not check_user_password_length_enter_value(user_enter_value):
        user_enter_value = get_user_enter_value(SHOWN_USER_PHRASE)

    password_length = int(user_enter_value)

    return password_length


def get_user_enter_value(shown_user_phrase):
    return input(shown_user_phrase)


def check_user_password_length_enter_value(user_enter_value):
    is_correct_value = True

    try:
        is_value_number(user_enter_value)
        check_number_range(int(user_enter_value))
    except ValueError as error:
        print(error)
        is_correct_value = False

    return is_correct_value


def is_value_number(user_enter_value):
    try:
        int(user_enter_value)
    except ValueError:
        raise ValueError("Debes introducir un valor númerico entero.")


def check_number_range(number_value):
    MAX_NUMBER_VALUE = 16
    MIN_NUMBER_VALUE = 8

    if not (MIN_NUMBER_VALUE <= number_value <= MAX_NUMBER_VALUE):
        raise ValueError(
            f"El número debe estar comprendido entre el {MIN_NUMBER_VALUE} y el {MAX_NUMBER_VALUE}, ambos incluidos."
        )


def get_password_letters():
    SHOWN_USER_PHRASE = "¿Quieres que la contraseña tenga mayúsculas? Y/N: "
    password_letters = string.ascii_lowercase
    user_enter_value = get_user_enter_value(SHOWN_USER_PHRASE)

    while not check_is_enter_value_is_boolean(user_enter_value):
        user_enter_value = get_user_enter_value(SHOWN_USER_PHRASE)

    has_uppercase = user_enter_value == "Y"
    if has_uppercase:
        password_letters = string.ascii_letters

    return password_letters


def check_is_enter_value_is_boolean(user_enter_value):
    is_correct_value = True
    correct_value_group = ["Y", "N"]

    try:
        if not user_enter_value in correct_value_group:
            raise ValueError("Error, debes introducir o sí (Y) o no (N).")
    except ValueError as error:
        print(error)
        is_correct_value = False

    return is_correct_value


def get_password_numbers():
    SHOWN_USER_PHRASE = "¿Quieres que la contraseña tenga números? Y/N: "
    password_numbers = ""
    user_enter_value = get_user_enter_value(SHOWN_USER_PHRASE)

    while not check_is_enter_value_is_boolean(user_enter_value):
        user_enter_value = get_user_enter_value(SHOWN_USER_PHRASE)

    has_numbers = user_enter_value == "Y"
    if has_numbers:
        password_numbers = string.digits

    return password_numbers


def get_password_symbols():
    SHOWN_USER_PHRASE = "¿Quieres que la contraseña tenga símbolos? Y/N: "
    password_symbols = ""
    user_enter_value = get_user_enter_value(SHOWN_USER_PHRASE)

    while not check_is_enter_value_is_boolean(user_enter_value):
        user_enter_value = get_user_enter_value(SHOWN_USER_PHRASE)

    has_symbols = user_enter_value == "Y"
    if has_symbols:
        password_symbols = string.punctuation

    return password_symbols


def generate_random_character(password_characters):
    return random.choice(password_characters)


password = generate_password()
print(f"\nLa contraseña es: {password}")
