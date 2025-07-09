
function findPrimeTwins(range) {
   
    if (range < 0) {
        return [];
    }


    let primeTwins = [];


    for (let i = 0; i < range; i++) {     
        if (isPrime(i) && isPrime(i+2)){
            primeTwins.push([i,i+2]);
        }       
    }

    return primeTwins;
    
}

function isPrime(num) {
    if (num <= 1) return false;

    

    for (let i = 2; i < num-1; i++) {
        if (num % i === 0) {
            return false;      
        }
        
    }

    return true;
}




console.log(findPrimeTwins(100))

