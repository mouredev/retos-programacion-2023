import re

patron = re.compile(r'-?\d+(\.\d+)?\s*[+\-*/%]\s*-?\d+(\.\d+)?(?:\s*[+\-*/%]\s*-?\d+(\.\d+)?)?')

def evaluador(expresion:str):
	match = patron.search(expresion)
	if match:
		return True 
	else:
		return False
    

print(evaluador('5 + 6 / 7 - 4'))
print(evaluador('5 a 3'))
print(evaluador('3.2 % 3 + 5 - 3 / 2'))