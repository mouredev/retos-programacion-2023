from datetime import datetime

def generador_num_pseudoAleatorio():
    fecha = str(datetime.now(tz=None))
    microsegs = fecha.split(".")[1][:2]
    #if para incluir la posibilidad de que salga el 100
    return int(microsegs)+1 if int(microsegs) > 0 else microsegs

print(generador_num_pseudoAleatorio())
