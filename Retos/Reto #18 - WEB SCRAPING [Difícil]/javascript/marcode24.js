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

const puppeteer = require('puppeteer');

const SITE = 'https://holamundo.day/';

const getShedule = async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
  });
  const page = await browser.newPage();
  await page.goto(SITE);
  const title = await page.title();
  const content = await page.$$('article.notion-page-content-inner');
  const events = content[7]; // 7 is the index of the events section

  const quoteElements = await events.$$('blockquote.notion-quote');
  const eventInfo = await Promise.all(quoteElements.map(async (quoteElement) => {
    const spanElement = await quoteElement.$('span[data-slate-string="true"]');
    const text = await quoteElement.evaluate((el) => el.textContent, spanElement);
    return text;
  }));
  const schedule = `${title}\n\n`.concat(eventInfo
    .map((event) => event.replace(/\n/g, ' '))
    .join('\n'));
  if (browser) await browser.close();
  return schedule;
};

getShedule().then((schedule) => console.log(schedule));

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges

