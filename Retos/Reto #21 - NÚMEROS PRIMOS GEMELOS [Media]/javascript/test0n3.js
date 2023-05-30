function PrimeNumber(input) {
  let limit = input;
  let twinPrimes = setTwinPrimes();

  function validLimit(input) {
    if (input < 2) {
      return false;
    }
    return true;
  }

  function isPrime(num) {
    let limit = Math.floor(Math.sqrt(num));
    if (limit <= 2) {
      limit = num - 1;
    }
    for (let divisor = 2; divisor <= limit; divisor++) {
      if (num % divisor == 0) {
        return false;
      }
    }
    return true;
  }

  function setTwinPrimes() {
    let temp = [];
    let resp = [];

    if (!validLimit(limit)) {
      return `${input} is not a valid input`;
    }

    for (let number = 2; number <= limit; number++) {
      if (!isPrime(number)) {
        continue;
      }

      temp.push(number);

      if (temp.length < 2) {
        continue;
      }

      let a = temp[0];
      let b = temp[1];
      if (b - a == 2) {
        resp.push([a, b]);
      }
      temp.shift();
    }
    return resp;
  }

  Object.defineProperty(this, "twinPrimes", {
    get: function () {
      return twinPrimes;
    },
  });
}

// console.log(new PrimeNumber(1).twinPrimes);
// console.log(new PrimeNumber(3).twinPrimes);
// console.log(new PrimeNumber(14).twinPrimes);
