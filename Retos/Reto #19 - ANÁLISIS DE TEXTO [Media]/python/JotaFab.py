'''
/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */
'''


import re

def analice_texto(text):

    words = re.findall(r'\w+', text)
    num_words = len(words)

    avg_word_length = sum(len(word) for word in words)/num_words

    sentences = re.findall(r'\.\s+', text)
    num_sentences = len(sentences)

    longest_word = max(words, key=len)

    print('Numero total de palabras:', num_words)
    print('Longitud media de las palabras:', avg_word_length)
    print('Número de oraciones:', num_sentences)
    print('Palabra mas larga:', longest_word)

if __name__ == '__main__':
    
    text = "Puedo escribir los versos mas tristes esta noche. Escribir, por ejemplo: «La noche está estrellada, y tiritan, azules, los astros, a lo lejos.» El viento de la noche gira en el cielo y canta. Puedo escribir los versos más tristes esta noche.        Yo la quise, y a veces ella también me quiso.        En las noches como ésta la tuve entre mis brazos.        La besé tantas veces bajo el cielo infinito.        Ella me quiso, a veces yo también la quería.        Cómo no haber amado sus grandes ojos fijos.        Puedo escribir los versos más tristes esta noche.        Pensar que no la tengo. Sentir que la he perdido.        Oír la noche inmensa, más inmensa sin ella.        Y el verso cae al alma como al pasto el rocío.        Qué importa que mi amor no pudiera guardarla.        La noche está estrellada y ella no está conmigo.        Eso es todo. A lo lejos alguien canta. A lo lejos        Mi alma no se contenta con haberla perdido.        Como para acercarla mi mirada la busca.        Mi corazón la busca, y ella no está conmigo.        La misma noche que hace blanquear los mismos árboles.        Nosotros, los de entonces, ya no somos los mismos.        Ya no la quiero, es cierto, pero cuánto la quise.        Mi voz buscaba el viento para tocar su oído.        De otro. Será de otro. Como antes de mis besos.        Su voz, su cuerpo claro. Sus ojos infinitos.        Ya no la quiero, es cierto, pero tal vez la uiero.        Es tan corto el amor, y es tan largo el olvido.        Porque en noches como ésta la tuve entre mis brazos,        mi alma no se contenta con haberla perdido.        Aunque éste sea el último dolor que ella me causa,        y estos sean los últimos versos que yo le escribo."

    
    analice_texto(text)