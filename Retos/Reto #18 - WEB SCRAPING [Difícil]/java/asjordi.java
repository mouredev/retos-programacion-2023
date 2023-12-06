import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import java.io.IOException;

public class HolaMundoDay {

    public static void main(String[] args) throws IOException {
        getSchedule();
    }

    public static void getSchedule() throws IOException{
        String URL = "https://holamundo.day";
        Document doc = Jsoup.connect(URL).get();
        Elements h1 = doc.select("h1");
        Element day = h1.get(h1.size() - 2);

        if (day != null){
            System.out.println(day.text());
            Element nextElem = day.nextElementSibling();
            while (nextElem != null && nextElem.tagName().equals("blockquote")){
                System.out.println(nextElem.text());
                nextElem = nextElem.nextElementSibling();
            }
        }
    }
}
