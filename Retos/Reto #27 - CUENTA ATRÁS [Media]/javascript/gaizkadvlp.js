// Desde el movil usando vim
// Hay que ejecutar el fichero y pasarle dos argumentos,
// el primero, desde donde iniciamos la cuenta atrás;
// el segundo, el intervalo. Por ejemplo:
// node gaizkadvlp.js 5 3
// Por defecto coge 3 y 1

const inicio = isNaN(+process.argv[2]) ? 3 : +process.argv[2]
const pausa = isNaN(+process.argv[3]) ? 1 : +process.argv[3]
const error = "\n\tError: sólo se admiten enteros positivos !=0 \n\t******";

function cuentaAtras(desde, intervalo){
	if (!Number.isInteger(desde) || !Number.isInteger(intervalo)) return console.log(error);
	if (desde < 1 || intervalo < 1) return console.log(error);

	console.log(desde)
	const delay = parseInt(intervalo)*1000;
	const temp = setInterval(() => {
			desde--
			console.log(desde)
			if (desde <= 0) clearInterval(temp)
		}, delay)
}

cuentaAtras(inicio, pausa);

