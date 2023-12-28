import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

/**
 * Program that uses an API: AEMET API (weather API).
 * This example is showing the prediction for today and tomorrow in Pulpí, Almería (Spain).
 * You can change the place changing the MUNICIPALITY constant.
 * You should create the AEMETKEY constant with YOUR personal API key and to add to this code: https://opendata.aemet.es/centrodedescargas/inicio
 * @author: José Manuel Muñoz Simó [irotdev]
 * @version 2023.03.11/1
 */

public class irotdev {
    // Municipality code: https://www.ine.es/daco/daco42/codmun/codmunmapa.htm
    private static final String MUNICIPALITY = "04075"; // City: Almería --> Pulpí
    private static final String AEMETKEY = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJpcm90ZGV2QGdtYWlsLmNvbSIsImp0aSI6IjkwMjE3ZjFkLWNiMTQtNDI0Yy05N2I1LTUyOWJhZDdmZTlhYSIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNjc4Mzc5MTY3LCJ1c2VySWQiOiI5MDIxN2YxZC1jYjE0LTQyNGMtOTdiNS01MjliYWQ3ZmU5YWEiLCJyb2xlIjoiIn0.8eUAyfPHxDjRiZJTUd0OGPDpRZueunsf89J84-xLEdw";


    /**
     * Getting data of the AEMET API, which needs 2 calls:
     * 1- JSON with the URL of the data of the city.
     * 2- JSON of the previous URL with the data.
     * @param args
     */
    public static void main(String[] args) {
        String url = "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/"
                + MUNICIPALITY + "/?api_key=" + AEMETKEY;

        JSONObject jsonObject1 = new JSONObject(getAPI(url));   // First call to the 1st API

        String url2 = jsonObject1.getString("datos");
        JSONArray jsonArray = new JSONArray(getAPI(url2));      // Second call to the 2nd API

        JSONObject jsonObject2 = (JSONObject) jsonArray.get(0);
        String city = jsonObject2.get("nombre").toString();
        String province = jsonObject2.get("provincia").toString();

        JSONObject prediccion = (JSONObject) jsonObject2.get("prediccion");
        System.out.println("Temperature forecast, by AEMET API and irotdev, in " + city + ", " + province + " (Spain):");

        JSONArray dia = (JSONArray) prediccion.get("dia");

        // Today (the index of dia is 0)
        JSONObject dia0 = (JSONObject) dia.get(0);
        System.out.println("Today, day " + ((String) dia0.get("fecha")).substring(0, 10));

        JSONObject temperatura0 = (JSONObject) dia0.get("temperatura");
        JSONArray dato0 = (JSONArray) temperatura0.get("dato");
        for (int i = 0; i < dato0.length(); i++) {
            JSONObject dataGet = (JSONObject) dato0.get(i);
            System.out.println(" -> " + dataGet.get("value") + "ºC at " + dataGet.get("hora") + "h.");
        }
    }

    /**
     * Get the AEMET API (it will run for others API)
     * @param urlApi
     * @return
     */
    private static String getAPI(String urlApi) {
        String message = "";
        try {
            URL url = new URL(urlApi);
            HttpURLConnection con = (HttpURLConnection) url.openConnection();
            con.setRequestMethod("GET");

            BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream(), StandardCharsets.UTF_8));
            int responseCode = con.getResponseCode();
            if (responseCode != 200) {
                System.out.println("Error "+ responseCode);
            } else {
                String line = null;
                while ((line = in.readLine()) != null) {
                    message += line;
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return message;
    }
}