const pseudoRandom = () => {
  let date = new Date();
  let rn = date.getMilliseconds();
  rn = Math.round(rn / 10);
  console.log(rn);
};

pseudoRandom();
