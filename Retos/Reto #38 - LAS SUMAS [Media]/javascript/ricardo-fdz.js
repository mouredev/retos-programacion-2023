
const convertToBinary = (num)=>{
    let binary = []
    while (num!==0){
        let remainder = parseInt(num%2)
        num = Math.floor(num/2);
        binary.push(remainder);
    }
    return binary
}

const getSumsArray=(array, target )=>{
    let sumsArray = [];
    const combinations = Math.pow(2,array.length);
    console.log(combinations);
    for (var i = 1; i < combinations; i++) {
        let positions = convertToBinary(i);
        positions = positions.map((pos,index)=>pos!==0? index:null)
        positions = positions.filter(pos=>pos !== null)
        let currentSum = 0;
        let curreSumArray= [];
        positions.forEach(pos=>{
            currentSum += array[pos];
            curreSumArray.push(array[pos]);
        })
        if(currentSum===target){
            sumsArray.push(curreSumArray)
        }
    }
    return sumsArray
}

let res = getSumsArray([1, 5, 3, 2,1],7);
console.log(res);







