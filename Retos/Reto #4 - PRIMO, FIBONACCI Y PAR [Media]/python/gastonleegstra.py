def isprimo_fib_par(nro):
  return str(nro) +' '+ isprimo(nro)+', '+ isfib(nro) + ', '+ispar(nro)

'''Determina si es Fibonacci o no es Fibonacci'''
def isfib(nro):
    pre = 0
    post =1
    isfib='no es fibonacci'
    while (pre <= nro):
      if pre == nro:
        isfib = 'fibonacci'
      suma = pre + post
      pre = post
      post = suma
    return str(isfib)

'''Determina si es Par o Impar'''
def ispar(nro):
  ispar = 'es impar'
  if nro % 2 == 0: 
    ispar = 'es par'
  return str(ispar)

'''Determina si es Primo o no es Primo'''
def isprimo(nro):
  isprimo = 'es primo'
  if nro == 1 : 
    return str(isprimo)
  for i in range(2,nro):
    if (nro % i == 0):
      isprimo = 'no es primo'
  return str(isprimo)

print(isprimo_fib_par(2))
print(isprimo_fib_par(7))