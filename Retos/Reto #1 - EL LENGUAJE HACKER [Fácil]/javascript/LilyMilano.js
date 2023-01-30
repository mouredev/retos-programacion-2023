'use strict';

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

// :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

function parseltongue(muggletext) {
	
		const parseltongueTranslator = {
			a:'4',	
			b:'I3',
			c:'[',
			d:')',
			e:'3',
			f:'|=',
			g:'&',
			h:'#',
			i:'1',
			j:',_|',
			k:'>|',
			l:'1',
			m:'/\\/\\',
			n:'^/',
			o:'0',
			p:'|*',
			q:'(_,)',
			r:'I2',
			s:'5',
			t:'7',
			u:'(_)',
			v:'\\/',
			w:'\\/\\/',
			x:'><',
			y:'j',
			z:'2',
			1:'L',
			2:'R',
			3:'E',
			4:'A',
			5:'S',
			6:'b',
			7:'T',
			8:'B',
			9:'g',
			0:'o',	
		};

		let encryptedSpell= '';

		for( let letter of muggletext.toLowerCase() ){
			encryptedSpell += parseltongueTranslator[letter] ?? letter;
		}

		return encryptedSpell;
	}

// :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

	console.log(parseltongue('Dobby has no master, Dobby is a free elf, and Dobby has come to save Harry Potter'));
	// Log: )0I3I3j #45 ^/0 /\/\4573I2, )0I3I3j 15 4 |=I233 31|=, 4^/) )0I3I3j #45 [0/\/\3 70 54\/3 #4I2I2j |*0773I2

	console.log(parseltongue('Do not let the muggles get you down'));
	// Log: )0 ^/07 137 7#3 /\/\(_)&&135 &37 j0(_) )0\/\/^/

	console.log(parseltongue('Las mujeres ya no lloran, ¡las mujeres facturan!'));
	// Log: 145 /\/\(_),_|3I235 j4 ^/0 110I24^/, ¡145 /\/\(_),_|3I235 |=4[7(_)I24^/!

	console.log(parseltongue('¡Hello, World!'));
	// Log: ¡#3110, \/\/0I21)!

	
// :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
