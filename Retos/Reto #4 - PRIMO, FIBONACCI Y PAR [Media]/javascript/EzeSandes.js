function describeProps(num) {
  return `${num} ${isPrime(num) ? '' : 'no '}es primo,${
    isFibonacciNumber(num) ? '' : ' no es'
  } fibonacci y ${isEven(num) ? 'es par' : 'es impar'}`;
}

function isPrime(num) {
  if (num < 2) return false;

  for (let i = 2; i < num; i++) {
    if (num % i === 0) return false;
  }

  return true;
}

function isEven(num) {
  return num % 2 === 0;
}

function isFibonacciNumber(num) {
  if (num === 0) return true;
  if (num === 1) return true;

  let mem = [0, 1];

  for (let i = 2; i <= num + 1; i++) {
    mem.push(mem[i - 1] + mem[i - 2]);
  }

  return mem.some(fib => fib === num);
}

/************************************** TESTS */

// Case 00: Functionality test
// Desc: We seek to verify the correct functioning of the programme with the tests provided.
console.log('Case 00 : ', describeProps(2)); // Expected output => Prime: yes, fib: si, even: si
console.log('Case 00 : ', describeProps(7)); // Expected output => Prime: yes, fib: no, even: no

// Case 01: Prime number
// Desc: We seek a number that is prime.
console.log('Case 01 : ', describeProps(4441)); // Expected output => Prime: yes, fib: no, even: no

// Case 02: number 1 is not prime number.
// Desc: We seek to verify that the number 1 is not a prime number.
console.log('Case 02 : ', describeProps(4430)); // Expected output => Prime: no, fib: no, even: yes

// Case 03: number 0 is fib number
// Desc: We seek to verify that the number 0 is a fib number.
console.log('Case 03 : ', describeProps(0)); // Expected output => Prime: no, fib: yes, even: yes

// Case 04: extreme case fib number
// Desc: We seek to verify that a big number is a fib number, checking the correct functionality of the program.
console.log('Case 04 : ', describeProps(63245986)); // Expected output => Prime: no, fib: yes, even: yes

// Case 05: even number
// Desc: We seek to check that a given number is even.
console.log('Case 05 : ', describeProps(8)); // Expected output => Prime: no, fib: yes, even: yes

// Case 06: odd number
// Desc: We seek to check that a given number is odd.
console.log('Case 06 : ', describeProps(11)); // Expected output => Prime: yes, fib: no, even: no
