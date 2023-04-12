// este script está inspirado en https://github.com/joaki-rivero

fun main() {
    val url = "https://retosdeprogramacion.com?year=2023&challenge=0&language=kotlin"
    val parameters = getParameters(url)
    println(parameters)
}

fun getParameters(url: String): List<Pair<String, String>> {
    val parametersList = mutableListOf<Pair<String, String>>()

    val queryString = url.substringAfter('?')
    if (queryString.isEmpty()) return parametersList

    queryString.split("&").forEach { param ->
        val keyValue = param.split("=")
        if (keyValue.size == 2) {
            val key = keyValue[0]
            val value = keyValue[1]
            parametersList.add(Pair(key, value))
        }
    }

    return parametersList
}
