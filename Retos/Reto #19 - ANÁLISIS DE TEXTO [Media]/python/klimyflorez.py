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
               
texto = """La nave estelar USS Enterprise está bajo un gran reacondicionamiento y su excomandante, James T. Kirk, ha sido ascendido a Almirante y ahora es Jefe de Operaciones 
de la Flota Estelar. Una poderosa fuerza alienígena, en forma de una masiva nube de energía con una longitud de 82 unidades astronómicas, es detectada en espacio Klingon y 
parece dirigirse rumbo a la Tierra. A su paso, la nube destruye tres naves Klingons y la estación espacial de la flota Epsilon 9. Como única nave en rango del alcance, 
la flota envía la Enterprise para interceptar la nube, acelerando su reacondicionamiento, el cual deberá ser probado en el transcurso de la misión asignada.
El Almirante Kirk toma el mando de la nave, lo cual disgusta al capitán Willard Decker, quien ha supervisado las mejoras como nuevo oficial. Con varios de los exmiembros 
de la tripulación a bordo, la Enterprise inicia su viaje."""
palabra = CheckTexto(texto)
print(palabra)