"""/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */"""
from collections import Counter
import string


def ask_text():
    return str(input("Texto: ").lower())


def counter_and_check(text):
    counter_letters = Counter(text)
    heterograma = check_text_heterogram(counter_letters)
    isograma = check_text_isogram(counter_letters)
    pangrama = check_text_pangram(counter_letters)

    return (heterograma, isograma, pangrama)


def check_text_heterogram(counter):
    for value in counter.values():
        if value > 1:
            return False
    return True


def check_text_isogram(counter):
    value_global = 0
    counter_times = 0
    for value in counter.values():
        if value != value_global and counter_times == 0:
            value_global = value
            counter_times = 1
        elif value != value_global:
            return False
    return True


def check_text_pangram(counter):
    counter_times = 0
    for key in counter.keys():
        if key.isalpha():
            counter_times += 1
    if counter_times > 27:
        return True
    else:
        return False


def string_constructor(tupla):
    dict_string = {}
    counter = 0
    for value in tupla:
        if value == False and counter == 0:
            dict_string["heterograma"] = "no es un heterograma"
        elif value == True and counter == 0:
            dict_string["heterograma"] = "es un heterograma"
        elif value == False and counter == 1:
            dict_string["isograma"] = "no es un isograma"
        elif value == True and counter == 1:
            dict_string["isograma"] = "es un isograma"
        elif value == False and counter == 2:
            dict_string["pangrama"] = "no es un pangrama"
        elif value == True and counter == 2:
            dict_string["pangrama"] = "es un pangrama"
        counter += 1
    print(
        f"Tu frase {dict_string['heterograma']}, {dict_string['isograma']} y {dict_string['pangrama']}."
    )


def main():
    tupla = counter_and_check(ask_text())
    string_constructor(tupla)


if __name__ == "__main__":
    main()
