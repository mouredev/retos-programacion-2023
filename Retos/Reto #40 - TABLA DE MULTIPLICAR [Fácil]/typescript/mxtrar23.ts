
/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */

interface MultiplicationTable  {
    multiplicand:number,
    multiplier:number,
    product:number,
}


const doMultiplicationTableByNumber = (multiplicand:number) => {

    const dataTable = multiplicationTable(multiplicand)
    printTable(multiplicand,dataTable)
}

const multiplicationTable = (multiplicand:number) :MultiplicationTable[] =>  {
    const dataTable :MultiplicationTable[] = []

    for (let index = 1; index <= 10; index++) {
        dataTable.push({
            multiplicand,
            multiplier : index,
            product: (multiplicand*index)
        })        
    }

    return dataTable
}

const printTable  = (multiplicand:number,dataMultiplicationTable:MultiplicationTable[]) => {
    console.log(`==== TABLE OF x${multiplicand} ====`)
    dataMultiplicationTable.forEach(row=>{
        const {multiplicand,multiplier,product} = row
        console.log(`     ${multiplicand} X ${multiplier} = ${product}`);
    })
    console.log(`====================`)

}


doMultiplicationTableByNumber(5);


/*==== TABLE OF x5 ====
     5 X 1 = 5
     5 X 2 = 10
     5 X 3 = 15
     5 X 4 = 20
     5 X 5 = 25
     5 X 6 = 30
     5 X 7 = 35
     5 X 8 = 40
     5 X 9 = 45
     5 X 10 = 50
====================*/