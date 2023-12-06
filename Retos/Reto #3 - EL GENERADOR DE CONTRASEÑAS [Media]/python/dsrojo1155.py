import argparse
import string
import random
# Autor DsRojo1155
parser = argparse.ArgumentParser(description="[+] Uso Passwords Generator")
parser.add_argument('-l', '--length',type=int, help='Determine the password length\n python3 .\passwords_generator.py -l 17')
parser.add_argument('-w', '--words', action='store_true', help="Specify if you want uppercase letters")
parser.add_argument('-d', '--digits', action='store_true', help="Specify if you want digits")
parser.add_argument('-s', '--symbols', action='store_true', help="Specify if you want symbols")
args = parser.parse_args()

def password_generate(length, characters):
    length = int(length)
    print("[+] Generating password")
    password = ""
    for i in range(length):
        password += random.choice(characters)

    print(f"[+] Generated password: {password}")

if __name__ == '__main__':
    # Validar que la longitud esté dentro de los límites
    if args.length and  args.length >= 8 and args.length <= 16 :
        print(f"Set the password length: {args.length}")

        # Verificar si se seleccionó alguna opción
        if not args.words and not args.digits and not args.symbols and args:
            print("Error: At least one option (words, digits, symbols) must be enabled.")
            exit(1)
        
        # Definir caracteres disponibles
        characters = ""
        if args.words:
            characters += string.ascii_uppercase
        if args.digits:
            characters += string.digits
        if args.symbols:
            characters += string.punctuation
        

    
        password_generate(args.length, characters)
    else:
        print("Error: Invalid length. Password length should be between 8 and 16.")
