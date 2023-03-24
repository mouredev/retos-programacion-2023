# /*
# * Llamar a una API es una de las tareas más comunes en programación.
# *
# * Implementa una llamada HTTP a una API(la que tú quieras) y muestra su
# * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
# *
# * Aquí tienes un listado de posibles APIs:
#  * https: // github.com/public-apis/public-apis
#  */
from datetime import datetime
import json
import requests


# /**
# * Ejemplo de llamada a la API de la NASA para obtener las fotos de Marte del Curiosity
# * filtradas por fecha de la tierra
# * Response:
#     2023-03-12 00: 00: 00.000: https: // mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03767/opgs/edr/fcam/FLB_731921172EDR_F1001084FHAZ00337M_.JPG
#     2023-03-12 00: 00: 00.000: https: // mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03767/opgs/edr/fcam/FRB_731921172EDR_F1001084FHAZ00337M_.JPG
#     2023-03-12 00: 00: 00.000: https: // mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03767/opgs/edr/rcam/RRB_731921206EDR_F1001084RHAZ00337M_.JPG
#     2023-03-12 00: 00: 00.000: https: // mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03767/opgs/edr/rcam/RLB_731921206EDR_F1001084RHAZ00337M_.JPG
#  */

API_KEY = 'DEMO_KEY'
URL_PHOTOS = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

# /**
# * Funcion para obtener las fotos de Marte del Curiosity filtradas por fecha de la tierra
# * @ param earthDate fecha de la tierra
# * @ return lista de fotos de Marte
# */
def get_photos(earth_date):
    url = f"{URL_PHOTOS}?earth_date={earth_date}&api_key={API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            body = json.loads(response.content)
            photos = body['photos']
            for photo in photos:
                print(photo['earth_date'] + ' - ' + photo['img_src'])

    except Exception as e:
        print(e)
        return []



get_photos('2015-6-3')