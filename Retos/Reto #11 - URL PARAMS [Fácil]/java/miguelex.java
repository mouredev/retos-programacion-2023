import java.util.ArrayList;
import java.util.List;

public class miguelex {

    public static Object findParameters(String url) {
        List<String> params = new ArrayList<>();

        String[] urlDividida = url.split("\\?");

        if (urlDividida.length > 1) {
            String[] listaParams = urlDividida[1].split("&");

            for (String param : listaParams) {
                String[] clearParam = param.split("=");
                if (clearParam.length > 1 && !clearParam[1].equals("")) {
                    params.add(clearParam[1]);
                } else {
                    return "La cadena no tiene parametros validos";
                }
            }

            return params;
        } else {
            return "La cadena no tiene parametros";
        }
    }

    public static void main(String[] args) {
        System.out.println(findParameters("https://retosdeprogramacion.com?year=2023&challenge=0"));
        System.out.println(findParameters("https://retosdeprogramacion.com"));
        System.out.println(findParameters("https://retosdeprogramacion.com?"));
        System.out.println(findParameters("https://retosdeprogramacion.com?year=2023"));
        System.out.println(findParameters("https://retosdeprogramacion.com?year=2023&"));
        System.out.println(findParameters("https://retosdeprogramacion.com?year=&"));
        System.out.println(findParameters("https://retosdeprogramacion.com?year=2023&challenge=0&languaje=python"));
    }
}
