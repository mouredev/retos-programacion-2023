function textoALeet(texto) { 
    let leetAlph={a:'@', 
      b:'8', 
      c:'(', 
      d:'|)',
      e: '3',
      f:'ph', 
      g:'g',
      h:'#',
      i:'l',
      j:'_|',
      k:'|<', 
      l:'1', 
      m:'^^', 
      n:'^/', 
      o:'0', 
      p:'|D', 
      q:'(,)', 
      r:'|2', 
      s:'5', 
      t:'+', 
      u:'|_|', 
      v:'|/', 
      w:'VV',
      x:'><', 
      y:'j', 
      z:'2'};
   
    texto = texto.toLowerCase();
    for (var i = 0; i < texto.length; i++) {
      if (leetAlph[texto[i]]) {
        texto = texto.replace(texto[i], leetAlph[texto[i]]);
      }
    }
    return(texto);
  }
  
  let texto='carolina';
  console.log(textoALeet(texto));