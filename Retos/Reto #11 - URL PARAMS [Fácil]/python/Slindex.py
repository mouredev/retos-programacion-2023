url = 'https://retosdeprogramacion.com/?year=2023&challenge=0&prueba=hola'

split = url.split('=')
paramsv = []

for string in split:
    if '&' in string:
        split2 = string.split('&')
        paramsv.append(split2[0])
paramsv.append(split[-1])

print(paramsv)