fun getParams(url: String): Array<String> {
    return url.split("?").drop(1).firstOrNull()?.split("&")?.map { it.split("=").drop(1).firstOrNull() ?: "" }?.toTypedArray() ?: arrayOf()
}

fun main() {
    println(getParams("https://retosdeprogramacion.com?year=2023&challenge=0").toList())
    println(getParams("https://retosdeprogramacion.com?year=2023&challenge").toList())
    println(getParams("https://retosdeprogramacion.com").toList())
}