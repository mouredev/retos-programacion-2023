import java.util.*

fun main(){
    hackeaLenguaje("Hola")
    hackeaLenguaje("a")
    hackeaLenguaje("Esto es una prueba")
    hackeaLenguaje("Bobo")
}
fun hackeaLenguaje (text: String){
    var mensajeTraducir = text
    val caracteresNormales = arrayOf('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9')
    val caracteresLeet = arrayOf("4","I3","[",")","3","|=","&","#","1",",_|",">|","1","/\\/\\","^/","0","|*","(_,)","I2","5","7","(_)","\\/","\\/\\/","><","j","2","o","L","R","E","A","S","b","T","B","g")
    var salida : String  = ""
    mensajeTraducir = mensajeTraducir.lowercase()
    for ( letra in mensajeTraducir.toList())
    {
         if(caracteresNormales.indexOf(letra) != -1){
             salida += caracteresLeet[caracteresNormales.indexOf(letra)]
         }else {
             salida += letra
         }


    }

    println(salida)
}

