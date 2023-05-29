import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class LaijieJi{
    public static void main(String[] args){
        try{
            Scanner sc = new Scanner(new File("in.txt")).useLocale(Locale.US);
            int count = 0,  maxLength = 0,
            pointCount = 0, totalLength = 0,
            tokenLength = 0;
            String token = "", largestWord = "";
            while(sc.hasNext()){
                count++;
                token = sc.next();
                tokenLength = token.length();
                totalLength += tokenLength;
                if (maxLength < tokenLength) {
                    maxLength = tokenLength;
                    largestWord = token;
                }
                if (token.contains(".")) ++pointCount;
            }
            sc.close();
            System.out.printf("There are %d words, with an average length of %d. There were %d sentences and the longest word was %s.", count,  totalLength/count, pointCount, largestWord);
        } catch (FileNotFoundException e){
            System.out.println("Archivo no encontrado");
        }
    }    
}
