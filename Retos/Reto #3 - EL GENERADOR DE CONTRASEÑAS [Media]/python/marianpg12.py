import re
print(
"""
--------------------------------------------------------------------------------------------------------
Expresión regular para buscar una letra minúscula, una letra mayúscula, un dígito y un caracter especial
module re
--------------------------------------------------------------------------------------------------------
"""
)

def is_valid_password(password):
    # Expresión regular para buscar una letra minúscula, una letra mayúscula, un dígito y un caracter especial
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$#!%*?&]{8,16}$')
    if pattern.match(password):
        return True
    else:
        return False

def validar(pwd):
    if is_valid_password(pwd):
        print('Password Validado')
    else:
        print('Password invalido, debe contener: al menos una letra minúscula, una letra mayúscula, un dígito y un caracter especial')

pwd = "Gar8Bua20m#da!@a"
pwd1 = "KIssMe89!"

validar(pwd)
validar(pwd1)        
