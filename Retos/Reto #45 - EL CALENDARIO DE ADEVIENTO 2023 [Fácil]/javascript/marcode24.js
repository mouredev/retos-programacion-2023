/*
 * ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
 * 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
 * Desde el 1 al 24 de diciembre.
 *
 * Crea un programa que simule el mecanismo de participación:
 * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
 *   participantes, mostrarlos, lanzar el sorteo o salir.
 * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
 * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
 *   (Y no lo duplicarás)
 * - Si seleccionas mostrar los participantes, se listarán todos.
 * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
 *   (Avisando de si lo has eliminado o el nombre no existe)
 * - Si seleccionas realizar el sorteo, elegirás una persona al azar 
 *   y se eliminará del listado.
 * - Si seleccionas salir, el programa finalizará.
 */

const readline = require('readline');

const participants = [];

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const showMenu = () => {
  console.log('\nSelecciona una opción:');
  console.log('1. Añadir participante');
  console.log('2. Mostrar participantes');
  console.log('3. Eliminar participante');
  console.log('4. Realizar sorteo');
  console.log('5. Salir');

  // eslint-disable-next-line no-use-before-define
  askOption();
};

const addParticipant = () => {
  rl.question('\nIntroduce el nombre del participante: ', (name) => {
    if (participants.includes(name)) {
      console.log('Este participante ya existe.');
    } else {
      participants.push(name);
      console.log('Participante añadido con éxito.');
    }
    showMenu();
  });
};

const showParticipants = () => {
  console.log('\nLista de participantes:');
  participants.forEach((participant, index) => {
    console.log(`${index + 1}. ${participant}`);
  });
  showMenu();
};

const removeParticipant = () => {
  rl.question('\nIntroduce el nombre del participante a eliminar: ', (name) => {
    const index = participants.indexOf(name);
    if (index !== -1) {
      participants.splice(index, 1);
      console.log('Participante eliminado con éxito.');
    } else {
      console.log('Este participante no existe.');
    }
    showMenu();
  });
};

const drawWinner = () => {
  if (participants.length === 0) {
    console.log('\nNo hay participantes para realizar el sorteo.');
  } else {
    const winnerIndex = Math.floor(Math.random() * participants.length);
    const winner = participants[winnerIndex];
    console.log(`\n¡El ganador es: ${winner}!`);
    participants.splice(winnerIndex, 1);
  }
  showMenu();
};

const askOption = () => {
  const menuOptions = {
    1: addParticipant,
    2: showParticipants,
    3: removeParticipant,
    4: drawWinner,
    5: () => rl.close(),
  };

  rl.question('Opción: ', (option) => (menuOptions[option] || (() => {
    console.log('\nOpción no válida. Inténtalo de nuevo.');
    showMenu();
  }))());
};

showMenu();

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
