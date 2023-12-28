object chintoz {
  def main(args: Array[String]): Unit = {
    def number = System.currentTimeMillis() % 101
    println(s"${Console.GREEN}Bienvenido al generador de número aleatorio entre 0 y 100. El número generado $number ")
  }
}
