import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

/*
 * ¡Estoy de celebración! He publicado mi primer libro:
 * "Git y GitHub desde cero"
 * - Papel: mouredev.com/libro-git
 * - eBook: mouredev.com/ebook-git
 *
 * ¿Sabías que puedes leer información de Git y GitHub desde la gran
 * mayoría de lenguajes de programación?
 *
 * Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
 * - Hash
 * - Autor
 * - Mensaje
 * - Fecha y hora
 *
 * Ejemplo de salida:
 * Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
 * 
 */

public class josepmonclus {

    public static void main(String[] args) {
        String repoUrl = "https://api.github.com/repos/mouredev/retos-programacion-2023/commits";
        int nCommits = 10;

        josepmonclus josepmonclus = new josepmonclus();
        List<Commit> commits = josepmonclus.getLatestCommits(repoUrl, nCommits);

        for(Commit commit : commits) {
            System.out.println(commit.toString());
        }
    }

    private List<Commit> getLatestCommits(String repoUrl, int nCommits) {
        List<Commit> commits = new ArrayList<>();

        try {
            URL url = new URL(repoUrl);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Accept", "application/vnd.github.v3+json");

            if (connection.getResponseCode() == HttpURLConnection.HTTP_OK) {
                BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
                StringBuilder response = new StringBuilder();
                String line;
                while ((line = reader.readLine()) != null) {
                    response.append(line);
                }
                reader.close();

                // Parsear la respuesta JSON utilizando GSON
                Gson gson = new Gson();
                JsonArray commitsArray = gson.fromJson(response.toString(), JsonArray.class);
                

                for(int i = 0; i < nCommits; i++) {
                    Commit commit = new Commit();

                    JsonObject commitObject = commitsArray.get(i).getAsJsonObject();
                    commit.setHash(commitObject.get("sha").getAsString());
                    commit.setAuthor(commitObject.get("commit").getAsJsonObject().get("author").getAsJsonObject().get("name").getAsString());
                    commit.setDate(commitObject.get("commit").getAsJsonObject().get("author").getAsJsonObject().get("date").getAsString());
                    commit.setMessage(commitObject.get("commit").getAsJsonObject().get("message").getAsString());
 
                    commits.add(commit);
                }
            } else {
                System.out.println("Error en la solicitud: " + connection.getResponseCode());
            }
        } catch(Exception e) {
            e.printStackTrace();
        }

        return commits;
    }

    private class Commit {
        private String hash;
        private String author;
        private String message;
        private String date;

        public void setHash(String hash) {
            this.hash = hash;
        }

        public void setAuthor(String author) {
            this.author = author;
        }

        public void setMessage(String message) {
            this.message = message;
        }

        public void setDate(String date) {
            this.date = date;
        }

        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder();

            //Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
            sb.append(hash);
            sb.append(" | ");
            sb.append(author);
            sb.append(" | ");
            sb.append(message);
            sb.append(" | ");
            sb.append(date);

            return sb.toString();
        }
    }
}