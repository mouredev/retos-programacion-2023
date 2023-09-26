import java.util.*

fun main() {
    val scanner = Scanner(System.`in`)
    println("Ingrese la longitud de la contraseña (8-16):")
    var longitud = scanner.nextInt()
    while (longitud < 8 || longitud > 16) {
        println("La longitud debe ser entre 8 y 16.")
        println("Ingrese la longitud de la contraseña (8-16):")
        longitud = scanner.nextInt()
    }
    println("Desea incluir mayúsculas en la contraseña? (S/N)")
    val incluirMayus = scanner.next()
    println("Desea incluir números en la contraseña? (S/N)")
    val incluirNumeros = scanner.next()
    println("Desea incluir símbolos especiales en la contraseña? (S/N)")
    val incluirSimbolos = scanner.next()

    val random = Random()
    val letras = "abcdefghijklmnopqrstuvwxyz"
    val letrasMayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    val numeros = "0123456789"
    val simbolos = "!@#$%^&*()_+-=[]{}|;':,.<>/?`~"
    val caracteres = StringBuilder()
    caracteres.append(letras)
    if (incluirMayus.toUpperCase() == "S") {
        caracteres.append(letrasMayus)
    }
    if (incluirNumeros.toUpperCase() == "S") {
        caracteres.append(numeros)
    }
    if (incluirSimbolos.toUpperCase() == "S") {
        caracteres.append(simbolos)
    }
    val caracteresArray = caracteres.toString().toCharArray()

    val contrasena = StringBuilder()
    for (i in 1..longitud) {
        contrasena.append(caracteresArray[random.nextInt(caracteresArray.size)])
    }
    println("La contraseña generada es: $contrasena")

}
