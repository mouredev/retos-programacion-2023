import java.awt.event.KeyEvent
import java.awt.event.KeyListener
import javax.swing.JFrame


fun main() {

    /*
    *
    * Reto #25 19/06/2023 EL CÓDIGO KONAMI
    *
    * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente
    * desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
    *
    * ↑ ↑ ↓ ↓ ← → ← → B A
    *
    *
    */

    println("RETO #25 - El código Konami")


    val frame = JFrame("Capturando pulsaciones de teclado")
    val keyListener = MyKeyListener()

    frame.addKeyListener(keyListener)
    frame.defaultCloseOperation = JFrame.EXIT_ON_CLOSE
    frame.setSize(300, 300)
    frame.isVisible = true


}



class MyKeyListener : KeyListener {
    val codigoKonami =  "38384040373937396665" //↑ ↑ ↓ ↓ ← → ← → B A
    var historialScreen :String = ""
    var historial :String = ""

    override fun keyPressed(e: KeyEvent) {
        // Capturar la tecla presionada
        val keyCode = e.keyCode
        //println("Tecla presionada: $keyCode")
        historial += keyCode

        when (keyCode) {
            38 -> historialScreen += "↑"
            40 -> historialScreen += "↓"
            37 -> historialScreen += "←"
            39 -> historialScreen += "→"
            66 -> historialScreen += "B"
            65 -> historialScreen += "A"
            else -> historialScreen = ""

        }
        println("> $historialScreen")

        if (codigoKonami == historial){
            println ("¡¡¡ CODIGO KONAMI INTRODUCIDO !!!")

        } else if (codigoKonami.contains(historial)){
            // null, aún hay posiblidades

        } else {
            // Ya se ha hechado a perder la secuncia
            println (" ¡¡¡ SECUENCIA ERRÓNEA !!!")
            historial = ""
            historialScreen = ""
        }
    }

    override fun keyReleased(e: KeyEvent) {
        // Acción cuando se suelta la tecla
    }

    override fun keyTyped(e: KeyEvent) {
        // Acción cuando se pulsa y se suelta una tecla
    }
}

