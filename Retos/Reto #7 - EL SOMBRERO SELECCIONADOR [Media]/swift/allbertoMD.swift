import Foundation


var gryffindor = 0
var slytherin = 0
var ravenclaw = 0
var hufflepuff = 0

var question1Selector = 0
var question2Selector = 0
var question3Selector = 0
var question4Selector = 0
var question5Selector = 0
var question6Selector = 0
var question7Selector = 0


print("\n[¿?] - ¿Dónde te sientes más cómodo?") // Pregunta 1.
question1()

if let q1 = readLine(), let q1Int = Int(q1) {
    question1Selector = q1Int
}

switch question1Selector {
case 1:
    gryffindor += 1
case 2:
    slytherin += 1
case 3:
    ravenclaw += 1
case 4:
    hufflepuff += 1
default:
    print("[!] - Seleccion no valida.")
    
}


print("\n[¿?] - ¿Cuál es tu mayor deseo?") // Pregunta 2.
question2()

if let q2 = readLine(), let q2Int = Int(q2) {
    question2Selector = q2Int
}

switch question2Selector {
case 1:
    ravenclaw += 1
case 2:
    hufflepuff += 1
case 3:
    gryffindor += 1
case 4:
    slytherin += 1
default:
    print("[!] - Seleccion no valida.")
}


print("\n[¿?] - ¿Qué cualidad valoras más en un amigo?") // Pregunta 3.
question3()

if let q3 = readLine(), let q3Int = Int(q3) {
    question3Selector = q3Int
}

switch question3Selector {
case 1:
    gryffindor += 1
case 2:
    hufflepuff += 1
case 3:
    ravenclaw += 1
case 4:
    slytherin += 1
default:
    print("[!] - Seleccion no valida.")
}


print("\n[¿?] - ¿Qué te gustaría aprender en Hogwarts?") // Pregunta 4.
question4()

if let q4 = readLine(), let q4Int = Int(q4) {
    question4Selector = q4Int
}

switch question4Selector {
case 1:
    hufflepuff += 1
case 2:
    ravenclaw += 1
case 3:
    slytherin += 1
case 4:
    gryffindor += 1
default:
    print("[!] - Seleccion no valida.")
}


print("\n[¿?] - ¿Qué tipo de magia prefieres?") // Pregunta 5.
question5()

if let q5 = readLine(), let q5Int = Int(q5) {
    question5Selector = q5Int
}

switch question5Selector {
case 1:
    slytherin += 1
case 2:
    ravenclaw += 1
case 3:
    hufflepuff += 1
case 4:
    gryffindor += 1
default:
    print("[!] - Seleccion no valida.")

}


print("\n[¿?] - ¿Qué animal mágico te gustaría tener como mascota?") // Pregunta 6.
question6()

if let q6 = readLine(), let q6Int = Int(q6) {
    question6Selector = q6Int
}

switch question6Selector {
case 1:
    gryffindor += 1
case 2:
    hufflepuff += 1
case 3:
    ravenclaw += 1
case 4:
    slytherin += 1
default:
    print("[!] - Seleccion no valida.")
}


print("\n[¿?]- ¿Qué hazaña valoras más?") // Pregunta 7.
question7()

if let q7 = readLine(), let q7Int = Int(q7) {
    question7Selector = q7Int
}

switch question7Selector {
case 1:
    ravenclaw += 1
case 2:
    slytherin += 1
case 3:
    gryffindor += 1
case 4:
    hufflepuff += 1
default:
    print("[!] - Seleccion no valida.")
}


if gryffindor > slytherin && gryffindor > ravenclaw && gryffindor > hufflepuff {
    print("\n[🏰] - Gryffindor!!")

} else if slytherin > gryffindor && slytherin > ravenclaw && slytherin > hufflepuff {
    print("\n[🏰] - Slytherin!!")

} else if ravenclaw > gryffindor && ravenclaw > slytherin && ravenclaw > hufflepuff {
    print("\n[🏰] - Ravenclaw!!")

} else if hufflepuff > gryffindor && hufflepuff > slytherin && hufflepuff > ravenclaw {
    print("\n[🏰] - Hafflepuff!!")

} else if gryffindor == slytherin {
    print("\n[🏰] - Gryffindor!!")

} else if gryffindor == ravenclaw {
    print("\n[🏰] - Ravenclaw!!")

} else if gryffindor == hufflepuff {
    print("\n[🏰] - Hafflepuff!!")

} else if slytherin == ravenclaw {
    print("\n[🏰] - Slytherin!!")

} else if slytherin == hufflepuff {
    print("\n[🏰] - Slytherin!!")

} else if ravenclaw == hufflepuff {
    print("\n[🏰] - Ravenclaw!!")

} else if gryffindor == slytherin && gryffindor == ravenclaw {
    print("\n[🏰] - Gryffindor!!")

} else if gryffindor == slytherin && gryffindor == hufflepuff {
    print("\n[🏰] - Gryffindor!!")

} else if gryffindor == ravenclaw && gryffindor == hufflepuff {
    print("\n[🏰] - Hafflepuff!!")

} else if slytherin == ravenclaw && slytherin == hufflepuff {
    print("\n[🏰] - Slytherin!!")

} else if slytherin == ravenclaw && slytherin == gryffindor {
    print("\n[🏰] - Gryffindor!!")

} else if slytherin == hufflepuff && slytherin == gryffindor {
    print("\n[🏰] - Gryffindor!!")

} else if ravenclaw == hufflepuff && ravenclaw == gryffindor {
    print("\n[🏰] - Ravenclaw!!")

} else if ravenclaw == hufflepuff && ravenclaw == slytherin {
    print("\n[🏰] - Slytherin!!")

} else if ravenclaw == gryffindor && ravenclaw == slytherin {
    print("\n[🏰] - Slytherin!!")

} else if hufflepuff == gryffindor && hufflepuff == slytherin {
    print("\n[🏰] - Hafflepuff!!")

} else if hufflepuff == gryffindor && hufflepuff == ravenclaw {
    print("\n[🏰] - Ravenclaw!!")

} else if hufflepuff == slytherin && hufflepuff == ravenclaw {
    print("\n[🏰] - Ravenclaw!!")
}




func question1() {
    print("\n")
    print("[1] - En un lugar bullicioso y lleno de actividad, rodeado de amigos.") // Gryffindor
    print("[2] - En un lugar donde pueda hacer alianzas estratégicas y avanzar hacia mis metas.") // Slytherin
    print("[3] - En una biblioteca rodeado de libros y conocimiento.") // Ravenclaw
    print("[4] - En un lugar tranquilo y acogedor, como mi habitación donde puedo estar con mis amigos más cercanos.") // Hufflepuff
}


func question2() {
    print("\n")
    print("[1] - Sabiduría y conocimiento para comprender el mundo que me rodea.") // Ravenclaw
    print("[2] - Amistad sincera y la oportunidad de ayudar a los demás.") // Hufflepuff
    print("[3] - Aventuras emocionantes y la oportunidad de probar mi valentía.") // Gryffindor
    print("[4] - Poder y reconocimiento por mis logros y ambiciones.") // Slytherin
}


func question3() {
    print("\n")
    print("[1] - Valentía y lealtad en momentos difíciles.") // Gryffindor
    print("[2] - Amabilidad y lealtad, alguien en quien pueda confiar plenamente.") // Hufflepuff
    print("[3] - Inteligencia y curiosidad para explorar nuevas ideas y conocimientos.") // Ravenclaw")
    print("[4] - Ambición y determinación para alcanzar nuestras metas juntos.") // Slytherin
}


func question4() {
    print("\n")
    print("[1] - Cuidado de Criaturas Mágicas para conocer y proteger a las criaturas más necesitadas.") // Hufflepuff
    print("[2] - Historia de la Magia para comprender mejor nuestro mundo mágico.") // Ravenclaw
    print("[3] - El arte de la magia oscura y la habilidad para manejarla.") // Slytherin
    print("[4] - Hechizos poderosos para proteger a mis seres queridos.") // Gryffindor
}


func question5() {
    print("\n")
    print("[1] - Magia que otorgue poder y control sobre los demás.") // Slytherin
    print("[2] - Magia que desafíe mi intelecto y capacidad de aprendizaje.") // Ravenclaw
    print("[3] - Magia que promueva la armonía y la ayuda mutua entre las personas.") // Hufflepuff
    print("[4] - Magia que requiera valor y coraje para realizar.") // Gryffindor
}

func question6() {
    print("\n")
    print("[1] - Un fénix, símbolo de renacimiento y valentía.") // Gryffindor
    print("[2] - Un perro, símbolo de lealtad y amistad.") // Hufflepuff
    print("[3] - Un búho, símbolo de sabiduría y conocimiento.") // Ravenclaw
    print("[4] - Una serpiente, símbolo de astucia y ambición.") // Slytherin
}

func question7() {
    print("\n")
    print("[1] - El descubrimiento de nuevos conocimientos que transforman el mundo.") // Ravenclaw
    print("[2] - El poder de influir y dirigir a otros hacia el éxito.") // Slytherin
    print("[3] - La valentía de enfrentarse a desafíos imposibles.") // Gryffindor
    print("[4] - La generosidad y el servicio desinteresado a los demás.") // Hufflepuff
}


