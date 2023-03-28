const friday13 = (year, month) => {
    return new Date(year, month - 1, 13).getDay() === 5;
}

console.log(friday13(2023, 3));
console.log(friday13(2023, 1));
console.log(friday13(2023, 13));
console.log(friday13(-2023, 1));
console.log(friday13(2023, "1"));
console.log(friday13(2023, 0));
console.log(friday13("Brais", "Moure"));