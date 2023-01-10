function str2leet(texto) {
  let org = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890';
  let dest = '4 I3 [ ) 3 |= & # 1 ,_| >| 1 /\\/\\ ^/ 0 |* (_,) I2 5 7 (_) \\/ \\/\\/ >< j 2 L R E A S b T B g o';
  let aDest = dest.split(' ');
  texto = texto.toUpperCase();
  let ret = '';
  for (let x = 0; x < texto.length; x++) {
    ret += (org.indexOf(texto[x]) == -1) ? texto[x] : aDest[org.indexOf(texto[x])];
  }
  return ret;
}
// Ejemplo: console.log(str2leet("Hola Mundo!")); => #014 /\/\(_)^/)0!
