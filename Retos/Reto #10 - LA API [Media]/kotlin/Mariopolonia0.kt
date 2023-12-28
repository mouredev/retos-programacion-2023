package EjercicioKotlin.Mouredev

import java.net.URI
import java.net.http.HttpClient
import java.net.http.HttpRequest
import java.net.http.HttpResponse.BodyHandlers

//https://bible-api.com/romans+12:1-1
class reto10 {
    fun result(libro: String, capitulo: Int, versiculos: String) {
        val httpClient = HttpClient.newBuilder().build()

        val request = HttpRequest.newBuilder().uri(URI.create("https://bible-api.com/$libro+$capitulo:$versiculos")).build()

        val response = httpClient.send(request, BodyHandlers.ofString())

        val divicionUno = response.body().split("\"text\":\"")
        val divicionDos = divicionUno[divicionUno.size - 1].split("\\n\"")[0]
        val divicionTres = divicionDos.split("\\n")
        
        divicionTres.map{
            println(it.replace('”',' '))
        }
    }
}

fun main() {
    reto10().result("genesis", 1, "1")
    reto10().result("matthew", 19, "6")
}
