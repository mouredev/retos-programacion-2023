for num in range(1, 101):
	if num % 3 == 0 and num % 5 == 0:
		print("fizzbuzz\n")
	elif num % 5 == 0:
		print("buzz\n")
	elif num % 3 == 0:
		print("fizz\n")
	else:
		print(num)
		print("") 
