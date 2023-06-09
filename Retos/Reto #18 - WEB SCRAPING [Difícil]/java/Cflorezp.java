package reto18WebScraping;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;

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
 * Gracias a AlbertoVf por su solucion en python
 */
public class Cflorezp {

    public static void main(String[] args) throws IOException {

        String url = "https://holamundo.day/";
        Document doc = Jsoup.connect(url).get();
        Elements h1s = doc.select("h1");
        Element day = h1s.get(h1s.size() - 2);
        if (day != null) {
            System.out.println(day.text());
            Element next_element = day.nextElementSibling();
            while (next_element != null && next_element.tagName().equals("blockquote")) {
                System.out.println(next_element.text());
                next_element = next_element.nextElementSibling();
            }
        }
    }


}
