const lehmerGenerator = (seed) => {
  for (let i = 0; i < 100; i++) {
    seed = ((seed * 48_271) % 2 ** 31) - 1;
  }
  return seed;
};

const getRandomWithEpoc = () => {
  return lehmerGenerator(Date.now()) % 101;
};

console.log(getRandomWithEpoc());
