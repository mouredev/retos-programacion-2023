/***********************************
Las tijeras cortan el papel.
El papel cubre la piedra.
La piedra aplasta el lagarto.
El lagarto envenena a Spock.
Spock aplasta las tijeras.
Las tijeras decapitan el lagarto.
El lagarto se come el papel.
El papel refuta a Spock.
Spock vaporiza la piedra.
La piedra aplasta a las tijeras.
**************************************/

enum class OPTIONS {
    PIEDRA, PAPEL, TIJERAS, LAGARTO, SPOCK;
    fun compara(OPTIONS option):Boolean{
        if (this==option) return true
        return false
    }
}


fun main() {
    //CREAR LAS JUGADAS

    var prueba=OPTIONS.LAGARTO
    var test=prueba.compara(OPTIONS.LAGARTO)
    println("testeando:"+test)
       
    }
}