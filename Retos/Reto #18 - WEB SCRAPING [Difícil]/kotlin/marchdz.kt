import it.skrape.core.htmlDocument
import it.skrape.fetcher.*

fun main() {
    skrape(HttpFetcher) {
        request { url = "https://holamundo.day/" }
        response {
            htmlDocument {
                document.selectFirst("h1:contains(Agenda 8)").nextElementSiblings()
                    .filter { it.`is`("blockquote") }
                    .forEach { println(it.text()) }
            }
        }
    }
}
