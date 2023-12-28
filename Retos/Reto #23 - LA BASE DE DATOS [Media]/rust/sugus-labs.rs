use mysql::*;
use mysql::prelude::*;
use chrono::NaiveDate;

fn query_database() {
    
    let host: &str = "mysql-5707.dinaserver.com";
    let port: &str = "3306";
    let user: &str = "mouredev_read";
    let passw: &str = "mouredev_pass";
    let database: &str = "moure_test";

    let mut url: String = String::from("mysql://");
    url.push_str(user);
    url.push_str(":");
    url.push_str(passw);
    url.push_str("@");
    url.push_str(host);
    url.push_str(":");
    url.push_str(port);
    url.push_str("/");
    url.push_str(database);

    //println!("{}", url);
    
    let pool = Pool::new(url).unwrap();
    let mut conn = pool.get_conn().unwrap();
        
    conn.query_iter("select id, name, difficulty, date from challenges")
      .unwrap()
      .for_each(|row| {
        let r:(i32, String, String, NaiveDate) = from_row(row.unwrap());
        println!("{}, {}, {}, {:?}", r.0, r.1, r.2, r.3);
      });

}

fn main() {

    query_database();

}