var mapaLenguaje = new Dictionary<string, string>(){
    {"a", "4"},
    {"b", "I3"},
    {"c", "["},
    {"d", ")"},
    {"e", "3"},
    {"f", "|="},
    {"g", "&"},
    {"h", "#"},
    {"i", "1"},
    {"j", ",_|"},
    {"k", ">|"},
    {"l", "1"},
    {"m", @"/\/\"},
    {"n", "^/"},
    {"o", "0"},
    {"p", "|*"},
    {"q", "(_,)"},
    {"r", "I2"},
    {"s", "5"},
    {"t", "7"},
    {"u", "(_)"},
    {"v", @"\/"},
    {"w", @"\/\/"},
    {"x", "><"},
    {"y", "j"},
    {"z", "2"}
};

string frase = Console.ReadLine();
string lenguajeHacker = "";

foreach (var caracter in frase)
{
    foreach (var map in mapaLenguaje)
    {
        if (map.Key == caracter.ToString().ToLower())
        {
            lenguajeHacker += map.Value;
        }
    }
}
Console.WriteLine(lenguajeHacker);
