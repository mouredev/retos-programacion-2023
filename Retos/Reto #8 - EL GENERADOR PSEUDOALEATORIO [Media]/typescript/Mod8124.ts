let lastRandomNumber: number = 0;

// generate a random number
const randomNumber = (): number => {
  let date: Date = new Date();
  return date.getTime() % 100;
};

// if the number already exits, the fn generates another number
const getRandomNumber = (): number => {
  let currentRandomNumber = randomNumber();
  while (currentRandomNumber === lastRandomNumber) {
    currentRandomNumber = randomNumber();
  }
  lastRandomNumber = currentRandomNumber;
  return currentRandomNumber;
};

const num = getRandomNumber(); 
const num2 = getRandomNumber(); 