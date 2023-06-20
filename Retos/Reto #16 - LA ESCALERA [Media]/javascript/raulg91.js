function stair(number) {

    let columns = Math.abs(number) + 1
    let stairs = Array();

    if (number > 0) {

        for (let i = 0; i < columns; i++) {
            let step = "";
            if (i == 0) {
                step = " ".repeat(columns * 2) + "_";
                stairs.push(step);
            }
            else {
                step = " ".repeat((columns - i) * 2) + "_|";
                stairs.push(step);
            }
        }
    }
    else if(number <0){
        for(let i= 0;i<columns;i++){
            let step = "";
            if(i==0){
                step = "_";

            }
            else{
                step = " ".repeat((i*2)-1) + "|_";
            }
            stairs.push(step);
      
        }
      
    }
    else{ //Number equal to 0
        stairs.push("__");
    }

    //Print results 

    for (let i = 0; i < stairs.length; i++) {
        console.log(stairs[i]);
    }

}

let number_steps = 5;
//let number_steps = -5;
//let number_steps = 0;

stair(number_steps);