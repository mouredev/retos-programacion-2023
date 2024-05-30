const monthsArr = [
	'enero',
	'febrero',
	'marzo',
	'abril',
	'mayo',
	'junio',
	'julio',
	'agosto',
	'septiembre',
	'octubre',
	'noviembre',
	'diciembre',
];

function checkFriday13(year, month) {
	let date = new Date(year, month - 1, 13);
	let formatedDate = `${date.getDate()} de ${
		monthsArr[date.getMonth()]
	} del ${date.getFullYear()}`;

	if (date.getDay() === 5) {
		console.log(`\nEl ${formatedDate} fue viernes 13`);
	} else {
		console.log(`\nEl ${formatedDate} no fue viernes 13`);
	}
}

checkFriday13(2003, 5);
checkFriday13(2012, 4);
checkFriday13(2004, 9);
checkFriday13(2013, 9);
