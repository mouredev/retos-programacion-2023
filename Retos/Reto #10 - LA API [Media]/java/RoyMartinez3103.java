
import java.io.IOException;
import java.net.URI;
import java.net.http.*;
import java.util.Base64;

/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 */
public class RoyMartinez3103 {

    private static final String CLIENT_ID = "fb6b45a88ab14f888c9b7a5ae6aed551";
    private static final String URL = "https://accounts.spotify.com/api/token";
    private static final String SECRET_ID = "4c59a2a4879e4870a9aa5e8ccaf9d7cc";

//Obtiene el token de acceso para hacer solicitudes.
    public static String getAccessToken() throws IOException, InterruptedException {
        String credentials = CLIENT_ID + ":" + SECRET_ID;
        String encodedCredentials = Base64.getEncoder().encodeToString(credentials.getBytes());
        //Spotify requiere las credenciales en Base64

        HttpRequest request = HttpRequest.newBuilder() //Se crea una solicitud http al endpoint de 
                .uri(URI.create(URL))
                .header("Authorization", "Basic " + encodedCredentials) //se envian credenciales
                .header("Content-Type", "application/x-www-form-urlencoded") //formato formulario
                .POST(HttpRequest.BodyPublishers.ofString("grant_type=client_credentials")) //tipo de auth
                .build();

        HttpClient client = HttpClient.newHttpClient(); //Se envia lo solicitud
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());  //Se obtiene el token en formato json

        // Extraer el token del JSON
        String responseBody = response.body();
        String accessToken = responseBody.split("\"access_token\":\"")[1].split("\"")[0];  //Se extrae el token de la respuesta

        return accessToken;
    }

    public static void main(String args[]) {
        try {
            String token = getAccessToken();
            String artistId = "3Ij56hbjOTHq8RgutQwfxC";
            String apiUrl = "https://api.spotify.com/v1/artists/" + artistId;

            HttpRequest request = HttpRequest.newBuilder() //Se crea la petición get
                    .uri(URI.create(apiUrl))
                    .header("Authorization", "Bearer " + token)
                    .GET()
                    .build();

            HttpClient client = HttpClient.newHttpClient();
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            System.out.println("Respuesta de Spotify: " + response.body());
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
