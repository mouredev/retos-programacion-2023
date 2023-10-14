// Creo una funcion para tomar tanto el numero que quieres saber la tabla (n), como la cantidad de numberos los cuales se multiplica (t)
function XTable(n, t){
  // se utiliza un loop para poder interactuar con la cantidad de la tabla 
  for(let i=1; i<= t; i++){
    const res = i * n; // se almacena el resultado como respuesta para terminar la fila de la multiplicacion
    console.log(`${n} x ${i} = ${res}`); // se printea cada resultado como se requiere en el problema
  }
}

XTable(5, 10)
XTable(2, 10)
