import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;
import com.google.gson.Gson;
import com.google.gson.JsonObject;

/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 */

public class josepmonclus {

    Scanner entrada = new Scanner(System.in);

    String pokemon = "";

    public static void main(String[] args) {
        josepmonclus josepmonclus = new josepmonclus();

        josepmonclus.getPokemon();

        
        josepmonclus.doAPICall();
    }

    private void doAPICall() {
        try{
            URL url = new URL("https://pokeapi.co/api/v2/pokemon/"+ pokemon);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.addRequestProperty("User-Agent", "cheese");
            conn.setRequestMethod("GET");

            BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String line;
            StringBuffer response = new StringBuffer();

            while ((line = reader.readLine()) != null) {
                response.append(line);
            }
            reader.close();

            // Parsear la respuesta JSON
            Gson gson = new Gson();
            JsonObject json = gson.fromJson(response.toString(), JsonObject.class);
            String name = json.get("name").getAsString();
            String id = json.get("id").getAsString();
            String height = json.get("height").getAsString();
            String weight = json.get("weight").getAsString();

            System.out.println("Nombre: " + name);
            System.out.println("# " + id);
            System.out.println("Altura: " + height);
            System.out.println("Peso: " + weight);

        } catch(Exception e) {
            System.out.println("Pokemon no encontrado!");
        }
    }

    private void getPokemon() {
        System.out.println("Introduce el nombre o el número del pokemon que quieres consultar:");

        pokemon = entrada.nextLine();
    }
}
