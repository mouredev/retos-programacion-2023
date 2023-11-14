def escalera(escalones:int):
    escalera_izquierda_a_derecha='_|'
    escalera_derecha_a_izquierda='|_'
    espacios=' '
    if escalones==0:
      print('__')
    elif escalones>0:
      for i in range(escalones):
          espacios+='  '
      print(espacios+'_')
      espacios=espacios.replace('  ','',1)
      escalera_izquierda_a_derecha=espacios+escalera_izquierda_a_derecha
      for j in range(escalones):
        print(escalera_izquierda_a_derecha)
        escalera_izquierda_a_derecha=escalera_izquierda_a_derecha.replace('  ','',1)
    else:
      print(espacios+'_')
      for i in range(escalones*-1):
          escalera_derecha_a_izquierda='  '+escalera_derecha_a_izquierda
          print(escalera_derecha_a_izquierda)

escalera(4)
escalera(-4)
escalera(0)