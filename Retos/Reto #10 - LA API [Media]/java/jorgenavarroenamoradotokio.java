package com.retos.ej10;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class jorgenavarroenamoradotokio {

	public static void main(String[] args) {
		try {
			String uri = "https://pokeapi.co/api/v2/pokemon/4";

			HttpRequest request = HttpRequest.newBuilder().uri(new URI(uri)).GET().build();

			HttpResponse<String> response;

			response = HttpClient.newBuilder().build().send(request, HttpResponse.BodyHandlers.ofString());

			System.out.println(response.body());
		} catch (IOException | InterruptedException | URISyntaxException e) {
			e.printStackTrace();
		}
	}
}
