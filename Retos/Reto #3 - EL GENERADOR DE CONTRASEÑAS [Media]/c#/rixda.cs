/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.   
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)

 condicion                         ascii code
Con o sin letras mayúsculas.   65-90  97-122
 * - Con o sin números.         48-57
 * - Con o sin símbolos.        33-47 58-64 
 */

 class passwordGenerator
 {
    
    public string passwordGenerator(int longitud,bool mayus = false , bool number = false,bool simbol = false){
        System.Random rnd = new System.Random();
        string text = "";
        if ((8 > longitud || longitud > 12))
        {
            return "longitud no permitida seleccione de 8 a 12 caracteres";
        }
        while (text.Length < longitud )
        {
             
            int passCha = rnd.Next(122);
            
            if ((97 <= passCha && passCha <= 122))
            {
                text += (char)passCha;
                continue;
            }

            if (mayus && (65 <= passCha && passCha <= 90))
            {
                text += (char)passCha;
                continue;
            }
            if (number && (48 <= passCha && passCha <= 57))
            {
                text += (char)passCha;
                continue;
            }
            if (simbol && ((33 <= passCha && passCha <= 47) || (58 <= passCha && passCha <= 64)))
            {
                text += (char)passCha;
                continue;
            }
            continue;
        }
        return text;
    }

 }