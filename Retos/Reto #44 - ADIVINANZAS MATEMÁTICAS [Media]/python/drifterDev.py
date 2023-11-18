import time
import random

def nums(level):
  if level % 2 == 0:
    return [random.randint(0, 10**(level//2 +1) - 1), random.randint(0, 10**(level//2) - 1)]
  else:
    potencia = 10**((level+1)//2) - 1
    return [random.randint(0, potencia), random.randint(0, potencia)]
  
def operacion(num1, num2, op, res):
  try:
    res = int(res)
    if res == num1+num2 and op == "+":
      return True
    elif res == num1-num2 and op == "-":
      return True
    elif res == num1*num2 and op == "*":
      return True
    elif res == num1//num2 and op == "/":
      return True
    else:
      print("\nRespuesta incorrecta")
  except:
    print("\nEntrada no valida")
  return False

def main():
  ops = ["+", "-", "*", "/"]
  level = 1
  aciertos = 0
  print("Bienvenido a la prueba de matematicas")
  print("Las operaciones se resolveran en menos de 3 segundos y las divisiones seran enteras\n")
  print("Nivel de dificultad:",(level),"\n")
  while True:
    num1, num2 = nums(level)
    op = random.choice(ops)
    if op == "/" and num2 == 0:
      num2 = 1
    tiempo = time.time()
    res = input(str(num1)+" "+op+" "+str(num2)+" = ")
    if time.time() - tiempo > 3:
      print("Se acabó el tiempo")
      break
    if operacion(num1, num2, op, res):
      aciertos += 1
    else:
      break
    if aciertos % 5 == 0:
      level += 1
      print("\nNivel de dificultad:",(level),"\n")


  print("Aciertos:",aciertos)

if __name__ == "__main__":
  main()
