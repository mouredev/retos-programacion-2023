/*
# Reto #9: Heterograma, isograma y pangrama
#### Dificultad: Fácil | Publicación: 27/02/23 | Corrección: 06/03/23

## Enunciado
*/

/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

//Heterograma: Un heterograma es una palabra o frase en la que cada letra del alfabeto aparece una sola vez.

string word = "Fabio me exige, sin tapujos, que añada cerveza al whisky";
Console.Write($@"{(IsHeterograma(word) ? "Es heterograma" : "No es heterograma")}, 
{(IsIsograma(word)? "es isograma":"no es isograma")}, {(IsPangrama(word) ? "Es pangrama" : "No es pangrama")}");


bool IsHeterograma(string text) => IsRepeatedLetters(text) && IsPangrama(text);

bool IsIsograma(string text) => IsRepeatedLetters(text);

bool IsPangrama(string text)
{
    text = RemoverAccents(text);

    for (int c = 97; c < 123; c++)
        if (!text.Contains((char)c))
            return false;
    
    return true;
}

bool IsRepeatedLetters(string text)
{
    text = RemoverAccents(text);
    int countCharacter = 0;
    for (int c = 97; c < 123; c++)
    {
        foreach (var t in text)
            if (t == (char)c) countCharacter++;
        
        if (countCharacter > 1) return false;
        else countCharacter = 0;
    }
    return true;
}

string RemoverAccents(string text)
{
    string[] vowelsWithAccents = new[] { "á", "é", "í", "ó", "ú" };
    string[] vowelsWithoutAccents = new[] { "a", "e", "i", "o", "u" };
    string newText = text.ToLower();

    for (int c = 0; c < 5; c++)
        newText = newText.Replace(vowelsWithAccents[c], vowelsWithoutAccents[c]);
    
    return newText;
}