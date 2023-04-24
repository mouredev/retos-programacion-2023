var estadofinal=''
var estadoP1="Love"
var estadoP2="Love"
while ((estadofinal!='ganador P1') && (estadofinal!='ganador P2'))
{
var dato = prompt("ingrese p1 o p2")

if (dato=='p1'){
	switch (estadoP1){
      	case "Love": estadoP1=15; break;
      	case 15: estadoP1=30; break;
      	case 30: estadoP1=40; break;
      	case 40: estadoP1=50; break;
    }

 }

if (dato=='p2'){
	switch (estadoP2){
    	case "Love": estadoP2=15; break;
      	case 15: estadoP2=30; break;
      	case 30: estadoP2=40; break;
      	case 40: estadoP2=50; break;
    }

 }

  estadofinal = estadoP1 + '-' + estadoP2;  
  if (estadoP1==50) estadofinal='ganador P1'
  if (estadoP2==50) estadofinal='ganador P2'
  
 if ((estadoP1==40) && (estadoP2==40))
 {
 	estadofinal='Deuce'
 }
 else
 if ((estadoP1==50) && (estadoP2==50))
 {
 	estadofinal='Deuce'
    	estadoP1=40
    	estadoP2=40
 }
 else
 if ((estadoP1==50) && (estadoP2==40))
 {
 	estadofinal = 'Ventaja P1'
    	estadoP1=40
    	estadoP2=30
 }
 else
  if ((estadoP2==50) && (estadoP1==40))
 {
 	estadofinal = 'Ventaja P2'
    	estadoP1=30
    	estadoP2=40
 }
alert(estadofinal);
console.log(estadofinal);
}