const sumaObjetiva = (array,objetivo) =>{
    //ordeno el array de mayor a menor
    const sortArray = array.sort((a,b)=> b-a)
    let matriz = []

    //bucle para recorrer el array
    for(let i=0;i<=array.length-1; i++){
        //en cada iteracion se va creando un nuevo array mas pequeño
        const newArray = sortArray.slice(i,array.length)
        //variables a ocupar
        let sum = 0
        let sum2 = 0
        let arreglo = []
        // bucle para realizar la suma
        for(let j=0;j<=newArray.length-1;j++){
            //en cada iteracion se agrega el valor del array
            arreglo.push(newArray[j])
            //Se realiza la suma ponderada
            sum += newArray[j]
            //en caso de que la suma supere el valor objetivo entonces ese valor se quita del array y la suma ponderada vulve a su valor anterior, ademas con el continue se termina esa iteracion
            if(sum>objetivo){
                arreglo.pop()
                sum=sum2
                continue
            }
            //En caso de que se cumpla el objetivo se agregara a la matriz de los resultados que cumplen la condicion
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