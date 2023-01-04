function fizzbuzz () {
  
    for (let i = 1; i < 101; i++) {
      	let output = ''
        if (i % 3 == 0){
          output += 'fizz'
        }
      	if (i % 5 == 0){
          output += 'buzz'
        }
      	if (!Boolean(output)){
          output += i.toString()
        }
      	console.log(output)
    }
}