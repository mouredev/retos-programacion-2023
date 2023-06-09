/* El día 128 del año celebramos en la comunidad el "Hola Mundo day"
 * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
 *
 * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
 * del día 8. Mostrando hora e información de cada uno.
 * Ejemplo: "16:00 | Bienvenida"
 *
 * Se permite utilizar librerías que nos faciliten esta tarea. */

const axios = require('axios');
const cheerio = require('cheerio');
const URL = 'https://holamundo.day';

const events = [];
let lastTimer = null;

// Extract event and timer from span
const extractSpan = (html, span) => {
  const text = html(span).text().trim();
  const isTimer = /\b([01]?\d|2[0-3]):([0-5]\d)\b/g;
  if (text === 'todos los niveles' || text === '|' || text === '') return;

  if (lastTimer) {
    events.push({ timer: lastTimer, event: text });
    lastTimer = null;
  }
  if (isTimer.test(text)) {
    lastTimer = text === '6:00' ? '16:00' : text;
  }
};

// Extract spans from blog quote
const extractSpans = (html) => (index, element) => {
  const spans = html(element)
    .children('span')
    .find('.StyledLeaf___StyledSpan-sc-129cvv1-0');
  spans.each((index, span) => extractSpan(html, span));
};

// Get events from webpage
const getEvents = async () => {
  const { data } = await axios(URL);
  const html = cheerio.load(data);
  html('.BlockquoteElement___StyledBlockquote-sc-1dtx4ci-0').each(
    extractSpans(html)
  );
  return events;
};

// Print event schedule
const printSchedule = (schedule, index) => {
    if (index <= 6) return
    const { event, timer } = schedule;
    const separator = '-'.repeat(event.length + timer.length + 3);
    console.log(`${separator}\n${timer} | ${event}`);
};

// Print all event schedules
const printAllSchedules = async () => {
  const schedules = await getEvents();
  schedules.forEach(printSchedule);
};

// Print all event schedules
printAllSchedules();



