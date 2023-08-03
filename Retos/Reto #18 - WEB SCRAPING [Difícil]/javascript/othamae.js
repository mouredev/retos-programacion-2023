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

import { chromium } from 'playwright';

async function getResults(PAGE) {
    const browser = await chromium.launch({ headless: true })
    const page = await browser.newPage()
    await page.goto(PAGE)

    const agenda = await page.$$('article.notion-page-content-inner')

    const agendaItems = await agenda[7].$$('blockquote.notion-quote')

    const listEvents = await Promise.all(agendaItems.map(async (element) => {
        const span = await element.$('span[data-slate-string="true"]')
        const content = await element.evaluate((el) => el.textContent, span)
        return content
    }))

    listEvents.splice(0, 7)

    await browser.close()
    return listEvents

}

const PAGE = 'https://holamundo.day/'

getResults(PAGE).then(res => console.log(res))
