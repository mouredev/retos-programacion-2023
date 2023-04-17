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

# ------------------------------------------------------------

def dec2any(numero, divisor):
    hex = '0123456789ABCDEF'
    return hex[numero] if numero < divisor else dec2any(numero // divisor, divisor) + hex[numero % divisor]

def transformar2(numero: int) -> str:
    sistemas = {'hexadecimal': 16, 'octal': 8}
    return {sis: dec2any(int(numero), num) for sis, num in sistemas.items()}

print(transformar(255))
print(transformar2(255))