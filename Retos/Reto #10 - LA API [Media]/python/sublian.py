#  * Llamar a una API es una de las tareas más comunes en programación.
#  *
#  * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
#  * resultado a través de la terminal. Para este ejemplo: Yahoo Finance
#  * Se obtiene un registro historico de los precios del oro/dolar en base a un año
#  * al final muestro el ultimo valor registrado en tiempo real
#  * Aquí tienes un listado de posibles APIs: 
#  * https://github.com/public-apis/public-apis

import yfinance as yf
import pandas as pd
import json, requests

def golddata():
    golddata= yf.Ticker("GC=F").history(period="1y")   
    print(golddata)
    print("Gold csv extraction Finished :)")

golddata()

gold = json.loads(requests.get("https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/XAU/USD").text)
data = gold[0]
dataextract = data["spreadProfilePrices"]
dataextract = dataextract[0]["ask"]
print(f"<Data>: Gold price {dataextract} <USD> in real time ")
