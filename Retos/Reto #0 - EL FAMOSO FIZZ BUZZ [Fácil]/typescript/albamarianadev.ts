const fizzBuzz = () => {
  const max = 100;

  for (let i = 0; i <= 100; i++) {
    let name;
    const fizz = i % 3 === 0 ? true : false;
    const buzz = i % 5 === 0 ? true : false;
    const fizzbuzz = i % 3 === 0 && i % 5 === 0 ? true : false;
  
    if (fizz === true) {
      name = 'fizz';
    } else if (buzz === true) {
      name = 'buzz';
    } else if (fizzbuzz === true) {
      name = 'fizzbuzz';
    } else {
      name = i;
    }
    console.log(name);
  }
}

fizzBuzz();
