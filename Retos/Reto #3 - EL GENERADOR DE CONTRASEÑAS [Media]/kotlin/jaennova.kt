import java.util.*

fun main() {
    val random = Random()

    // Pedir la longitud de la contraseña
    print("Ingresa la longitud de la contraseña (entre 8 y 16): ")
    val longitud = readLine()!!.toInt()

    print("¿Incluir letras mayúsculas? (s/n): ")
    val incluirMayusculas = readLine()!!.toLowerCase() == "s"

    print("¿Incluir números? (s/n): ")
    val incluirNumeros = readLine()!!.toLowerCase() == "s"

    print("¿Incluir símbolos? (s/n): ")
    val incluirSimbolos = readLine()!!.toLowerCase() == "s"

    val caracteres = mutableListOf<Char>()
    val letrasMinusculas = 'a'..'z'
    val letrasMayusculas = 'A'..'Z'
    val numeros = '0'..'9'
    val simbolos = listOf('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}','?')

    caracteres.addAll(letrasMinusculas)
    if (incluirMayusculas) caracteres.addAll(letrasMayusculas)
    if (incluirNumeros) caracteres.addAll(numeros)
    if (incluirSimbolos) caracteres.addAll(simbolos)
    
    // Generar la contraseña
val contrasena = StringBuilder()
for (i in 1..longitud) {
    contrasena.append(caracteres[random.nextInt(caracteres.size)])
}

println("Contraseña  de $longitud caracteres generada: $contrasena")

}