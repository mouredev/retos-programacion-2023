fun main() {
    print(getParameters("https://retosdeprogramacion.com?year=2023&challenge=0"))
}

fun getParameters(url: String): List<String> {
    val parametersList = mutableListOf<String>()

    if (!url.contains('?')) return parametersList

    url.substring(url.indexOf('?') + 1)
        .split("&")
        .forEach { param ->
            parametersList.add(param.substring(param.indexOf("=") + 1))
        }

    return parametersList
}