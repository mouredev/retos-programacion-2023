
// readline es un módulo en Node.js que proporciona una interfaz para leer datos desde un flujo de entrada

import * as readline from 'readline';

// Creamos la interfaz para realizar operaciones de entrada/salida
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Preguntamos si queremos mostrar el menú de nuevo
const menuPrompt = () => {
  drawLine();
  console.log("(Introduce '0' si quieres volver a mostrar el menú.)");
  handleUserChoice();
};

const drawLine = () => console.log("------------------------");

// creamos una clase para gestionar los participantes
class ParticipantesSorteoaDEViento {
  participants: string[];

  constructor() {
    this.participants = [];
  }

  // métodos para gestionar la clase
  addParticipant(participantName: string): void {
    if (this.participants.includes(participantName))
      console.log("El Participante ya existe");
    else {
      this.participants.push(participantName);
      console.log(`Felicidades! ${participantName} ha sido añadido.`);
    }
  }

  removeParticipant(participantName: string): void {
    if (this.participants.includes(participantName)) {
      const index = this.participants.indexOf(participantName);
      this.participants.splice(index, 1);
      console.log(`${participantName} ha sido eliminado del sorteo.`);
    } else console.log("El Participante no existe");
  }

  showParticpants(): void {
    this.participants.length === 0
      ? console.log("No hay ningún participante")
      : this.participants.forEach((e) => console.log(e));
  }

  theWinnerIs(): void {
    if (this.participants.length === 0)
      console.log("No hay ningún participante todavía");
    else {
      const indexWinner = Math.floor(Math.random() * this.participants.length);
      const winnerName = this.participants[indexWinner];

      console.log(`Muchas Felicidades! El ganador es ${winnerName}`);
      this.removeParticipant(winnerName);
    }
  }
}

// creamos los participantes e inicializamos mostrando el menú
const participants = new ParticipantesSorteoaDEViento();
showMenu();

// Mostamos el menú de opciones en la terminal
function showMenu(): void {
  console.log(`Menú:
  1. Añade un nuevo participante.
  2. Borra un participante.
  3. Muestra todos los participantes.
  4. Elije un ganador.
  5. Salir.`);
  drawLine();
  handleUserChoice();
}

// configuramos rl para leer desde la consola y escribir en la consola.
function handleUserChoice(): void {
  rl.question("Selecciona una opción: ", (respuesta) => {
    drawLine();
    // respuesta recibe una string=>  la convertimos a number
    switch (Number(respuesta)) {
      case 0:
        showMenu();
        break;
      case 1:
        rl.question("Introduce un participante: ", (respuesta) => {
          participants.addParticipant(respuesta);
          menuPrompt();
        });
        break;
      case 2:
        rl.question("Introduce el participante a eliminar: ", (respuesta) => {
          participants.removeParticipant(respuesta);
          menuPrompt();
        });

        break;
      case 3:
        participants.showParticpants();
        menuPrompt();
        break;
      case 4:
        participants.theWinnerIs();
        menuPrompt();
        break;
      case 5:
        rl.close();
        break;
      default:
        console.log(
          "Esta opción no es valida. Selecciona una opción del menú."
        );
        drawLine();
        showMenu();
    }
  });
}

// Cerrar la interfaz readline al finalizar
rl.on("close", () => {
  console.log("¡Hasta luego!");
  process.exit(0);
});
