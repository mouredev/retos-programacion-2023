import secrets


class gen_pass_config():
    '''
    Class gen_pass_config
    '''

    def __init__(self, long_char: int = 8, with_upper: bool = False, with_number: bool = False, with_symn: bool = False) -> None:
        '''
        Al instanciar el objeto se configuran tipo de password se genera
            long_char: Determina el largo de la clave. Debe ser un valor entre 8 y 16 caracteres. 
            with_upper: Determina si en la tabla de caracters a utilizar se incluye los caracteres alfabeticos en mayuscula
            with_numbre: Determina si en la tabla de caracteres a utilizar se incluye los caracteres numericos.
            with_sym : Determina si en la tabla de caracteres a utilizar se incluye los caracteres de simbolos.

            El objeto utiliza la tabla ascii para calcular los caracteres. Se tiene en cuenta los caracteres del valor igual a 32 al 126. 
        '''

        self.long_char = long_char
        self.with_upper = with_upper
        self.with_number = with_number
        self.with_symn = with_symn

    def get_random_char(self) -> str:
        '''
        Se genera un caracter alfabetico de manera aleatoria. Se evalua si la configuración incluye los caracteres en mayuscula.
        Si incluye mayuscula, primer se selecciona entre ambas tabla ( minuscula y mayuscula ) y a partir de allí determina un valor aleatorio entre:
            minuscula : entre 97 y 122
            mayuscula : entre 65 y 90
        '''
        if self.with_upper == True:
            # si el valor 0 -> se seleecionar un caracter en minuscula
            if secrets.randbelow(2) == 0:
                char_random = chr(secrets.randbelow(25) + 97)
            else:
                char_random = chr(secrets.randbelow(25) + 65)
        else:
            # opción por defecto, si es SIN mayuscula, entonces devuelve una minuscula
            char_random = chr(secrets.randbelow(25) + 97)
        return char_random

    def get_random_int(self) -> str:
        '''
        Se genera un caracter numerico de manera aleatoria. Se utiliza la tabla ascii para generar el valor, donde los numeros van de la posición 48 a la 57.
        '''
        return chr(secrets.randbelow(10) + 48)

    def get_random_symn(self) -> str:
        '''
        Se genera un caracter de simbolo de manera aleatoria. Se utiliza la tabla ascii para generar el valor, donde los numeros van de la posición:
            32 al 47 ( total de simbolos : 16 )
            58 al 64 ( total de simbolos : 7 )
            91 al 96 ( total de simbolos : 6 )
            123 al 126 ( total de simbolos : 4 )

        Como existen 4 porciones dentro de la tabla, se calcula un valor entre 0 y 33. Dependiendo el valor se sabe que tabla va utilizar:
            0 - 15 : entre el rango de 32 y 47
            16 - 22 : entre el rango 58 y 64 
            23 - 28 : entre el rango 91 y 96
            29 - 33 : entre el rango 123 y 126

        '''
        number_char = secrets.randbelow(34)

        if 0 <= number_char <= 15:
            char_random = chr(number_char + 32)   # 0 - 15

        elif 15 < number_char <= 22:
            char_random = chr(number_char + 58 - 16)  # 16 - 22

        elif 22 < number_char <= 28:
            char_random = chr(number_char + 91 - 23)

        elif 28 < number_char:
            char_random = chr(number_char + 123 - 29)

        return char_random

    def calc_table_random(self):
        ''' 
            Se genera una lista con la referencia a las funciones para determinar que tabla de caracteres utilizaremos para genera el password
        '''
        self.table_random = []

        self.table_random.append(self.get_random_char)

        if self.with_number:
            self.table_random.append(self.get_random_int)

        if self.with_symn:
            self.table_random.append(self.get_random_symn)

    def get_random_pass(self) -> str:
        '''
        Encargado de recorrer la tabla de caracteres a utilizar y calcular 
        '''

        password = ""
        count_table = len(self.table_random)
        count = 0
        while count <= self.long_char:
            if count_table == 0:
                number_table = 0
            else:
                number_table = secrets.randbelow(count_table)
            password = password + self.table_random[number_table]()
            count += 1

        return password


if __name__ == '__main__':
    long_char = int(input('Ingrese el largo de la clave (entre 8 y 16 caracteres ) '))
    with_upper = str( input('Ingrese si desea incluir mayuscula : (True/False) ')).lower() == 'true'
    with_number = str( input('Ingrese si desea incluir numeros : (True/False) ')).lower() == 'true'
    with_symn = str(input('Ingrese si desea incluir simbolo : (True/False) ')).lower() == 'true'

    generador = gen_pass_config(long_char, with_upper, with_number, with_symn)

    generador.calc_table_random()
    print(generador.get_random_pass())
