fun main() {
    println(traducir("mario"))
    println(traducir("eskerni"))
}

fun traducir(oracion :String):String {
    var traducida = ""

    oracion.map{ it ->
        traducida += cambiarLetra(it)
    }

    return traducida
}

fun cambiarLetra(char:Char):String{
    return when(char){
        'a'->"aurek"
        'A'->"aurek"
        'b'->"besh"
        'B'->"besh"
        'c'->"cresh"
        'C'->"cresh"
        'd'->"dorn"
        'D'->"dorn"
        'e'->"esk"
        'E'->"esk"
        'f'->"forn"
        'F'->"forn"
        'g'->"grek"
        'G'->"grek"
        'h'->"herf"
        'H'->"herf"
        'i'->"isk"
        'I'->"isk"
        'j'->"jenth"
        'J'->"jenth"
        'k'->"krill"
        'K'->"krill"
        'l'->"leth"
        'L'->"leth"
        'm'->"mern"
        'M'->"mern"
        'n'->"nern"
        'N'->"nern"
        'o'->"osk"
        'O'->"osk"
        'p'->"peth"
        'P'->"peth"
        'q'->"qek"
        'Q'->"qek"
        'r'->"resh"
        'R'->"resh"
        's'->"senth"
        'S'->"senth"
        't'->"trill"
        'T'->"trill"
        'u'->"usk"
        'U'->"usk"
        'v'->"vev"
        'V'->"vev"
        'w'->"wesk"
        'W'->"wesk"
        'x'->"xesh"
        'X'->"xesh"
        'y'->"yirt"
        'Y'->"yirt"
        'z'->"zerek"
        'Z'->"zerek"
        else -> ""
    }
}
