function XTable(n, t){
  for(let i=1; i<= t; i++){
    const res = i * n;
    console.log(`${n} x ${i} = ${res}`);
  }
}

XTable(5, 10)
