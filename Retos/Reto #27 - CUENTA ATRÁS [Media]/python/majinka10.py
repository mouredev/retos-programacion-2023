import time

def cuenta_atras(inicio:int,intervalo:int):
  while inicio:
    m, s = divmod(inicio, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m,s)
    print(min_sec_format)
    time.sleep(intervalo)
    inicio-=1
  print('Cuenta atrás finalizada!')

cuenta_atras(10,1)
cuenta_atras(5,2)