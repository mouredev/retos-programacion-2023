import kotlin.random.Random

/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

fun main(){

   println(generaPassword(10,true,true,true))
    println(generaPassword(10,false,true,false))

}

fun generaPassword(longitud:Int=8, mayusculas:Boolean=false, numeros:Boolean=true, simbolos:Boolean=false):String{

    var password:String="";
    if (longitud<8 || longitud>16)
        password= "Tambaño solicitado de conntraseña incorrecto (8-16)"

    //Cuplir restricciones iniciales.
    if(mayusculas) password+=(randomChar().uppercase()) else password+=randomChar()
    if(numeros) password+=randomNumber()
    if(simbolos) password+=randomSimbol()

    //Completar aleatoriamente.
    var opciones=1
    if(mayusculas) opciones++
    if(numeros) opciones++
    if(simbolos) opciones++

    while (password.length<longitud){
        when(Random.nextInt(1,opciones)){
            1 -> password+=randomChar()
            2 -> password+=(randomChar().uppercase())
            3 -> password+=randomNumber()
            4 -> password+=randomSimbol()
        }
    }

    return password
}

fun randomChar():Char= Char(Random.nextInt(97,122))
fun randomNumber():Char=Char(Random.nextInt(48,57))
fun randomSimbol():Char=Char(Random.nextInt(35,38))
