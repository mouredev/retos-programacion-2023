import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import java.io.IOException;

public class EspinoLeandroo {

    public static void main(String[] args) {
        String url = "https://holamundo.day";

        try {
            Document doc = Jsoup.connect(url).get();
            
            // Encuentra la sección de la agenda del día 8
            Elements agendaItems = doc.select("div.agenda-day-8 div.agenda-item");

            // Itera sobre los elementos de la agenda e imprime la hora e información
            for (Element item : agendaItems) {
                String hora = item.select("span.agenda-hour").text();
                String informacion = item.select("span.agenda-info").text();
                System.out.println(hora + " | " + informacion);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

