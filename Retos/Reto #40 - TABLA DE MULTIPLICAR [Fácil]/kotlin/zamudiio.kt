import java.util.Scanner

fun main(args: Array<String>) {
   println("🔢 Tabla de multiplicar 🔢")
   val scanner = Scanner(System.`in`)
   val value: String = scanner.nextLine()
   if(value.isEmpty() || !tryIntParse(value)){
       println("Porfavor ingresa un formato valido, debe ser un numero entero")
       main(args)
   }else{
       operation(value.toInt())
   }
}

fun operation(number: Int) {
println("La tabla de multiplicacion de $number es:")
for (i in 1..10) {
    println("$number x $i = ${number * i}")
}
}

fun tryIntParse(value:String) : Boolean {
   return try {
       value.toInt()
       true
   } catch (e:NumberFormatException){
       false
   }
}