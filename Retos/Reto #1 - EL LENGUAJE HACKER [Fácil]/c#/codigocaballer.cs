using System;
using System.Collections.Generic;
using System.Linq;


abstract class LeetSpeak{
	private readonly Dictionary<string, string> leetAlphabet;
	private readonly Dictionary<string, string> leetNumbers = new Dictionary<string, string>{
		{"1","L"},{"2","R"},{"3","E"},{"4","A"},{"5","S"},{"6","b"},
		{"7","T"},{"8","B"},{"9","g"},{"0","o"}		
	};
	

	protected LeetSpeak(Dictionary<string, string> modelAlphabet){
		this.leetAlphabet = modelAlphabet;
	}

	public string translate(string plainText){
		string leetChar = "", inputChar ="", result = "";		

		foreach(char c in plainText){
			inputChar = c.ToString();
			
			try{
				if (c>=48 && c<=57)
					leetChar = leetNumbers[inputChar];
				else if (c>=65 && c<=90){
					inputChar = inputChar.ToLower();
					leetChar = leetAlphabet[inputChar];
				}
				else if (c>=97 && c<=122)		
					leetChar = leetAlphabet[inputChar];				
				else
					leetChar = inputChar;				
			} catch
			{
				leetChar = inputChar;
			}			
			result+=leetChar;
		}
		
		return result;		
	}
}

class LeetSpeakBasic : LeetSpeak{

	public LeetSpeakBasic() : base(new Dictionary<string, string>
	{
		{"a", "4"},{"e", "3"},{"i", "1"},{"o", "0"},{"u", "(_)"}		
	}) {}
}

class LeetSpeakAdvanced : LeetSpeak{

	public LeetSpeakAdvanced() : base(new Dictionary<string, string>
	{
		{"a", "@"},{"b", "!3"},{"c", "<"},{"d", "[)"},{"e", "e"},{"f", "|=_"},
		{"g", "(_+"},{"h", "#"},{"i", "!"},{"j", "_|"},{"k", "|<"},{"l", "|_"},
		{"m", @"]\/["},{"n", @"[\]"},{"ñ", "ñ"},{"o", "[]"},{"p", "|º"},{"q", "9"},
		{"r", "12"},{"s", "5"},{"t", "']['"},{"u", "|_|"},{"v", @"\/"},{"w", @"\_:_/"},
		{"x", "><"},{"y", @"\/"},{"z", "-/_"}
	}) {}
}

class LeetSpeakIntermediate : LeetSpeak{

	public LeetSpeakIntermediate() : base(new Dictionary<string, string>
	{
		{"a", "4"},{"b", "I3"},{"c", "["},{"d", "|)"},{"e", "3"},{"f", "ph"},
		{"g", "6"},{"h", "#"},{"i", "1"},{"j", "]"},{"k", "|<"},{"l", "1"},
		{"m", @"/\/\"},{"n", @"|\|"},{"ñ", "ñ"},{"o", "0"},{"p", "|>"},{"q", "0_"},
		{"r", "I2"},{"s", "5"},{"t", "7"},{"u", "(_)"},{"v", @"\/"},{"w", @"\/\/"},
		{"x", "><"},{"y", "j"},{"z", "2"}	
	}) {}
}

class LeetSpeakFullRetard : LeetSpeak{

	public LeetSpeakFullRetard() : base(new Dictionary<string, string>
	{
		{"a", @"/\"},{"b", "!3"},{"c", "©"},{"d", "|}"},{"e", "€"},{"f", "ph"},
		{"g", "gee"},{"h", "1-1"},{"i", "!"},{"j", "_|"},{"k", "|{"},{"l", "|_"},
		{"m", @"]\/["},{"n", @"<\>"},{"ñ", "ñ"},{"o", "oh"},{"p", "|º"},{"q", "2"},
		{"r", "12"},{"s", "es"},{"t", "†"},{"u", "µ"},{"v", "|/"},{"w", "\'"},
		{"x", "×"},{"y", @"\|/"},{"z", "7_"}	
	}) {}
}

public class Reto1{	
	public const string TestInputText =        @"abcdefghijklmnñopqrstuvwxyz1234567890=?¿_:,<ºª!|·#$~%&¬/()+*ç-";
	public const string TestBasicOutputText =  @"4bcd3fgh1jklmnñ0pqrst(_)vwxyzLREASbTBgo=?¿_:,<ºª!|·#$~%&¬/()+*ç-";	

	public const string TestAdvancedOutputText =  @"@!3<[)e|=_(_+#!_||<|_]\/[[\]ñ[]|º9125']['|_|\/\_:_/><\/-/_LREASbTBgo=?¿_:,<ºª!|·#$~%&¬/()+*ç-";			
	
	public const string TestIntermediateOutputText =  @"4I3[|)3ph6#1]|<1/\/\|\|ñ0|>0_I257(_)\/\/\/><j2LREASbTBgo=?¿_:,<ºª!|·#$~%&¬/()+*ç-";
	public const string TestFullRetardOutputText =  @"/\!3©|}€phgee1-1!_||{|_]\/[<\>ñoh|º212es†µ|/'×\|/7_LREASbTBgo=?¿_:,<ºª!|·#$~%&¬/()+*ç-";	                                                  	
	                                                 	                		
	public const string TestInputTextUpper =   @"ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890=?¿_:,<ºª!|·#$~%&¬/()+*Ç-";												 
	public const string TestBasicOutputUpper = @"4bcd3fgh1jklmnÑ0pqrst(_)vwxyzLREASbTBgo=?¿_:,<ºª!|·#$~%&¬/()+*Ç-";	

	static void test(){			
		LeetSpeak leetSpeakBasic = new LeetSpeakBasic();			
		Console.WriteLine("TestBasic Lower: ¿Passed Test? {0}",leetSpeakBasic.translate(TestInputText).Equals(TestBasicOutputText));					
		Console.WriteLine("TestBasic Upper: ¿Passed Test? {0}\n",leetSpeakBasic.translate(TestInputTextUpper).Equals(TestBasicOutputUpper));		

		LeetSpeakAdvanced leetSpeakAdvanced = new LeetSpeakAdvanced();
		Console.WriteLine("TestAdvanced Lower: ¿Passed Test? {0}",leetSpeakAdvanced.translate(TestInputText).Equals(TestAdvancedOutputText));

		LeetSpeakIntermediate leetSpeakIntermediate =  new LeetSpeakIntermediate();
		Console.WriteLine("TestIntermediate Lower: ¿Passed Test? {0}",leetSpeakIntermediate.translate(TestInputText).Equals(TestIntermediateOutputText));

		LeetSpeakFullRetard leetSpeakFullRetard =  new LeetSpeakFullRetard();
		//.Equals(TestIntermediateOutputText
		Console.WriteLine("TestFullRetard Lower: ¿Passed Test? {0}",leetSpeakFullRetard.translate(TestInputText).Equals(TestFullRetardOutputText));
	}
	
	
	public static void Main(){
		string text = "", textLevel = "";
		bool validText = false, validLevel = false;
		Console.WriteLine("---------------------------------\n|TEXT TO HACKER LANGUAGE ENCODER|\n---------------------------------\n");			

		Reto1.test();
		
		do{
			Console.Write("\nInsert a plain text to transform to Leet Mixed Level: ");
			text = Console.ReadLine();
			validText = (text.Length > 0);
			if (!validText) Console.WriteLine("ERROR: Please insert a valid text\n");
		} while(!validText);


		int level = 0;
		
		do{
			Console.WriteLine("\nInsert the encoding level to transform to Leet Mixed Level: ");
			Console.WriteLine("1.-Basic Level\t       2.-Advanced Level");			
			Console.WriteLine("3.-Intermediate Level\t4.-FullRetard Level\n");			
			textLevel = Console.ReadLine();
			validLevel = int.TryParse(textLevel, out level) && level > 0 && level <=4;			
			if (!validLevel) Console.WriteLine("ERROR: Please insert a valid level\n");
		} while(!validLevel);


		LeetSpeak leetSpeak = null;
		switch(level){
			case 1:
				leetSpeak = new LeetSpeakBasic();
				break;
			case 2:
				leetSpeak = new LeetSpeakAdvanced();
				break;				
			case 3:
				leetSpeak = new LeetSpeakIntermediate();
				break;		
			case 4:
				leetSpeak = new LeetSpeakFullRetard();
				break;				
		}		
				
		Console.WriteLine("Encoded Text:\n"+leetSpeak.translate(text));		
	}
}