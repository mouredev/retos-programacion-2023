fun main() {

    /*
    * Reto #11 13/03/2023
    *
    * Dada una URL con parámetros, crea una función que obtenga sus valores.
    * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
    *
    * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
    * los parámetros serían ["2023", "0"]
    *
    */
    var urlPruebas = listOf(
        "https://retosdeprogramacion.com?year=2023&challenge=0",
        "https://retosdeprogramacion.com?year=2023&challenge=0&challengenumber=11",
        "https://retosdeprogramacion.com?year=2023",
        "https://retosdeprogramacion.com",
        "https://retosdeprogramacion.com?year=2023&challenge=0&challengenumber=11&dificultad=facil"
    )
    urlPruebas.forEach { url ->
        println(url)
        println(getUrlParametros(url))
    }


}

fun getUrlParametros(url: String): List<String> {
    var parametros = mutableListOf<String>()

    var partes = url.split('?')

    if (partes.count() > 1) {
        var parametros2 = partes[1].split('&')

        parametros2.forEach { p ->
            val partes = p.split('=')
            parametros.add(partes[1])

        }
    }
    return parametros

}