# reto de programación No. 2
# 06-ene-2023
# fundalab by jesus becerra
# siguiendo retosdeprogramacion.com by mouredev
'''
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
 '''
my_dict={"a":"4","b":"I3","c":"[","d":")","e":"3","f":"|=","g":"&","h":"#","i":"1","j":",_|",
"k":">|","l":"1","m":"/\/\\","n":"^/","o":"0","p":"|*","q":"(_,)","r":"I2","s":"5","t":"7","u":"(_)",
"v":"\/","w":"\/\/","x":"><","y":"j","z":"2"} 

texto_entrada = input("Por favor ingrese un texto: ")    #solicitamos el texto
texto_entrada= texto_entrada.lower()
texto_salida=""
for ctr in texto_entrada:
    for clave in my_dict:
        if ctr==clave:
            texto_salida=texto_salida+my_dict[clave]
print(texto_salida)      