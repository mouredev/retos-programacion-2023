package EjercicioKotlin.Mouredev

import java.lang.Exception

fun main(){
    Testing()
}

class Testing{

    init {
        testingOne()
        testingTwo()
        testingThree()
    }

    //Testing con los valores negativos
    private fun testingOne(){
        try {
            Reto12(-9,-2015)
            println("paso el testing")
        }catch (e:Exception){
            println("no paso el testing")
        }
    }

    //Testing con los valores fuera de rango
    private fun testingTwo(){
        try {
            Reto12(50,2015)
            println("paso el testing")
        }catch (e:Exception){
            println("no paso el testing")
        }
    }

    //Testing con los valores mu grande
    private fun testingThree(){
        try {
            Reto12(20595059,20595959)
            println("paso el testing")
        }catch (e:Exception){
            println("no paso el testing")
        }
    }
}
