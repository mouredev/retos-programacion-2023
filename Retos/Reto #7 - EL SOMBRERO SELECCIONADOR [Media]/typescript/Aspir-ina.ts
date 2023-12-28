/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */
import { intro, outro, select } from "@clack/prompts"

const questions = [
  {
    question: '¿Qué es lo que más te gusta de la magia?',
    answers: [
      'La magia oscura',
      'La magia blanca',
      'La magia de la naturaleza',
      'La magia de la mente'
    ]
  },
  {
    question: '¿Qué animal te gustaría ser?',
    answers: [

      'Un dragón',
      'Un lobo',
      'Un águila',
      'Un león'
    ]
  },
  {
    question: '¿Qué es lo que más te gusta de Hogwarts?',
    answers: [
      'El bosque prohibido',
      'La sala común',
      'La biblioteca',
      'El gran comedor'
    ]
  },
  {
    question: '¿Qué es lo que más te gusta de la naturaleza?',
    answers: [
      'Las estrellas',
      'Los árboles',
      'Las flores',
      'Los animales'
    ]
  },
  {
    question: '¿Qué es lo que más te gusta de la vida?',
    answers: [
      'El poder',
      'La amistad',
      'El conocimiento',
      'La aventura'
    ]
  }
]

const houses = [
  {
    name: 'Gryffindor',
    description: 'Los valientes',
    traits: [
      'Valentía',
      'Lealtad',
      'Coraje',
      'Audacia'
    ]
  },
  {
    name: 'Slytherin',
    description: 'Los astutos',
    traits: [
      'Astucia',
      'Ambición',
      'Lealtad',
      'Coraje'
    ]
  },
  {
    name: 'Hufflepuff',
    description: 'Los leales',
    traits: [
      'Lealtad',
      'Valentía',
      'Coraje',
      'Audacia'
    ]
  },
  {
    name: 'Ravenclaw',
    description: 'Los sabios',
    traits: [
      'Inteligencia',
      'Astucia',
      'Lealtad',
      'Coraje'
    ]
  }
]

enum House {
  Slytherin,
  Hufflepuff,
  Ravenclaw,
  Gryffindor
}

const houseChooser = (answers: any[]) => {
  const gryffindor: number = answers.filter((answer: number) => answer === House.Gryffindor).length
  const slytherin: number = answers.filter((answer: number) => answer === House.Slytherin).length
  const hufflepuff: number = answers.filter((answer: number) => answer === House.Hufflepuff).length
  const ravenclaw: number = answers.filter((answer: number) => answer === House.Ravenclaw).length

  const housesArray: number[] = [gryffindor, slytherin, hufflepuff, ravenclaw]

  const max: number = Math.max(...housesArray)

  return houses[housesArray.indexOf(max)]
}

intro('Bienvenido al sombrero seleccionador de Hogwarts')

const answers: any[] = []
for (const question of questions) {
  const answer = await select({
    message: question.question,
    options: question.answers.map((answer: string, idx: number) => ({
      label: answer,
      value: idx
    }))
  })
  answers.push(answer)
}

const house = houseChooser(answers)

outro(`El sombrero seleccionador ha decidido que eres de la casa de ${house.name}. ¡Enhorabuena!`)
outro(`Los rasgos de la casa de ${house.name} son: ${house.traits.join(', ')}`)