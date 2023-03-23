for(let i = 1; i <= 100; i++){
    let output = "";
    //let flag = false;
    if(i%3 == 0){
        output += 'fizz';
        //flag=true;
    }
    if(i%5 == 0){
        output += 'buzz';
        //flag=true;
    }
    if(output === ""){
        console.log(i);
    }else{
        console.log(output);
    }
}