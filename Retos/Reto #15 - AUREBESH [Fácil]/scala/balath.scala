import Translator._ 

val text = "En algun lugar de la Mancha, de cuyo nombre no quiero acordarme"

assert(text.equals(toSpanish(toAurebesh(text))))
println(translate(text))

//Probar online en https://scastie.scala-lang.org/D7qp02bnSz6Zhis0MTuiqg

//---------------------------Translator---------------------------

object Translator {
  
  import Dictionaries._
  
  def toAurebesh(text: String): String = text.length match {
    case 0 => ""
    case 1 => spanishToAurebesh.getOrElse(text, text)
    case _ =>
      val pair = text.take(2).mkString
      val char = text.head.toString()
      if (spanishToAurebesh.contains(pair))
        s"${spanishToAurebesh(pair)}${toAurebesh(text.drop(2))}"
      else
        s"${spanishToAurebesh.getOrElse(char, char)}${toAurebesh(text.drop(1))}"
  }
  
  def toSpanish(text: String): String = {
    def tryLetters(text: String, range: Int): String =
      (range, text.length, text.take(range).toString) match {
        case (_, 0, _)    => ""
        case (1, _, char) => s"$char${tryLetters(text.tail, AUREBESH_MAX_LENGTH)}"
        case (_, _, letters) if aurebeshToSpanish.contains(letters) =>
          s"${aurebeshToSpanish(letters)}${tryLetters(text.drop(range), AUREBESH_MAX_LENGTH)}"
        case _ => tryLetters(text, range - 1)
      }
    tryLetters(text, AUREBESH_MAX_LENGTH)
  }
  
  def translate(text: String): String = {
    val textLower = text.toLowerCase
    val isAurebesh = "[eiouEIOU]sk|aurek".r.findFirstIn(textLower).isDefined
    val translatedText = if (isAurebesh) toSpanish(textLower) else toAurebesh(textLower)
    s"Source text: $text\nTranslated: $translatedText"
  }

}

//---------------------------Dictionaries---------------------------

object Dictionaries {

  val spanishToAurebesh = Map(
    "a" -> "aurek",
    "ae" -> "enth",
    "b" -> "besh",
    "c" -> "cresh",
    "ch" -> "cherek",
    "d" -> "dorn",
    "e" -> "esk",
    "eo" -> "onith",
    "f" -> "forn",
    "g" -> "grek",
    "h" -> "herf",
    "i" -> "isk",
    "j" -> "jenth",
    "k" -> "krill",
    "kh" -> "krenth",
    "l" -> "leth",
    "m" -> "mern",
    "n" -> "nern",
    "ng" -> "nen",
    "o" -> "osk",
    "oo" -> "orenth",
    "p" -> "peth",
    "q" -> "qek",
    "r" -> "resh",
    "s" -> "senth",
    "sh" -> "shen",
    "t" -> "trill",
    "th" -> "thesh",
    "u" -> "usk",
    "v" -> "vev",
    "w" -> "wesk",
    "x" -> "xesh",
    "y" -> "yirt",
    "z" -> "zerek"
  )

  val aurebeshToSpanish = Map(
    "esk" -> "e",
    "nen" -> "ng",
    "nern" -> "n",
    "aurek" -> "a",
    "mern" -> "m",
    "onith" -> "eo",
    "vev" -> "v",
    "thesh" -> "th",
    "peth" -> "p",
    "resh" -> "r",
    "krill" -> "k",
    "senth" -> "s",
    "enth" -> "ae",
    "xesh" -> "x",
    "jenth" -> "j",
    "yirt" -> "y",
    "krenth" -> "kh",
    "trill" -> "t",
    "usk" -> "u",
    "forn" -> "f",
    "isk" -> "i",
    "cherek" -> "ch",
    "qek" -> "q",
    "besh" -> "b",
    "grek" -> "g",
    "leth" -> "l",
    "cresh" -> "c",
    "herf" -> "h",
    "wesk" -> "w",
    "orenth" -> "oo",
    "osk" -> "o",
    "zerek" -> "z",
    "dorn" -> "d",
    "shen" -> "sh"
  )

  val AUREBESH_MAX_LENGTH = 6

}