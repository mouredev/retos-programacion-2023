/*
  * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
 */

const validapuntos = () => {   
  var puntuacion = 0;
  var acumuladopuntos = 0
  var diccionario = {a:1,b:2,c:3,d:4,e:5,f:6,g:7,h:8,i:9,j:10,k:11,l:12,m:13,n:14,ñ:15,o:16,p:17,q:18,r:19,s:20,t:21,u:22,v:23,w:24,x:25,y:26,z:27}
  
  while(acumuladopuntos < 100){
  var palabra = prompt(`Qué palabra quieres puntuar? La palabra vale ${puntuacion} y un total de ${acumuladopuntos}`);
  
  if(palabra===null)
    return
  
    if(palabra==="") alert(`No puedes poner una palabra vacía`)
   // Validamos
   for (let i in palabra){
     let letra = palabra.charAt(i)
     if (letra in diccionario){
       puntuacion += diccionario[letra];        
     }
   }
   // almacena en localstorage para el acumulado.
   if(!localStorage.getItem("acumuladopuntos")){
      localStorage.setItem("acumuladopuntos",puntuacion);
      acumuladopuntos = parseInt(localStorage.getItem("acumuladopuntos"))
   }else{
     acumuladopuntos = parseInt(localStorage.getItem("acumuladopuntos"))+puntuacion
     localStorage.setItem("acumuladopuntos",acumuladopuntos);
   }
   
   if(acumuladopuntos >= 100){
     alert('Enhorabuena!! Has pasado los 100 puntos');
     localStorage.removeItem("acumuladopuntos");
   }
   console.log(`Tus puntos son: ${puntuacion} y llevas acumulados ${acumuladopuntos}`)
   
}
}

validapuntos()
