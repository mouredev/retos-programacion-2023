#/*
# * Escribe un programa que muestre por consola (con un print) los
# * números de 1 a 100 (ambos incluidos y con un salto de línea entre
# * cada impresión), sustituyendo los siguientes:
# * - Múltiplos de 3 por la palabra "fizz".
# * - Múltiplos de 5 por la palabra "buzz".
# * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
# */
contador = 1 #iniciamos contador. 
while contador <= 100: #contamos de 1 a 100 con un while porque me apetece
	if contador%3 == 0 and contador%5==0: # ¿es múltiplo de 15?
		print("fizzbuzz")
	elif contador%3 == 0: # ¿es múltiplo de 3?
		print("fizz")
	elif contador%5 == 0: # ¿es múltiplo de 5?
		print("buzz")
	else:
		print (contador)
	contador  +=1 #incrementa 1
print ("Hasta luegui") #despedida totalmente innecesaria
