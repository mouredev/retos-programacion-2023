const startCountDown = (start, shift) => {
  if (start < 1 || shift < 1) {
    console.log("Invalid input");
    return 0;
  }

  let currentTime = Math.floor(Date.now() / 1000);
  let control = currentTime;

  while (start >= 0) {
    control = Math.floor(Date.now() / 1000);
    if (control == currentTime) {
      console.log(start);
      currentTime += shift;
      start -= 1;
    }
  }
};

startCountDown(5, 3);
startCountDown(5, -1);
startCountDown(-4, 3);
startCountDown(0, 3);
startCountDown(3, 10);
