/*
Run in:
https://jsfiddle.net/jandro5/zcvLfqbk/16/
*/

const dayOfWeek = 5 // Friday { 0: Sunday, ..., 6: Saturday}
const dayMissing = 13 // day of the week that is missing

function isFridayThirteen(year, month) {
	let date = new Date(year, month - 1, dayMissing)
  
  return date.getDay() === dayOfWeek
}

// Examples
console.log(isFridayThirteen(2023, 1)); // true
console.log(isFridayThirteen(2023, 2)); // false
console.log(isFridayThirteen(2023, 3)); // false
console.log(isFridayThirteen(2023, 10)); // true