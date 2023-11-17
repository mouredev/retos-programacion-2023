import random

def simulador_clima(dias: int):
    temp_ini = int(input("Digita la temperatura inicial: "))
    prob_lluv = int(input("Digita el % de probabilidad de lluvia: "))
    dias_luvia = 0
    temp_min = 100
    temp_max = 0
    lluvia = "No"

    for dia in range(0, dias):
        prob_tem = random.randint(0,10) == 1
        aum_o_dis = random.randint(1,2)
        
        if prob_tem:    
            if aum_o_dis == 1:
                temp_ini += 2
            else:
                temp_ini -= 2
        if temp_ini > 25:
            if prob_lluv >= 100:
                prob_lluv = 100
            elif prob_lluv < 100:
                restante = 100 - prob_lluv
                prob_lluv += restante
            else: 
                prob_lluv += 20
        if prob_lluv == 100:
            temp_ini -= 1
            lluvia = "Si"
        if temp_ini < 5:
            if prob_lluv <= 0:
                prob_lluv = 0
            else:   
                prob_lluv -= 20
        if temp_ini > temp_max:
            temp_max = temp_ini
        if temp_ini < temp_min:
            temp_min = temp_ini
        if prob_lluv < 100:
            lluvia = "No"
        if lluvia == "Si":
            dias_luvia += 1
        print(f"Dia: {dia} , Temperatura: {temp_ini} ,probabilidad de Lluvia: {lluvia, prob_lluv}")
    print(f"Temperatura max: {temp_max}")
    print(f"Temperatura min: {temp_min}")
    print(f"Dias de Luvia: {dias_luvia}")
    

simulador_clima(10)