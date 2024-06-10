import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

class Main {
  public static void main(String[] args) {

    URI uri = URI.create("https://jsonplaceholder.typicode.com/todos/1");

    HttpClient client = HttpClient.newHttpClient();
    HttpRequest request = HttpRequest.newBuilder().uri(uri).build();

    try {
      HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
      System.out.println(response.body());
    } catch (Exception e) {
      e.printStackTrace();
    }

  }
}
