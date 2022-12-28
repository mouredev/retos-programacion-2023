
numero = 1
my_list =[]
while numero <=100:
    
    if numero % 3==0 and numero % 5 ==0:

        my_list.append('fizzbuzz')
        numero += 1
    elif numero % 5 ==0:

        my_list.append('buzz')
        numero += 1
    elif numero % 3 ==0:
        
        my_list.append('fizz')
        numero += 1
    else:
        
        my_list.append(numero)
        numero += 1

for element in my_list:
    print(element)