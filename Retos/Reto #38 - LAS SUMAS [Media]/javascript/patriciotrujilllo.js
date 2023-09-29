const sumaObjetiva = (array,objetivo) =>{
    const sortArray = array.sort((a,b)=> b-a)
    let matriz = []

    for(let i=0;i<=array.length-1; i++){
        const newArray = sortArray.slice(i,array.length)
        let sum = 0
        let sum2 = 0
        let arreglo = []
        
        for(let j=0;j<=newArray.length-1;j++){
            arreglo.push(newArray[j])
            sum += newArray[j]
            if(sum>objetivo){
                arreglo.pop()
                sum=sum2
                continue
            }
            if(sum===objetivo){
                matriz.push([...arreglo])
                sum2=sum 
            }
            if(sum<objetivo){
                sum2=sum   
            }
            
        }

    }
    return matriz
}
const res = sumaObjetiva([1, 5, 3, 2],6)
console.log(res)