import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

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

public class josepmonclus {
    public static void main(String[] args) {
        String url = "https://holamundo.day";

        try {
            // Realizar la solicitud HTTP y obtener el documento HTML
            Document document = Jsoup.connect(url).get();
            
            Elements paragraphElements = document.select("h1");
            for(Element h1 : paragraphElements) {
                if(h1.text().contains("Agenda 8 de mayo")) {
                    Elements agenda = h1.nextElementSiblings().select("blockquote");
                    for(Element event : agenda) {
                        System.out.println(event.text());
                    }
                }
            }
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
}
