const MIN = 1
const MAX = 100

function isMultiplo(number, targets = []) {
    if(number == null) return false
    if(!Array.isArray(targets)) targets = [targets]

    return targets.every(target => number % target === 0)
}

for(let i = MIN; i <= MAX; i++) {
    if(isMultiplo(i, [3, 5])) console.log('fizzbuzz')
    else if(isMultiplo(i, 3)) console.log('fizz')
    else if(isMultiplo(i, 5)) console.log('buzz')
    else console.log(i)
}