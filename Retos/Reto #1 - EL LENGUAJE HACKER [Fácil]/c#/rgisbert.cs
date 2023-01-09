Dictionary<string, string> replaceAlphabet = new()
{
    { "A", "4" },
    { "B", "I3" },
    { "C", "[" },
    { "D", ")" },
    { "E", "3" },
    { "F", "|=" },
    { "G", "&" },
    { "H", "#" },
    { "I", "1" },
    { "J", ",_|" },
    { "K", ">|" },
    { "L", "1" },
    { "M", @"/\/\" },
    { "N", "^/" },
    { "O", "0" },
    { "P", "|*" },
    { "Q", "(_,)" },
    { "R", "I2" },
    { "S", "5" },
    { "T", "7" },
    { "U", "(_)" },
    { "V", "/" },
    { "W", "//" },
    { "X", "><" },
    { "Y", "j" },
    { "Z", "2" },
};


string hackerLanguage(string letter)
{
    return replaceAlphabet.ContainsKey(letter.ToUpper())
        ? replaceAlphabet[letter.ToUpper()]
        : letter;
}


string leet(string sentence, Func<string, string> fn)
{
    string res = "";
    foreach(char letter in sentence)
        res += fn(letter.ToString());

    return res;
}

string example = "Tipico Hola Mundo!";
Console.WriteLine(leet(example, hackerLanguage));