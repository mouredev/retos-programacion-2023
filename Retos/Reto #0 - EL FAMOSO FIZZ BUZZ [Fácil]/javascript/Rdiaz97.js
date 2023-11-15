        let i=1;
    while(i<=100){

        if(i%3==0 && i%5==0){
            let z ="fizzbuzz";
            console.log(z);
        }else if(i%3==0){
            let n="fizz";
            console.log(n);
        }else if(i%5==0){
            let m="buzz";
            console.log(m);
        }else{
            console.log(i);
        }
        i++;
    }
