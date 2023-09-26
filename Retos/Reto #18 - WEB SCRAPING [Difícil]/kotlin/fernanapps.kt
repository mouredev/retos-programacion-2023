import java.net.URL
/**
..........................   Printing   .............................................
@author: FernanApps

    &gt;_ Agenda 8 de mayo | “Hola Mundo” day

    16:00 | Bienvenida
    16:30 | De Junior a Junior: cómo abrirte paso | Antonio Rodríguez
    17:00 | El Rol del Analista Funcional en el Ciclo de Desarrollo | Luisina de Paula
    17:30 | Taller: Git y Github para el mundo | Ehud Aguirre
    18:00 | Mesa redonda
    18:30 | Descanso + Sorteos
    19:00 | Clean Code: cómo dormir más y mejor | Fran Sierra
    19:30 | Abrazando al fracaso | Afor Digital
    20:00 | Taller: Descubre el mundo de machine learning | Stefy Mojica
    20:30 | Elevator pitch
    21:00 | Invitados
    21:30 | Mi primer año como Desarrollador a los 45 años | Gerardo Arrieta
    22:00 | Taller: Testing, más que código | Manu Rodríguez
    22:30 | Descanso + Sorteos
    23:00 | Despedida

 */
fun main() {

    val pageUrl = "https://holamundo.day/"
    val title8May = "Agenda 8 de mayo"

    val htmlString = downloadPage(pageUrl)
    val articleBlocks = extractHTMLTagBlock("article", htmlString)
    val articleBlock8May = articleBlocks.filter { it.contains(title8May) }.toString()
    val articleBlock8MayFilter = Regex("<h1.+${title8May}.+").find(articleBlock8May)!!.value

    val title = extractHTMLTagContent(extractHTMLTagBlock("h1", articleBlock8MayFilter).first())
    val events = extractHTMLTagBlock("blockquote", articleBlock8MayFilter).map {
        extractHTMLTagContent(it)
    }

    println(title)
    println()
    events.forEach { event ->
        println(event)
    }
}

fun downloadPage(pageUrl: String): String {
    val html = URL(pageUrl).openConnection().apply {
        setRequestProperty("User-Agent", "Mozilla/5.0")
    }.getInputStream().bufferedReader().use {
        it.readText()
    }
    return html
}

fun extractHTMLTagBlock(tag: String, html: String): List<String> {
    val regex = Regex("<$tag.*?</$tag>", RegexOption.DOT_MATCHES_ALL)
    val blocks: List<String> = regex.findAll(html).map {
        it.value
    }.toList()
    return blocks
}

fun extractHTMLTagContent(input: String): String {
    val regex = "<[^>]*>".toRegex()
    return regex.replace(input, "")
}