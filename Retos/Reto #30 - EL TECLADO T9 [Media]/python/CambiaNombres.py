'''
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
'''
# Crea una función que transforme las pulsaciones del T9 a su representación con letras.
def t9(entrada: str) -> str:
    
  salida = ""

# - Debes buscar cuál era su correspondencia original.
  teclas = [[".", ",", "'", "1"], ["a", "b", "c", "2"], ["d", "e", "f", "3"], 
            ["g", "h", "i", "4"], ["j", "k", "l", "5"], ["m", "n", "o", "6"],
            ["p", "q", "r", "s", "7"], ["t", "u", "v", "8"], ["w", "x", "y", "z", "9"],
            [" ", "0"]]
  
  block = ""

  if entrada == "": # Si está vacía
    return salida # Se retorna ""
  else:
# - Cada bloque de pulsaciones va separado por un guión.
    lista = entrada.split("-") # Se guarda en una lista donde se divide la entrada por cada "-"
    for block in lista:
      added = False
      if block.isdigit(): # Si es un dígito
        for number in block:
# - Si un bloque tiene más de un número, debe ser siempre el mismo.
          if len(block) == block.count(str(number)): # Si son iguales todos los digitos
            if not added: # Si no ha sido agregado
              salida += teclas[int(number) - 1][len(block) - 1]
              added = True
          else:
            return ""
      else:
        return ""
      
    return salida
'''
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
'''
print(t9("6-666-88-777-33-3-33-888"))
print(t9("44-666-555-2")) # Salida = hola