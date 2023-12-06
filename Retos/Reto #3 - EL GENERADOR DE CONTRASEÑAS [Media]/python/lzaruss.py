import random
import argparse

parser = argparse.ArgumentParser(add_help=False, description="")
parser.add_argument('-f', '--file', help="Name of the output file (if not exist, the script will create it)")
parser.add_argument('-l', '--lenght', type=int, required=True, help="Lenght of password")
parser.add_argument('-c', '--count', type=int, required=True, help="Count of passwords")
parser.add_argument('-q', '--quiet', action='store_true', help="Mode if you only want view at console and not save to the file")
parser.add_argument('-h', '--help', action='help', help="Password Generator [-h to help]")
args = parser.parse_args()

chars = [
    "abcdefghijklmnopqrstuvwxyz",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "0123456789",
    "!@#$%*£_"
]

choice = random.randint(0, 3)
chars[choice]

def random_word(len:int, quiet:bool):
  word = ""
  for i in range(len):
    choice = random.randint(0, 3)
    let = chars[choice]
    word += random.choice(let)
  if not quiet:
    writePWD(word)
  else:
    print(word)

def writePWD(pwd:str):
  file = args.file
  if args.file is None:
    file = 'temp.txt'
  with open(file, 'a', encoding='utf-8') as f:
    f.write(f'{pwd}\n')

if __name__ == '__main__':
  for i in range(args.count):
    random_word(args.lenght, args.quiet)