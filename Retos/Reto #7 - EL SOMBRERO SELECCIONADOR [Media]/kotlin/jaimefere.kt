private enum class HogwartsHouseValue() {
    COURAGE, BRAVERY, DETERMINATION, DARING, HONESTY, LOYALTY, HARD_WORK, FRIENDSHIP, CLEVERNESS, CREATIVITY, KNOWLEDGE, CURIOSITY, CUNNING, AMBITION, WIT
}

private enum class HogwartsHouse(var values: Array<HogwartsHouseValue>, var affinity: Int = 0) {
    GRYFFINDOR(arrayOf(HogwartsHouseValue.COURAGE, HogwartsHouseValue.BRAVERY, HogwartsHouseValue.DETERMINATION, HogwartsHouseValue.DARING)),
    HUFFLEPUFF(arrayOf(HogwartsHouseValue.HONESTY, HogwartsHouseValue.LOYALTY, HogwartsHouseValue.HARD_WORK, HogwartsHouseValue.FRIENDSHIP)),
    RAVENCLAW(arrayOf(HogwartsHouseValue.CLEVERNESS, HogwartsHouseValue.CREATIVITY, HogwartsHouseValue.KNOWLEDGE, HogwartsHouseValue.CURIOSITY)),
    SLYTHERIN(arrayOf(HogwartsHouseValue.CUNNING, HogwartsHouseValue.AMBITION, HogwartsHouseValue.WIT, HogwartsHouseValue.DETERMINATION));
}

private fun updateHogwartsHouseAffinities(answerValues: Array<HogwartsHouseValue>) {
    HogwartsHouse.values().forEach { house ->
        house.values.forEach {houseValue ->
            if(answerValues.contains(houseValue)) {
                house.affinity += 1
            }
        }
    }
}

private fun selectedBySortingHat(): HogwartsHouse {
    println("¿Qué actividad mágica te gustaría aprender más?")
    println("a) Transformaciones de objetos y personas")
    println("b) Creación de pociones mágicas")
    println("c) Control y manipulación del clima")
    println("d) Protección contra las artes oscuras")
    println("Selecciona una respuesta de las anteriores:")
    when(readLine()) {
        "a" -> updateHogwartsHouseAffinities(arrayOf(HogwartsHouseValue.CREATIVITY, HogwartsHouseValue.AMBITION))
        "b" -> updateHogwartsHouseAffinities(arrayOf(HogwartsHouseValue.KNOWLEDGE, HogwartsHouseValue.CURIOSITY))
        "c" -> updateHogwartsHouseAffinities(arrayOf(HogwartsHouseValue.DETERMINATION, HogwartsHouseValue.AMBITION))
        "d" -> updateHogwartsHouseAffinities(arrayOf(HogwartsHouseValue.BRAVERY, HogwartsHouseValue.CLEVERNESS))
    }

    println("¿Qué tipo de aventuras te gustaría vivir en Hogwarts?")
    println("a) Conocer lugares nuevos e interesante")
    println("b) Tener emocionantes duelos mágicos")
    println("c) Resolver misterios y acertijos")
    println("d) Ayudar a los demás y hacer amigos nuevos")
    println("Selecciona una respuesta de las anteriores:")
    when(readLine()) {
        "a" -> updateHogwartsHouseAffinities(arrayOf(HogwartsHouseValue.CURIOSITY, HogwartsHouseValue.COURAGE))
        "b" -> updateHogwartsHouseAffinities(arrayOf(HogwartsHouseValue.COURAGE, HogwartsHouseValue.BRAVERY))
        "c" -> updateHogwartsHouseAffinities(arrayOf(HogwartsHouseValue.CLEVERNESS, HogwartsHouseValue.CREATIVITY))
        "d" -> updateHogwartsHouseAffinities(arrayOf(HogwartsHouseValue.FRIENDSHIP, HogwartsHouseValue.LOYALTY))
    }

    println("¿Qué habilidades te gustaría desarrollar durante tu tiempo en Hogwarts?")
    println("a) Aprender hechizos poderosos")
    println("b) Desarrollar habilidades atléticas y físicas")
    println("c) Mejorar tu capacidad de comunicación y liderazgo")
    println("d) Aprender a trabajar en equipo y a colaborar con otros")
    println("Selecciona una respuesta de las anteriores:")
    when(readLine()) {
        "a" -> updateHogwartsHouseAffinities(arrayOf(HogwartsHouseValue.AMBITION, HogwartsHouseValue.HARD_WORK))
        "b" -> updateHogwartsHouseAffinities(arrayOf(HogwartsHouseValue.HARD_WORK, HogwartsHouseValue.DETERMINATION))
        "c" -> updateHogwartsHouseAffinities(arrayOf(HogwartsHouseValue.CLEVERNESS, HogwartsHouseValue.CREATIVITY))
        "d" -> updateHogwartsHouseAffinities(arrayOf(HogwartsHouseValue.LOYALTY, HogwartsHouseValue.KNOWLEDGE))
    }

    println("Qué tipo de magia te resulta más interesante?")
    println("a) Hechizos que te permiten viajar a lugares lejanos")
    println("b) Hechizos que te permiten controlar elementos naturales")
    println("c) Hechizos que te permiten transformar objetos y personas")
    println("d) Hechizos que te permiten sanar heridas y enfermedades")
    println("Selecciona una respuesta de las anteriores:")
    when(readLine()) {
        "a" -> updateHogwartsHouseAffinities(arrayOf(HogwartsHouseValue.CURIOSITY, HogwartsHouseValue.AMBITION))
        "b" -> updateHogwartsHouseAffinities(arrayOf(HogwartsHouseValue.KNOWLEDGE, HogwartsHouseValue.CREATIVITY))
        "c" -> updateHogwartsHouseAffinities(arrayOf(HogwartsHouseValue.CREATIVITY, HogwartsHouseValue.AMBITION))
        "d" -> updateHogwartsHouseAffinities(arrayOf(HogwartsHouseValue.KNOWLEDGE, HogwartsHouseValue.HONESTY))
    }

    println("¿Qué actitud o comportamiento consideras que es más importante para triunfar en Hogwarts?")
    println("a) Ser valiente y arriesgado")
    println("b) Ser trabajador y constante")
    println("c) Ser inteligente y astuto")
    println("d) Ser leal y honesto")
    println("Selecciona una respuesta de las anteriores:")
    when(readLine()) {
        "a" -> updateHogwartsHouseAffinities(arrayOf(HogwartsHouseValue.BRAVERY, HogwartsHouseValue.DETERMINATION))
        "b" -> updateHogwartsHouseAffinities(arrayOf(HogwartsHouseValue.AMBITION, HogwartsHouseValue.HARD_WORK))
        "c" -> updateHogwartsHouseAffinities(arrayOf(HogwartsHouseValue.CUNNING, HogwartsHouseValue.WIT))
        "d" -> updateHogwartsHouseAffinities(arrayOf(HogwartsHouseValue.LOYALTY, HogwartsHouseValue.HONESTY))
    }

    return HogwartsHouse.values().maxBy{ it.affinity }
}

fun main() {
    println(selectedBySortingHat())
}