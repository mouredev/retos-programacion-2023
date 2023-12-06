import time

def cuenta_atras(inicio, segundos):
  if not isinstance(inicio, int) or not isinstance(segundos, int):
    raise ValueError("Ambos parametros deben ser numeros enteros")
    
  if inicio <= 0 or segundos <= 0:
    raise ValueError("Ambos parametros deben ser numeros enteros positivos")
  
  while inicio > 0:
    print(inicio)
    time.sleep(segundos)
    inicio -= 1
  
  
try:
  inicio = int(input("ingrese el numero incial de la cuenta atras: "))
  intervalo = int(input("Ingrese los segundos entre cada cuenta: "))
  cuenta_atras(inicio, intervalo)
except ValueError as e:
  print("Error: ", e)