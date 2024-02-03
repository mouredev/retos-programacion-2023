const cifradoCesar = (s, action) => {
	const regEx = /^[a-zA-Z]+$/;
	const actionChosen = action.toLowerCase();
	
	if (regEx.test(s)) return "Ingrese solo caracteres alfabéticos";
	if (actionChosen !== "descifrar" && actionChosen !== "cifrar")
		return "Solo es posible descifrar o cifrar, realiza una acción correcta";
    
    return transformText(s, action)
};

const transformText = (s, action) => {
    const letters = Array.from({ length: 26 }, (_, index) =>
		String.fromCharCode(97 + index)
	);
	let result = "";

	for (let i = 0; i < s.length; i++) {
		let letterIndex = letters.indexOf(s[i]);
		let offset = action === "cifrar" ? 3 : -3;
		let letterToReplace = letters[(letterIndex + offset + 26) % 26];

		if (s[i] === " ") {
			result += " ";
			continue;
		}

		result += letterToReplace;
	}
	return result;
};

console.log(cifradoCesar("Hola Mundo js", "cifrar")); // krod pxqgr mv
console.log(cifradoCesar("krod pxqgr mv", "descifrar")); // hola mundo js
