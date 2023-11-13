# Reto #19: Análisis de texto
# Dificultad: Media | Publicación: 11/05/23 | Corrección: 15/05/23 | Solución: 07/11/2023
# Enunciado
"""
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 * - Todo esto utilizando un único bucle.
 """
 
class CheckTexto:
    def __init__(self, texto):
        self.texto = texto
        self.palabras = "".join(e for e in texto if e.isalnum() or e.isspace()).split()
        self.num_palabras = len(self.palabras)
        self.longitud_total = sum(len(palabra) for palabra in self.palabras)
        self.num_oraciones = texto.count('.')
        self.palabra_mas_larga = max(self.palabras, key=len)
        
    def longitud_media(self):
        return self.longitud_total / self.num_palabras
        
    def __str__(self):
        return f"Número total de palabras: {self.num_palabras}\n" \
               f"Longitud media de las palabras: {self.longitud_media():.2f}\n" \
               f"Número de oraciones del texto: {self.num_oraciones}\n" \
               f"Palabra más larga: '{self.palabra_mas_larga}', con: {len(self.palabra_mas_larga)} letras"
               
texto = """En un mundo de código y sintaxis,
Python se alza con elegancia y eficacia.
Con su legibilidad y estructura clara,
El lenguaje de programación que nos deslumbra.

Desde su inicio, su filosofía se destaca,
Con énfasis en la legibilidad, nunca se opaca.
Con indentación y bloques bien definidos,
Python nos guía por caminos fluidos y unidos.

Sus librerías y módulos son vastos y poderosos,
Desde matemáticas hasta inteligencia artificial, asombrosos.
Con una comunidad activa y colaborativa,
Python nos brinda soluciones creativas.

Ya sea en desarrollo web o análisis de datos,
Python se destaca en diferentes campos y mercados.
Su versatilidad lo hace único y especial,
Un lenguaje que nos impulsa a crear sin igual.

Así, Python conquista corazones con pasión,
Uniendo a programadores en cada ocasión.
Con su belleza y simplicidad sin igual,
Python, el lenguaje que nunca dejará de brillar."""
palabra = CheckTexto(texto)
print(palabra)