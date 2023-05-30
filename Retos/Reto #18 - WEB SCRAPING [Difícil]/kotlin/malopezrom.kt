/*
 * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
 * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
 *
 * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
 * del día 8. Mostrando hora e información de cada uno.
 * Ejemplo: "16:00 | Bienvenida"
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
 *
 */
import org.jsoup.Jsoup


/**
 * Función que imprime la agenda del día 8 de mayo
 */
fun printDay8() {
    val url = "https://holamundo.day"
    val doc = Jsoup.connect(url).get()
    val results = doc.select("h1")

    for (result in results) {
        if (result.text().contains("Agenda 8 de mayo")) {
            println(result.text())

            var sibling = result.nextElementSibling()!!
            while (sibling.text().contains(":")){
                println(sibling.text())
                sibling = sibling.nextElementSibling()!!
            }

        }
    }
}

/**
 * Función main
 */
fun main() {
    printDay8()
}
