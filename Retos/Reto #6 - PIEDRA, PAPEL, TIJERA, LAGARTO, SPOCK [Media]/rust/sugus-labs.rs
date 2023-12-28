fn scissor_game(game_list: Vec<(String, String)>) {
    
    // Scissor game function
    
    // Codification:
    // ------------
    // ST: "🗿" (piedra) 
    // PA: "📄" (papel)
    // SC: "✂️" (tijera)
    // LI: "🦎" (lagarto)
    // SP: "🖖" (spock)
    
    let mut player_1_points: usize = 0;
    let mut player_2_points: usize = 0;
    
    for game in game_list {

        let mut player_1_option: String = game.0;
        let mut player_2_option: String = game.1;

        if player_1_option == String::from("ST") {
            if player_2_option == String::from("PA") 
                || player_2_option == String::from("SP") {
                player_1_points = player_1_points + 1
            
            } else if player_2_option == String::from("SC") 
                || player_2_option == String::from("LI") {
                player_2_points = player_2_points + 1
        
            }
        }

        if player_2_option == String::from("ST") {
            if player_1_option == String::from("PA") 
                || player_1_option == String::from("SP") {
                player_2_points = player_2_points + 1
            
            } else if player_1_option == String::from("SC") 
                || player_1_option == String::from("LI") {
                player_1_points = player_1_points + 1
        
            }
        }        

        if player_1_option == String::from("PA") {
            if player_2_option == String::from("SP") {
                player_1_points = player_1_points + 1
            
            } else if player_2_option == String::from("SC") 
                || player_2_option == String::from("LI") {
                player_2_points = player_2_points + 1
        
            }
        }

        if player_2_option == String::from("PA") {
            if player_1_option == String::from("SP") {
                player_2_points = player_2_points + 1
            
            } else if player_1_option == String::from("SC") 
                || player_1_option == String::from("LI") {
                player_1_points = player_1_points + 1
        
            }
        }        

        if player_1_option == String::from("SC") {
            if player_2_option == String::from("LI") {
                player_1_points = player_1_points + 1
            
            } else if player_2_option == String::from("SP") {
                player_2_points = player_2_points + 1
        
            }
        }

        if player_2_option == String::from("SC") {
            if player_1_option == String::from("LI") {
                player_2_points = player_2_points + 1
            
            } else if player_1_option == String::from("SP") {
                player_1_points = player_1_points + 1
        
            }
        }        

        if player_1_option == String::from("LI") {
            if player_2_option == String::from("SP") {
                player_1_points = player_1_points + 1
            
            } 
        } 

        if player_2_option == String::from("LI") {
            if player_1_option == String::from("SP") {
                player_2_points = player_2_points + 1
            
            } 
        }         
    }

    if player_1_points == player_2_points{
        println!("TIE!") 
    } else if player_1_points == player_2_points {
        println!("Player 1 wins!") 
    } else {
        println!("Player 2 wins!")
    }

    //println!("{} {}", player_1_points, player_2_points)       
}

fn main() {

    let game_list: Vec<(String, String)> = vec!(
        (String::from("ST"), String::from("SC")), 
        (String::from("SC"), String::from("ST")),
        (String::from("PA"), String::from("SC"))
    );
    scissor_game(game_list);

}