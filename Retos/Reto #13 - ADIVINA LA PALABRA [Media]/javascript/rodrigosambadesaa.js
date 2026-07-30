'use strict';

class WordGame {
  constructor(word, attempts = 6, random = Math.random) {
    if (!word || !Number.isInteger(attempts) || attempts < 1) throw new Error('Configuración no válida');
    this.word = String(word);
    this.attempts = attempts;
    this.revealed = Array.from(this.word, character => character === ' ');
    const positions = [...this.word].map((_, index) => index).filter(index => this.word[index] !== ' ');
    for (let index = positions.length - 1; index > 0; index--) {
      const other = Math.floor(random() * (index + 1));
      [positions[index], positions[other]] = [positions[other], positions[index]];
    }
    const hidden = Math.max(1, Math.floor(positions.length * 0.6));
    this.revealed.fill(true);
    positions.slice(0, hidden).forEach(index => { this.revealed[index] = false; });
  }

  get maskedWord() {
    return [...this.word].map((character, index) => this.revealed[index] ? character : '_').join('');
  }

  get status() {
    if (this.revealed.every(Boolean)) return 'won';
    return this.attempts === 0 ? 'lost' : 'playing';
  }

  guess(value) {
    if (this.status !== 'playing') return this.result();
    const guess = String(value).toLocaleLowerCase('es');
    const target = this.word.toLocaleLowerCase('es');
    let hit = false;
    if ([...guess].length === 1) {
      [...target].forEach((character, index) => {
        if (character === guess) {
          this.revealed[index] = true;
          hit = true;
        }
      });
    } else if (guess === target) {
      this.revealed.fill(true);
      hit = true;
    }
    if (!hit) this.attempts--;
    return this.result();
  }

  result() {
    return { word: this.maskedWord, attempts: this.attempts, status: this.status };
  }
}

module.exports = { WordGame };

if (require.main === module) {
  const game = new WordGame('mouredev');
  console.log(game.result());
}
