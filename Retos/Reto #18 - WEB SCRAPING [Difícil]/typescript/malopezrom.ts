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


import axios from 'axios';
import cheerio from 'cheerio';


/**
 * Función para imprimir la agenda del día 8 de mayo
 * Utilizando la librería axios para hacer la petición y cheerio para parsear el HTML
 */
async function printDay8(): Promise<void> {
    const url = 'https://holamundo.day';
    const response = await axios.get(url);
    const $ = cheerio.load(response.data);
    const results = $('h1');

    results.each((index, element) => {
        const result = $(element);
        if (result.text().includes('Agenda 8 de mayo')) {
            console.log(result.text());
            let sibling = result.nextAll();
            sibling.each((index, agenda) => {
                const agendaElement = $(agenda);
                if (agendaElement.is('blockquote')) {
                    console.log(agendaElement.text());
                }
            });
        }
    });
}

printDay8();