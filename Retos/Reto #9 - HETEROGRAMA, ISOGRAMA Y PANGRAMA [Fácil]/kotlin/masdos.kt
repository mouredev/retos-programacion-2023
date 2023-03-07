/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 *
 * Heterograma = es una palabra o frase que no contiene ninguna letra repetida.
 * Isograma = es una palabra o frase en la que cada letra aparece el mismo número de veces.
 * Pangrama = es una frase en la que aparecen todas las letras del abecedario.
 * https://es.wikipedia.org/wiki/Heterograma#:~:text=Un%20isograma%20(del%20griego%20isos,segundo%20orden%20y%20as%C3%AD%20sucesivamente.
 */
fun main() {

  val heterogram = "dermatoglyphics"
  val isogram = "reappear"
  val pangram = "Farmer jack realized that big yellow quilts expensive"

  println(isHeterogram(heterogram))
  println(isIsogram(isogram))
  println(isPangram(pangram))
}

private fun isHeterogram(text: String): Boolean {
  val validText = getEnglishAlphabetOnly(text)
  return validText.chars().distinct().count().toInt() == validText.count()
}

private fun isIsogram(text: String): Boolean {
  val validText = getEnglishAlphabetOnly(text)
  return validText.count() % validText.chars().distinct().count().toInt() == 0
}

private fun isPangram(text: String): Boolean {
  val numberLettersAlphabet = 26
  return getEnglishAlphabetOnly(text).chars().distinct().count().toInt() == numberLettersAlphabet
}

private fun getEnglishAlphabetOnly(text: String): String =
  text.lowercase().filter { char -> char in 'a'..'z' }