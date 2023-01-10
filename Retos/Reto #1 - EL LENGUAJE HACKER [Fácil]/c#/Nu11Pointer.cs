var leetSpeak = new Dictionary<char, string>()
{
    {'A', @"1"},      {'B', @"I3"}, {'C', @"["},   {'D', @")"},   {'E', @"3"},    {'F', @"|="},
    {'G', @"&"},      {'H', @"#"},  {'I', @"1"},   {'J', @",_|"}, {'K', @">|"},   {'L', @"1"},
    {'M', @"/\\/\\"}, {'N', @"^/"}, {'O', @"0"},   {'P', @"|*"},  {'Q', @"(_,)"}, {'R', @"I2"},
    {'S', @"5"},      {'T', @"7"},  {'U', @"(_)"}, {'V', @"\\/"}, {'W', @"\/\/"}, {'X', @"><"},
    {'Y', @"j"},      {'Z', @"2"},  {'1', @"L"},   {'2', @"R"},   {'3', @"E"},    {'4', @"A"},
    {'5', @"S"},      {'6', @"b"},  {'7', @"T"},   {'8', @"B"},   {'9', @"g"},    {'0', @"o"},
};

var toLeet = (string str) =>
{
    var result = str.Select(chr => leetSpeak.TryGetValue(char.ToUpper(chr), out _) ? leetSpeak[char.ToUpper(chr)] : chr.ToString());
    return string.Join("", result);
};

Console.WriteLine("Introduce el texto a traducir.");
Console.Write(">> ");

string request = Console.ReadLine()!;

Console.WriteLine("\nTexto traducido.");
Console.WriteLine($"> {toLeet(request)}");