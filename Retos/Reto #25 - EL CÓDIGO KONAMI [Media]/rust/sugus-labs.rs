use device_query::{DeviceQuery, DeviceState, Keycode, DeviceEvents};
use std::{thread, time::Duration};

fn main() {
    let mut _continue: bool = true;
    let device_state = DeviceState::new();
    let mut key_str: String = String::new();
    let konami_key_vec: Vec<String> = vec![
        String::from("Up"), String::from("Up"), 
        String::from("Down"), String::from("Down"), 
        String::from("Left"), String::from("Right"), 
        String::from("Left"), String::from("Right"), 
        String::from("B"), String::from("A"), 
        String::from("Enter")];
    let mut key_vec: Vec<String> = vec![];
    while _continue == true {
        let keys: Vec<Keycode> = device_state.get_keys();
        for key in keys.iter() {
            key_str = key.to_string();
            //println!("Pressed key: {:?}", key);
            if key_vec.len() == 11 {
                key_vec.remove(0);
                key_vec.push(key_str);
            } else {
                key_vec.push(key_str);
            }
            if key_vec == konami_key_vec {
                println!("\nYou WIN!\n");
                _continue = false;
                break;
            }
            //println!("{:?}", key_vec);
            thread::sleep(Duration::from_millis(300));
        }
    }
}