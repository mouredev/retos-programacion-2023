import time

def reto(inicio:int,tiempo:int):

	if (inicio <= 0 or tiempo <= 0):
		return None

	for i in range(inicio,-1,-1):
		print(i)
		time.sleep(tiempo)

reto(5,2)