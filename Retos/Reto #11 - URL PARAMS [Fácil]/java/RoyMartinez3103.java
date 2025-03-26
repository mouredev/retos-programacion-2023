
/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */
public class RoyMartinez3103 {

    static void getParams(String url) {
        String a = url.split("\\?")[1];
        String[] b = a.split("&");
        for (String s : b) {
            System.out.println(s);
        }
    }

    public static void main(String args[]) {
        String url = "https://api.spotify.com/v1/search?q=coldplay&type=artist&limit=5";
        getParams(url);
    }
}
