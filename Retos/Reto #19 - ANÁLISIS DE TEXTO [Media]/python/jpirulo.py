class CheckTexto:
    def __init__(self, texto):
        self.texto = texto
        self.palabras = texto.split()
        self.num_palabras = len(self.palabras)
        self.longitud_total = sum(len(palabra) for palabra in self.palabras)
        self.num_oraciones = texto.count('.')
        self.palabra_mas_larga = max(self.palabras, key=len)
        
    def longitud_media(self):
        return self.longitud_total / self.num_palabras
        
    def __str__(self):
        return f"Número total de palabras: {self.num_palabras}\n" \
               f"Longitud media de las palabras: {self.longitud_media()}\n" \
               f"Número de oraciones del texto: {self.num_oraciones}\n" \
               f"Palabra más larga: {self.palabra_mas_larga}"
               
texto = """INTRODUCCIÓN Durante casi veinte siglos, los hombres han tratado de comprender los hechos que dieron origen al cristianismo. ¿Cómo se produjo ese milagroso salto de una religión judía a una nueva fe universal? ¿Por qué las enseñanzas de un hombre que murió en la cruz y fue ajusticiado por los romanos despertaron tanto odio como amor?
La respuesta es compleja y tal vez nunca llegue a ser completa. Pero en Caballo de Troya, el lector encontrará una versión insólita, trepidante, sorprendente.
En el otoño de 1973, un oficial de la Fuerza Aérea de Estados Unidos contactó conmigo y me reveló algo que, en principio, consideré absurdo: en pleno siglo XX, y gracias a una técnica secreta de los norteamericanos, se había logrado viajar en el tiempo. A bordo de un caza F-14D, la persona podía desplazarse a cualquier lugar del pasado y volver sin dejar huella alguna. Lo más increíble era que este viaje se podía grabar, filmar.
Después de varias conversaciones, me mostró una película: era la crucifixión de Jesús de Nazaret.
Impresionado, emocionado, comencé una investigación que se prolongó durante años. Finalmente, en el otoño de 1981, acompañado por él, volé a Israel para realizar el mayor y más asombroso reportaje de mi vida. Sí, lo reconozco: al principio, me sentí como el teniente en la puerta del bunker de Hitler.
Con la ayuda de un especialista, «viajé» en el tiempo y asistí a escenas insólitas. Allí, en Palestina, pude conocer a los protagonistas y, como testigo directo, observar los acontecimientos que han dado origen al cristianismo.
Este libro es la crónica de ese increíble viaje. JJ Benítez"""
palabra = CheckTexto(texto)
print(palabra)