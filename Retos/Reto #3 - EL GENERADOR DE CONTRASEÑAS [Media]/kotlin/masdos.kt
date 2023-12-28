fun main() {

  /*
   * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
   * Podrás configurar generar contraseñas con los siguientes parámetros:
   * - Longitud: Entre 8 y 16.
   * - Con o sin letras mayúsculas.
   * - Con o sin números.
   * - Con o sin símbolos.
   * (Pudiendo combinar todos estos parámetros entre ellos)
   */

  val passwordSize = addPasswordSize(8, 16)
  val hasUppercase = hasPreference("mayúsculas")
  val hasNumbers = hasPreference("números")
  val hasSymbols = hasPreference("símbolos")

  val password = generatePassword(passwordSize, hasUppercase, hasNumbers, hasSymbols)
  println(password)
}

private fun addPasswordSize(minSize: Int, maxSize: Int): Int {
  var passwordSize = minSize
  var validSize = false
  while (!validSize) {
    println(
      "¿Cuántos caracteres desea en la contraseña? Siendo $minSize el mínimo y $maxSize el máximo: "
    )
    passwordSize = readln().toInt()
    if (passwordSize in minSize..maxSize) validSize = true
    else
      println(
        "El parámetro '$passwordSize' no es correcto. Aceptados: $minSize a $maxSize incluidos"
      )
  }
  return passwordSize
}

private fun hasPreference(preferenceName: String): Boolean {
  var preference = false
  var validPreference = false
  while (!validPreference) {
    println("¿Desea tener $preferenceName? (si o no)")
    when (val response = readln().lowercase()) {
      "si" -> {
        preference = true
        validPreference = true
      }

      "no" -> {
        preference = false
        validPreference = true
      }

      else -> println("El parámetro '$response' no es correcto. Aceptados: si o no")
    }
  }
  return preference
}

private fun generatePassword(
  passwordSize: Int,
  hasUppercase: Boolean,
  hasNumbers: Boolean,
  hasSymbols: Boolean
): String {
  var password = generateLowercasePassword(passwordSize)
  do {
    if (hasUppercase) password = addUppercase(password)
    if (hasNumbers) password = addNumbers(password)
    if (hasSymbols) password = addSymbols(password)
  } while (!isValidPassword(password, hasUppercase, hasNumbers, hasSymbols))
  return password
}

fun isValidPassword(
  password: String,
  hasUppercase: Boolean,
  hasNumbers: Boolean,
  hasSymbols: Boolean
): Boolean {
  if (!password.any { it in 'a'..'z' }) return false
  if (hasUppercase && !password.any { it in 'A'..'Z' }) return false
  if (hasNumbers && !password.any { it in '0'..'9' }) return false
  if (hasSymbols && !password.any { it in listOf('!', '¡', '?', '¿', '#', '@', '$', '%', '&') })
    return false
  return true
}

private fun generateLowercasePassword(passwordSize: Int): String {
  val lowercase = ('a'..'z')
  var password = ""
  for (i in 1..passwordSize) password += lowercase.random()
  return password
}

private fun addUppercase(password: String): String {
  val uppercase = ('A'..'Z').toList()
  return replaceRandomCharacters(password, uppercase)
}

private fun addNumbers(password: String): String {
  val numbers = ('0'..'9').toList()
  return replaceRandomCharacters(password, numbers)
}

private fun addSymbols(password: String): String {
  val symbols = listOf('!', '¡', '?', '¿', '#', '@', '$', '%', '&')
  return replaceRandomCharacters(password, symbols)
}

private fun replaceRandomCharacters(text: String, newCharacters: List<Char>): String {
  val lettersToChange = ((Math.random() * (text.length / 2)) + 1).toInt()
  val lettersChanged = IntArray(lettersToChange)
  val newText = text.toCharArray()
  for (i in 0 until lettersToChange) {
    var positionChange: Int
    do {
      positionChange = (Math.random() * text.length).toInt()
    } while (lettersChanged.any() { it == positionChange })
    newText[positionChange] = newCharacters.random()
    lettersChanged[i] = positionChange
  }
  return newText.joinToString("")
}
