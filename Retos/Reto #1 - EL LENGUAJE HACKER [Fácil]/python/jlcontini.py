# Reto #1 - Leet translator

def change_to_leet(original_string: str) -> str:
  
  leet_dict: dict = {"A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#",
                     "I": "1", "J": ",_|", "K": ">|", "L": "1", "M": "/\/\\", "N": "^/", "O": "0",
                     "P": "|*", "Q": "(_,)", "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "\/",
                     "W": "\/\/", "X": "><", "Y": "j", "Z": "2"}
  
  leet_string = ""
  upper_case_string = original_string.upper()
  
  for character in upper_case_string:
    if character in leet_dict:
      leet_string += leet_dict[character]
    else:
      leet_string += character
  
  return leet_string


def get_string() -> str:
  original_string = str(input("Ingresa el texto que quieras transformar a 'lenguaje hacker': \n"))
  return original_string


def show_results(original_string, leet_string):
  print(f"""
        Texto original ingresado:
        {original_string}
        
        Texto en formato leet:
        {leet_string}
        
        """)


def main():
  print("\n\nLEET: esto es una prueba")
  print(change_to_leet("LEET: esto es una prueba\n\n"))
  
  original_string = get_string()
  leet_string = change_to_leet(original_string)
  show_results(original_string, leet_string)
  
  print(f'\nResultado de la transformacion: \n{leet_string}\n')



if __name__ == "__main__":
  main()
