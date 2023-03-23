import java.util.ArrayList;
import java.util.Arrays;

class ycanas{
    public static ArrayList <String> getParams(String url){
        ArrayList <String> params = new ArrayList <String> (Arrays.asList(url.split("\\?")[1].split("&")));
        ArrayList <String> url_params = new ArrayList <String> ();

        params.forEach(param -> {
            url_params.add(param.split("=")[1]);
        });

        return url_params;
    }
    
    public static void main(String[] args){
        ArrayList <String> params = getParams("http://example.com?product=1234&utm_source=google");
        System.out.println(params);
    }
}
