/*
 * Author: Sergio Flor https://github.com/balath
 * Run it on Scastie: https://scastie.scala-lang.org/FcVv61h5SpWSbOOxUiMQuQ
 */
case class MultiBaseNumber(decimal: String, octal: String, hex: String) {

  override def toString(): String =
    s"\tDecimal: $decimal\n\tOctal: $octal\n\tHexadecimal: $hex"

  def unary_- : MultiBaseNumber =
    MultiBaseNumber(s"-$decimal", s"-$octal", s"-$hex")
}

object MultiBaseNumber {

  def apply(input: Int): MultiBaseNumber = {
    val absolutInput = input.abs
    val output = MultiBaseNumber(
      decimal = s"$absolutInput",
      octal = decimalToBase(absolutInput, 8, n => s"$n"),
      hex = decimalToBase(absolutInput, 16, n => littleDecToHex(n))
    )
    if (input >= 0) output
    else -output
  }

  def decimalToBase(input: Int, base: Int, toBaseString: Int => String): String = {
    val remainder = toBaseString(input % base)
    val quotient = input / base
    if (quotient == 0) remainder
    else s"${decimalToBase(quotient, base, toBaseString)}$remainder"
  }

  def littleDecToHex(n: Int) = n match {
    case _ if n < 10 => s"$n"
    case 10          => "A"
    case 11          => "B"
    case 12          => "C"
    case 13          => "D"
    case 14          => "E"
    case 15          => "F"
  }
}

//Test
def test(testName: String, testInput: MultiBaseNumber, expectedOctal: String, expectedHex: String): Unit = {
  assert(testInput.octal.equals(expectedOctal), s"Octal conversion fails with ${testInput.decimal} != $expectedOctal")
  println(s"$testName: octal conversion ok")
  assert(testInput.hex.equals(expectedHex), s"Hexadecimal conversion fails with ${testInput.decimal} != $expectedHex")
  println(s"$testName: hexadecimal conversion ok")
  println(s"$testName result:\n$testInput\n\n")
}

val test1 = MultiBaseNumber(3425)
val test2 = MultiBaseNumber(9)
val test3 = MultiBaseNumber(-18)

test("Test 1", test1, expectedOctal = "6541", expectedHex = "D61")
test("Test 2", test2, expectedOctal = "11", expectedHex = "9")
test("Test 3", test3, expectedOctal = "-22", expectedHex = "-12")