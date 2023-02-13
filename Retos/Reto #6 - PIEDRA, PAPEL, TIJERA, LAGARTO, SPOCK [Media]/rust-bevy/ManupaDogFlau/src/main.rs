use bevy::prelude::*;
use rand::Rng;
use std::{thread, time};
const NORMAL_BUTTON: Color = Color::rgb(0.15, 0.15, 0.15);
const HOVERED_BUTTON: Color = Color::rgb(0.25, 0.25, 0.25);
const PRESSED_BUTTON: Color = Color::rgb(0.35, 0.75, 0.35);
// Define un tipo de dato para los posibles jugadores
#[derive(PartialEq, Default)]
enum Player {
    #[default]
    User,
    Robot,
    Answer,
    Reset,
}

#[derive(PartialEq, Default, Debug)]
enum Decision {
    #[default]
    Nothing,
    Rock,
    Paper,
    Scissors,
    Lizard,
    Spock,
}

#[derive(Default, Component, Resource)]
struct GameState {
    current_player: Player,
    user_select: Decision,
    computer_select: Decision,
    textresult: String,
}

#[derive(Component)]
struct ResultText;
#[derive(Component)]
struct ComputerText;
#[derive(Component)]
struct UserText;

fn main() {
    App::new()
        .insert_resource(GameState::default())
        .add_plugins(DefaultPlugins)
        .add_startup_system(setup_game_state)
        .add_startup_system(setup_window)
        .add_system(button_system)
        .add_system(text_system_user)
        .add_system(computer_input)
        .add_system(text_system_computer)
        .add_system(select_winner)
        .add_system(text_system_result)
        .add_system(reset)
        .run();
}

fn reset(mut game_state: ResMut<GameState>) {
    if game_state.current_player == Player::Reset {
        game_state.user_select = Decision::Nothing;
        game_state.computer_select = Decision::Nothing;
        game_state.current_player = Player::User;
    }
}

fn setup_game_state(mut commands: Commands) {
    commands.spawn(GameState {
        current_player: Player::User,
        user_select: Decision::Nothing,
        computer_select: Decision::Nothing,
        textresult: String::from(""),
    });
}

fn computer_input(mut game_state: ResMut<GameState>) {
    if game_state.current_player == Player::Robot {
        let al = rand::thread_rng().gen_range(1..6);
        match al {
            1 => game_state.computer_select = Decision::Rock,
            2 => game_state.computer_select = Decision::Paper,
            3 => game_state.computer_select = Decision::Scissors,
            4 => game_state.computer_select = Decision::Lizard,
            5 => game_state.computer_select = Decision::Spock,
            _ => println!("Error"),
        }
        game_state.current_player = Player::Answer;
    }
}

fn select_winner(mut game_state: ResMut<GameState>) {
    /*1 = rock
    2 = paper
    3 = scissors
    4 = lizard
    5 = spock*/
    if game_state.current_player == Player::Answer {
        if game_state.user_select == game_state.computer_select {
            println!("Tie!");
            game_state.textresult = String::from("Tie!");
        } else if game_state.user_select == Decision::Rock
            && game_state.computer_select == Decision::Scissors
        {
            println!("Rock crushes scissors!");
            println!("You win!");
            game_state.textresult = String::from("Rock crushes scissors!\nYou win!");
        } else if game_state.user_select == Decision::Rock
            && game_state.computer_select == Decision::Lizard
        {
            println!("Rock crushes lizard!");
            println!("You win!");
            game_state.textresult = String::from("Rock crushes lizard!\nYou win!");
        } else if game_state.user_select == Decision::Paper
            && game_state.computer_select == Decision::Rock
        {
            println!("Paper covers rock!");
            println!("You win!");
            game_state.textresult = String::from("Paper covers rock!\nYou win!");
        } else if game_state.user_select == Decision::Paper
            && game_state.computer_select == Decision::Spock
        {
            println!("Paper disproves Spock!");
            println!("You win!");
            game_state.textresult = String::from("Paper disproves Spock!\nYou win!");
        } else if game_state.user_select == Decision::Scissors
            && game_state.computer_select == Decision::Paper
        {
            println!("Scissors cuts paper!");
            println!("You win!");
            game_state.textresult = String::from("Scissors cuts paper!\nYou win!");
        } else if game_state.user_select == Decision::Scissors
            && game_state.computer_select == Decision::Lizard
        {
            println!("Scissors decapitates lizard!");
            println!("You win!");
            game_state.textresult = String::from("Scissors decapitates lizard!\nYou win!");
        } else if game_state.user_select == Decision::Lizard
            && game_state.computer_select == Decision::Paper
        {
            println!("Lizard eats paper!");
            println!("You win!");
            game_state.textresult = String::from("Lizard eats paper!\nYou win!");
        } else if game_state.user_select == Decision::Lizard
            && game_state.computer_select == Decision::Spock
        {
            println!("Lizard poisons Spock!");
            println!("You win!");
            game_state.textresult = String::from("Lizard poisons Spock!\nYou win!");
        } else if game_state.user_select == Decision::Spock
            && game_state.computer_select == Decision::Rock
        {
            println!("Spock vaporizes rock!");
            println!("You win!");
            game_state.textresult = String::from("Spock vaporizes rock!\nYou win!");
        } else if game_state.user_select == Decision::Spock
            && game_state.computer_select == Decision::Scissors
        {
            println!("Spock smashes scissors!");
            println!("You win!");
            game_state.textresult = String::from("Spock smashes scissors!\nYou win!");
        } else {
            println!("You lose!");
            game_state.textresult = String::from("You lose!");
        }
        game_state.current_player = Player::Reset;
    }
}

fn setup_window(mut commands: Commands, asset_server: Res<AssetServer>) {
    // UI camera
    commands.spawn(Camera2dBundle::default());
    // Text with multiple sections
    commands.spawn((
        // Create a TextBundle that has a Text with a list of sections.
        TextBundle::from_sections([
            TextSection::new(
                "You selected: ",
                TextStyle {
                    font: asset_server.load("fonts/FiraSans-Bold.ttf"),
                    font_size: 60.0,
                    color: Color::WHITE,
                },
            ),
            TextSection::new("Nothing",TextStyle {
                font: asset_server.load("fonts/FiraMono-Medium.ttf"),
                font_size: 60.0,
                color: Color::GOLD,
            }),
        ])
        .with_text_alignment(TextAlignment::TOP_CENTER)
        // Set the style of the TextBundle itself.
        .with_style(Style {
            position_type: PositionType::Absolute,
            position: UiRect {
                //centered_horizontally: true,
                left: Val::Percent(10.0),
                ..Default::default()
            },

            ..default()
        }),
        UserText,
    ));
    commands.spawn((
        // Create a TextBundle that has a Text with a list of sections.
        TextBundle::from_sections([
            TextSection::new(
                "Computer selected: ",
                TextStyle {
                    font: asset_server.load("fonts/FiraSans-Bold.ttf"),
                    font_size: 60.0,
                    color: Color::WHITE,
                },
            ),
            TextSection::new("Nothing",TextStyle {
                font: asset_server.load("fonts/FiraMono-Medium.ttf"),
                font_size: 60.0,
                color: Color::GOLD,
            }),
        ])
        .with_text_alignment(TextAlignment::TOP_CENTER)
        // Set the style of the TextBundle itself.
        .with_style(Style {
            position_type: PositionType::Absolute,
            position: UiRect {
                //centered_horizontally: true,
                left: Val::Percent(50.0),
                ..Default::default()
            },

            ..default()
        }),
        ComputerText,
    ));
    commands.spawn((
        // Create a TextBundle that has a Text with a list of sections.
        TextBundle::from_sections([
            TextSection::new(
                "                                                   Result:                                                   \n",
                TextStyle {
                    font: asset_server.load("fonts/FiraSans-Bold.ttf"),
                    font_size: 60.0,
                    color: Color::WHITE,
                },
            ),
            TextSection::from_style(TextStyle {
                font: asset_server.load("fonts/FiraMono-Medium.ttf"),
                font_size: 60.0,
                color: Color::GOLD,
            }),
        ])
        .with_text_alignment(TextAlignment::TOP_CENTER)
        // Set the style of the TextBundle itself.
        .with_style(Style {
            position_type: PositionType::Absolute,
            size: Size::new(Val::Percent(40.0), Val::Percent(20.0)),
            position: UiRect {
                left: Val::Percent(15.0),
                right: Val::Auto,
                top: Val::Percent(20.0),
                ..default()
            },
            ..default()
        }),
        ResultText,
    ));
    commands
        .spawn(ButtonBundle {
            style: Style {
                size: Size::new(Val::Px(150.0), Val::Px(65.0)),
                // center button
                margin: UiRect::all(Val::Auto),
                // horizontally center child text
                justify_content: JustifyContent::Center,
                // vertically center child text
                align_items: AlignItems::Center,
                ..default()
            },
            background_color: NORMAL_BUTTON.into(),
            ..default()
        })
        .with_children(|parent| {
            parent.spawn(TextBundle::from_section(
                "Rock",
                TextStyle {
                    font: asset_server.load("fonts/FiraSans-Bold.ttf"),
                    font_size: 40.0,
                    color: Color::rgb(0.9, 0.9, 0.9),
                },
            ));
        });
    commands
        .spawn(ButtonBundle {
            style: Style {
                size: Size::new(Val::Px(150.0), Val::Px(65.0)),
                // center button
                margin: UiRect::all(Val::Auto),
                // horizontally center child text
                justify_content: JustifyContent::Center,
                // vertically center child text
                align_items: AlignItems::Center,
                ..default()
            },
            background_color: NORMAL_BUTTON.into(),
            ..default()
        })
        .with_children(|parent| {
            parent.spawn(TextBundle::from_section(
                "Paper",
                TextStyle {
                    font: asset_server.load("fonts/FiraSans-Bold.ttf"),
                    font_size: 40.0,
                    color: Color::rgb(0.9, 0.9, 0.9),
                },
            ));
        });
    commands
        .spawn(ButtonBundle {
            style: Style {
                size: Size::new(Val::Px(150.0), Val::Px(65.0)),
                // center button
                margin: UiRect::all(Val::Auto),
                // horizontally center child text
                justify_content: JustifyContent::Center,
                // vertically center child text
                align_items: AlignItems::Center,
                ..default()
            },
            background_color: NORMAL_BUTTON.into(),
            ..default()
        })
        .with_children(|parent| {
            parent.spawn(TextBundle::from_section(
                "Scissors",
                TextStyle {
                    font: asset_server.load("fonts/FiraSans-Bold.ttf"),
                    font_size: 40.0,
                    color: Color::rgb(0.9, 0.9, 0.9),
                },
            ));
        });
    commands
        .spawn(ButtonBundle {
            style: Style {
                size: Size::new(Val::Px(150.0), Val::Px(65.0)),
                // center button
                margin: UiRect::all(Val::Auto),
                // horizontally center child text
                justify_content: JustifyContent::Center,
                // vertically center child text
                align_items: AlignItems::Center,
                ..default()
            },
            background_color: NORMAL_BUTTON.into(),
            ..default()
        })
        .with_children(|parent| {
            parent.spawn(TextBundle::from_section(
                "Lizard",
                TextStyle {
                    font: asset_server.load("fonts/FiraSans-Bold.ttf"),
                    font_size: 40.0,
                    color: Color::rgb(0.9, 0.9, 0.9),
                },
            ));
        });
    commands
        .spawn(ButtonBundle {
            style: Style {
                size: Size::new(Val::Px(150.0), Val::Px(65.0)),
                // center button
                margin: UiRect::all(Val::Auto),
                // horizontally center child text
                justify_content: JustifyContent::Center,
                // vertically center child text
                align_items: AlignItems::Center,
                ..default()
            },
            background_color: NORMAL_BUTTON.into(),
            ..default()
        })
        .with_children(|parent| {
            parent.spawn(TextBundle::from_section(
                "Spock",
                TextStyle {
                    font: asset_server.load("fonts/FiraSans-Bold.ttf"),
                    font_size: 40.0,
                    color: Color::rgb(0.9, 0.9, 0.9),
                },
            ));
        });
}

fn text_system_user(
    mut queryuser: Query<&mut Text, With<UserText>>,
    game_state: ResMut<GameState>,
) {
    for mut usertext in &mut queryuser {
        if game_state.user_select != Decision::Nothing {
            usertext.sections[1].value = format!("{0:#?}", game_state.user_select);
        }
    }
}

fn text_system_computer(
    mut querycomputer: Query<&mut Text, With<ComputerText>>,
    game_state: ResMut<GameState>,
) {
    for mut computertext in &mut querycomputer {
        if game_state.computer_select != Decision::Nothing {
            computertext.sections[1].value = format!("{0:#?}", game_state.computer_select);
        }
    }
}

fn text_system_result(
    mut queryresult: Query<&mut Text, With<ResultText>>,
    game_state: ResMut<GameState>,
) {
    for mut resulttext in &mut queryresult {
        resulttext.sections[1].value = format!("{0}", game_state.textresult);
    }
}

fn button_system(
    mut interaction_query: Query<
        (&Interaction, &mut BackgroundColor, &Children),
        (Changed<Interaction>, With<Button>),
    >,
    mut text_query: Query<&mut Text>,
    mut game_state: ResMut<GameState>,
) {
    if game_state.current_player == Player::User {
        for (interaction, mut color, children) in &mut interaction_query {
            let text = text_query.get_mut(children[0]).unwrap();
            let mut decision = Decision::Nothing;
            match text.sections[0].value.as_str() {
                "Rock" => decision = Decision::Rock,
                "Paper" => decision = Decision::Paper,
                "Scissors" => decision = Decision::Scissors,
                "Lizard" => decision = Decision::Lizard,
                "Spock" => decision = Decision::Spock,
                _ => println!("Error"),
            }
            match *interaction {
                Interaction::Clicked => {
                    *color = PRESSED_BUTTON.into();
                    game_state.user_select = decision;
                    game_state.current_player = Player::Robot;
                }
                Interaction::Hovered => {
                    *color = HOVERED_BUTTON.into();
                }
                Interaction::None => {
                    *color = NORMAL_BUTTON.into();
                }
            }
        }
    }
}
