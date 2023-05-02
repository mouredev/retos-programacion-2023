package reto17GitYGithub;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;

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
public class Cflorezp {


    public static void main(String[] args) throws IOException {

        String url = "https://api.github.com/repos/mouredev/retos-programacion-2023/commits?per_page=10";
        HttpURLConnection connection = (HttpURLConnection) new URL(url).openConnection();
        connection.setRequestMethod("GET");
        int responseCode = connection.getResponseCode();

        if (responseCode == 200) {
            Scanner scanner = new Scanner(connection.getInputStream());
            StringBuilder content = new StringBuilder();
            while (scanner.hasNextLine()) {
                content.append(scanner.nextLine());
            }
            scanner.close();

            Gson gson = new Gson();
            JsonArray commits = gson.fromJson(content.toString(), JsonArray.class);
            for (int i = 0; i < commits.size(); i++) {
                JsonObject commit = commits.get(i).getAsJsonObject();
                String hash = commit.get("sha").getAsString();
                String author = commit.get("commit").getAsJsonObject().get("author").getAsJsonObject().get("name").getAsString();
                String message = commit.get("commit").getAsJsonObject().get("message").getAsString();
                String date = commit.get("commit").getAsJsonObject().get("author").getAsJsonObject().get("date").getAsString();

                System.out.println("Commit " + (i + 1) + " | " + hash + " | " + author + " | " + message + " | " + date);
            }
        } else {
            System.out.println("Error al obtener los datos de la API de GitHub. Código: " + responseCode);
        }
        connection.disconnect();
    }
}
