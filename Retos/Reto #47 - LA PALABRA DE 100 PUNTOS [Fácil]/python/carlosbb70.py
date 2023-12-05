

abecedario = {
   'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
   'k':11, 'l':12, 'm':13, 'n':14, 'ñ':15, 'o':16, 'p':17, 'q':18, 'r':19,
   's':20, 't':21, 'u':22, 'v':23, 'w':24, 'x':25, 'y':26, 'z':27
}

while True:
	palabra = input("Por favor introduzca una palabra: ")
	palabra = palabra.lower()
	suma = 0
	for char in palabra:
		for clave in abecedario:
			if char == clave:
				suma += abecedario [clave]
				print(clave, ' -> ', abecedario[clave])
	print("La palabra ", palabra,  " suma ", suma, " puntos.")
	if suma == 100:
		print("Lo lograstes la palabra suma 100 puntos.")
		break

		
			
    
