
// creamos la funcion principal
fn main(){
    for number in 1..101 {  // creamos un ciclo for que va de 1 al 100
        fizzbuzz(number)   // llamamos la funcion para que se ejecute con cada numero
    }
}

fn fizzbuzz(number: i32){

    match (number % 3 == 0, number % 5 == 0 ){ // usamos match y creamos la estructura comparativa
        (true,true) => println!("fizzbuzz"),
        (false,true) => println!("buzz"),
        (true,false) => println!("fizz"),
        _ => println!("{}",number),
    }
}