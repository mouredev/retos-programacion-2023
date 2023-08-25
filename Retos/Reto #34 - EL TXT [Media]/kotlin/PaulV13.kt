import java.io.File
import java.nio.file.Files
import java.nio.file.Paths

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

fun main(){
    elTxt()
}

fun createFile(): File {
    val file = File("text.txt")
    file.createNewFile()
    println("Se a creado un nuevo archivo.")

    return file
}

fun fileExist(): Boolean {
    val filePath = "text.txt"
    val path = Paths.get(filePath)

    return Files.exists(path)
}

fun showOptions(){
    println("Opciones:")
    println("---------------")
    println("1 - Seguir escribiendo")
    println("2 - Borrar contenido y comenzar del principio")
    println("3 - Salir")
    println("")
}

fun showContentFile(file: File){
    println("Contenido del archivo: ")
    println("------------")
    println(file.readText())
    println("-----------")
    println("")
}

fun elTxt(){
    while (true){
        if(fileExist()){
            val file = File("text.txt")
            println("El archivo existe.")
            showOptions()
            println("Ingrese una opcion: ")
            var text: String
            when(readln()){
                "1" -> {
                    showContentFile(file)
                    println("Ingrese un texto: ")
                    text = readln()
                    var fileContent = file.readText()
                    fileContent += "\n$text"
                    file.writeText(fileContent)
                }
                "2" -> {
                    print("Contenido del archivo borrado.")
                    print("Ingrese un texto: ")
                    text = readln()
                    file.writeText(text)
                }
                "3" -> {
                    println("Fin del programa!!!")
                    return
                }
            }
            showContentFile(file)
        }else{
            println("No existe el archivo.")
            val file = createFile()
            println("Ingrese un texto: ")
            val text = readln()
            file.writeText(text)
            showContentFile(file)
        }
    }
}
