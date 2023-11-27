const readline = require('readline')

let questCount = 1
let correct = 0
const ops = ['+', '-', '*', '/']

const createIF = (readline) => readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

const getOperation = (ops, quesCount) => {
  const op = ops[Math.round(Math.random() * (ops.length - 1))]
  let left
  let right
  if(quesCount <= 5) {
    left = Math.round(Math.random() * 9)
    right = Math.round(Math.random() * 9)
  } else if(quesCount > 5 && quesCount <= 10) {
    left = Math.round(Math.random() * 90)
    right = Math.round(Math.random() * 9)
  } else if(quesCount > 10 && quesCount <= 15) {
    left = Math.round(Math.random() * 99)
    right = Math.round(Math.random() * 99)
  } else {
    left = Math.round(Math.random() * 999)
    right = Math.round(Math.random() * 99)
  }
  return [
    `${left}${op}${right}`,
    eval(`Math.trunc(${left}${op}${right})`)
  ]
}

console.clear()
console.log(
` <--- MATH OPS GAME --->
All results must be rounded to the nearest integer
3 seconds contdown per question...`)

const question =() => {
  return new Promise((res, rej) => {
    let rl = createIF(readline)
    let [opstring, expect] = getOperation(ops, questCount)
    rl.question(
    `- Question ${questCount}:
    Which is the result of ${opstring}?\n`, (result) => {
      if(parseInt(result) === expect) correct++
      rl.close()
      console.clear()
      res('')
    })
    setTimeout(() => {
      rl.close()
      rej('')
    }, 3000)
  })
}

setTimeout(async () => {
  console.clear()
  while(questCount <= 20) {
    try { await question() }
    catch(_) { break }
    questCount ++
  }
  console.clear()
  console.log(`
  GAME END!!!
  Correct answers: ${correct}/20
  ${correct <= 10 ?
    'Meh... better luck next time' :
    correct > 10 && correct <= 15 ?
    'Not bad, but you can improve' :
    correct > 15 && correct <= 19 ?
    'Great work!' : 'Perfect!!!'
  }`)
  process.exit(0)
}, 4000)
