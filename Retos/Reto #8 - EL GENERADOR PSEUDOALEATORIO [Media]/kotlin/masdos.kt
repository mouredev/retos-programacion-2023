import java.time.LocalDateTime


/*
* Crea un generador de números pseudoaleatorios entre 0 y 100.
* - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
*
* Es más complicado de lo que parece...
*/
fun main() {
  println(randomNumber())
}

private fun randomNumber(): Int {
  val randomNumber = LocalDateTime.now().minute + LocalDateTime.now().second
  return if (randomNumber > 100) randomNumber - 100 else randomNumber
}