fn generate_game_steps(player_list: Vec<&str>, game_step_list: &[&str; 4]) {
    
    // text to Tennis game function
    
    let mut player_1_pos: usize = 0;
    let mut player_2_pos: usize = 0;
    let mut player_1_str: String = String::from("");
    let mut player_2_str: String = String::from("");
    let mut game_str: String = String::from("");
    let mut first_deuce: bool = false;
    
    println!("{player_1_pos} - {player_2_pos} - {first_deuce}");
    println!("{player_list:?}");
    println!("{game_step_list:?}");
    
    for player in player_list {
        //println!("{player}");

        if player == "P1" {
            if first_deuce == true {
                player_1_pos = player_1_pos + 1;
                player_1_str = String::from("Advantage P1");
                player_2_str = String::from("");
            } else {
                player_1_pos = player_1_pos + 1;
                player_1_str = String::from(game_step_list[player_1_pos]);
                player_2_str = String::from(game_step_list[player_2_pos]);
            }
        } else if player == "P2" {
            if first_deuce == true {
                player_2_pos = player_2_pos + 1;
                player_1_str = String::from("");
                player_2_str = String::from("Advantage P2");
            } else {            
                player_2_pos = player_2_pos + 1;
                player_1_str = String::from(game_step_list[player_1_pos]);
                player_2_str = String::from(game_step_list[player_2_pos]);
            }
        }

        if player_1_pos < 4 && player_2_pos < 4 {
            if player_1_str != "" && player_2_str != "" {
                game_str = format!("{} - {}", player_1_str, player_2_str);
            } else {
                game_str = format!("{}{}", player_1_str, player_2_str);
            }
            if player_1_pos == 3 && player_2_pos == 3 {
                game_str = String::from("Deuce");
                first_deuce = true;
                player_1_pos = player_1_pos - 1;
                player_2_pos = player_2_pos - 1;
            }
        } else {
            if player_1_pos == 4 {
                game_str = String::from("P1 wins!");
            } else if player_2_pos == 4 {
                game_str = String::from("P2 wins!");    
            } 
        }     
    println!("{game_str}")
        //println!("{player_1_pos} - {player_1_str} - {player_2_pos} - {player_2_str} - {first_deuce}");
    }    
}

fn main() {

    let player_list = vec!["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P1", "P2", "P2", "P2"];
    const GAME_STEP_LIST: [&str; 4] = ["Love", "15", "30", "40"];

    generate_game_steps(player_list, &GAME_STEP_LIST);

}
    