const list: number[] = [1, 5, 3, 2];
const target: number = 5;
//obtener todas las combinaciones
const getCombinations = (array: number[]) => {
     const combinations: number[][] = [[]];

     for (let i in array) {
          const mainPositionValue = array[Number(i)];

          const tempCombinations: number[][] = combinations.map(
               (combination) => [mainPositionValue, ...combination]
          );
          combinations.push(...tempCombinations);
     }
     return combinations;
};
//obtener el total de los valores de un array de numeros 
const totalize = (arr: number[]) => {
     return arr.reduce((acc, value) => acc + value, 0);
};

const result = getCombinations(list).filter(
     (combination) => totalize(combination) === target
);

console.log(result);
