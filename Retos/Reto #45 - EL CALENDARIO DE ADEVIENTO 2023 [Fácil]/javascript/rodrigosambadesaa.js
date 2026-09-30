'use strict';

class AdventRaffle {
  constructor(random = Math.random) {
    this.random = random;
    this.participants = new Set();
  }

  add(name) {
    const participant = String(name).trim();
    if (!participant || this.participants.has(participant)) return false;
    this.participants.add(participant);
    return true;
  }

  remove(name) {
    return this.participants.delete(String(name).trim());
  }

  list() {
    return [...this.participants];
  }

  draw() {
    if (!this.participants.size) return null;
    const participants = this.list();
    const winner = participants[Math.floor(this.random() * participants.length)];
    this.participants.delete(winner);
    return winner;
  }
}

module.exports = { AdventRaffle };

if (require.main === module) {
  const raffle = new AdventRaffle();
  process.argv.slice(2).forEach(name => raffle.add(name));
  console.log(`Ganador: ${raffle.draw() ?? 'sin participantes'}`);
}
