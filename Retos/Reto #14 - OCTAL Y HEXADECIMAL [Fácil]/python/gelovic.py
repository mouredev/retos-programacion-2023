def transformar(numero: int) -> str:
    hex = '0123456789ABCDEF'
    sistemas = {'hexadecimal': 16, 'octal': 8}
    
    for sis, num in sistemas.items():
        resultado = ''
        temp = int(numero)
        
        while temp >= num:
            resultado = hex[temp % num] + resultado
            temp //= num
        sistemas[sis] = hex[temp] + resultado
    
    return sistemas

print(transformar(255))