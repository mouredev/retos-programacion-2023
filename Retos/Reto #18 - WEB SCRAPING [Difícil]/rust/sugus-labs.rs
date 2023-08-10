use scraper::Html;

fn download_events_from(url: String) {

    let mut second_day_idx: i32 = 0;

    let response: String = reqwest::blocking::get(url)
        .unwrap().text().unwrap();    

    let document: Html = Html::parse_document(&response);
    let section: scraper::Selector = scraper::Selector::parse("#section-37c93060-be70-11ed-a6a0-03f7635e8df3").unwrap();
    let all_sections: scraper::html::Select<'_, '_> = document.select(&section);
    let all_blockquotes: scraper::Selector = scraper::Selector::parse("div>article>blockquote").unwrap();
    for s in all_sections {
        let blockquotes: scraper::element_ref::Select<'_, '_> = s.select(&all_blockquotes);
        for (num, blockquote) in blockquotes.enumerate() {
            let mut element: String = blockquote.text().collect::<Vec<_>>().join(" ");
            element = element.trim().replace("\n", " ");
            if element.contains("Bienve") {
                second_day_idx = second_day_idx + 1;
            }
            if second_day_idx == 2 {
                if element == String::from("1 6:00   |  Bienvenida") {
                    element = String::from("16:30  |  Bienvenida")
                }
                println!("{}", element);
            }
        }
    }
}

fn main() {

    let url:String = String::from("https://holamundo.day/");
    download_events_from(url);

}