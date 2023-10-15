def show(n:int)->None:
  print("Tabla del "+str(n))
  for i in range(1,11):
    print(str(n)+" x "+str(i)+" = "+str(n*i))
  print()

def main()->None:
  n=int(input("Ingrese un numero: "))
  show(n)
  # Casos de prueba
  # show(0)
  # show(1)
  # show(-2)
  # show(238945)

if __name__ == "__main__":
  main()
