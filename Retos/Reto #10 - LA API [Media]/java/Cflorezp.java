package reto10ConsumirApi;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpClient.Redirect;
import java.net.http.HttpClient.Version;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.http.HttpResponse.BodyHandlers;
import java.time.Duration;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;

/*
 * Llamar a una API
 *
 * Implementa una llamada HTTP a una API y muestra su
 * resultado a través de la terminal.
 *
 * API (url) tomada de:
 * https://github.com/public-apis/public-apis
 *
 * se usa la dependencia gson version 2.8.7
 */
public class Cflorezp {

    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newBuilder()
                .version(Version.HTTP_2)
                .followRedirects(Redirect.NORMAL)
                .build();

        HttpRequest request = HttpRequest.newBuilder()
                .uri(new URI("https://www.mmobomb.com/api1/games"))
                .GET()
                .timeout(Duration.ofSeconds(10))
                .build();

        HttpResponse<String> response = client.send(request, BodyHandlers.ofString());

        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        JsonElement jsonElement = JsonParser.parseString(response.body());
        String prettyJsonString = gson.toJson(jsonElement);

        System.out.println(prettyJsonString);
    }
}
