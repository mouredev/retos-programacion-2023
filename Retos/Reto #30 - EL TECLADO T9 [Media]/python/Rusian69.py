# Los primeros dispositivos móviles tenían un teclado llamado T9
# con el que se podía escribir texto utilizando únicamente su
# teclado numérico (del 0 al 9).

# Crea una función que transforme las keystrokes del T9 a su
# representación con letras.

# - Debes buscar cuál era su correspondencia original.
# - Cada bloque de keystrokes va separado por un guión.
# - Si un bloque tiene más de un número, debe ser siempre el mismo.
# - Ejemplo:
#     Entrada: 6-666-88-777-33-3-33-888
#     Salida: MOUREDEV

teclado = {"1":[".",",","?","!"], "2":["a","b","c"], 
           "3":["d","f","g"], "4":["h","i","j"], 
           "5":["k","l","m"], "6":["n","o","p"], 
           "7":["q","r","s"], "8":["t","u","v"], 
           "9":["w","x","y","z"], "0": [" "]
           }

def keyboar_t9 (numb:str):
    try:
        actual_num = ""
        number_long = 0
        result = ""
        for index in numb:
            if index == "-":
                result += teclado[actual_num][number_long-1]
                number_long = 0
            else:
                actual_num = index
                number_long += 1
                index = ""
        if index == "":
            result += teclado[actual_num][number_long-1]
        return result
    except:
        return {"ERROR": "ERROR UNEPEXT"}

print(keyboar_t9("4-66-55-2"))
