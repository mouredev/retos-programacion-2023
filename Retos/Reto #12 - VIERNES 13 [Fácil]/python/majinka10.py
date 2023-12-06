from datetime import datetime

meses={'Enero':'01','Febrero':'02','Marzo':'03','Abril':'04','Mayo':'05'
       ,'Junio':'06','Julio':'07','Agosto':'08','Septiembre':'09','Octubre':'10','Noviembre':'11','Diciembre':'12'}

def viernes13(mes:str,año):
       date_str=f'{13}/{meses[mes]}/{año}'
       date = datetime.strptime(date_str, '%d/%m/%Y')
       return True if date.strftime('%A') == 'Friday' else False
       
print(viernes13('Enero',2023))
print(viernes13('Febrero',2020))
