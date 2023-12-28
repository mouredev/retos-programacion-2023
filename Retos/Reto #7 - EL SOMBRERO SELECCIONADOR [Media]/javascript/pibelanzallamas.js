//declaracion de variables/arreglos
let preguntas = [];
let opciones = [0,0,0,0];
let opcMasElegida = 0;
let casaElegida = 2;
//preguntas---------------------
do{
    preguntas[0] = prompt(`Que color le gusta mas?
    1. Rojo
    2. Verde
    3. Amarillo
    4. Azul`);
}while(preguntas[0] < 1 || preguntas[0] > 4);
do{
    preguntas[1] = prompt(`Que animal le gusta mas?
    1. Leon
    2. Serpiente
    3. Tejon
    4. Aguila`);
}while(preguntas[1] < 1 || preguntas[1] > 4);
do{
    preguntas[2] = prompt(`Que mago le gusta mas?
    1. Hermione Granger
    2. Draco Malfoy
    3. Nymphadora Tonks
    4. Luna Lovegood`);
}while(preguntas[2] < 1 || preguntas[2] > 4);
do{
    preguntas[3] = prompt(`Con que cualidad se identifica mas?
    1. Valor
    2. Ambicion
    3. Justicia
    4. Creatividad
    `);
}while(preguntas[3] < 1 || preguntas[3] > 4);
do{
    preguntas[4] = prompt(`Que especialidad lo indentifica mas?
    1. Fuerza
    2. Determinacion
    3. Lealtad
    4. Erudicion
    `);
}while(preguntas[4] < 1 || preguntas[4] > 4);
//contado votos------------------
for(var i = 0; i < preguntas.length; i++){
    switch(parseInt(preguntas[i])){
        case 1:
            opciones[0] += 1;
            break;
        case 2:
            opciones[1] += 1;
            break;
        case 3:
            opciones[2] += 1;
            break;
        case 4:
            opciones[3] += 1;
            break;
    }
}
//comparando votos----------------
for(var i = 0; i < opciones.length; i++){
    if(opcMasElegida < opciones[i]){
        opcMasElegida = opciones[i];
        casaElegida = i+1;
    }
}
//seleccionando casa--------------
switch(casaElegida){
    case 1:
        console.log('Gryffindor!');
        break;
    case 2:
        console.log('Slytherin!');
        break;
    case 3:
        console.log('Hufflepuff!');
        break;
    case 4:
        console.log('Ravenclaw!');
        break;
}
