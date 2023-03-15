import java.util.ArrayList;

public class Qv1ko {

    public static void main(String[] args) {
        getParameters("https://retosdeprogramacion.com?year=2023&challenge=0");
    }//main

    private static void getParameters(String url) {
        ArrayList<String> parameters=new ArrayList<String>();
        String parameter="";
        boolean add=false;
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
        System.out.println(parameters.toString());
    }//getParameters

}//class