'use strict';

const fs = require('node:fs');

class TextFile {
  constructor(path = 'text.txt', fileSystem = fs) {
    this.path = path;
    this.fs = fileSystem;
  }

  exists() {
    return this.fs.existsSync(this.path);
  }

  read() {
    return this.exists() ? this.fs.readFileSync(this.path, 'utf8') : '';
  }

  append(line) {
    this.fs.appendFileSync(this.path, `${line}\n`, 'utf8');
  }

  reset() {
    this.fs.writeFileSync(this.path, '', 'utf8');
  }
}

async function runTerminal(path = 'text.txt') {
  const readline = require('node:readline/promises');
  const terminal = readline.createInterface({ input: process.stdin, output: process.stdout });
  const file = new TextFile(path);
  if (file.exists()) {
    const choice = (await terminal.question('¿Continuar (c) o borrar (b)? ')).toLowerCase();
    if (choice === 'b') file.reset();
    else console.log(file.read());
  }
  console.log('Escribe líneas. Usa /salir para terminar.');
  while (true) {
    const line = await terminal.question('> ');
    if (line === '/salir') break;
    file.append(line);
  }
  terminal.close();
}

module.exports = { TextFile, runTerminal };

if (require.main === module) runTerminal().catch(console.error);
