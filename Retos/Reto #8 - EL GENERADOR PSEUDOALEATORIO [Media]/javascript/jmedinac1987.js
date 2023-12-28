function random() {
  let number = [];

  for (let i = 0; i <= 100; i++) {
    number.push(i);
  }
  
  let millisecondsToIndex = new Date();
  millisecondsToIndex = millisecondsToIndex.getMilliseconds();

  if (millisecondsToIndex > 100) {
    let auxiliary = 0;
  
    millisecondsToIndex = millisecondsToIndex.toString().split("");
  
    millisecondsToIndex.forEach((element, index) => {
      if (index < 2) {
        auxiliary += parseInt(element);
      }
    });

    millisecondsToIndex = auxiliary;
  }

  return number[millisecondsToIndex];
}
console.log("This is a random value:", random());