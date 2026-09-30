'use strict';

class CarRace {
  constructor(length = 10, random = Math.random) {
    if (!Number.isInteger(length) || length < 4) throw new Error('La pista debe tener al menos cuatro posiciones');
    this.length = length;
    this.random = random;
    this.cars = [
      { symbol: '🚙', position: length, stopped: false, trees: this.createTrees() },
      { symbol: '🚗', position: length, stopped: false, trees: this.createTrees() }
    ];
  }

  createTrees() {
    const trees = new Set();
    const amount = 1 + Math.floor(this.random() * 3);
    while (trees.size < amount) trees.add(1 + Math.floor(this.random() * (this.length - 1)));
    return trees;
  }

  step() {
    for (const car of this.cars) {
      if (car.position === 0) continue;
      if (car.stopped) {
        car.stopped = false;
        continue;
      }
      car.position = Math.max(0, car.position - (1 + Math.floor(this.random() * 3)));
      if (car.position > 0 && car.trees.has(car.position)) car.stopped = true;
    }
    return { tracks: this.render(), winner: this.winner() };
  }

  winner() {
    const finished = this.cars.filter(car => car.position === 0);
    if (!finished.length) return null;
    return finished.length === 2 ? 'Tie' : finished[0].symbol;
  }

  render() {
    return this.cars.map(car => {
      let track = '🏁';
      for (let position = 1; position <= this.length; position++) {
        if (position === car.position) track += car.stopped ? '💥' : car.symbol;
        else track += car.trees.has(position) ? '🌲' : '_';
      }
      return track;
    });
  }
}

module.exports = { CarRace };

if (require.main === module) {
  const race = new CarRace(Number(process.argv[2] ?? 10));
  while (!race.winner()) console.log(race.step().tracks.join('\n'), '\n');
  console.log(`Ganador: ${race.winner()}`);
}
