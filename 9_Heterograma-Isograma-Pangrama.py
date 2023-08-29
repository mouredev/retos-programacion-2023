class TextDetector():

  def __init__(self, word:str):
    self.word = word

  def isograma(self):
    letras_vistas = set()
    return all(
      letras_vistas.add(letter) or not letter.isalpha() or (
        letter in letras_vistas) for letter in self.word.lower() )

  def heterograma(self):
    pass

  def pangrama(self):
    pass


# Crear una instancia y utilizar su método.
objeto = TextDetector("Luuz")
print("La palabra es un isograma" if objeto.isograma(
) else "La palabra no es un isograma")
