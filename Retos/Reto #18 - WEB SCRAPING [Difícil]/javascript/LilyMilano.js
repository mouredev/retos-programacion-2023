/*
 * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
 * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
 *
 * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
 * del día 8. Mostrando hora e información de cada uno.
 * Ejemplo: "16:00 | Bienvenida"
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
 *
 */

const PORT = 8000;
const axios = require('axios');
const cheerio = require('cheerio');
const express = require('express');

const app = express();
const url = 'https://holamundo.day';

axios(url)
	.then((response) => {
		const html = response.data;
		const $ = cheerio.load(html);
		const activities = [];
		$('blockquote', html).each(function () {
			const activity = $(this).text();
			activities.push(activity);
		});
		const schedule = activities.slice(21, activities.length);
		console.log(schedule);
	})
	.catch((err) => console.log(err));

app.listen(PORT, () => console.log(`server running on PORT ${PORT}`));

// console.log(schedule):

//     server running on PORT 8000
// [
//     '16:00 | Bienvenida',
//     '16:30 | De Junior a Junior: cómo abrirte paso | Antonio Rodríguez',
//     '17:00 | El Rol del Analista Funcional en el Ciclo de Desarrollo | Luisina de Paula',
//     '17:30 | Taller: Git y GitHub para el mundo | Ehud Aguirre',
//     '18:00 | Mesa redonda: ¿Cómo sacarle más partido a la comunidad?',
//     '18:30 | Descanso + Sorteos',
//     '19:00 | Clean Code: cómo dormir más y mejor | Fran Sierra',
//     '19:30 | Abrazando al fracaso | Afor Digital',
//     '20:00 | Taller: Descubre el mundo del machine learning | Stefy Mojica',
//     '20:30 | Elevator pitch',
//     '21:00 | Invitados',
//     '21:30 | Mi primer año como Desarrollador a los 45 años | Gerardo Arrieta',
//     '22:00 | Taller: Testing, más que código | Manu Rodríguez',
//     '22:30 | Descanso + Sorteos',
//     '23:00 | Despedida'
//   ]
