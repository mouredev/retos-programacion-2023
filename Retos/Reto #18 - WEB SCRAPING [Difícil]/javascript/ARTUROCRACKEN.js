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

/* ----- SOLO FUNCIONA EN EL WEB BROWSER ----- */

const URL = "https://holamundo.day";

async function webScrapper(URL) {
  try {
    const response = await fetch(URL);
    const html = await response.text();

    const parser = new DOMParser();
    const doc = parser.parseFromString(html, "text/html");

    const agendaItems = doc.querySelectorAll(".rt-Text.rt-r-size-4");

    // Extract Info
    let agenda = Array.from(agendaItems).map((item) => {
      const time = item.querySelector("strong")?.textContent.trim(); // Get Time
      const info = item.textContent.replace(time, "").trim(); // Get Info
      return { time, info };
    });

    // Filter only the agenda elements.
    agenda = agenda.splice(25, 16);

    agenda.map((agendaItem) => {
      console.log(`${agendaItem.time} | ${agendaItem.info}`);
    });
  } catch (error) {
    console.error("Error al obtener los datos.", error);
  }
}

webScrapper(URL);
