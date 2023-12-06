# Reto 30: El teclado T9
# by gerickt

# Usando diccionario
def t9_to_abc(x: str):
    result = ""
    keys = {"1": ",.?!",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": " ",}
    pulses = x.split("-")
    for pulse in pulses:
        x = len(pulse) - 1
        if 0 <= x < 3:
            letter = keys.get(pulse[0])
            result += letter[x]            
        else:            
            result = "Input erroneo."
            break
    return result.upper()

if __name__ == "__main__":
    input = "6-666-88-777-33-3-33-888"    
    print(f"Entrada: {input}")
    print("Salida: ",t9_to_abc(input))
    print("Salida: ",t9_to_abc("44-666-555-2"))
