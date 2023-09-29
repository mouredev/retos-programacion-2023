string txtOriginal = "mi nombre es grilloneithor";
string txtAlterado = "mI nombro es gri110neith0r";
List<string> caracteres = new List<string>();

for (int i = 0; i < txtOriginal.Length; i++)
{
    if (txtOriginal.Substring(i, 1) != txtAlterado.Substring(i, 1)) caracteres.Add(txtAlterado.Substring(i, 1)); 
}
  
Console.WriteLine(string.Concat(txtOriginal, " / ", txtAlterado, " -> ", string.Concat(caracteres)));