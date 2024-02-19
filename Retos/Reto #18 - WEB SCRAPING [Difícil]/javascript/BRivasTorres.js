import puppeteer from "puppeteer";

const webScraping = async() => {
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