// let number = 0;

// while (number < 100) {
//   number++;
//   if (number % 3 === 0 && number % 5 === 0) {
//       console.log("fizzbuzz");
//     }   else if (number % 3 === 0) {
//     console.log("fizz");
//   } else if (number % 5 === 0) {
//     console.log("buzz");
//   } else {
//     console.log(number);
//   }
// }

const fizz = "fizz";
const buzz = "buzz";

for (let i = 1; i <= 100; i++) {
  if (i % 3 === 0 && i % 5 === 0) {
    console.log(fizz + buzz);
  } else if (i % 3 === 0) {
    console.log(fizz);
  } else if (i % 5 === 0) {
    console.log(buzz);
  } else {
    console.log(i);
  }
}
