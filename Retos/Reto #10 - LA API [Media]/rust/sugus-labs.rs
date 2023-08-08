use hyper;

#[tokio::main]
async fn main() ->  Result<(), Box<dyn std::error::Error>>{
    // Create a new client object
    let client: hyper::Client<hyper::client::HttpConnector> = hyper::Client::new();

    let req: hyper::Request<hyper::Body> = hyper::Request::builder()
        .method(hyper::Method::GET)
        .uri("http://api.open-notify.org/iss-now.json")
        .body(hyper::Body::from(""))?;

    // Pass our request builder object to our client.
    let resp: hyper::Response<hyper::Body> = client.request(req).await?;

    // Get the response body bytes.
    let body_bytes: hyper::body::Bytes = hyper::body::to_bytes(resp.into_body()).await?;

    // Convert the body bytes to utf-8
    let body: String = String::from_utf8(body_bytes.to_vec()).unwrap();

    println!("{}", body);

    Ok(())

}