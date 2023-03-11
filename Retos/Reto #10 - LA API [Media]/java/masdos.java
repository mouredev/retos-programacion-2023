import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Masdos {

    public static void main(String[] args) throws URISyntaxException, IOException, InterruptedException {
        System.out.println(getActivity());
    }

    private static String getActivity() throws URISyntaxException, IOException, InterruptedException {
        String uri = "http://www.boredapi.com/api/activity/";

        HttpRequest request = HttpRequest.newBuilder()
                .uri(new URI(uri))
                .GET()
                .build();

        HttpResponse<String> response = HttpClient.newBuilder()
                .build()
                .send(request, HttpResponse.BodyHandlers.ofString());

        return response.body();
    }
}