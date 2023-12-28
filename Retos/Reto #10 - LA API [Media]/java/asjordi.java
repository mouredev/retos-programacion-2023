import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class RickAndMortyApi {

    private final int id;

    public RickAndMortyApi(int id) {
        this.id = id;
    }

    public String getCharacter() throws URISyntaxException, IOException, InterruptedException {

        if (this.id > 826 || this.id < 1) return "The id parameter must be between 1 and 826";

        String url = String.format("https://rickandmortyapi.com/api/character/%s", this.id);

        HttpClient httpClient = HttpClient.newHttpClient();

        HttpRequest getRequest = HttpRequest.newBuilder()
                .uri(new URI(url))
                .GET()
                .build();

        HttpResponse<String> getResponse = httpClient.send(getRequest, HttpResponse.BodyHandlers.ofString());

        if (getResponse.statusCode() > 400) return "There was an error!";

        return getResponse.body();

    }

}
