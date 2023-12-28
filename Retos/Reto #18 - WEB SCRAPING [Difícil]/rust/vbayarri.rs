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

// Se utilizarán las librerías reqwest y scrapper
//[dependencies]
//reqwest = {version = "0.11", features = ["blocking"]}
//scraper = "0.12.0"

// El programa mustra la siguiente salida
// 16:00 | Bienvenida
// 16:30 | De Junior a Junior: cómo abrirte paso | Antonio Rodríguez
// 17:00 | El Rol del Analista Funcional en el Ciclo de Desarrollo | Luisina de Paula
// 17:30 | Taller: Git y Github para el mundo | Ehud Aguirre
// 18:00 | Mesa redonda: ¿Cómo sacarle más partido a la comunidad?
// 18:30 | Descanso + Sorteos
// 19:00 | Clean Code: cómo dormir más y mejor | Fran Sierra
// 19:30 | Abrazando al fracaso | Afor Digital
// 20:00 | Taller: Descubre el mundo de machine learning | Stefy Mojica
// 20:30 | Elevator pitch
// 21:00 | Invitados
// 21:30 | Mi primer año como Desarrollador a los 45 años | Gerardo Arrieta
// 22:00 | Taller: Testing, más que código | Manu Rodríguez
// 22:30 | Descanso + Sorteos
// 23:00 | Despedida

// Los puntos de mejora del programa son:
// 1. Se filtra por posición la ubicación de la agenda
// 2. Se elimina la agenda del día 4 por número de elementos.

// Se importan las librerías
use reqwest::blocking::get;
use scraper::{Html, Selector};

// Constante con el nombre del site a scrapear
const SITE: &str = "https://holamundo.day";

fn main() {

    // Se obtiene el contenido de la página
    let body = get(SITE).unwrap().text().unwrap();

    // Se parsea el contenido de la página
    let document = Html::parse_document(&body);

    // Se crea un selector para obtener la sección de la página de la agenda
    let mut selector = Selector::parse("article.notion-page-content-inner").unwrap();

    // Se obtienen el principal
    let mut principal = document.select(&selector);

    // La agenda de eventos del día 4 y 8 está en el octavo elemento
    let agenda = principal.nth(7).unwrap();

    // Se obtienen los eventos del día 8
    selector = Selector::parse("blockquote").unwrap();
    let events = agenda.select(&selector);
    
    // Se filtrarán los eventos del día 4 borrando los 7 primeros elementos
    let events = events.skip(7);

    // Se recorren los eventos
    for event in events {

        // Se imprime el evento
        println!("{}", event.text().collect::<String>());

        //println!("Loop");

        /* 
        // Se obtiene el día del evento
        let day = event
            .select(&Selector::parse("div.day").unwrap())
            .next()
            .unwrap()
            .inner_html();

        // Se obtiene la hora del evento
        let hour = event
            .select(&Selector::parse("div.hour").unwrap())
            .next()
            .unwrap()
            .inner_html();

        // Se obtiene el título del evento
        let title = event
            .select(&Selector::parse("div.title").unwrap())
            .next()
            .unwrap()
            .inner_html();

        // Se imprime el evento
        println!("{} | {} | {}", day, hour, title);

        */
    }
}
