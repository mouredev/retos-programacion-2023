import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class PasswordGenerator 
{
	private static Map<Integer, String> letters;
	private static Map<Integer, String> symbols;
	
	public static void initializeAlphabets()
	{
		letters = new HashMap<Integer, String>();
		symbols = new HashMap<Integer, String>();
		
		char [] lett = "abcdefghijklmnopqrstuvwxyz".toCharArray();
		
		for (int i = 0; i < lett.length; i++)
		{
			letters.put(i, String.valueOf(lett[i]));
		}
		
		char [] sym = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~".toCharArray();
		
		for (int i = 0; i < sym.length; i++)
		{
			symbols.put(i, String.valueOf(sym[i]));
		}
	}
	
	public static String generatePassword(int size, boolean capLetters, boolean num, boolean sym)
	{
		if (size > 7 && size < 17)
		{
			
			String newPassword = new String();
			Random r = new Random();
			Random cL = new Random();
			Map<Integer, String> alphabet = letters;
			int s = alphabet.size();
			
			if (num)
			{	
				for (int i = 0; i < 10; i++)
				{
					alphabet.put(s, String.valueOf(i));
					s++;
				}
			}
			
			if (sym)
			{
				for (int i = 0; i < symbols.size(); i++)
				{
					alphabet.put(s, symbols.get(i));
					s++;
				}
			}
			
			for (int i = 0; i < size; i++)
			{
				String c = alphabet.get(r.nextInt(alphabet.size()));
				
				if (capLetters)
				{
					boolean isCap = cL.nextBoolean();
					
					if (isCap)
					{
						c = c.toUpperCase();
					}
				}
				
				newPassword += c;
			}
			
			return newPassword;
		}
		else
		{
			return "The password must have between 8 and 16 characters!";
		}
	}
	
	public static void main(String[] args)
	{
		int size = 12;
		boolean capitalLetters = true;
		boolean numbers = true;
		boolean symbols = true;
		
		initializeAlphabets();
		String pwd = generatePassword(size, capitalLetters, numbers, symbols);
		System.out.println(pwd);
	}
}