import java.io.*

fun main() {

    /*
    * Reto #34 21/08/2023 El TXT
    *
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


    val nombreArchivo = "text.txt"

    val archivo = File(nombreArchivo)
    val contenido : String

    if (archivo.exists()) {
        var opcion = "X"
        while ( opcion != "C" && opcion != "N"){
            println("El archivo ya existe ¿qué deseas hacer? \n [C] Continuar escribiendo \n [N] Crear nuevo fichero")
            opcion = readLine()!!
        }

        if (opcion == "C") {
            mostrarArchivo(archivo)
            contenido = pedirTexto()
            addTextoArchivo(archivo, contenido)

        } else {
            contenido = pedirTexto()
            borrarArchivo(nombreArchivo)
            crearArchivo(archivo, contenido)

        }

    } else {
        contenido = pedirTexto()
        crearArchivo(archivo, contenido)

    }

}

fun pedirTexto(): String {
    println("Escribe el texto a grabar")
    print(">")
    return readLine()!!
}

fun crearArchivo ( archivo : File, contenido:String ){
    try {
        archivo.createNewFile() // Crea el archivo si no existe
        val escritor = archivo.bufferedWriter()

        escritor.write(contenido)

        escritor.close()

    } catch (ex: Exception) {
        println("Ocurrió un error al crear el archivo: ${ex.message}")
    }

}

fun addTextoArchivo( archivo: File, contenido: String){
    try {
        val escritor = FileWriter(archivo, true) // El segundo parámetro "true" indica que se agregará al final del archivo existente
        val bufferEscritor = BufferedWriter(escritor)
        bufferEscritor.newLine()
        bufferEscritor.write(contenido)
        bufferEscritor.close()

    } catch (ex: Exception) {
        println("Ocurrió un error al agregar texto al archivo: ${ex.message}")
    }

}


fun mostrarArchivo(archivo: File){

    val lector = BufferedReader(FileReader(archivo))
    val contenido = StringBuilder()
    var linea: String? = lector.readLine()

    while (linea != null) {
        contenido.append(linea)
        contenido.append(System.lineSeparator()) // Agrega un salto de línea después de cada línea
        linea = lector.readLine()
    }

    lector.close()
    println ( contenido.toString())
}


fun borrarArchivo(nombreArchivo:String) {

    val archivo = File(nombreArchivo)
    if (archivo.exists()) {
        try {
            if (archivo.delete()) {
                println("Archivo borrado exitosamente: $nombreArchivo")
            } else {
                println("No se pudo borrar el archivo: $nombreArchivo")
            }
        } catch (ex: Exception) {
            println("Ocurrió un error al borrar el archivo: ${ex.message}")
        }
    } else {
        println("El archivo no existe: $nombreArchivo")
    }

}