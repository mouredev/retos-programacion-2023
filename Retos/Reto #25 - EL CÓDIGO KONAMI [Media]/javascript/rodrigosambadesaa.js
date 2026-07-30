'use strict';

const KONAMI = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'b', 'a'];

class KonamiDetector {
  constructor(sequence = KONAMI) {
    this.sequence = sequence;
    this.progress = 0;
  }

  press(key) {
    const normalized = String(key).toLowerCase();
    if (normalized === this.sequence[this.progress]) {
      this.progress++;
      if (this.progress === this.sequence.length) {
        this.progress = 0;
        return true;
      }
    } else {
      this.progress = normalized === this.sequence[0] ? 1 : 0;
    }
    return false;
  }
}

function listenForKonami(input = process.stdin) {
  const readline = require('node:readline');
  const detector = new KonamiDetector();
  readline.emitKeypressEvents(input);
  if (input.isTTY) input.setRawMode(true);
  console.log('Introduce el Código Konami (Ctrl+C para salir)');
  input.on('keypress', (_, key) => {
    if (key.ctrl && key.name === 'c') process.exit();
    if (detector.press(key.name)) console.log('¡Código Konami detectado!');
  });
}

module.exports = { KONAMI, KonamiDetector, listenForKonami };

if (require.main === module) listenForKonami();
