const list: number[] = [1, 5, 3, 2];
const target: number = 5;
//obtener todas las combinaciones
function sumasFuerzaBruta(nums: number[], target: number) {
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
}

function sumasBackTracking(nums: number[], target: number) {
     const result: number[][] = [];

     function encuentraSuma(
          nums: number[],
          target: number,
          comb: number[] = []
     ) {
          for (let i = 0; i < nums.length; i++) {
               const resta = target - nums[i];
               const newComb = [...comb, nums[i]];
               if (resta === 0) {
                    result.push([...newComb]);
               } else if (resta < 0) {
               } else if (resta > 0) {
                    encuentraSuma(nums.slice(i + 1), resta, newComb);
               }
          }
     }
     encuentraSuma(nums, target);
     console.log(result);
}

sumasBackTracking(list, target);
