//Genera un número aleatorio entre un rango de enteros
function aleatorio(minimo, maximo)
{
    var numero = Math.floor( Math.random() * (maximo - minimo + 1) + minimo );
    return numero;
}

var piedra = 0;
var papel = 1;
var tijera = 2;
var lagarto = 3;
var spock = 4;

var opciones = ["Piedra", "Papel", "Tijera", "Lagarto", "Spock"];

var opcionUsuario;
var opcionMaquina = aleatorio(0,4);

opcionUsuario = prompt("¿Qué eliges?\nPiedra: 0\nPapel: 1\nTijera: 2\nLagarto: 3\nSpock: 4", 0);

alert("Elegiste " + opciones[opcionUsuario]);


if(opcionUsuario == piedra)
{
	alert("Sheldon eligió " + opciones[opcionMaquina]);
    if(opcionMaquina == piedra)
    {
        alert("Empate!");
    }
    else if(opcionMaquina == papel)
    {
        alert("Perdiste :( ");
    }
    else if(opcionMaquina == tijera)
    {
        alert("Ganaste!");
    }
	else if(opcionMaquina == lagarto)
    {
        alert("Ganaste!");
    }
	else if(opcionMaquina == spock)
    {
        alert("Perdiste :(");
    }
}
else if(opcionUsuario == papel)
{
	alert("Sheldon eligió " + opciones[opcionMaquina]);
    if(opcionMaquina == piedra)
    {
        alert("Ganaste!");
    }
    else if(opcionMaquina == papel)
    {
        alert("Empate!");
    }
    else if(opcionMaquina == tijera)
    {
        alert("Perdiste!");
    }
	else if(opcionMaquina == lagarto)
    {
        alert("Perdiste :(");
    }
	else if(opcionMaquina == spock)
    {
        alert("Ganaste!");
    }
}
else if(opcionUsuario == tijera)
{
	alert("Sheldon eligió " + opciones[opcionMaquina]);
    if(opcionMaquina == piedra)
    {
        alert("Perdiste :(");
    }
    else if(opcionMaquina == papel)
    {
        alert("Ganaste!");
    }
    else if(opcionMaquina == tijera)
    {
        alert("Empate!");
    }
	else if(opcionMaquina == lagarto)
    {
        alert("Ganaste!");
    }
	else if(opcionMaquina == spock)
    {
        alert("Perdiste :(");
    }
}
else if(opcionUsuario == lagarto)
{
	alert("Sheldon eligió " + opciones[opcionMaquina]);
    if(opcionMaquina == piedra)
    {
        alert("Perdiste!");
    }
    else if(opcionMaquina == papel)
    {
        alert("Ganaste!");
    }
    else if(opcionMaquina == tijera)
    {
        alert("Perdiste :(");
    }
	else if(opcionMaquina == lagarto)
    {
        alert("Empate!");
    }
	else if(opcionMaquina == spock)
    {
        alert("Ganaste!");
    }
}
else if(opcionUsuario == spock)
{
	alert("Sheldon eligió " + opciones[opcionMaquina]);
    if(opcionMaquina == piedra)
    {
        alert("Ganaste!");
    }
    else if(opcionMaquina == papel)
    {
        alert("Perdiste!");
    }
    else if(opcionMaquina == tijera)
    {
        alert("Ganaste!");
    }
	else if(opcionMaquina == lagarto)
    {
        alert("Perdiste!");
    }
	else if(opcionMaquina == spock)
    {
        alert("Empate!");
    }
}
else
{
    alert("Elige 0, 1, 2, 3 o 4 pelon");
    location.reload(true);
}