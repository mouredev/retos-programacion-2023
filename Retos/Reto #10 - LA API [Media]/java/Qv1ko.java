import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;

public class Qv1ko {
    
    public static void main(String[] args) {
        try {
            URL url = new URL("https://api.coinpaprika.com/v1/coins/btc-bitcoin/ohlcv/latest");
            HttpURLConnection connection=(HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.connect();
            int responseCode=connection.getResponseCode();
            if(responseCode!=200) {
                throw new RuntimeException("Error "+responseCode);
            } else {
                StringBuilder data=new StringBuilder();
                Scanner sc=new Scanner(url.openStream());
                while(sc.hasNext()) {
                    data.append(sc.nextLine());
                }
                sc.close();
                System.out.println(data);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }//main

}//class