console.log("Hola, mundo!");

let str = "María";
let int = 30;
let flt = 11.20;

const BIRTHDAY = "1992/11/20";

if (int > 25) {
  console.log("Bigger than 25");
} else if (int === 30) {
  console.log("Equal to 30");
} else {
  console.log("No matches");
};

let arr = [1, 2, 3, 4, 5];

for (num in arr) {
  console.log(arr[num] * 2);
}

const sayHi = () => {
  return "Hiiiii!";
}

console.log(sayHi());

const sayBye = () => {
  console.log("Bye...");
}

sayBye();


class Person {
  constructor(name, age, city) {
    this.name = name;
    this.age = age;
    this.city = city
  }
}

let me = new Person("Maria", 30, "Nara")
console.log(me);
