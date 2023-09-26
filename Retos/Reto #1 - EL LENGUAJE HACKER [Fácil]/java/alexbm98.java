import java.util.HashMap;
import java.util.Map;

public class alexbm98
{
	private static Map<String,String> dicc = new HashMap<>();
	
	public static void createDicc()
	{
		dicc.put("a","4");
        dicc.put("b","I3");
        dicc.put("c","[");
        dicc.put("d",")");
        dicc.put("e","3");
        dicc.put("f","|=");
        dicc.put("g","&");
        dicc.put("h","#");
        dicc.put("i","1");
        dicc.put("j",",_|");
        dicc.put("k",">|");
        dicc.put("l","1");
        dicc.put("m","/\\/\\");
        dicc.put("n","^/");
        dicc.put("o","0");
        dicc.put("p","|*");
        dicc.put("q","(_,)");
        dicc.put("r","I2");
        dicc.put("s","5");
        dicc.put("t","7");
        dicc.put("u","(_)");
        dicc.put("v","\\/");
        dicc.put("w","\\/\\/");
        dicc.put("x","><");
        dicc.put("y","j");
        dicc.put("z","2");
        dicc.put("0", "o");
        dicc.put("1", "L");
        dicc.put("2", "R");
        dicc.put("3", "E");
        dicc.put("4", "A");
        dicc.put("5", "S");
        dicc.put("6", "b");
        dicc.put("7", "T");
        dicc.put("8", "B");
        dicc.put("9", "g");
	}
	
	public static String translateText(String text)
    {
		createDicc();
		
        String translatedText = new String();

        for (int i = 0; i < text.length(); i++)
        {        	        	
        	String c = String.valueOf(text.charAt(i));
        	        	
        	if (dicc.get(c.toLowerCase()) != null)
        	{
        		translatedText += dicc.get(c.toLowerCase());
        	}
        	else
        	{
        		translatedText += c;
        	}
        }
        
        return translatedText;
    }
	
	public static void main(String[] args)
	{
		String text = "Hi! I am Alejandro and I am 24 years old.";
		String translatedText = translateText(text);
		System.out.print(translatedText);
	}
}