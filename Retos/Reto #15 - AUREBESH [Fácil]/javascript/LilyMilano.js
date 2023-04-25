/*
 * Crea una función que sea capaz de transformar Español al lenguaje básico del universo
 * Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
 */

const aurebeshTranslator = {
	a: 'aurek',
	b: 'besh',
	c: 'cresh',
	d: 'dorn',
	e: 'esseles',
	f: 'forn',
	g: 'grek',
	h: 'herf',
	i: 'isk',
	j: 'jenth',
	k: 'krill',
	l: 'leth',
	m: 'mern',
	n: 'nern',
	ñ: 'nerf',
	o: 'osk',
	p: 'pei',
	q: 'qek',
	r: 'resh',
	s: 'senth',
	t: 'trill',
	u: 'ujeb',
	v: 'vev',
	w: 'wirch',
	x: 'xesh',
	y: 'yirt',
	z: 'zerek',
	ch: 'cherek',
	ae: 'enth',
	eo: 'onith',
	kh: 'krenth',
	ng: 'nen',
	oo: 'orenth',
	sh: 'shen',
	th: 'thesh',
};

const fromSpanishToAurebesh = (sentence) => {
	let aurebeshTranslation = '';
	sentence
		.toLowerCase()
		.split('')
		.map((char) => {
			const translatedChar = aurebeshTranslator[char] || char;
			aurebeshTranslation = `${aurebeshTranslation}${translatedChar}`;
		});
	return aurebeshTranslation;
};

const fromAurebeshToSpanish = (sentence) => {
	let spanishTranslation = '';
	let phrase = sentence[0].toLowerCase();
	let sentenceLower = sentence.toLowerCase();

	for (let i = 1; i < sentenceLower.length; i++) {
		const char = sentenceLower[i];
		Object.prototype.hasOwnProperty.call(aurebeshTranslator, char)
			? (phrase += char)
			: ((spanishTranslation += char), (phrase = ''));

		const value = Object.entries(aurebeshTranslator).find(
			([k, v]) => v === phrase
		);

		if (value !== undefined) {
			spanishTranslation += `${value[0]}`;
			phrase = '';
		}
	}

	return spanishTranslation;
};

//Testing:

console.log(fromSpanishToAurebesh('yo soy tu padre'));
// Log: yirtosk senthoskyirt trillujeb peiaurekdornreshesseles

console.log(
	fromAurebeshToSpanish(
		'yirtosk senthoskyirt trillujeb peiaurekdornreshesseles'
	)
);
// Log: yo soy tu padre
