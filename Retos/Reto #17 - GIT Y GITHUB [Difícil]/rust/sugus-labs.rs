use std::process::Command;
//use std::io::{self, Write};
use std::str;

fn retrieve_last_commits() -> Vec<String> {

    let mut log: String = String::new();
    let output = Command::new("git").arg("log")
        .arg("-10").arg("--pretty=format:\"%h | %an | %s | %ad\"")
        .output().expect("failed to execute process");

    //    git log --pretty=format:"%h - %an, %ar : %s"
    //let commits = output.stdout;
    //println!("{:?}", output)
    //println!("{:?}", commits)
    //println!("status: {}", output.status);
    log.push_str(match str::from_utf8(&output.stdout) {
        Ok(val) => val,
        Err(_) => panic!("got non UTF-8 data from git"),
    });
    //io::stdout().write_all(&output.stdout).unwrap();
    let log_split = log.split("\n");
    let log_vec: Vec<&str> = log_split.collect();
    let mut log_vec_str: Vec<String> = vec![];

    for r in log_vec {
        //println!("{}", r);
        log_vec_str.push(String::from(r));
    }

    return log_vec_str;
    
    //assert!(output.status.success());    


}

fn main() {

    let log_vec = retrieve_last_commits();
    for r in log_vec {
        println!("{}", r);
    }

}