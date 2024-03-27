// usage: scala-cli avelasquezhe84.scala 8 -u -s -n -> generates 8 char password with lower, upper, symbols and numbers

@main def main(args: String*) = 
    val lower = ('a' to 'z').toList
    val upper = ('A' to 'Z').toList
    val symbols = (' ' to '/').toList ++:
        (':' to '@').toList ++:
        ('[' to '`').toList ++:
        ('{' to '~').toList
    val nums = ('0' to '9').toList
    var chars = lower
    if args.contains("-u") then chars = chars ++ upper
    if args.contains("-s") then chars = chars ++ symbols
    if args.contains("-n") then chars = chars ++ nums
    val length = args(0).toInt
    val password = (1 to length).map(_ => chars(scala.util.Random.nextInt(chars.length))).mkString
    println(password)
