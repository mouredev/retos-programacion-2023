/*
 * Reto #7: EL SOMBRERO SELECCIONADOR
 *
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts:
 *   (Gryffindor, Slytherin, Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas
 *   y crear el algoritmo seleccionador:
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */

fun main() {
  val game = SortingHat()
  game.play()
}

class SortingHat {

  fun play() {
    println(
      """
      «Las cuatro casas se llaman Gryffindor, Hufflepuff, Ravenclaw y Slytherin. 
      Cada casa tiene su propia noble historia y cada una ha producido notables brujas y magos.
      
      La Ceremonia de Selección tendrá lugar dentro de pocos minutos...
      
      Durante unos pocos segundos, se hizo un silencio completo. Entonces el sombrero se movió.
      Una rasgadura cerca del borde se abrió, ancha como una boca, y el sombrero comenzó a cantar:
      
        Oh, podrás pensar que no soy bonito,
        pero no juzgues por lo que ves.
        Me comeré a mí mismo si puedes encontrar
        un sombrero más inteligente que yo.
        Puedes tener bombines negros,
        sombreros altos y elegantes.
        Pero yo soy el Sombrero Seleccionador de Hogwarts
        y puedo superar a todos.
        No hay nada escondido en tu cabeza
        que el Sombrero Seleccionador no pueda ver.
        Así que pruébame y te diré
        dónde debes estar.
        Puedes pertenecer a Gryffindor,
        donde habitan los valientes.
        Su osadía, temple y caballerosidad
        ponen aparte a los de Gryffindor.
        Puedes pertenecer a Hufflepuff
        donde son justos y leales.
        Esos perseverantes Hufflepuff
        de verdad no temen el trabajo pesado.
        O tal vez a la antigua sabiduría de Ravenclaw,
        Si tienes una mente dispuesta,
        porque los de inteligencia y erudición
        siempre encontrarán allí a sus semejantes.
        O tal vez en Slytherin
        harás tus verdaderos amigos.
        Esa gente astuta utiliza cualquier medio
        para lograr sus fines.
        
        ¡Así que pruébame! ¡No tengas miedo!
        ¡Y no recibirás una bofetada!
        Estás en buenas manos (aunque yo no las tenga).
        Porque soy el Sombrero Pensante.»
        
      Rowling, J. K. (1997). Harry Potter y la piedra filosofal (pp. 93-97). Salamandra.
      """
    )
    println(selectHouse(doForm()).value)
  }

  private fun doForm(): List<Char> {
    val form: Map<String, Array<String>> =
      mapOf(
        "El núcleo de tu varita es de..." to
            arrayOf(
              "A. Fibras de corazón de dragón",
              "B. Pelo de cola de unicornio",
              "C. Pelo de veela",
              "D. Plumas de fénix"
            ),
        "No soportas..." to
            arrayOf(
              "A. Un examen sorpresa",
              "B. Dejarlo todo para el último momento",
              "C. Perder tus cosas",
              "D. Las reglas"
            ),
        "Irías a Hogwarts junto a..." to arrayOf("A. 🦉", "B. 🐇", "C. 🐈", "D. 🐢"),
        "Si pudieses elegir un plan..." to
            arrayOf(
              "A. Un partido de Quidditch",
              "B. Unas cervezas de mantequilla",
              "C. Unas partidas al ajedrez mágico",
              "D. Una aventura en el bosque tenebroso"
            ),
        "Tu hechizo favorito..." to
            arrayOf("A. Expelliarmus", "B. Petrificus Totalus", "C. Accio", "D. Alohomora")
      )
    return form.map { doQuestion(it.key, it.value) }
  }

  private fun doQuestion(question: String, options: Array<String>): Char {
    var answer = ' '
    var valid = false
    while (!valid) {
      println(question)
      options.forEach { println(it) }
      when (val response = readln()) {
        "a",
        "A" -> {
          answer = 'A'
          valid = true
        }

        "b",
        "B" -> {
          answer = 'B'
          valid = true
        }

        "c",
        "C" -> {
          answer = 'C'
          valid = true
        }

        "d",
        "D" -> {
          answer = 'D'
          valid = true
        }

        else -> println("La respuesta '$response' no es correcta. Aceptadas: A, B, C o D")
      }
    }
    return answer
  }

  private fun selectHouse(answers: List<Char>): House {
    val rules =
      mapOf(
        'A' to House.GRYFFINDOR,
        'B' to House.HUFFLEPUFF,
        'C' to House.RAVENCLAW,
        'D' to House.SLYTHERYN
      )
    val majorityOption = answers.groupingBy { it }.eachCount().maxBy { it.value }.key
    return rules[majorityOption]!!
  }
}

enum class House(val value: String) {
  GRYFFINDOR(
    """
      ¡Gryffindor!
      
      «La Casa de Gryffindor valora el coraje por encima de todo, pero también la osadía,
      el temple y la caballerosidad. Sus estudiantes son valientes, pero también muy imprudentes.
      
      Colores: Escarlata y oro.
      
      Miembros más famosos:
      Harry Potter, Ron Weasley, Hermione Granger, Albus Dumbledore.»
      
      REF: https://www.fotogramas.es/noticias-cine/g29530040/harry-potter-cual-es-tu-casa-de-hogwarts/
      """
  ),
  HUFFLEPUFF(
    """
      ¡Hufflepuff!
      
      «La Casa de Hufflepuff se caracteriza por valorar la capacidad de trabajo, con estudiantes 
      amigables y leales. Los estudiantes de esta casa son conocidos por ser trabajadores, 
      amigables, leales y sin prejuicios.
      
      Colores: Amarillo y negro.
      
      Miembros más famosos:
      Newt Scamander, Cedric Diggory, Nymphadora Tonks, profesora Pomona Sporut.»
      
      REF: https://www.fotogramas.es/noticias-cine/g29530040/harry-potter-cual-es-tu-casa-de-hogwarts/
      """
  ),
  RAVENCLAW(
    """
      ¡Ravenclaw!
      
      «La Casa Ravenclaw valora el aprendizaje, la sabiduría, el ingenio, y el intelecto como
      elementos importantes para formar parte de su casa. Al ser magos de mucho talento,
      Hermione Granger estuvo a punto de ser seleccionada por Ravenclaw.
      
      Colores: Azul y bronce.
      
      Miembros más famosos:
      Luna Lovegood, Cho Chang.»
      
      REF: https://www.fotogramas.es/noticias-cine/g29530040/harry-potter-cual-es-tu-casa-de-hogwarts/
      """
  ),
  SLYTHERYN(
    """
      ¡Slytherin!
      
      «La Casa Slytherin cuenta con miembros ambiciosos, inteligentes, muy astutos y que tienden a 
      ser líderes fuertes. Aunque también son unos supervivientes, lo que les hace pensar antes de 
      actuar (al contrario que los Gryffindor), pese a tener un claro desprecio por las reglas.

      Colores: Verde y plata.

      Miembros más famosos:
      Voldemort, Draco Malfoy.»
      
      REF: https://www.fotogramas.es/noticias-cine/g29530040/harry-potter-cual-es-tu-casa-de-hogwarts/
      """
  )
}
