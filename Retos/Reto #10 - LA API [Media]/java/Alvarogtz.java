import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Alvarogtz {
    public static void main(String[] args){
        System.out.println("------ POKEDEX EVOLUCIONES ------");
        Scanner sc = new Scanner(System.in);
        String response = "";
        String pokemon = "";
        do {
            System.out.println("Introduce pokemon o su numero en la pokedex: ");
            pokemon = sc.nextLine().trim();
            if(!pokemon.equals("")) {
                response = response("https://pokeapi.co/api/v2/pokemon-species/" + pokemon);
                if(!response.equals("")) {
                    String urlEvolution = getUrlEvolution(response);
                    response = response(urlEvolution);
                    printEvolutions(response, pokemon);
                }
            }
        }while(!pokemon.trim().equals(""));

    }

    private static String getUrlEvolution(String content) {
        String[] json = content.split("},");
        String urlEvolution = "";
        for(String a : json){
            if(a.contains("evolution_chain")) {
                a = a.substring(a.indexOf("evolution_chain"),a.length()-1).replace("\"","");
                return a.substring(a.indexOf("url"),a.length()-1).replace("url:","");
            }
        }

        return urlEvolution;
    }

    private static void printEvolutions(String content,String pokemon) {
        Pattern codePattern = Pattern.compile("\"species\":\\{\"name\".*\",");
        Matcher code_matcher = codePattern.matcher(content);
        boolean has_evolution = false;

        if (code_matcher.find() ) {
            String[] evolutions = code_matcher.group(0).split(",");
            System.out.println("-> " + pokemon.toUpperCase());
            for(String evolution : evolutions) {
                if(evolution.contains("\"name\"") && !evolution.toUpperCase().contains(pokemon.toUpperCase())) {
                    has_evolution = true;
                    evolution = evolution.substring(evolution.indexOf("\":\""),evolution.length()-1).replace("\":\"","");
                    System.out.println("- " + evolution.toUpperCase());
                }
            }
        }

        if(!has_evolution)
            System.out.println(pokemon.toUpperCase() + " NO tiene más formas .... =(");
    }

    public static String response(String path){

        URL url = null;
        String response = "";
        try {
            url = new URL(path);
            HttpURLConnection con = (HttpURLConnection) url.openConnection();
            con.setRequestMethod("GET");
            con.setRequestProperty("Content-Type", "application/json");
            con.setConnectTimeout(5000);
            con.setReadTimeout(5000);
            BufferedReader in = new BufferedReader(
                    new InputStreamReader(con.getInputStream()));
            String inputLine;
            StringBuffer content = new StringBuffer();
            while ((inputLine = in.readLine()) != null) {
                content.append(inputLine);
            }
            in.close();
            con.disconnect();
            return content.toString();

        } catch (Exception e) {
            System.out.println("Pokemon no encontrado");
        }
        return response;
    }
}
