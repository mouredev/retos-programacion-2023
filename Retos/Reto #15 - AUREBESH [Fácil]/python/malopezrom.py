# /*
# * Crea una función que sea capaz de transformar Español al lenguaje básico del universo
# * Star Wars: el "Aurebesh".
# * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
# * - También tiene que ser capaz de traducir en sentido contrario.
# *
# * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
# *
# * ¡Que la fuerza os acompañe!
# */


from enum import Enum
import re

# /**
# * Enumerado que representa el tipo de traducción
# */
class AurebeshTranslation(Enum):
    AUREBESH2SPANISH = 0
    SPANISH2AUREBESH = 1


# /**
# * Función que traduce de español a aurebesh y viceversa
# * @ param text Texto a traducir
# * @ param translation Tipo de traducción
# */

def translate(text,translation):
    aurebesh_map = {
        "a": "aurek",
        "b": "besh",
        "c": "cresh",
        "d": "dorn",
        "e": "esseles",
        "f": "forn",
        "g": "grek",
        "h": "herf",
        "i": "isk",
        "j": "jenth",
        "k": "krill",
        "l": "leth",
        "m": "mern",
        "n": "nern",
        "ñ": "nerf",
        "o": "osk",
        "p": "pei",
        "q": "qek",
        "r": "resh",
        "s": "senth",
        "t": "trill",
        "u": "ujeb",
        "v": "vev",
        "w": "wirch",
        "x": "xesh",
        "y": "yirt",
        "z": "zerek",
        "ch": "cherek",
        "ae": "enth",
        "eo": "onith",
        "kh": "krenth",
        "ng": "nen",
        "oo": "orenth",
        "sh": "shen",
        "th": "thesh",

    }

    if translation == AurebeshTranslation.SPANISH2AUREBESH:
        regex_spanish = "|".join(re.escape(x)  for x in aurebesh_map.keys())
        return re.sub(regex_spanish, lambda match: aurebesh_map[match.group()], text)
    else:
        spanish_map = {v: k for k, v in aurebesh_map.items()}
        regex_aurebesh = "|".join(re.escape(x) for x in spanish_map.keys())
        return re.sub(regex_aurebesh, lambda match: spanish_map[match.group()], text)


# /**
# * Función que traduce de español a aurebesh
# * @ param text Texto a traducir
# */
def spanish2aurebesh(text):
    return translate(text,AurebeshTranslation.SPANISH2AUREBESH)
# /**
# * Función que traduce de aurebesh a español
# * @ param text Texto a traducir
# */
def aurebesh2spanish(text):
    return translate(text,AurebeshTranslation.AUREBESH2SPANISH)


print(spanish2aurebesh('Que la fuerza te acompañe'))
print(aurebesh2spanish("""lethaurek lethujebnernaurek aureksenthoskmernaurek: fornesselesdornesselesreshiskcreshosk grekaurekreshcreshíaurek lethoskreshcreshaurek
                       creshujebaureknerndornosk senthaureklethesseles lethaurek lethujebnernaurek
                       senthesseles peiiskesselesreshdornesselesnern lethaureksenth creshaurekmernpeiaureknernaureksenth
                       yirt aurekpeiaurekreshesselescreshesselesnern lethaureksenth senthesselesnerndornaureksenth
                       iskmernpeiesselesnernesselestrillreshaurekbeshlethesselessenth.
                       creshujebaureknerndornosk senthaureklethesseles lethaurek lethujebnernaurek,
                       esselesleth mernaurekresh creshujebbeshreshesseles lethaurek trilliskesselesreshreshaurek
                       yirt esselesleth creshoskreshaurekzerekónern senthesseles senthiskesselesnerntrillesseles
                       isksenthlethaurek esselesnern esselesleth isknernfornisknernisktrillosk.
                       nernaurekdorniskesseles creshoskmernesseles nernaurekreshaureknernjenthaureksenth
                       beshaurekjenthosk lethaurek lethujebnernaurek lethlethesselesnernaurek.
                       esselessenth peireshesselescreshisksenthosk creshoskmernesselesresh
                       fornreshujebtrillaurek vevesselesreshdornesseles yirt herfesseleslethaurekdornaurek.
                       creshujebaureknerndornosk senthaureklethesseles lethaurek lethujebnernaurek
                       dornesseles creshiskesselesnern reshosksenthtrillreshosksenth iskgrekujebaureklethesselessenth,
                       lethaurek mernosknernesselesdornaurek dornesseles peilethaurektrillaurek
                       senthosklethlethoskzerekaurek esselesnern esselesleth beshosklethsenthisklethlethosk."""))  #Prueba a traducirlo a ver que sale ;)

