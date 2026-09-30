'use strict';

const RIDDLES = [
  { question: 'Tengo agujas y no sé coser. ¿Qué soy?', answer: 'reloj' },
  { question: 'Cuanto más seco, más mojo. ¿Qué soy?', answer: 'toalla' },
  { question: 'Tiene dientes y no come. ¿Qué es?', answer: 'peine' },
  { question: 'Vuelo sin alas y lloro sin ojos. ¿Qué soy?', answer: 'nube' }
];
const DIRECTIONS = {
  norte: [-1, 0], sur: [1, 0], este: [0, 1], oeste: [0, -1]
};

class HauntedHouse {
  constructor(random = Math.random) {
    this.random = random;
    this.position = [0, 0];
    this.candy = [3, 2];
    this.pending = [];
  }

  options() {
    return Object.entries(DIRECTIONS)
      .filter(([, [row, column]]) => {
        const next = [this.position[0] + row, this.position[1] + column];
        return next.every(value => value >= 0 && value < 4);
      })
      .map(([direction]) => direction);
  }

  enterRoom() {
    if (this.won || (this.position[0] === 0 && this.position[1] === 0)) {
      this.pending = [];
      return;
    }
    const count = this.random() < 0.1 ? 2 : 1;
    this.pending = Array.from({ length: count }, () => RIDDLES[Math.floor(this.random() * RIDDLES.length)]);
  }

  get riddle() {
    return this.pending[0]?.question ?? null;
  }

  answer(value) {
    if (!this.pending.length) return true;
    if (String(value).trim().toLocaleLowerCase('es') !== this.pending[0].answer) return false;
    this.pending.shift();
    return this.pending.length === 0;
  }

  move(direction) {
    if (this.pending.length) throw new Error('Primero debes resolver el enigma');
    if (!this.options().includes(direction)) throw new Error('Movimiento no válido');
    const movement = DIRECTIONS[direction];
    this.position = [this.position[0] + movement[0], this.position[1] + movement[1]];
    this.enterRoom();
    return this.position;
  }

  get won() {
    return this.position[0] === this.candy[0] && this.position[1] === this.candy[1];
  }
}

module.exports = { HauntedHouse, RIDDLES };

if (require.main === module) console.log('Importa HauntedHouse para comenzar la aventura.');
