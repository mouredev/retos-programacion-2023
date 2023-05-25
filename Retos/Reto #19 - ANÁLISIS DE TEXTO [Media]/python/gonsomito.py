"""
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 * Todo esto utilizando un único bucle.
"""
def control_de_texto(texto):
    if texto == "":
        print("Primero, necesito un texto para analizar.\n")
    else:
#En el caso de tener un texto, lo troceo (espacios por defecto) y lo meto a una lista de palabras.
        palabras = texto.split()      #print(palabras)
#inicio los totalizadores 
        long_palabra=0                         
        palabras_mas_larga=""
        total_oraciones=0
#Voy a recorrer la lista de palabras. Me interesa comprobar si termina en . ? ! para controlar oraciones.
        for palabra in palabras:
            if palabra.isalnum() == False:
#si tengo un símbolo de apertura, me sobra y habrá que restarlo para computar totales de caracteres
                if palabra[0] == "¿" or palabra[0] == "¡" or palabra[0] == "(" or palabra[0] == "{" or palabra[0] == "[" or palabra[0] == "<":
                    palabra=palabra[1:]
#si tengo un símbolo de cierre hay que ver cual es y restarlo para computar totales de caracteres y oraciones
                if palabra[-1] == "." or palabra[-1] == "?" or palabra[-1] == "!":
                    total_oraciones = total_oraciones + 1
                    palabra=palabra[:-1]
#si es cualquier otro de fin de palabra habrá que restarlo , : ; } ] ? ! para que no sume de más
                if palabra[-1] == "," or palabra[-1] == ":" or palabra[-1] == ";" or palabra[-1] == ")" or palabra[-1] == "}" or palabra[-1] == "]" or palabra[-1] == ">":
                    palabra=palabra[:-1]
            long_palabra = long_palabra + len(palabra)
            if len(palabra) > len(palabras_mas_larga):
                palabras_mas_larga=palabra
                
#Salida de pantalla con los items pedidos.
        print("El texto tiene un total de " + str(len(palabras)) + " palabras.")
        print("El tamaño medio de las palabras es " + str(long_palabra/len(palabras)) + " caracteres.")
        print("El palabra más larga es " + palabras_mas_larga)
        print("Hay un total de " + str(total_oraciones) + " oraciones.\n")

#LA PREMISA INICIAL ES QUE EL TEXTO NOS LLEGA CON UN FORMATO CORRECTO Y QUE NO SE CUMPLEN LAS REGLAS DE PUNTUACIÓN 
texto=""
control_de_texto(texto)
#monopalabra
texto="MONOPALABRA."
control_de_texto(texto)
#frase única
texto = "DAME UN TEXTO SIMPLE."
control_de_texto(texto)
#Existen varios tipos de oraciones.
texto = "HAY MUCHOS TIPOS DE FRASES: ENUNCIATIVA, EXCLAMATIVA, DUBITATIVA, ETC. ¡ALGUNOS CON ADMIRACIONES! PERO EXISTEN OTROS (UNOS MENOS HABITUALES). ¿CUÁL SERÍA EL TEXTO MÁS ADECUADO?" 
control_de_texto(texto)
#bloque de 2 párrafos lipsum.com
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ornare venenatis arcu, in tincidunt libero finibus eu. Praesent vitae pretium felis, nec tempor nibh. Fusce dapibus justo ut luctus rutrum. Pellentesque turpis nulla, tempus et venenatis sit amet, porttitor at dolor. Donec ligula orci, placerat posuere diam ut, egestas mollis mi. Mauris volutpat tellus quis lacinia faucibus. Quisque facilisis malesuada cursus. Curabitur aliquam consectetur sollicitudin. Praesent augue dolor, tristique id erat in, posuere tincidunt mauris. Nullam eget ante sed ante dapibus bibendum ut sit amet metus. Integer tortor tellus, hendrerit et maximus sed, dictum in mauris. Donec et sem faucibus, venenatis nibh a, convallis mauris. Nullam et enim eu ipsum mattis efficitur. Aenean at laoreet risus. Nunc lectus eros, facilisis ut dapibus faucibus, interdum at sapien. Pellentesque vel iaculis sapien. Mauris eu est arcu. Nam elementum velit quis convallis volutpat. Praesent vehicula finibus viverra. Nam gravida, massa et elementum faucibus, tellus diam vulputate enim, ac varius nisl ex quis urna. Praesent tincidunt tortor nec nunc venenatis, at efficitur justo cursus. Nam iaculis, massa sollicitudin viverra elementum, eros nisi cursus lectus, vitae sagittis eros nunc ut leo. Pellentesque maximus imperdiet elit, nec pulvinar leo imperdiet id. Ut id nunc dui. Nunc pellentesque, odio sit amet porta facilisis, magna magna dignissim sem, vitae ullamcorper felis ex tincidunt ante. Pellentesque dapibus urna vitae pharetra sodales. Duis vitae lorem feugiat, hendrerit leo at, scelerisque felis. Vivamus suscipit lacus in augue suscipit dignissim. Etiam ut sollicitudin orci, a sodales augue. Pellentesque a fermentum leo, nec ullamcorper mi. Curabitur nec nunc euismod, consequat turpis ut, convallis tellus."
control_de_texto(texto)
