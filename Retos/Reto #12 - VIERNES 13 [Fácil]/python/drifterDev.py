import datetime

ano, mes=input().split()
ano=int(ano)
mes=int(mes)
bool=datetime.date(ano, mes, 13).weekday()==4
if bool:
    print("True")
else:
    print("False")
