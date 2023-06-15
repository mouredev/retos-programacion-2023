#!/usr/bin/python3
# Reto #10: La API
#### Dificultad: Media | Publicación: 06/03/23 | Corrección: 13/03/23

## Enunciado

'''
/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 */
'''
# curl -X GET "http://dataservice.accuweather.com/currentconditions/v1/locationKey?apikey=lNMqkrONMLGZMvBf8jO3NMU6wLRO5458&language=en-us&details=true"
import requests

class Weather_BA(object):
    __URL__     = 'http://dataservice.accuweather.com'
    __PATH__    = 'currentconditions/v1/7894'
    __APIKEY__  = '?apikey=lNMqkrONMLGZMvBf8jO3NMU6wLRO5458&language=en-us&details=true'  
    
    def  __init__(self,country_code:str,apikey:str)->None:
        self.__CODE_COUNTRY__ = country_code
        self.__PATH__   = f'/currentconditions/v1/{country_code}'
        self.__APIKEY__ = {'apikey' : apikey, 'language':'en-us', 'details' : 'true'}
        
    def get_current(self)-> str:
        
        call_api = requests.get(self.__URL__+self.__PATH__, params=self.__APIKEY__)
        
        return call_api.json()
    
    def get_location(self)-> str:
        
        call_api = requests.get(self.__URL__+ f'/locations/v1/{self.__CODE_COUNTRY__}' , params=self.__APIKEY__)
        
        return call_api.json()
    
    def __str__(self)-> str:
        
        json_text       =  self.get_location()
        city_name       =  f'Ubicación : {json_text["LocalizedName"]}'
        
        
        json_text       =  self.get_current()
        datetime        = f"Fecha : Hora :\t{json_text[0]['LocalObservationDateTime']}"
        temp_current    = f"Temperatura : {json_text[0]['Temperature']['Metric']['Value']} {json_text[0]['Temperature']['Metric']['Unit']}"
        temp_realfeel   = f"Sens. Termica : {json_text[0]['RealFeelTemperature']['Metric']['Value']} {json_text[0]['RealFeelTemperature']['Metric']['Unit']}"
        relative_humidity = f"Humedad Relativa : {json_text[0]['RelativeHumidity']}% "
        wind            = f"Viento Direción : {json_text[0]['Wind']['Direction']['Localized']} ({json_text[0]['Wind']['Direction']['Degrees']}) - Velocidad :{json_text[0]['Wind']['Speed']['Metric']['Value']} {json_text[0]['Wind']['Speed']['Metric']['Unit']}"
        uv_level        = f"Nivel UV : {json_text[0]['UVIndexText']} ( {json_text[0]['UVIndex']} )"
        visibility      = f"Visibilidad : {json_text[0]['Visibility']['Metric']['Value']}{json_text[0]['Visibility']['Metric']['Unit']}"
        pressure        = f"Visibilidad : {json_text[0]['Pressure']['Metric']['Value']}{json_text[0]['Pressure']['Metric']['Unit']}"
        
        return str( city_name + '\n'+ 
                    datetime + '\n' + 
                    temp_current + '\t' + temp_realfeel + '\n' + 
                    relative_humidity + '\n' + wind + '\n' + 
                    uv_level + '\n' +
                    visibility + '\n' + 
                    pressure)
 
if __name__ == '__main__':
    
    AA = Weather_BA('7894', 'lNMqkrONMLGZMvBf8jO3NMU6wLRO5458')
    print(AA)
    
