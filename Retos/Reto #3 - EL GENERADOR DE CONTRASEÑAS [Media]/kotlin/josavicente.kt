fun main(){
    passwordGenerator(32,true, true, true)
    passwordGenerator(10,true, true, true)
    passwordGenerator(128,true, false, true)
    passwordGenerator(32,true, true, false)
    passwordGenerator(256,false, true, true)
}
    
private fun passwordGenerator(longitud: Int, mayus: Boolean, numeros: Boolean, simbolos: Boolean){
    val caracteres = "abcdefghijklmnopqrstuvwxyz"
    val digitos = "0123456789"
    val caracteresEspeciales = "!@#$%^&*()_+-=[]{}\\|;:'\",.<>/?"
    var password = ""
    var caracteresValidos = caracteres
    
    if (mayus){
        caracteresValidos += caracteres.uppercase()
    }
    if (numeros){
        caracteresValidos += digitos
    }
    if(simbolos){
        caracteresValidos += caracteresEspeciales
    }

    for(posicion : Int in 1..longitud){
        password += caracteresValidos[Random.nextInt(0, caracteresValidos.length)]
    }

    println(password)
}