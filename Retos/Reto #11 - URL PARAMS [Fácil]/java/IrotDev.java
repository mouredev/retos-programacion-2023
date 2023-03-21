import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * Reto11 of MoureDev: https://github.com/irotdev/retos-programacion-2023/blob/main/Retos/Reto%20%2311%20-%20URL%20PARAMS%20%5BF%C3%A1cil%5D/ejercicio.md
 * Giving a URL with params, get the values of the params.
 * Example: https://retosdeprogramacion.com?year=2023&challenge=0  --> ["2023"] ["0"]
 *
 * (*** BONUS ***: Get the keys and values of the params ) --> ['year','2023'] ['challenge','0']
 * @author José Manuel Muñoz Simó | irotdev
 * @version v1.0
 */

public class IrotDev {
    public static void main(String[] args) {
        String url = "https://retosdeprogramacion.com?year=2023&challenge=0";
        System.out.println(getParamsString(url));

        // BONUS (getting keys and value of the params)
        Map<String, String> map = getParamsMap(url);
        map.forEach((k,v) -> System.out.print("['" + k + "','" + v + "'] "));
    }

    public static String getParamsString(String url) {
        String str = "";
        String stringParams = url.substring(url.indexOf('?')+1);
        String[] arrayParams = stringParams.split("&");
        for (String arrayParam : arrayParams)
            str += "['" + arrayParam.substring(arrayParam.indexOf('=') + 1) + "'] ";

        return str;
    }


    // BONUS (getting keys and value of the params)
    public static Map<String, String> getParamsMap(String url) {
        Map<String, String> map = new HashMap<String, String>();
        String stringParams = url.substring(url.indexOf('?')+1);
        String[] arrayParams = stringParams.split("&");
        for (String arrayParam : arrayParams) {
            String[] arrayKeyValue = arrayParam.split("=");
            map.put(arrayKeyValue[0], arrayKeyValue[1]);
        }
        return map;
    }


}
