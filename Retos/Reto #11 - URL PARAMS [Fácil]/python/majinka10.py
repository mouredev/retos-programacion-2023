def params(url):
    text=url.split('?')
    param=text[1].split('&')
    parametros=[]
    
    for i in param:
        param=i.split('=')
        parametros.append(param[1])
        
    print(parametros)

params('https://retosdeprogramacion.com?year=2023&challenge=0')