package reto11ExtraerValoresURL;

import java.net.URI;
import java.net.URISyntaxException;
import java.util.HashMap;
import java.util.Map;

/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 */
public class Cflorezp {

    public static void main(String[] args) {
        String url = "https://retosdeprogramacion.com?year=2023&challenge=0";

        Map<String, String> parameters = getParametersFromUrl(url);
        System.out.println(parameters);
    }

    public static Map<String, String> getParametersFromUrl(String url) {
        Map<String, String> parameters = new HashMap<>();
        try {
            URI uri = new URI(url);
            String query = uri.getQuery();
            if (query != null) {
                String[] pairs = query.split("&");
                for (String pair : pairs) {
                    int idx = pair.indexOf("=");
                    String key = idx > 0 ? pair.substring(0, idx) : pair;
                    String value = idx > 0 && pair.length() > idx + 1 ? pair.substring(idx + 1) : null;
                    parameters.put(key, value);
                }
            }
        } catch (URISyntaxException e) {
            e.printStackTrace();
        }
        return parameters;
    }
}
