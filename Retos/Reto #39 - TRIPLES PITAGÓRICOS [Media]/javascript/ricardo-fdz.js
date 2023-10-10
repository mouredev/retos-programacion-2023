const getTriplex = (limit) => {
  let triplex= [];
  for (let p=2; ((p * p) + 1) <= limit; p++) {
    for (let q = 1; q < p; q++) {
      let a = (p * p) + (q * q);
      if(a<=limit){
        let b = (p * p) - (q * q);
        let c = 2 * p * q;
        triplex.push([a, b, c]);
      }  
    }
  }
  return triplex;
};

const res = getTriplex(10);
console.log(res);
