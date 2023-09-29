from datetime import datetime

meses={'Enero':'01','Febrero':'02','Marzo':'03','Abril':'04','Mayo':'05'
       ,'Junio':'06','Julio':'07','Agosto':'08','Septiembre':'09','Octubre':'10','Noviembre':'11','Diciembre':'12'}

def viernes13(mes:str,año):
  try:
    date_str=f'{13}/{meses[mes]}/{año}'
    date = datetime.strptime(date_str, '%d/%m/%Y')
    return date.strftime('%A') == 'Friday'
  except:
    return False
       
def test_viernes13_true_date():
  assert viernes13('Enero',2023) 

def test_viernes13_false_date():
  assert not viernes13('Febrero',2020) 

def test_viernes13_invalid_year():
  assert not viernes13('Enero', -2023)
  assert not viernes13('Marzo', "-2020")
  assert not viernes13('Junio', "Juan")

def test_viernes13_invalid_month():
  assert not viernes13(12, 2020)
  assert not viernes13('dos', 2015)

def test_viernes13_invalid_data():
  assert not viernes13('Hola','Chao')