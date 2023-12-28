package EjercicioKotlin.Mouredev

import java.net.URI
import java.net.http.HttpClient
import java.net.http.HttpRequest
import java.net.http.HttpResponse

class reto11 {

    private var libro = ""
    private var capitulo = 0
    private var versiculos = ""

    init {
        readData()
        result()
    }

    private fun readData() {
        println("\nFind your favorite verse")
        
        print("Enter the book in English:")
        libro = readLine()!!
        
        print("Enter the chapter:")
        capitulo = readLine()!!.toInt()
        
        print("Enter from to which verse example 1-3:")
        versiculos = readLine()!!
    }

    private fun result() {
        val httpClient = HttpClient.newBuilder().build()

        val request =
            HttpRequest.newBuilder().uri(URI.create("https://bible-api.com/$libro+$capitulo:$versiculos")).build()

        val response = httpClient.send(request, HttpResponse.BodyHandlers.ofString())

        val divicionUno = response.body().split("\"text\":\"")
        val divicionDos = divicionUno[divicionUno.size - 1].split("\\n\"")[0]
        val divicionTres = divicionDos.split("\\n")


        divicionTres.map {
            println("\n" + it.replace('”', ' '))
        }
    }
}

fun main() {
    var stop = false

    while (!stop) {
        reto11()

        print("\nyou want to look for another verse\n1.yes \n2.no\nenter the answer:")
        
        if (readLine()!!.toInt() != 1)
            stop = true
    }
}
