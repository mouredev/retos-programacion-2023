
def check_string(sone: str, stwo:str) -> list:
    diffs = []

    one_list = [*sone]
    two_list = [*stwo]

    if len(one_list) == len(two_list):
        for index,char in enumerate(one_list):
            if char == two_list[index]:
                continue
            else:
                diffs.append(two_list[index])
        print(diffs)
        return diffs
    else:
        print(f'Ambas cadenas de texto deben ser iguales en longitud. En este caso, la primera cadena tenía {len(one_list)} y la segunda {len(two_list)}')
    

if __name__ == '__main__':
    check_string("hola","hoalii")
    check_string("hola","hola")
    check_string("Me llamo mouredev","Me llemo mouredov")
    check_string("Me llamo.Brais Moure","Me llamo brais moure")

