
fun main() {
    traducir("esto es una PRUEBA")
}

fun traducir(texto:String) {

    var newTexto:String = texto.lowercase()
    val alfabetoHacker = arrayListOf<String>("4", "I3", "[", ")", "3", "|=", "&", "#", "1", ",_|", ">|", "1", "/\\/\\",
                                    "^/", "0", "|*", "(_,)", "I2", "5", "7", "(_)", "\\/", "\\/\\/", "><", "j", "2")

    var count = 0
    for(vocal in 'a'..'z'){
        newTexto = newTexto.replace(vocal.toString(), alfabetoHacker[count])
        count++
    }

    println(newTexto)
}
