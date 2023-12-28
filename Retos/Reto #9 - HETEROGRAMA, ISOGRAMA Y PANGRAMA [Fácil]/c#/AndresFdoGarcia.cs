using System.Text;

namespace Reto8;
class Program
{
    static void Main(string[] args)
    {
        List<string> test = new List<string>{
            "Un jugoso zumo de piña y kiwi bien frío es exquisito y no lleva alcohol",
            "mamá",            
            "yuxtaponer"
        };
        for(int i =0; i<test.Count;i++){
            Console.WriteLine($" -- Ejemplo {i+1}: "+ test[i]);
            var intermedio = frecuencias(test[i].ToLower());            
            Console.WriteLine(heterograma(intermedio));
            Console.WriteLine(isograma(intermedio));
            Console.WriteLine(pangrama(intermedio));
            Console.WriteLine("");
        }        
    }

    public static int[] frecuencias(string s)
    {
        Encoding utf8 = Encoding.UTF8;
        int[] frecuencia = new int[256];
        string e = s.Normalize(NormalizationForm.FormD);
        foreach(char c in e){
            if(char.IsLetter(c))
            {
                byte[] bytes = utf8.GetBytes(new[] { c });
                char letra = utf8.GetString(bytes)[0];
                frecuencia[letra]++;
            }
        }
        return frecuencia;
    }

    public static string heterograma(int[] data)
    {
        bool evaluado = data.Where(x => x > 0).Select(x => x).All(x => x == 1);
        if(evaluado){
            return "Es un heterograma";
        }
        else{
            return "NO es un heterograma";
        }
    }

    public static string isograma(int[] data)
    {
        bool evaluado = data.Where(x => x > 0).GroupBy(x => x).Select(g => g.Count()).Distinct().Count() == 1;
        if(evaluado){
            return "Es un isograma";
        }
        else{
            return "NO es un isograma";
        }
    }

    public static string pangrama(int[] data)
    {
        var range = new Range(97,123);
        bool evaluado = data[range].All(x => x != 0);        
        if(evaluado){
            return "Es un pangrama";
        }
        else{
            return "NO es un pangrama";
        }
    }

}
