use std::collections::HashMap;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let url = "https://dog.ceo/api/breeds/image/random";

    // Realizar la solicitud GET
    let response = reqwest::get(url)
        .await?
        .json::<HashMap<String, String>>()
        .await?;

    println!("{:#?}", response);
    
    Ok(())
}