import java.util.ArrayList;
import java.util.List;

public class UrlUtils {

    public String[] getParams(String url){

        List<String> params = new ArrayList<>();
        int indexQuestionMark = url.indexOf("?");

        if (indexQuestionMark != -1) {
            String parametersUrl = url.substring(indexQuestionMark + 1);
            String[] pairParameters = parametersUrl.split("&");

            for (String pairParam : pairParameters) {
                String[] part = pairParam.split("=");
                if (part.length == 2) {
                    params.add(part[1]);
                }
            }

        }

        return params.toArray(new String[0]);

    }

}
