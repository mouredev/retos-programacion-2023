
string ToLeet(string words)
{
    var alfabeto = "abcdefghijklmnñopqrstuvwxyz1234567890 ";

    var leet = new List<string> {"4", "I3", "[", ")", "3", "|=", "&", "#", "1", ",_|",
        ">|", "1", "/\\/\\", "^/", "^/", "0", "|*", "(_,)",  "I2", "5", "7", "(_)",
        "\\/", "\\/\\/", "><", "j", "2", "L", "R", "E", "A", "S", "b", "T", "B", "g", "o", " " };

    return
     string
     .Join("", words.ToLower().Select(c=> leet[alfabeto.IndexOf(c)]));
}