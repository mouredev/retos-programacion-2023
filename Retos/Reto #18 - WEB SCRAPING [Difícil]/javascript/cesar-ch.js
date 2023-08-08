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

import puppeteer from "puppeteer";

async function webScraping() {
    const browser = await puppeteer.launch({
        headless: false,
        slowMo: 400 
    });
    const page = await browser.newPage();
    await page.goto("https://holamundo.day");
    const result = await page.evaluate(() => {
        const blockquotes = document.querySelectorAll("blockquote");
        const data = [...blockquotes].slice(21,).map(blockquote => {
            const time = blockquote.innerText
            return time

        })
        return data
    })
    console.log(result.join('\n'))
    await browser.close()
}

webScraping()