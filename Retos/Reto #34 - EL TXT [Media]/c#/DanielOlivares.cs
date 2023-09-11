using System.IO;


/*
 * Crea un programa capaz de interactuar con un fichero TXT.
 * IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección. 
 * Únicamente el código.
 * 
 * - Si no existe, debe crear un fichero llamado "text.txt".
 * - Desde el programa debes ser capaz de introducir texto por consola y guardarlo
 *   en una nueva línea cada vez que se pulse el botón "Enter".
 * - Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
 *   a continuación o borrar su contenido y comenzar desde el principio.
 * - Si se selecciona continuar escribiendo, se tiene que mostrar por consola
 *   el texto que ya posee el fichero.  
 */



#region Campos
var path = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments), "RetosProgramacion");
bool finalizado = false;
string texto = String.Empty;
string textoNuevo = String.Empty;
#endregion

#region Programa
if (!File.Exists(path))
    CreaArchivo(path, string.Empty);
else
    ArchivoExiste();


while (finalizado == false)
{
    finalizado = AgregaArchivo(path);
}

Console.WriteLine("Editor Finalizado");
Console.ReadKey();
#endregion

#region Funciones

void CreaArchivo(string p, string t)
{
    Console.WriteLine("""Creamo un archivo con el nombre "text.txt" hora puedes editarlo, diviertete""");
    File.WriteAllText(path, "");
}
bool AgregaArchivo(string p)
{
    MostrarContenido(p);
    Console.WriteLine("""Para agregar texto, escribelo y preciona "Enter". Para finalizar el editor escribe "S" """);
    textoNuevo = "\n" + Console.ReadLine() ?? "";
    if (textoNuevo.Trim() == "S" || textoNuevo.Trim() == "s")
    {
        return true;
    }

    File.AppendAllText(path, textoNuevo);
    return false;
}
void ArchivoExiste()
{
    Console.WriteLine("El archivo ya existe, deseas editrarlo, borrarlo o ver el contido? Editar=E/Borrar=B/Ver=V");
    string validacionB = Console.ReadLine() ?? "";
    if (validacionB != "E" && validacionB != "e" && validacionB != "B" && validacionB != "b" && validacionB != "V" && validacionB != "v")
    {
        finalizado = true;
        return;
    }
    else if (validacionB == "B" || validacionB == "b")
    {
        BorrarArchivo(path);
        CreaArchivo(path, "");
    }
    else if (validacionB == "V" || validacionB == "v")
    {
        MostrarContenido(path);
        ArchivoExiste();
    }
}
void BorrarArchivo(string p)
{
    File.Delete(p);
}

void MostrarContenido(string p)
{
    texto = File.ReadAllText(p);
    if (!String.IsNullOrWhiteSpace(texto))
        Console.WriteLine("Texto: " + texto);
}
#endregion