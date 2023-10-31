const board = [
  ["🚪", "⬜", "⬜", "⬜"],
  ["⬜", "⬜", "⬜", "⬜"],
  ["⬜", "⬜", "⬜", "⬜"],
  ["⬜", "⬜", "⬜", "⬜"],
];

const questions = {
  firstQuestion: { q: "¿Desea entrar a la casa? (y/n)", a: ["y"], e: "n" },
  restart: {
    q: "🎉 YOU WIN!\nQuieres jugar nuevamente(y/n)",
    a: ["y"],
    e: "n",
  },
  exit: { q: "quieres salir del juego? (y/n)", a: ["n"], e: "y" },
  questions: [
    {
      q: "¿Cuál es el libro más vendido de todos los tiempos?",
      a: ["La Biblia"],
    },
    {
      q: "¿Quién escribió el libro 'Cien años de soledad'?",
      a: ["Gabriel García Márquez"],
    },
    {
      q: "¿Cuál es el libro más largo de la historia?",
      a: ["'En busca del tiempo perdido' de Marcel Proust"],
    },
    {
      q: "¿Quién escribió el libro '1984'?",
      a: ["George Orwell"],
    },
    {
      q: "¿Cuál es el libro más traducido en el mundo después de la Biblia?",
      a: ["'El principito' de Antoine de Saint-Exupéry"],
    },
    {
      q: "¿Quién escribió el libro 'Don Quijote de la Mancha'?",
      a: ["Miguel de Cervantes"],
    },
    {
      q: "¿Cuál es el libro más antiguo que se conserva?",
      a: ["'La epopeya de Gilgamesh'"],
    },
    {
      q: "¿Quién escribió el libro 'Orgullo y prejuicio'?",
      a: ["Jane Austen"],
    },
    {
      q: "¿Cuál es el libro más vendido después de la Biblia?",
      a: [
        "'El ingenioso hidalgo Don Quijote de la Mancha' de Miguel de Cervantes",
      ],
    },
    {
      q: "¿Quién escribió el libro 'Matar a un ruiseñor'?",
      a: ["Harper Lee"],
    },
    {
      q: "¿Cuál es el libro más corto de la historia?",
      a: ["'La ocupación' de Sergio Chejfec"],
    },
    {
      q: "¿Quién escribió el libro 'Ulises'?",
      a: ["James Joyce"],
    },
    {
      q: "¿Cuál es el libro más caro del mundo?",
      a: ["'Codex Leicester' de Leonardo da Vinci"],
    },
    {
      q: "¿Quién escribió el libro 'Crimen y castigo'?",
      a: ["Fiódor Dostoyevski"],
    },
    {
      q: "¿Cuál es el libro más leído en el mundo después de la Biblia?",
      a: ["'El principito' de Antoine de Saint-Exupéry"],
    },
    {
      q: "¿Quién escribió el libro 'El gran Gatsby'?",
      a: ["F. Scott Fitzgerald"],
    },
    {
      q: "¿Cuál es el libro más pequeño del mundo?",
      a: ["'Teeny Ted from Turnip Town' de Malcolm Douglas Chisolm"],
    },
    {
      q: "¿Quién escribió el libro 'En busca del tiempo perdido'?",
      a: ["Marcel Proust"],
    },
    {
      q: "¿Cuál es el libro más vendido de la historia después de la Biblia?",
      a: [
        "'El ingenioso hidalgo Don Quijote de la Mancha' de Miguel de Cervantes",
      ],
    },
    {
      q: "¿Quién escribió el libro 'El principito'?",
      a: ["Antoine de Saint-Exupéry"],
    },
    {
      q: "¿Cuál es el libro más pesado del mundo?",
      a: [
        "'Bhutan: A Visual Odyssey Across the Last Himalayan Kingdom' de Michael Hawley",
      ],
    },
    {
      q: "¿Quién escribió el libro 'Romeo y Julieta'?",
      a: ["William Shakespeare"],
    },
    {
      q: "¿Cuál es el libro más antiguo que se conoce impreso?",
      a: ["La Biblia de Gutenberg"],
    },
    {
      q: "¿Quién escribió el libro 'Las aventuras de Alicia en el País de las Maravillas'?",
      a: ["Lewis Carroll"],
    },
    {
      q: "¿Cuál es el libro más leído en el mundo?",
      a: ["La Biblia"],
    },
    {
      q: "¿Quién escribió el libro 'Las crónicas de Narnia'?",
      a: ["C.S. Lewis"],
    },
    {
      q: "¿Cuál es el libro más caro vendido en una subasta?",
      a: ["'Codex Leicester' de Leonardo da Vinci"],
    },
    {
      q: "¿Quién escribió el libro 'El señor de los anillos'?",
      a: ["J.R.R. Tolkien"],
    },
    {
      q: "¿Cuál es el libro más popular de Harry Potter?",
      a: ["'Harry Potter y la piedra filosofal'"],
    },
    {
      q: "¿Quién escribió el libro 'Moby Dick'?",
      a: ["Herman Melville"],
    },
    {
      q: "¿Cuál es el libro más vendido de la historia?",
      a: ["La Biblia"],
    },
    {
      q: "¿Quién escribió el libro 'El código Da Vinci'?",
      a: ["Dan Brown"],
    },
    {
      q: "¿Cuál es el libro más famoso de Sherlock Holmes?",
      a: ["'El sabueso de los Baskerville'"],
    },
    {
      q: "¿Quién escribió el libro 'Los juegos del hambre'?",
      a: ["Suzanne Collins"],
    },
    {
      q: "¿Cuál es el libro más antiguo del mundo?",
      a: ["'La epopeya de Gilgamesh'"],
    },
    {
      q: "¿Quién escribió el libro 'El retrato de Dorian Gray'?",
      a: ["Oscar Wilde"],
    },
    {
      q: "¿Cuál es el libro más vendido en el siglo XX?",
      a: ["'El principito' de Antoine de Saint-Exupéry"],
    },
    {
      q: "¿Quién escribió el libro 'Crepúsculo'?",
      a: ["Stephenie Meyer"],
    },
    {
      q: "¿Cuál es el libro más famoso de Julio Verne?",
      a: ["'Veinte mil leguas de viaje submarino'"],
    },
    {
      q: "¿Quién escribió el libro 'La Odisea'?",
      a: ["Homero"],
    },
    {
      q: "¿Cuál es el libro más leído de Harry Potter?",
      a: ["'Harry Potter y la piedra filosofal'"],
    },
    {
      q: "¿Quién escribió el libro 'El alquimista'?",
      a: ["Paulo Coelho"],
    },
    {
      q: "¿Cuál es el libro más antiguo que se conserva completo?",
      a: ["La Biblia"],
    },
    {
      q: "¿Quién escribió el libro 'El nombre de la rosa'?",
      a: ["Umberto Eco"],
    },
    {
      q: "¿Cuál es el libro más vendido en el siglo XXI?",
      a: ["'Harry Potter y las reliquias de la muerte'"],
    },
    {
      q: "¿Quién escribió el libro 'El gran Gatsby'?",
      a: ["F. Scott Fitzgerald"],
    },
    {
      q: "¿Cuál es el libro más famoso de Agatha Christie?",
      a: ["'Diez negritos'"],
    },
    {
      q: "¿Quién escribió el libro 'El león, la bruja y el armario'?",
      a: ["C.S. Lewis"],
    },
    {
      q: "¿Cuál es el libro más leído de la historia?",
      a: ["La Biblia"],
    },
    {
      q: "¿Quién escribió el libro 'El diario de Ana Frank'?",
      a: ["Ana Frank"],
    },
    {
      q: "¿Cuál es el libro más vendido de no ficción?",
      a: ["'El libro tibetano de los muertos'"],
    },
    {
      q: "¿Quién escribió el libro 'La metamorfosis'?",
      a: ["Franz Kafka"],
    },
    {
      q: "¿Cuál es el libro más vendido de ciencia ficción?",
      a: ["'Dune' de Frank Herbert"],
    },
    {
      q: "¿Quién escribió el libro 'Los pilares de la Tierra'?",
      a: ["Ken Follett"],
    },
    {
      q: "¿Cuál es el libro más largo del mundo?",
      a: ["'En busca del tiempo perdido' de Marcel Proust"],
    },
    {
      q: "¿Quién escribió el libro 'La sombra del viento'?",
      a: ["Carlos Ruiz Zafón"],
    },
    {
      q: "¿Cuál es el libro más vendido de autoayuda?",
      a: ["'El secreto' de Rhonda Byrne"],
    },
    {
      q: "¿Quién escribió el libro 'La guerra y la paz'?",
      a: ["León Tolstói"],
    },
    {
      q: "¿Cuál es el libro más vendido de la historia después de la Biblia?",
      a: [
        "'El ingenioso hidalgo Don Quijote de la Mancha' de Miguel de Cervantes",
      ],
    },
    {
      q: "¿Quién escribió el libro 'El principito'?",
      a: ["Antoine de Saint-Exupéry"],
    },
    {
      q: "¿Cuál es el libro más pesado del mundo?",
      a: [
        "'Bhutan: A Visual Odyssey Across the Last Himalayan Kingdom' de Michael Hawley",
      ],
    },
    {
      q: "¿Quién escribió el libro 'Romeo y Julieta'?",
      a: ["William Shakespeare"],
    },
    {
      q: "¿Cuál es el libro más antiguo que se conoce impreso?",
      a: ["La Biblia de Gutenberg"],
    },
    {
      q: "¿Quién escribió el libro 'Las aventuras de Alicia en el País de las Maravillas'?",
      a: ["Lewis Carroll"],
    },
    {
      q: "¿Cuál es el libro más leído en el mundo?",
      a: ["La Biblia"],
    },
  ],
};

let position: [number, number];

const directions: {
  [key: string]: { value: [number, number]; text: string; go: boolean };
} = {
  w: {
    value: [-1, 0],
    text: "arriba[W]",
    go: false,
  },
  d: {
    value: [0, 1],
    text: "derecha[D]",
    go: false,
  },
  s: {
    value: [1, 0],
    text: "abajo[S]",
    go: false,
  },
  a: {
    value: [0, -1],
    text: "izquierda[A]",
    go: false,
  },
};

const getRandomIndex = () => {
  return Math.floor(Math.random() * questions.questions.length);
};

const exit = (log: string) => {
  console.log(`\n${log}`);
  Deno.exit();
};

const askQuestion = async (
  { q, a, e }: { q: string; a?: string[]; e?: string },
) => {
  Deno.stdout.writeSync(new TextEncoder().encode("\x1b[2J\x1b[0;0H"));
  const buf = new Uint8Array(1024);
  const outBoard = board.map((row) => row.join(""));
  Deno.stdout.write(
    new TextEncoder().encode(
      `Titulo\n${outBoard.join("\n")}\n${q}: `,
    ),
  );
  const n = await Deno.stdin.read(buf) || undefined;
  const answer = new TextDecoder().decode(buf.subarray(0, n)).trim()
    .toLowerCase();

  if (answer === "e") return exit("🏃💨 Saliendo...");
  if (a?.includes(answer)) return answer;
  if (answer === e) return false;
  return undefined;
};

const move = async ([x, y]: number[]) => {
  let keepAsking;

  do {
    keepAsking = true;

    directions.s.go = (position[0] < 3) ? true : false;
    directions.w.go = (position[0] > 0) ? true : false;
    directions.d.go = (position[1] < 3) ? true : false;
    directions.a.go = (position[1] > 0) ? true : false;

    const options = Object.keys(directions)
      .map((key) => directions[key].go && directions[key].text)
      .filter(Boolean);

    Deno.stdin.setRaw(true);
    const direction = await askQuestion(
      {
        q: `a donde te quieres mover?\n${options.join(" ")}`,
        a: ["s", "w", "a", "d"],
      },
    );
    if (
      direction === undefined || direction === false ||
      !directions[direction].go
    ) {
      continue;
    }

    const [xMove, yMove] = directions[direction].value;
    position[0] += xMove;
    position[1] += yMove;
    keepAsking = false;

    Deno.stdin.setRaw(false);

    if (position[0] === 0 && position[1] === 0) {
      Deno.stdin.setRaw(true);
      const answer = await askQuestion(questions.exit);
      if (answer === false) {
        return exit("🏃💨 Saliendo...");
      } else {
        Deno.stdin.setRaw(false);
        position = [x, y];
        keepAsking = true;
        continue;
      }
    }
  } while (keepAsking);

  !(x === 0 && y === 0) && (board[x][y] = "⬜");

  if (position[0] === 3 && position[1] === 3) {
    let answer;

    board[position[0]][position[1]] = "🍭";
    do {
      answer = await askQuestion(questions.restart);
      (answer === false) && Deno.exit();
    } while (!answer);

    return main();
  }

  if (Math.random() < 0.1) {
    board[position[0]][position[1]] = "👻";
    return "double";
  } else {
    board[position[0]][position[1]] = "❓";
    return "single";
  }
};

async function makeQuestion() {
  const mode = await move(position);
  let answer;

  if (mode === "double") {
    let count = 0;
    do {
      answer = await askQuestion(questions.questions[getRandomIndex()]);
      answer && ++count;
    } while (!(answer && count === 2));
  } else {
    do {
      answer = await askQuestion(questions.questions[getRandomIndex()]);
    } while (!answer);
  }

  await makeQuestion();
}

const main = async (): Promise<void> => {
  board[3][3] = "⬜";
  position = [0, 0];
  let answer;

  do {
    Deno.stdin.setRaw(true);
    answer = await askQuestion(questions.firstQuestion);
    if (answer === false) {
      exit("🏃💨 Saliendo...");
    }
  } while (!answer);

  Deno.stdin.setRaw(false);
  return await makeQuestion();
};

main();
