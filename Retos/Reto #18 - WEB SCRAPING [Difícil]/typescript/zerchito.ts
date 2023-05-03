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
import { JSDOM } from 'jsdom';

const WEB_URL = "https://holamundo.day"

async function scrapWeb (url: string): Promise<void> {
  await axios.get(url)
  .then(response => {
    const html = response.data;
    const document: Document  = new JSDOM(html).window.document
    const elements: Element[] = [...document.getElementsByClassName('notion-page-content-inner')];
    // Event element is the 7th
    const eventsBlock: Element = elements[7];
    // Agenda for the 8th is the 7th
    const events: Element[] = [...eventsBlock.getElementsByClassName('notion-quote')].slice(7);
    console.log('Agenda 8 de mayo');
    events.forEach(listItem => {
      const data: Element[] = [...listItem.getElementsByClassName('slate-bold')];
      let counter = 0;
      let eventText = '';
      data.forEach(el => {
        const spans = [...el.getElementsByTagName('span')];
        // only one span exists
        eventText += spans[0].innerHTML;
        counter++;
        // every 4 items is a row
        if (counter === 4){
          counter = 0;
          console.log(eventText);
          eventText = '';
        }
      })  
      console.log(eventText);
    });
  })
  .catch(error => console.log(error));
}

scrapWeb(WEB_URL);