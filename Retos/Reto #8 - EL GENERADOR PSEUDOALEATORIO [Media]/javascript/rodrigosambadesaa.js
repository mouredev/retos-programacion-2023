'use strict';

class PseudoRandom {
  constructor(seed = Date.now()) {
    this.state = Math.abs(Math.trunc(seed)) % 2147483647 || 1;
  }

  next() {
    this.state = this.state * 16807 % 2147483647;
    return this.state % 101;
  }
}

module.exports = { PseudoRandom };

if (require.main === module) console.log(new PseudoRandom().next());
