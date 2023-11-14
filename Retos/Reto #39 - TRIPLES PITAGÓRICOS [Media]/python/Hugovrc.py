def triples_pitagoricos(numero_max: int):
   for lado_a in range(1,numero_max+1):
      for lado_b in range(lado_a, numero_max+1):
         cuadrado_de_a_y_b = lado_a**2 + lado_b**2
         lado_c = int(cuadrado_de_a_y_b ** 0.5)
         if lado_c**2 == cuadrado_de_a_y_b and lado_c <= numero_max:
            print(f"({lado_a},{lado_b},{lado_c})")
      

triples_pitagoricos(10)
triples_pitagoricos(25)
