const puppeteer = require('puppeteer');
const jsdom = require('jsdom');

async function do_scraping() {
    let found = false;
    let finish = false
    let result = "";
    try {
        const browser = await puppeteer.launch();
        const page = await browser.newPage();
        const response = await page.goto('https://www.holamundo.day');
        const body = await response.text();

        // Paser JSDOM
        const { window: { document } } = new jsdom.JSDOM(body);

        // Seleccionamos los títulos y lo mostramos en consola

        document.querySelectorAll('h1, blockquote')
            .forEach(element => {
                // Let's find first the H1 that contains the agenda
                if (element.textContent == '>_ Agenda 8 de mayo | “Hola Mundo” day') {
                    found = true;

                }
                // Agenda is delimited once following text is found
                else if (element.textContent == '>_ Hola, soy Brais Moure') {
                    finish = true;

                }
                //if start point for agenda is reached and not the end of agenda, concatenate text
                else if (found && !(finish)) {
                    result = result + element.textContent + "\n";

                }


            });
        // Close puppeteer
        await browser.close();
        return result;

    } catch (error) {
        console.error(error);
    }

}


do_scraping().then(value => {
    console.log(value);
})