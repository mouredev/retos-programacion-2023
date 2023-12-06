import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class ReadCommits {

    public static void main(String[] args) throws URISyntaxException, IOException, InterruptedException {

        Gson gson = new Gson();
        String url = "https://api.github.com/repos/mouredev/retos-programacion-2023/commits?per_page=10";
        HttpClient httpClient = HttpClient.newHttpClient();

        HttpRequest getRequest = HttpRequest.newBuilder()
                .uri(new URI(url))
                .GET()
                .build();

        HttpResponse<String> getResponse = httpClient.send(getRequest, HttpResponse.BodyHandlers.ofString());
        int responseCode = getResponse.statusCode();

        if (responseCode != 200) System.out.println("There was an error!");

        String responseBody = getResponse.body();
        JsonArray commits = gson.fromJson(responseBody, JsonArray.class);

        for (int i = 0; i < commits.size(); i++) {
            JsonObject commit = commits.get(i).getAsJsonObject();
            JsonObject commitDetails = commit.get("commit").getAsJsonObject();
            String hash = commit.get("sha").getAsString();
            String author = commitDetails.get("author").getAsJsonObject().get("name").getAsString();
            String message = commitDetails.get("message").getAsString();
            String date = commitDetails.get("author").getAsJsonObject().get("date").getAsString();

            System.out.println("Commit " + (i + 1) + " | " + hash + " | " + author + " | " + message + " | " + date);
        }

    }

}
