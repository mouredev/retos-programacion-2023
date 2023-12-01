import readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

enum RoomType {
  Door,
  Room,
  Ghost,
  Exit
};

type Mansion = [
  [RoomType, RoomType, RoomType, RoomType],
  [RoomType, RoomType, RoomType, RoomType],
  [RoomType, RoomType, RoomType, RoomType],
  [RoomType, RoomType, RoomType, RoomType],
];

type Position = [number, number];

interface Question {
  q: string;
  a: string;
}

const questions: Array<Question> = [
  {
    "q": "¿Qué se moja mientras se seca?",
    "a": "Una toalla."
  },
  {
    "q": "¿Qué tiene un mar pero no agua?",
    "a": "Un mapa."
  },
  {
    "q": "¿Qué es tan frágil que decir su nombre lo rompe?",
    "a": "El silencio."
  },
  {
    "q": "¿Cuál palabra se escribe incorrectamente en todos los diccionarios?",
    "a": "Incorrectamente."
  },
  {
    "q": "Cuanto más la quitas, más grande se vuelve. ¿Qué es?",
    "a": "Un agujero."
  },
  {
    "q": "Si tienes doce manzanas y te llevas todas menos nueve, ¿cuántas tienes?",
    "a": "Nueve."
  },
  {
    "q": "Un avión choca en la frontera entre Canadá y Estados Unidos. ¿Dónde entierran a los sobrevivientes?",
    "a": "No se entierran a los sobrevivientes."
  },
  {
    "q": "¿Qué pesa más: un kilogramo de hierro o un kilogramo de plumas?",
    "a": "Pesa lo mismo, un kilogramo."
  },
  {
    "q": "¿Qué viene antes que ayer?",
    "a": "Anteayer."
  },
  {
    "q": "Si un tren eléctrico viaja hacia el sur, ¿hacia qué dirección sopla el humo?",
    "a": "Los trenes eléctricos no producen humo."
  },
  {
    "q": "¿Qué pregunta nunca puede ser respondida con un 'sí'?",
    "a": "¿Estás dormido?"
  },
  {
    "q": "¿Qué tiene un inicio y un final, pero no un principio ni un fin?",
    "a": "Una cuerda."
  },
  {
    "q": "¿Qué tiene cientos de dientes pero no puede morder?",
    "a": "Un peine."
  },
  {
    "q": "¿Qué es amarillo por fuera y blanco por dentro?",
    "a": "Un plátano."
  },
  {
    "q": "¿Qué palabra empieza con 'e' y termina con 'e' pero solo tiene una letra?",
    "a": "Sobre."
  },
  {
    "q": "¿Qué tiene una cabeza, una cola, pero no cuerpo?",
    "a": "Una moneda."
  },
  {
    "q": "¿Qué es más útil cuando está roto?",
    "a": "Un huevo."
  },
  {
    "q": "¿Qué se rompe sin tocarse?",
    "a": "Una promesa."
  },
  {
    "q": "¿Qué tiene infinitas palabras?",
    "a": "Un libro."
  },
  {
    "q": "¿Qué puedes atrapar pero no lanzar?",
    "a": "Un resfriado."
  },
  {
    "q": "¿Qué es más alto cuando está sentado que cuando está de pie?",
    "a": "Un perro."
  },
  {
    "q": "¿Qué es de tu padre, de tu madre, pero no es tuyo ni de tus hermanos?",
    "a": "Tu apellido."
  },
  {
    "q": "¿Qué tiene un banco pero no tiene dinero?",
    "a": "Un banco de un parque."
  },
  {
    "q": "¿Qué tiene ciudades pero no casas, ríos pero no agua, y bosques pero no árboles?",
    "a": "Un mapa."
  },
  {
    "q": "¿Qué es tan liviano que puede flotar en el aire, pero un hombre no puede sostenerlo por mucho tiempo?",
    "a": "Su aliento."
  },
  {
    "q": "¿Qué es lo que todos tienen delante y los pocos detrás?",
    "a": "El futuro."
  },
  {
    "q": "Si ves una ardilla en una jaula y un conejo en otra, ¿cuántas patas ves en total?",
    "a": "Ninguna, porque no puedes ver a través de las jaulas."
  },
  {
    "q": "¿Qué se llena con una mano pero puede llevar algo más grande que una casa?",
    "a": "Un guante."
  },
  {
    "q": "¿Qué animal da vueltas y más vueltas mientras duerme?",
    "a": "El murciélago."
  },
  {
    "q": "¿Cuál es la única letra del abecedario que es vegetal?",
    "a": "La 'P' de papa."
  },
  {
    "q": "¿Qué es lo que sube y baja sin moverse?",
    "a": "La temperatura."
  },
  {
    "q": "Si me lanzas al agua, volveré. ¿Qué soy?",
    "a": "Una pelota."
  },
  {
    "q": "¿Qué pasa una vez en junio, dos veces en agosto y no pasa en septiembre?",
    "a": "La letra 'o'."
  },
  {
    "q": "¿Qué es algo que siempre sube pero nunca baja?",
    "a": "La edad."
  },
  {
    "q": "¿Qué se puede medir pero no se puede ver ni tocar?",
    "a": "El tiempo."
  },
  {
    "q": "¿Qué tiene patas pero no camina?",
    "a": "Una mesa."
  },
  {
    "q": "¿Qué es lo que si lo pones en un barril lo hará más ligero?",
    "a": "Un agujero."
  },
  {
    "q": "¿Qué es aquello que si lo compartes, lo pierdes?",
    "a": "Un secreto."
  },
  {
    "q": "¿Qué tiene un solo oído pero puede escuchar?",
    "a": "Una mazorca de maíz."
  },
  {
    "q": "¿Qué es lo que nunca vuelve aunque siempre va?",
    "a": "Ayer."
  },
  {
    "q": "¿Qué es más grande que un elefante pero no pesa nada?",
    "a": "La sombra de un elefante."
  },
  {
    "q": "¿Cuántos segundos hay en un año?",
    "a": "12 (el segundo día de enero, el segundo día de febrero, etc.)"
  },
  {
    "q": "¿Qué es lo que corre pero nunca camina, murmura pero nunca habla, tiene una cama pero nunca duerme y tiene una boca pero nunca come?",
    "a": "Un río."
  },
  {
    "q": "¿Qué tiene un río pero no tiene agua?",
    "a": "La palabra 'río'."
  },
  {
    "q": "¿Qué es lo que está lleno durante el día y vacío durante la noche?",
    "a": "Un zapato."
  },
  {
    "q": "¿Qué tiene un corazón que no siente?",
    "a": "Un melón."
  },
  {
    "q": "¿Qué es lo que tiene muchas llaves pero no abre ninguna puerta?",
    "a": "Un piano."
  },
  {
    "q": "¿Qué es lo que da vueltas y vueltas y permanece en el mismo lugar?",
    "a": "Una lavadora."
  },
  {
    "q": "Si un gallo pone un huevo en la cima de un tejado, ¿hacia qué lado caerá el huevo?",
    "a": "Los gallos no ponen huevos."
  },
  {
    "q": "¿Qué es lo que está al final del arcoíris?",
    "a": "La letra 's'."
  },
  {
    "q": "¿Qué es lo que es rojo cuando es nuevo, negro cuando lo usas y gris cuando lo tiras?",
    "a": "El carbón."
  },
  {
    "q": "¿Qué tiene muchas hojas pero no es un árbol?",
    "a": "Un libro."
  },
  {
    "q": "¿Qué es lo que si lo tiras al suelo, se rompe; pero si lo pones en el agua, flota?",
    "a": "Un papel."
  },
  {
    "q": "Si tres gatos cazan tres ratas en tres minutos, ¿cuántos minutos tardarían cien gatos en cazar cien ratas?",
    "a": "Tres minutos."
  },
  {
    "q": "¿Qué es lo que puedes encontrar en medio de París?",
    "a": "La letra 'r."
  },
  {
    "q": "¿Qué es lo que no tiene ni principio ni fin y está en medio de la noche?",
    "a": "La letra 'o."
  },
  {
    "q": "¿Qué es lo que es más grande que Dios, más malo que el diablo, los pobres lo tienen y los ricos lo necesitan?",
    "a": "Nada."
  },
  {
    "q": "¿Qué animal tiene la cabeza y la cola pero no tiene cuerpo?",
    "a": "Una moneda."
  },
  {
    "q": "¿Qué es lo que tiene forma de pera, pero más verde que la hierba, y si lo necesitas, te espera dentro de una cesta?",
    "a": "Una pelota."
  },
  {
    "q": "¿Qué tiene sábanas pero no duerme?",
    "a": "Un libro."
  },
  {
    "q": "¿Qué es lo que es tuyo, pero los demás lo usan más que tú?",
    "a": "Tu nombre."
  },
  {
    "q": "¿Qué es lo que tiene un montón de dientes pero no muerde?",
    "a": "Un peine."
  },
  {
    "q": "¿Qué animal es siempre anciano?",
    "a": "La cebra (porque es blanco y negro)."
  },
  {
    "q": "¿Qué es lo que es suyo pero otras personas lo usan más que usted?",
    "a": "Su nombre."
  },
  {
    "q": "¿Qué es lo que tiene pulpa, pepitas y no es una naranja?",
    "a": "Una manzana."
  },
  {
    "q": "¿Qué tiene tapa pero no es botella y es de madera pero no es árbol?",
    "a": "Una mesa."
  },
  {
    "q": "¿Qué es lo que tiene una lengua y no puede hablar?",
    "a": "Un zapato."
  },
  {
    "q": "¿Qué es lo que siempre está delante de ti pero no puedes verlo?",
    "a": "El futuro."
  },
  {
    "q": "¿Qué es lo que pasa y nunca regresa?",
    "a": "El tiempo."
  },
  {
    "q": "Si dos es compañía y tres es multitud, ¿cuatro y cinco son qué?",
    "a": "Nueve."
  },
  {
    "q": "¿Qué es lo que es más grande que un elefante pero no pesa nada?",
    "a": "La sombra de un elefante."
  },
  {
    "q": "¿Qué es lo que es negro cuando lo compras, rojo cuando lo usas y gris cuando lo tiras?",
    "a": "El carbón."
  },
  {
    "q": "¿Qué es lo que tiene agujas pero no cose?",
    "a": "Un reloj."
  },
  {
    "q": "¿Qué es lo que es tuyo pero otros lo usan más que tú?",
    "a": "Tu nombre."
  },
  {
    "q": "¿Qué es lo que te pertenece pero otros lo usan más que tú?",
    "a": "Tu nombre."
  },
  {
    "q": "¿Qué es lo que da vueltas todo el día y se queda en el mismo lugar?",
    "a": "Una puerta."
  },
  {
    "q": "¿Qué es lo que puedes ver en la oscuridad y es muy ligero?",
    "a": "La luz."
  },
  {
    "q": "¿Qué es lo que es más grande que un elefante pero no pesa nada?",
    "a": "La sombra de un elefante."
  },
  {
    "q": "¿Qué tiene una cama y no duerme, tiene una boca y no come?",
    "a": "Un río."
  },
  {
    "q": "¿Qué es lo que es tan alto como un pino y pesa menos que un ratón?",
    "a": "El humo."
  },
  {
    "q": "¿Qué es lo que tiene forma de pera pero no es fruta, tiene muchas llaves pero no puede abrir puertas?",
    "a": "Un llavero."
  },
  {
    "q": "¿Qué es lo que si lo lanzas al aire no caerá nunca al suelo?",
    "a": "Un pensamiento."
  },
  {
    "q": "¿Qué es lo que es más útil cuando está vacío?",
    "a": "Una mochila."
  },
  {
    "q": "¿Qué es lo que tiene orejas pero no puede oír?",
    "a": "Una jarra."
  },
  {
    "q": "¿Qué tiene cuatro ruedas y vuela?",
    "a": "Un camión de basura."
  },
  {
    "q": "¿Qué es lo que no puedes tener para el desayuno y la cena?",
    "a": "Almuerzo."
  },
  {
    "q": "¿Qué es lo que cuanto más tomas, más dejas atrás?",
    "a": "Pasos."
  },
  {
    "q": "¿Qué es lo que todos tienen pero algunos tienen más que otros?",
    "a": "Edad."
  },
  {
    "q": "¿Qué es lo que nunca pide respuestas pero siempre es respondido?",
    "a": "Un teléfono."
  },
  {
    "q": "¿Qué es lo que puedes servir pero nunca comer?",
    "a": "Una pelota de tenis."
  }
];

const mapTypeToEmoji: Record<RoomType, string> = {
  "0": '🚪',
  "1": '⬜️',
  "2": '👻',
  "3": '🍭'
};

const generateMansion = (): Mansion => {
  let mansion: Mansion = [
    [RoomType.Door, RoomType.Room, RoomType.Room, RoomType.Room],
    [RoomType.Room, RoomType.Room, RoomType.Room, RoomType.Room],
    [RoomType.Room, RoomType.Room, RoomType.Room, RoomType.Room],
    [RoomType.Room, RoomType.Room, RoomType.Room, RoomType.Room],
  ];
  const [outX, outY] = [(Math.floor(Math.random()*3) + 1), (Math.floor(Math.random()*3) + 1)]
  mansion[outY][outX] = RoomType.Exit;

  mansion = mansion.map(row =>
    row.map(cell => {
      if (cell !== RoomType.Room) return cell;
      if (Math.random() < 0.1) return RoomType.Ghost;
      return cell;
    })
  ) as Mansion;
  return mansion;
};

const printMansion = (mansion: Mansion, pos: Position, releasedRooms: Position[]) => {
  console.log(mansion.map((row, y) => row.map((cell, x) => {
    if (releasedRooms.some(rp => rp[0] === x && rp[1] === y)) return '✅';
    if (pos[0] === x && pos[1] === y) return '🧍';
    return mapTypeToEmoji[cell];
  }).join('')).join('\n'))
};

const askQuestion = (question: Question): Promise<boolean> => {
  return new Promise((resolve) => {
    rl.question(question.q, (answer) => {
      resolve(answer.toLowerCase() === question.a.toLowerCase());
    });
  });
};

const move = async (pos: Position, mansion: Mansion, releasedRooms: Position[]) => {
  const [x, y] = pos;
  let options: string[] = [];
  if (x > 0) options.push('oeste');
  if (x < 3) options.push('este');
  if (y > 0) options.push('norte');
  if (y < 3) options.push('sur');

  return new Promise<Position>((resolve) => {
    rl.question(`¿Dónde deseas moverte? (${options.join(', ')}) `, (movep) => {
      console.log({movep})
      switch (movep) {
        case 'norte':
          resolve([x, y - 1]);
          break;
        case 'sur':
          resolve([x, y + 1]);
          break;
        case 'este':
          resolve([x + 1, y]);
          break;
        case 'oeste':
          resolve([x - 1, y]);
          break;
        default:
          console.log('Opción inválida');
          move(pos, mansion, releasedRooms).then(resolve);
      }
    });
  });
};

const game = async () => {
  let winnedGames = 0;
  let playing = true;

  while (playing) {
    let userPosition: Position = [0, 0];
    let mansion = generateMansion();
    let releasedRooms: Array<Position> = [[0, 0]];

    while (mansion[userPosition[1]][userPosition[0]] !== RoomType.Exit) {
      printMansion(mansion, userPosition, releasedRooms);
      let currentRoom = mansion[userPosition[1]][userPosition[0]];

      if (currentRoom === RoomType.Ghost || currentRoom === RoomType.Room) {
        const success = await askQuestion(questions[Math.floor(Math.random() * questions.length)]);
        if (!success) continue; // If failed, don't move.
      }

      releasedRooms.push(userPosition);
      userPosition = await move(userPosition, mansion, releasedRooms);
    }

    winnedGames++;
    console.log("¡Has encontrado la sala de los dulces! 🍭");

    rl.question('¿Quieres jugar de nuevo? (sí/no) ', (answer) => {
      if (answer.toLowerCase() !== 'sí') {
        playing = false;
        console.log(`Has ganado ${winnedGames} ${winnedGames === 1 ? 'vez' : 'veces'}. ¡Gracias por jugar!`);
        rl.close();
      }
    });
  }
};

game();
