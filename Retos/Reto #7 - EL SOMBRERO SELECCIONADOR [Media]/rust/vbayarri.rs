// Se importa la librería de entrada y salida
use std::io::stdin;

// Se crea un enum para las casas de Hogwarts
enum HPHouses {
    Gryffindor,
    Hufflepuff,
    Ravenclaw,
    Slytherin,
}

// Se crea una constante para el número de casas de Hogwarts
const NUM_HOUSES: usize = 4;

// Se crea una constante para el número de preguntas del sombrero seleccionador
const NUM_QUESTIONS: usize = 4;

// Se crea una constante con las preguntas del sombrero seleccionador
static QUESTIONS: [&str; NUM_QUESTIONS] = [
    "¿Cuál es tu color favorito?", 
    "¿Cuál es tu animal favorito?", 
    "¿Cuál es tu profesor favorito?", 
    "¿Cuál es tu materia favorita?",
];

// Se crea una constante con las respuestas del sombrero seleccionador
static ANSWERS: [[&str; NUM_HOUSES]; NUM_QUESTIONS] = [
    ["Rojo" , "Amarillo", "Azul", "Verde",],
    ["León" , "Ciervo", "Aguila", "Serpiente",],
    ["Dumbledore" , "McGonagall", "Sprout", "Snape",],
    ["Defensa contra las artes oscuras" , "Pociones", "Adivinación", "Historia de la magia",],
];

// Funcion principal del programa
fn main() {

    // Se llama a la función welcome y se guarda el nombre del estudiante
    let name = welcome();

    // Se llama a la función sorting_hat y se guarda la casa a la que pertenece el estudiante
    println!("\n[McGonagall] Cuando diga su nombre, se acercarán, les pondré el sombrero seleccionador y sabrán cuál es su casa…!");

    // Se llama a la función sombrero y se guarda la casa a la que pertenece el estudiante
    let house = sombrero();

    // Se imprime la casa a la que pertenece el estudiante
    println!("\n[McGonagall] ¡Bienvenid@ {} a la casa de {}!", name, match house {
        HPHouses::Gryffindor => "Gryffindor",
        HPHouses::Hufflepuff => "Hufflepuff",
        HPHouses::Ravenclaw => "Ravenclaw",
        HPHouses::Slytherin => "Slytherin",
    });
}

// Se crea una función para dar la bienvenida al estudiante de Hogwarts y retornar su nombre
fn welcome () -> String {

    // Se escribe "Welcome to Hogwarts!" en ascii art style
    println!("
    .  .                   ;-.      .   .           
    |  |                   |  )     |   |           
    |--| ,-: ;-. ;-. . .   |-'  ,-. |-  |-  ,-. ;-. 
    |  | | | |   |   | |   |    | | |   |   |-' |   
    '  ' `-` '   '   `-|   '    `-' `-' `-' `-' '   
    ");
 
    // Se pide el nombre del estudiante
    println!("¿Cuál es su nombre?");
    let mut name = String::new();
    stdin().read_line(&mut name).expect("Error al leer el nombre");

    // Se retorna el nombre del estudiante
    name.trim().to_string()
}

// Funcion que muestra el arte del sombrero seleccionador
fn muestra_sorting_hat() {

    // Se escribe "Sorting Hat" en ascii art style
    println!("
                                                                                
                                          %%%%%%&%&/                            
                                         %%&&%%&%%%%%%%%%                       
                                       %%%%%@@@@%&%%&%%%%%%%%                   
                                    #%%%%%%%%%&%@%@%                            
                                   %%%%%&%%&@@@&%                               
                                  %%%%%&%%%%%@&%%%                              
                                 %%%%%%%%%&%@@@&%%                              
                                %%%&@@@@@%@@&@@&&%.                             
                               &%&%%&@@@@@&&@@@%%%%&                            
                               @&%%%%&@@@@@@%%%%%@@                             
                              %%%%%%%%%%%&@@@@@@@@&                             
                             &%%%%%%%&%%%%%%%%%%@&%&                            
                             %%%%%&%&&@@@@@@@@@@@%%%                            
                          %%%%%%&@@@@@@@@@&&@@@@@@@%&&                          
                          %%%@@%%%%&@%%%%%%%%%%%%%%%%%#                         
                          %%%&&%%%%%%%%%%%%%&%%@@@@%%%%%                        
         %%%%%%%%%%%&&  #&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%/    */%%@%%             
        %%%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&@@@@@@@@@@@@@%          
         &%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@&&&@@@@@@&&@,                
              *%%&&%%%%%%%%%%%%%%%%%#                                           
                                           
    ");
}

// Se crea una función para el sombrero seleccionador
// Retorna la casa a la que pertenece
fn sombrero () -> HPHouses {

    // Se crea un vector para guardar las respuestas del estudiante
    let mut answers = Vec::new();

    // Se deja un espacio en el terminal
    muestra_sorting_hat();

    // Se recorren las preguntas del sombrero seleccionador
    for (i, question) in QUESTIONS.iter().enumerate() {

        // Se muestra la pregunta
        println!("\n{}", question);

        // Se muestran las opciones de respuesta
        for (j, house_answer) in ANSWERS[i].iter().enumerate() {
            println!("{}. {}", j + 1, house_answer);
        }

        // Se pide la respuesta del estudiante y debe ser un entero entre 1 y el número de casas
        loop {
            println!("¿Cuál es su respuesta?");
            let mut answer = String::new();
            stdin().read_line(&mut answer).expect("Error al leer la respuesta");
            let answer = answer.trim();
            let answer = answer.parse::<usize>().unwrap_or(1);
            if answer > 0 && answer <= NUM_HOUSES {
                answers.push(answer);
                break;
            }
        }
    }

    // Se recorre el vector de respuestas del estudiante y se suma el valor de cada respuesta a cada casa
    let mut houses = [0; NUM_HOUSES];
    for answer in answers.iter() {
        // Se obtiene la respuesta del estudiante
        let answer = answer - 1;
        // Se suma el valor de la respuesta al vector de casas
        houses[answer] += 1;
    }

    // Se busca la casa con el valor más alto. En caso de empate, se envía a Gryffindor
    let mut max = 0;
    let mut house = HPHouses::Gryffindor;
    for (i, value) in houses.iter().enumerate() {
        if *value > max {
            max = *value;
            house = match i {
                0 => HPHouses::Gryffindor,
                1 => HPHouses::Hufflepuff,
                2 => HPHouses::Ravenclaw,
                3 => HPHouses::Slytherin,
                _ => HPHouses::Gryffindor,
            };
        }
    }
    
    return house;
}