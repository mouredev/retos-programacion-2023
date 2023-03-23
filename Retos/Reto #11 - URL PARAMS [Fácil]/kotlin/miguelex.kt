private fun findParameters(url: String): Any {
    val params = mutableListOf<String>()
    val urlDividida = url.split("?")
    
    if (urlDividida.size > 1) {
        val listaParams = urlDividida[1].split("&")
        
        for (param in listaParams) {
            val clearParam = param.split("=")
            if (clearParam.size > 1 && clearParam[1].isNotEmpty()) {
                params.add(clearParam[1])
            } else {
                return "La cadena no tiene parametros validos"
            }
        }
        
        return params
    } else {
        return "La cadena no tiene parametros"
    }
}

fun main() {
    println(findParameters("https://retosdeprogramacion.com?year=2023&challenge=0"))
    println(findParameters("https://retosdeprogramacion.com"))
    println(findParameters("https://retosdeprogramacion.com?"))
    println(findParameters("https://retosdeprogramacion.com?year=2023"))
    println(findParameters("https://retosdeprogramacion.com?year=2023&"))
    println(findParameters("https://retosdeprogramacion.com?year=&"))
    println(findParameters("https://retosdeprogramacion.com?year=2023&challenge=0&languaje=python"))
}