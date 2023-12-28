import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import string

def buscar_clave_externa(dic, valor_buscado):
    for clave_externa, dic_interno in dic.items():
        for clave_interna, valores in dic_interno.items():
            if valor_buscado in valores:
                return clave_externa
    return None

#base de conocimiento 
casas = {"Gryffindor":{"color":{"escarlata","dorado"},"animal":{"león","tigre","leopardo","jaguar"},"cualidades":{"osadía", "valor", "espíritu", "caballerosidad"},"elemento":{"fuego"}, "habilidades":{"duelo","protección"}},
         "Hufflepuff":{"color":{"amarillo","negro"},"animal":{"tejón","mofeta","puercoespin","nutria"},"cualidades":{"trabajadores", "pacientes", "equitativos", "justo", "leales", "modestos"},"elemento":{"tierra"},"habilidades":{"plantas","curación","animales", "pociones"}},
         "Ravenclaw":{"color":{"azul","bronce"},"animal":{"aguila","halcón","buitre","condor"},"cualidades":{"ingenio","aprendizaje","sabiduría","aceptación","inteligencia", "creatividad"},"elemento":{"aire"}, "habilidades":{"encantamientos","matemáticas","runas", "astronomia"}},
         "Slytherin":{"color":{"verde","plata"},"animal":{"serpiente","lagarto","iguana","camaleón"},"cualidades":{"ambición","astucia","determinación", "ingenio","auto-preservació"},"elemento":{"agua"}, "habilidades":{"pociones","persuasión"}}}

# Crear listas para cada categoría
colores = []
animales = []
cualidades = []
elementos = []
habilidades = []

for casa, atributos in casas.items():
    colores.extend(atributos["color"])
    animales.extend(atributos["animal"])
    cualidades.extend(atributos["cualidades"])
    elementos.extend(atributos["elemento"])
    habilidades.extend(atributos["habilidades"])

# Convertir a conjuntos para eliminar duplicados y luego a listas
colores = list(set(colores))
animales = list(set(animales))
cualidades = list(set(cualidades))
elementos = list(set(elementos))
habilidades = list(set(habilidades))

random.shuffle(colores)
random.shuffle(animales)
random.shuffle(cualidades)
random.shuffle(elementos)

opciones = [colores, animales, cualidades, elementos]

def answer_list(): 
    preguntas = ["¿Con qué color te identificas más de entre los siguientes?","¿Con qué animales te identificas más de entre los siguientes?", "¿Con qué habilidad te identificas más de entre los siguientes?", "¿Con qué elemento te identificas más de entre los siguientes?"]
    respuestas = {"Gryffindor":0,"Hufflepuff":0,"Ravenclaw":0,"Slytherin":0}

    for i in range(len(preguntas)): 
        print(f"{preguntas[i]}")
        print(*opciones[i],sep = ", ")
        respuesta = input("Introduce tu respuesta: ").lower()
        
        # Verificar si la respuesta está en la lista de opciones
        while respuesta not in opciones[i]:
            print("Respuesta no válida. Por favor, elige una opción de la lista.")
            print(*opciones[i],sep = ", ")
            respuesta = input("Introduce tu respuesta: ")

        respuestas[buscar_clave_externa(casas, respuesta)] +=1         

    return respuestas


# Función de preprocesamiento
def preprocess(text):
    # Convertir a minúsculas y eliminar signos de puntuación
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    return text

def categorizar_habilidad(respuestas):
    # Lista de habilidades mágicas predefinidas
    habilidades = ["duelo","protección", "plantas","curación","animales", "pociones", "encantamientos","aritmética","runas", "astronomia", "persuasión"]

    # Inicializar el vectorizador TF-IDF con ngram_range
    vectorizer = TfidfVectorizer(ngram_range=(1,2)).fit(habilidades)

    # Vectorizar las habilidades y la respuesta libre
    tfidf_habilidades = vectorizer.transform(habilidades)
    respuesta = input("Describe tus gustos o habilidades. Por ejemplo: Me gusta cocinar y las estrellas: ")
    respuesta = preprocess(respuesta)
    respuesta_tfidf = vectorizer.transform([respuesta])

    # Calcular la similitud del coseno
    similitudes = linear_kernel(respuesta_tfidf, tfidf_habilidades).flatten()

    # Identificar las top N habilidades más similares
    N = 3
    top_indices = similitudes.argsort()[-N:][::-1]
    top_habilidades = [habilidades[i] for i in top_indices]

    for elemento in top_habilidades:
        respuestas[buscar_clave_externa(casas, elemento)] += 2

    return respuestas

def sombrero_seleccionador(): 
    r = answer_list()
    r1 = categorizar_habilidad(r)
    return max(r1, key = r1.get) 

print(sombrero_seleccionador())