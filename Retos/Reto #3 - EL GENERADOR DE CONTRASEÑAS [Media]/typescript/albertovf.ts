const reto = (longitud: number, mayusculas: boolean = true, numeros: boolean = true, simbolos: boolean = true) => {

	let lowercase = "abcdefghijklmnopqrstuvwxyz";
	let uppercase = lowercase.toUpperCase();
	let numbers = "0123456789", simbol = "!#$%&/()=?¡¿";
	let password = "", characters = lowercase;


	if (longitud < 8 || longitud > 16) {
		console.log("La longitud debe ser entre 8 y 16");
		return null
	}

	if (mayusculas) characters += uppercase;
	if (numeros) characters += numbers;
	if (numeros) characters += simbol;

	while (password.length != longitud) {
		password += characters.charAt(Math.floor(Math.random() * characters.length));
	}

	console.log(password);

	return password;

}

reto(16, true, false, false)