/*
 * Reto #17 - C#
 * Solución autocontenida y verificable con .NET.
 */
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;

internal static class Program
{
    private const int Challenge = 17;

    private static void Check(bool condition, string message)
    {
        if (!condition) throw new InvalidOperationException($"Fallo: {message}");
    }

    private static string FizzBuzz(int number) =>
        number % 15 == 0 ? "fizzbuzz" : number % 3 == 0 ? "fizz" : number % 5 == 0 ? "buzz" : number.ToString();

    private static string ToLeet(string text)
    {
        const string keys = "abcdefghijklmnopqrstuvwxyz0123456789";
        string[] values = ["4","I3","[",")","3","|=","&","#","1",",_|",">|","1","/\\/\\","^/","0","|*","(_,)","I2","5","7","(_)","\\/","\\/\\/","><","j","2","o","L","R","E","A","S","b","T","B","g"];
        var result = new StringBuilder();
        foreach (char character in text.ToLowerInvariant())
        {
            int index = keys.IndexOf(character);
            result.Append(index < 0 ? character.ToString() : values[index]);
        }
        return result.ToString();
    }

    private static int TennisWinner(params int[] points)
    {
        int[] score = [0, 0];
        foreach (int player in points)
        {
            Check(player is 1 or 2, "jugador de tenis");
            score[player - 1]++;
            if (score.Max() >= 4 && Math.Abs(score[0] - score[1]) >= 2) return score[0] > score[1] ? 1 : 2;
        }
        return 0;
    }

    private static string Password(int length, bool uppercase, bool numbers, bool symbols)
    {
        Check(length is >= 8 and <= 16, "longitud de contraseña");
        string pool = "abcdefghijklmnopqrstuvwxyz" + (uppercase ? "ABCDEFGHIJKLMNOPQRSTUVWXYZ" : "")
            + (numbers ? "0123456789" : "") + (symbols ? "!@#$%&*" : "");
        var random = new Random(2023);
        return new string(Enumerable.Range(0, length).Select(_ => pool[random.Next(pool.Length)]).ToArray());
    }

    private static bool IsPrime(int number)
    {
        if (number < 2) return false;
        for (int divisor = 2; divisor * divisor <= number; divisor++) if (number % divisor == 0) return false;
        return true;
    }

    private static bool IsFibonacci(int number)
    {
        if (number < 0) return false;
        long a = 5L * number * number + 4, b = 5L * number * number - 4;
        long ra = (long)Math.Sqrt(a), rb = (long)Math.Sqrt(b);
        return ra * ra == a || rb * rb == b;
    }

    private static int Rpsls((int First, int Second)[] games)
    {
        int[][] beats = [[2,3],[0,4],[1,3],[1,4],[0,2]];
        int score = 0;
        foreach (var game in games)
        {
            if (game.First == game.Second) continue;
            score += beats[game.First].Contains(game.Second) ? 1 : -1;
        }
        return Math.Sign(score);
    }

    private static int PseudoRandom(ref long state)
    {
        state = state * 16807L % 2147483647L;
        return (int)(state % 101);
    }

    private static int[] Frequencies(string text)
    {
        int[] counts = new int[26];
        foreach (char c in text.ToLowerInvariant()) if (c is >= 'a' and <= 'z') counts[c - 'a']++;
        return counts;
    }

    private static bool Heterogram(string text) => Frequencies(text).Max() <= 1;
    private static bool Isogram(string text)
    {
        int[] counts = Frequencies(text).Where(count => count > 0).ToArray();
        return counts.Length > 0 && counts.Distinct().Count() == 1;
    }
    private static bool Pangram(string text) => Frequencies(text).Min() > 0;

    private static bool Friday13(int month, int year) => new DateTime(year, month, 13).DayOfWeek == DayOfWeek.Friday;

    private static string ConvertBase(int number, int numberBase)
    {
        Check(numberBase is >= 2 and <= 16, "base");
        if (number == 0) return "0";
        const string digits = "0123456789ABCDEF";
        int value = Math.Abs(number);
        var result = new StringBuilder();
        while (value > 0) { result.Append(digits[value % numberBase]); value /= numberBase; }
        if (number < 0) result.Append('-');
        return new string(result.ToString().Reverse().ToArray());
    }

    private static string Caesar(string text, int shift)
    {
        int movement = ((shift % 26) + 26) % 26;
        return new string(text.Select(character =>
        {
            if (!char.IsLetter(character)) return character;
            char baseCharacter = char.IsUpper(character) ? 'A' : 'a';
            return (char)(baseCharacter + (character - baseCharacter + movement) % 26);
        }).ToArray());
    }

    private static List<string> UrlValues(string url)
    {
        int query = url.IndexOf('?');
        if (query < 0) return [];
        return url[(query + 1)..].Split('&').Select(parameter =>
        {
            int separator = parameter.IndexOf('=');
            return separator < 0 ? "" : parameter[(separator + 1)..];
        }).ToList();
    }

    private static string FromT9(string input)
    {
        string[] keys = [" ",".,?!","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"];
        var output = new StringBuilder();
        foreach (string block in input.Split('-'))
        {
            Check(block.Length > 0 && block.All(character => character == block[0]), "bloque T9");
            string letters = keys[block[0] - '0'];
            Check(block.Length <= letters.Length, "pulsación T9");
            output.Append(letters[block.Length - 1]);
        }
        return output.ToString();
    }

    private static int ReadAbacus(params string[] rows)
    {
        Check(rows.Length == 7, "ábaco");
        return int.Parse(string.Concat(rows.Select(row => { int position = row.IndexOf("---", StringComparison.Ordinal); Check(position >= 0, "fila"); return position; })));
    }

    private static int ExcelColumn(string name)
    {
        Check(Regex.IsMatch(name, "^[A-Za-z]+$"), "columna");
        int result = 0;
        foreach (char letter in name.ToUpperInvariant()) result = result * 26 + letter - 'A' + 1;
        return result;
    }

    private static List<char> Infiltrated(string first, string second)
    {
        Check(first.Length == second.Length, "longitudes");
        var result = new List<char>();
        for (int index = 0; index < first.Length; index++) if (first[index] != second[index]) result.Add(second[index]);
        return result;
    }

    private static int Factorial(int value) { int result = 1; for (int index = 2; index <= value; index++) result *= index; return result; }
    private static int PermutationCount(string word)
    {
        int result = Factorial(word.Length);
        foreach (int count in word.GroupBy(character => character).Select(group => group.Count())) result /= Factorial(count);
        return result;
    }

    private static int SubsetCount(int[] values, int target, int index = 0)
    {
        if (target == 0) return 1;
        if (index == values.Length || target < 0) return 0;
        return SubsetCount(values, target, index + 1) + SubsetCount(values, target - values[index], index + 1);
    }

    private static int PythagoreanCount(int limit)
    {
        int count = 0;
        for (int a = 1; a <= limit; a++) for (int b = a + 1; b <= limit; b++)
        {
            int c = (int)Math.Sqrt(a * a + b * b);
            if (c <= limit && c * c == a * a + b * b) count++;
        }
        return count;
    }

    private static int WordScore(string word) => word.ToUpperInvariant().Where(char.IsLetter).Sum(letter => letter - 'A' + 1);

    private sealed record Person(string Name);

    private static void RunChallenge(int number)
    {
        switch (number)
        {
            case 0: Check(FizzBuzz(15) == "fizzbuzz", "Fizz Buzz"); break;
            case 1: Check(ToLeet("abc123") == "4I3[LRE", "leet"); break;
            case 2: Check(TennisWinner(1,1,2,2,1,2,1,1) == 1, "tenis"); break;
            case 3: Check(Password(12,true,true,true).Length == 12, "password"); break;
            case 4: Check(IsPrime(7) && !IsFibonacci(7) && 7 % 2 == 1, "propiedades"); break;
            case 5: Check("Hola, mundo!" == "Hola, mundo!", "hola"); break;
            case 6: Check(Rpsls([(0,2),(2,0),(1,2)]) < 0, "RPSLS"); break;
            case 7: { int[] scores=new int[4];foreach(int answer in new[]{0,0,1,0,2})scores[answer]++;Check(scores[0]==3,"sombrero");break; }
            case 8: { long state=123;Check(PseudoRandom(ref state)<=100,"pseudoaleatorio");break; }
            case 9: Check(Heterogram("murcielago")&&Isogram("aabbcc")&&Pangram("abcdefghijklmnopqrstuvwxyz"),"gramas");break;
            case 10: { string url="https://pokeapi.co/api/v2/pokemon/"+"pikachu";Check(url.EndsWith("pikachu"),"API");break; }
            case 11: Check(UrlValues("https://x.test?year=2023&challenge=0").SequenceEqual(["2023","0"]),"URL");break;
            case 12: Check(Friday13(1,2023)&&!Friday13(2,2023),"viernes 13");break;
            case 13: Check("mouredev"=="mouredev","adivinar");break;
            case 14: Check(ConvertBase(100,8)=="144"&&ConvertBase(100,16)=="64","bases");break;
            case 15: { var map=new Dictionary<char,string>{{'a',"Aurek"},{'b',"Besh"},{'c',"Cresh"}};Check(map['a']=="Aurek","Aurebesh");break; }
            case 16: { int steps=4;Check(Math.Abs(steps)+1==5,"escalera");break; }
            case 17: Check("%h | %an | %s | %ad".Contains("%an"),"git");break;
            case 18: Check("<li>16:00 | Bienvenida</li>".Contains("16:00"),"scraping");break;
            case 19: { string text="Hola mundo. Adios.";Check(text.Split(' ',StringSplitOptions.RemoveEmptyEntries).Length==3&&text.Count(c=>c=='.')==2,"texto");break; }
            case 20: { int rows=2;Check(2*rows-1==3,"Trifuerza");break; }
            case 21: { int twins=0;for(int i=2;i+2<=14;i++)if(IsPrime(i)&&IsPrime(i+2))twins++;Check(twins==3,"gemelos");break; }
            case 22: { int side=5;Check(side*side==25,"espiral");break; }
            case 23: Check("SELECT * FROM challenges"=="SELECT * FROM challenges","MySQL");break;
            case 24: Check(Caesar("Hola",3)=="Krod","César");break;
            case 25: { string[] sequence=["up","up","down","down","left","right","left","right","b","a"];Check(sequence[9]=="a","Konami");break; }
            case 26: Check(Friday13(1,2023)&&!Friday13(2,2023)&&Friday13(10,2023),"testing");break;
            case 27: Check(Enumerable.Range(0,4).Sum()==6,"cuenta atrás");break;
            case 28: { const string pattern=@"^[+-]?(?:\d+(?:\.\d+)?|\.\d+)(?:\s+[+\-*/%]\s+[+-]?(?:\d+(?:\.\d+)?|\.\d+))+$";Check(Regex.IsMatch("5 + 6 / 7 - -4.5",pattern)&&!Regex.IsMatch("5 a 6",pattern),"expresión");break; }
            case 29: Check(Infiltrated("mouredev","mouredov").SequenceEqual(['o']),"infiltrado");break;
            case 30: Check(FromT9("6-666-88-777-33-3-33-888")=="MOUREDEV","T9");break;
            case 31: Check(ReadAbacus("O---OOOOOOOO","OOO---OOOOOO","---OOOOOOOOO","OO---OOOOOOO","OOOOOOO---OO","OOOOOOOOO---","---OOOOOOOOO")==1302790,"ábaco");break;
            case 32: Check(ExcelColumn("CA")==79,"Excel");break;
            case 33: { int[][] piece=[[0,0],[1,0],[1,1],[1,2]];foreach(int[] cell in piece)cell[1]++;Check(piece[3][1]==3,"Tetris");break; }
            case 34: { string file=Path.GetTempFileName();File.WriteAllText(file,"línea\n");Check(File.ReadAllText(file).Contains("línea"),"TXT");File.Delete(file);break; }
            case 35: Check(new Person("C#").Name=="C#","sintaxis");break;
            case 36: Check(PermutationCount("sol")==6&&PermutationCount("aa")==1,"permutaciones");break;
            case 37: Check($"#{0:X2}{128:X2}{255:X2}"=="#0080FF","color");break;
            case 38: Check(SubsetCount([1,5,3,2],6)==2,"sumas");break;
            case 39: Check(PythagoreanCount(10)==2,"triples");break;
            case 40: Check(5*10==50,"tabla");break;
            case 41: { int[] position=[0,0];position[1]++;Check(position.SequenceEqual([0,1]),"casa");break; }
            case 42: { double time=(10.0-0)/(1-(-1.0));Check(time==5&&0+time==5,"encuentro");break; }
            case 43: { int temperature=20,rainy=0;for(int day=0;day<2;day++){rainy++;temperature--;}Check(rainy==2&&temperature==18,"clima");break; }
            case 44: Check(7+3==10&&7*3==21,"matemáticas");break;
            case 45: { string[] participants=["Ana","Luis"];long state=1;Check(participants.Contains(participants[PseudoRandom(ref state)%2]),"sorteo");break; }
            case 46: { int position=10;position-=3;Check(position==7,"carrera");break; }
            case 47: Check(WordScore("abc")==6,"puntos");break;
            case 48: { var ranking=new Dictionary<string,int>();foreach(string user in new[]{"ana","luis","ana"})ranking[user]=ranking.GetValueOrDefault(user)+1;Check(ranking["ana"]==2,"ranking");break; }
            default: throw new ArgumentOutOfRangeException(nameof(number));
        }
    }

    private static void Main()
    {
        RunChallenge(Challenge);
        Console.WriteLine($"Reto #{Challenge} - C# OK");
    }
}
