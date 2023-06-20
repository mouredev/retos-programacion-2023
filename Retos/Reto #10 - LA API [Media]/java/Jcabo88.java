package org.jcabo;


import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Jcabo88 {

    public static final String URL_HARRY_POTTER = "https://hp-api.onrender.com/api/characters";

    public static void main(String[] args) throws Exception {
        HttpRequest request = HttpRequest
                .newBuilder()
                .uri(new URI(URL_HARRY_POTTER))
                .header("Accept", "application/json")
                .GET()
                .build();

        HttpResponse response = HttpClient
                .newBuilder()
                .build()
                .send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("httpGetRequest status code: " + response.statusCode());
        System.out.println("httpGetRequest: " + response.body().toString());
    }
}