
import java.util.ArrayList;

public class Reto11 {

    public static void main(String[] args) {
        String url = "https://retosdeprogramacion.com?year=2023&challenge=0&example=";
        System.out.println(getUrlParameters(url));
    }

    private static ArrayList<String> getUrlParameters(String url) {
        String[] values = url.split("&");
        ArrayList<String> parameters = new ArrayList<>();
        for (String value : values) {
            String parameter = value.substring(value.indexOf("=") + 1);
            if (!parameter.isBlank() && !parameter.isEmpty())
                parameters.add(parameter);
        }
        return parameters;
    }
}