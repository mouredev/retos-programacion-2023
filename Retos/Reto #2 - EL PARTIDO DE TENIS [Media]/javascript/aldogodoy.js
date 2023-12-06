function gameResult (sequence){
    const points = {
      0 : 'love',
      1 : '15',
      2 : '30',
      3 : '40',
      4 : 'Deuce',
      5 : 'Ventaja',
      6 : 'Win'
    }
    let results = [ {P1: 0, P2:0 } ];
    for(let player of sequence) {
    
      let lastResult = {};
      lastResult = results[results.length - 1];
      lastResult[player] = lastResult[player] + 1;
      results.push({...lastResult});
    }
    results.pop();
    
    let finalResult = '\n';
    for(let i = 0; i<results.length; i++){
      // si es menor a 3 (40)
      if (i === results.length - 1){
        const winner = sequence[sequence.length - 1];
        finalResult += `Ha ganado el ${winner} \n`;
      }else if ( results[i].P1 <= 2 || results[i].P2 <= 2) {
        finalResult += `${points[results[i].P1]} - ${points[results[i].P2]} \n`
      // si es 40 a 40
      }else if (results[i].P1 === results[i].P2 && results[i].P1 === 3 ) {
        finalResult += `Deuce\n`
      // si P1 está en ventaja
      }else if (results[i].P1 === 5 && results[i].P2 === 3) {
        finalResult += `${points[results[i].P1]} P1 \n`
      // si P2 está en ventaja
      }else if (results[i].P2 === 5 && results[i].P1 === 3) {
        finalResult += `${points[results[i].P2]} P2 \n`
      }
    }
    return finalResult;
  }
  
  gameResult(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1', 'P1']);
//(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1', 'P1']);
//(['P2', 'P2', 'P1', 'P1', 'P2', 'P1', 'P2', 'P2', 'P2'])
//(['P2' , 'P1', 'P2', 'P1', 'P2', 'P1', 'P2', 'P1'])
