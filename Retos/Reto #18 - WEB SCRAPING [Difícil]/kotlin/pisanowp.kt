import org.jsoup.Jsoup
import org.jsoup.nodes.Document

fun main() {

    /*
    * Reto #18 01/05/2023
    *
    * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
    * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
    *
    * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
    * del día 8. Mostrando hora e información de cada uno.
    * Ejemplo: "16:00 | Bienvenida"
    *
    * Se permite utilizar librerías que nos faciliten esta tarea.
    *
    *
    *  Preparaciión registrar las dependencias.
    *  Para IntelliJ IDEA editar el fichero build.gradle.kts en el bloque dependencies añadir:
    *
    *    implementation("org.jsoup:jsoup:1.10.3")
    */


    // Recuperamos el DOM de la web
    val url = "https://holamundo.day/"
    val document: Document = Jsoup.connect(url).get()

    // Localizamos donde esta la Agenda del día 8
    val titulo = document.select("span:contains(Agenda 8 de mayo)")[1]
    val h1 = titulo.parent().parent()

    // Los elementos "hermano" del h1 son varios, pero los blockquote son
    // los que tienen la agenda
    val agenda = h1.siblingElements()

    // Recorremos los elementos "hermanos"
    agenda.forEach {

        // .. y si es de tipo blockquote ...
        if (it.`is`("blockquote")){
            // .. mostramos su contenido
            println(it.text())

        }

    }

}