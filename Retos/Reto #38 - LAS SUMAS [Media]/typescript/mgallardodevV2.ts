const numeros:number[] = [1,6,3,2];
const target: number  = 6;


function buscar(nums: number[], target: number){
  
  const result:number[][] = [ ]
  
  function encuentraSuma(nums: number[], target: number, comb: number[]=[]){
    for(let i = 0; i < nums.length; i++){
      const resta = target - nums[i]
      const newComb = [...comb, nums[i]];
      if(resta === 0){
        result.push([...newComb])
      }else if(resta < 0) {
      }else if(resta > 0){
        encuentraSuma(nums.slice(i+1), resta, newComb)
      }
    }
  }
  encuentraSuma(nums, target)
  console.log(result)

}

buscar(numeros, target)
