import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Qv1ko {

    public static void main(String[] args) {
        getParameters("https://retosdeprogramacion.com?year=2023&challenge=0");
        getParametersWithSplit("https://retosdeprogramacion.com?year=2023&challenge=0");
        getParametersWithRegex("https://retosdeprogramacion.com?year=2023&challenge=0");
    }//main

    private static void getParameters(String url) {
        ArrayList<String> parameters=new ArrayList<String>();
        String parameter="";
        boolean containsParameters=false,add=false;
        for(int i=0;i<url.length();i++) {
            if(url.charAt(i)=='?') {
                containsParameters=true;
                break;
            } else {
                containsParameters=false;
            }
        }
        if(containsParameters) {
            for(int i=0;i<url.length();i++) {
                if(add&&url.charAt(i)!='&') {
                    parameter+=url.charAt(i);
                }
                if(url.charAt(i)=='=') {
                    add=true;
                    parameter+="\"";
                } else if(url.charAt(i)=='&'||url.length()-1==i) {
                    add=false;
                    parameters.add(parameter+"\"");
                    parameter="";
                }
            }
            System.out.println(parameters);
        } else {
            System.out.println("The URL has no parameters");
        }
    }//getParameters

    private static void getParametersWithSplit(String url) {
        ArrayList<String> parameters=new ArrayList<String>();
        String[] splits=url.split("&");
        if(splits.length>1) {
            for(int i=0;i<splits.length;i++) {
                if(splits[i].split("=").length==2) {
                    parameters.add("\""+splits[i].split("=")[1]+"\"");
                }
            }
            System.out.println(parameters.toString());
        } else {
            System.out.println("The URL has no parameters");
        }
    }//getParametersWithSplit

    private static void getParametersWithRegex(String url) {
        ArrayList<String> parameters=new ArrayList<String>();
        Pattern regex=Pattern.compile("=([\\w\\d-_%]+)");
        Matcher matches=regex.matcher(url);
        if(matches.find()) {
            parameters.add("\""+matches.group(1)+"\"");
            while(matches.find()) {
                parameters.add("\""+matches.group(1)+"\"");
            }
            System.out.println(parameters.toString());
        } else {
            System.out.println("The URL has no parameters");
        }
    }//getParametersWithRegex

}//class