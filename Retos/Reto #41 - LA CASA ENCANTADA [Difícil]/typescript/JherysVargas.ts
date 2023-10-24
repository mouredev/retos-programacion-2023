type Position = {
  x: number;
  y: number;
};

type Question = {
  question: string;
  answer: string;
};

enum Moves {
  North = "norte",
  South = "sur",
  East = "este",
  West = "oeste",
}

enum ItemsEnum {
  START = "🚪",
  PHANTOM = "👻",
  CANDY = "🍭",
  EMPTY = "⬜️",
  CURRENT = "📍",
}

const questions: Question[] = [
  {
    question: "¿Cuál es la capital de Francia?",
    answer: "París",
  },
  {
    question: "¿Cuál es el planeta más grande del sistema solar?",
    answer: "Júpiter",
  },
  {
    question: "¿Cuál es el río más largo del mundo?",
    answer: "El río Amazonas",
  },
  {
    question: "¿Quién escribió 'Don Quijote de la Mancha'?",
    answer: "Miguel de Cervantes",
  },
  {
    question: "¿En qué año comenzó la Primera Guerra Mundial?",
    answer: "1914",
  },
  {
    question: "¿Cuál es el símbolo químico del oro?",
    answer: "Au",
  },
  {
    question: "¿Cuál es la montaña más alta del mundo?",
    answer: "El Monte Everest",
  },
  {
    question: "¿Quién pintó la 'Mona Lisa'?",
    answer: "Leonardo da Vinci",
  },
  {
    question: "¿Cuál es el océano más grande del mundo?",
    answer: "El océano Pacífico",
  },
  {
    question: "¿En qué año se fundó Google?",
    answer: "1998",
  },
  {
    question: "¿Quién escribió 'Romeo y Julieta'?",
    answer: "William Shakespeare",
  },
  {
    question: "¿Cuál es el símbolo químico del hidrógeno?",
    answer: "H",
  },
  {
    question: "¿Cuál es el elemento más abundante en la Tierra?",
    answer: "El oxígeno",
  },
  {
    question: "¿Cuál es el quinto planeta en el sistema solar?",
    answer: "Júpiter",
  },
  {
    question: "¿Cuál es la capital de Japón?",
    answer: "Tokio",
  },
  {
    question:
      "¿En qué año se firmó la Declaración de Independencia de los Estados Unidos?",
    answer: "1776",
  },
  {
    question: "¿Quién fue el primer presidente de Estados Unidos?",
    answer: "George Washington",
  },
  {
    question: "¿Cuál es la fórmula química del agua?",
    answer: "H2O",
  },
  {
    question: "¿Quién fue el primer ser humano en orbitar la Tierra?",
    answer: "Yuri Gagarin",
  },
  {
    question: "¿Cuál es el metal más abundante en la corteza terrestre?",
    answer: "El aluminio",
  },
  {
    question: "¿Cuál es la capital de Australia?",
    answer: "Camberra",
  },
  {
    question: "¿Quién escribió '1984'?",
    answer: "George Orwell",
  },
  {
    question: "¿Cuál es el símbolo químico del carbono?",
    answer: "C",
  },
  {
    question: "¿En qué año se cayó el Muro de Berlín?",
    answer: "1989",
  },
  {
    question: "¿Quién fue el primer hombre en la Luna?",
    answer: "Neil Armstrong",
  },
  {
    question: "¿Cuál es la capital de China?",
    answer: "Pekín",
  },
  {
    question: "¿En qué año se descubrió la penicilina?",
    answer: "1928",
  },
  {
    question: "¿Cuál es el océano más pequeño del mundo?",
    answer: "El océano Ártico",
  },
  {
    question: "¿Quién escribió 'Cien años de soledad'?",
    answer: "Gabriel García Márquez",
  },
  {
    question: "¿Cuál es la moneda de Japón?",
    answer: "El yen",
  },
  {
    question: "¿En qué año se fundó Microsoft?",
    answer: "1975",
  },
];

const positions: Map<ItemsEnum, Position> = new Map<ItemsEnum, Position>();

const uniqueItems: Readonly<Set<ItemsEnum>> = new Set([
  ItemsEnum.START,
  ItemsEnum.CANDY,
]);

const items: Readonly<Array<ItemsEnum>> = Object.values(ItemsEnum);

const sleep = (ms = 200): Promise<void> => {
  return new Promise((resolve) => setTimeout(resolve, ms));
};

const generateMansion = (): Array<Array<ItemsEnum>> => {
  let board: ItemsEnum[][] = [];

  const addedItems: Set<ItemsEnum> = new Set<ItemsEnum>();

  for (let y = 0; y < 4; y++) {
    board[y] = [];
    for (let x = 0; x < 4; x++) {
      const randomItem = getRandomItem(addedItems);

      addedItems.add(randomItem);

      if (randomItem === ItemsEnum.START) {
        positions.set(ItemsEnum.START, { x, y });
      }

      if (randomItem === ItemsEnum.CANDY) {
        positions.set(ItemsEnum.CANDY, { x, y });
      }

      board[y][x] = randomItem;
    }
  }

  return board;
};

const getRandomItem = (addedItems: Set<ItemsEnum>): ItemsEnum => {
  let item: ItemsEnum;

  do {
    const randomItem = Math.floor(Math.random() * (items.length - 1));
    item = items[randomItem];
  } while (uniqueItems.has(item) && addedItems.has(item));

  return item;
};

const showCurrentPosition = (board: ItemsEnum[][]) => {
  console.log("Actualmente estás aquí");

  const currentPosition: Position = positions.get(ItemsEnum.START)!;

  for (let y = 0; y < board.length; y++) {
    const rows: Array<ItemsEnum> = board[y].map(
      (item: ItemsEnum, x: number) => {
        if (x === currentPosition.x && y === currentPosition.y) {
          return ItemsEnum.CURRENT;
        }

        if (item !== ItemsEnum.START) {
          return ItemsEnum.EMPTY;
        }

        return item;
      }
    );

    console.log(rows);
  }
};

const getMove = (): string | null => {
  const possibleMoves: Set<Moves> = new Set(Object.values(Moves));
  const currentPosition: Position = positions.get(ItemsEnum.START)!;

  if (currentPosition.y === 0) {
    possibleMoves.delete(Moves.North);
  } else if (currentPosition.y === 3) {
    possibleMoves.delete(Moves.South);
  }

  if (currentPosition.x === 0) {
    possibleMoves.delete(Moves.West);
  } else if (currentPosition.x === 3) {
    possibleMoves.delete(Moves.East);
  }

  let response: string | null = "";
  const moves: string[] = [];

  possibleMoves.forEach((_, value) => {
    moves.push(value);
  });

  while (!moves.includes(response?.toLowerCase() ?? "")) {
    const textQuestion: string = `A donde quieres desplazarte? (${moves.join(
      "/"
    )})`;
    response = prompt(textQuestion);
  }

  return response;
};

const getNewPosition = (move: string): Position => {
  const { x, y }: Position = positions.get(ItemsEnum.START)!;

  if (move === Moves.North) {
    return { x, y: y - 1 };
  }
  if (move === Moves.South) {
    return { x, y: y + 1 };
  }
  if (move === Moves.East) {
    return { x: x + 1, y };
  }
  return { x: x - 1, y };
};

const updatePosition = (position: Position) => {
  positions.set(ItemsEnum.START, position);
};

const handleAskQuestion = (containPhantom: boolean): boolean => {
  let counter = containPhantom ? 2 : 1;

  while (counter) {
    if (containPhantom) alert("Apareció un fantasma, respondes 2 preguntas!");

    const numRandomQuestion: number = Math.floor(
      Math.random() * questions.length
    );

    const { question, answer } = questions[numRandomQuestion];

    const response: string = prompt(question) ?? "";

    const correctAnswer = response?.toLowerCase() === answer.toLowerCase();

    if (correctAnswer) {
      counter--;
      questions.splice(numRandomQuestion, 1);
    } else {
      alert("Respuesta incorrecta!");
    }
  }

  return !counter;
};

const validateFinishGame = (board: ItemsEnum[][], move: string): boolean => {
  const newPosition = getNewPosition(move!);
  const { x: endX, y: endY }: Position = positions.get(ItemsEnum.CANDY)!;

  if (newPosition.x === endX && newPosition.y === endY) {
    updatePosition(newPosition);
    return true;
  }

  if (
    handleAskQuestion(board[newPosition.y][newPosition.x] === ItemsEnum.PHANTOM)
  ) {
    updatePosition(newPosition);
  }

  return false;
};

const runGame = async (board: ItemsEnum[][]) => {
  let finishGame = false;

  while (!finishGame) {
    showCurrentPosition(board);
    await sleep();
    const move = getMove();
    finishGame = validateFinishGame(board, move!);
  }

  console.log("Felicidades, haz completado el juego 🎉🎉!");
};

const board = generateMansion();

runGame(board);
