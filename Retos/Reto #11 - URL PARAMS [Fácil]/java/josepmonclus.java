import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

public class josepmonclus {

    Scanner entrada = new Scanner(System.in);

    String url = "";

    public static void main(String[] args) {
        josepmonclus josepmonclus = new josepmonclus();

        josepmonclus.getUrl();

        for(Map.Entry<String, String> entry : josepmonclus.getUrlParameters().entrySet()){
            System.out.println(entry.getKey() + " : " + entry.getValue());
        }
    }

    private Map<String, String> getUrlParameters() {
        String[] params = url.split("\\?")[1].split("&");

        Map<String, String> paramsMap = new HashMap();
        for(String param : params) {
            paramsMap.put(param.split("=")[0], param.split("=")[1]);
        }

        return paramsMap;
    }

    private void getUrl() {
        System.out.println("Introduce la url:");

        url = entrada.nextLine();
    }
}
