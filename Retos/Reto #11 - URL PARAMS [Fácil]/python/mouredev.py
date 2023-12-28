import re

url = "https://retosdeprogramacion.com?year=2023&challenge=0&languaje=python"

components = url.split("&")

for component in components:
    if "=" in component:
        param = component.split("=")
        if len(param) == 2 and param[1] != "":
            print(param[1])

# Solución con una expresión regular
regex = r"=([a-zA-Z0-9._%-]+)"
params = re.findall(regex, url)
print(params)
