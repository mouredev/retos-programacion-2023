/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts:
 *   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas
 *   y crear el algoritmo seleccionador:
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */
val HogwartsHouses: HashMap<String,Int> = hashMapOf(
    "Slytherin" to 0,
    "Gryffindor" to 0,
    "Ravenclaw" to 0,
    "Hufflepuff" to 0,
)

fun main(args: Array<String>) {
    println("Cual de estas frases describe mejor tu personalidad?")
    println("a) Soy una persona muy analitica y logica")
    println("b) Soy una persona muy amable y empatica")
    println("c) Soy una persona muy aventurera y arriesgada")
    println("d) Soy una persona muy ambiciosa y astuta")
    do{
        print("Elige una opcion : ")
        var choose = setPoint(readLine()!!)
    }while(choose.equals("invalid"))

    println("Que es lo que mas valoras de una persona?")
    println("a) La inteligencia y el conocimiento")
    println("b) La amabilidad y la empatia")
    println("c) El coraje y la valentia")
    println("d) La astucia y el deseo de poder")
    do{
        print("Elige una opcion : ")
        var choose = setPoint(readLine()!!)
    }while(choose.equals("invalid"))

    println("Cual de estas situciaones te haria sentir mas incomodo?")
    println("a) Estar en un lugar donde no hay nada que hacer")
    println("b) Estar en un lugar rodeado de personas que no conoces")
    println("c) Estar en un lugar donde hay mucho peligro")
    println("d) Estar en un lugar donde no puedes ser tu mismo")
    do{
        print("Elige una opcion : ")
        var choose = setPoint(readLine()!!)
    }while(choose.equals("invalid"))

    println("Cual de esta opciones te describe mejor?")
    println("a) Prefiero pensar antes de actuar")
    println("b) Soy muy protector con las personas que quiero")
    println("c) Me gusta tomar riesgos y hacer cosas emocionantes")
    println("d) Me gusta perseguir mis objetivos sin importar el costo")
    do{
        print("Elige una opcion : ")
        var choose = setPoint(readLine()!!)
    }while(choose.equals("invalid"))

    println("Que es lo que mas te gusta hacer en tu tiempo libre?")
    println("a) Leer y aprender cosas nuevas")
    println("b) Pasar tiempo con amigos y familiares")
    println("c) Hacer cosas emocionantes y aventureras")
    println("d) Molestar a mis amigos y personas cercanas")
    do{
        print("Elige una opcion : ")
        var choose = setPoint(readLine()!!)
    }while(choose.equals("invalid"))

    println("Cual de estas virtudes es la mas importante para ti?")
    println("a) La inteligencia y la sabiduria")
    println("b) La amabilidad y la compasion")
    println("c) El coraje y la valentia")
    println("d) La ambicion y el deseo de exito")
    do{
        print("Elige una opcion : ")
        var choose = setPoint(readLine()!!)
    }while(choose.equals("invalid"))

    println("Cual de estas cosas te da mas miedo?")
    println("a) No ser lo suficientemente inteligente")
    println("b) No tener amigos o ser rechazado por los demas")
    println("c) Enfrentarte a tus miedos y no tener exito")
    println("d) No alcanzar tu exito soñado")
    do{
        print("Elige una opcion : ")
        var choose = setPoint(readLine()!!)
    }while(choose.equals("invalid"))
    
    belongsTo()
}

fun setPoint(choose: String): String{
    var choose1 = choose.lowercase()
    when (choose1){
        "a" ->{
            HogwartsHouses["Ravenclaw"] = HogwartsHouses["Ravenclaw"]!! + 1
        }
        "b" ->{
            HogwartsHouses["Hufflepuff"]= HogwartsHouses["Hufflepuff"]!! + 1
        }
        "c" ->{
            HogwartsHouses["Gryffindor"]= HogwartsHouses["Gryffindor"]!! + 1
        }
        "d" ->{
            HogwartsHouses["Slytherin"]= HogwartsHouses["Slytherin"]!! + 1
        }
        else ->{
            return "invalid"
        }
    }
    return "valid"
}

fun belongsTo(){
    var posibleWinner = HogwartsHouses.maxBy {it.value}
    var chooseHouse: String? = "0";
    for (house in HogwartsHouses){
        if(house.key == posibleWinner.key) continue
        if(house.value == posibleWinner.value){
            println("Puedes elegir entre ${house.key} y ${posibleWinner.key}, ingresa tu eleccion: ")
            var notOk = true
            do{
                println("1. ${posibleWinner.key}")
                println("2. ${house.key}")
                chooseHouse = readLine()
                if (chooseHouse.equals("1")) notOk = false
                else if (chooseHouse.equals("2")) notOk = false
            }while(notOk)

            println(if (chooseHouse == "1") "Pertences a... ${posibleWinner.key}!!!!!" else "Perteneces a... ${house.key}!!!!!")
            break
        }
    }

    println(if(chooseHouse == "0") "Perteneces a... ${posibleWinner.key}!!!!!" else "")
}