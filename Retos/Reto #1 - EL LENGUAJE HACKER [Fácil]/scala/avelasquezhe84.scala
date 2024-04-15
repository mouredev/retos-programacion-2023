// Scala 3

@main def main(args: String*) =
    println(args.map(w => translate(w.toLowerCase())).mkString(" "))

def translate(word: String): String =
    val w = word.toList.map(_.toString())
    val az = ('a' to 'z').map(_.toString())
    val leet = List("4", "I3", "[", ")", "3", "|=", "&", "#", "1", ",_|", ">|", "1", "/\\/\\", "^/", "0", "|*", "(_,)", "I2", "5", "7", "(_)", "\\/", "\\/\\", "><", "j", "2")
    val substitutions = (az zip leet).toMap
    val res = w.map(c => substitutions.getOrElse(c, c))
    res.mkString