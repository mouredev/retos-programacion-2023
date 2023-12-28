/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */


/**
 * Ejecuta la función getParams
 */
fun main(){
    println(getParams("https://retosdeprogramacion.com?year=2023&challenge=0"))
}

main()



/**
 * Función que obtiene los parámetros de una URL usando expresiones regulares
 * @param url
 * @returns {string[][]} Array de arrays con los parámetros y sus valores
 */
fun getParams(url: String): List<List<String>> {

    val regexUrl = Regex("^(https?://)?([\\da-z.-]+)\\.([a-z.]{2,6})([/\\w.-]*)*/?\\?(.*)\$")
    if(regexUrl.matches(url)){
        val regexParams = Regex("([?&])([^=]+)=([^&]+)")
        val params = regexParams.findAll(url)

        return  params.map {
            listOf(it.value.substring(1).split("=")[0], it.value.substring(1).split("=")[1])
        }.toList()

    }

    return listOf()



}