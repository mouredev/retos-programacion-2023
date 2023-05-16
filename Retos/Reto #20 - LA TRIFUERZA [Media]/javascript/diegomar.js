let espacio=" ";
let asterisco="*"
function trifuerza(number){
    console.log("Trifuerza de: "+number)
    let espacios23=((2*number)-1)+number;
    let espacios_inicio=((2*number)-1);
    for(let a=0;a<number*2;a++){
        let linea=trifuerza123(number, a, espacios23, espacios_inicio);
        console.log(linea)
        if(a<number){
            espacios23--;
        }
        else{
            espacios23--;
            espacios23--;
        }
        espacios_inicio--;
    }
}
function trifuerza123(number, a, espacios23, espacios_inicio){
    let linea="";
    if(a<number){
        for (var i = 0; i < espacios_inicio; i++) {
            linea += espacio;
        }
        for (var i = 0; i <= (2*a); i++) {
            linea += asterisco;
        }
    }
    else{
        for (var i = 0; i < espacios_inicio; i++) {
            linea += espacio;
        }
        for (var i = 0; i <= (2*(a-number)); i++) {
            linea += asterisco;
        }
        for (var i = 0; i <= espacios23-1; i++) {
            linea += espacio;
        }
        for (var i = 0; i <= (2*(a-number)); i++) {
            linea += asterisco;
        }
    }
    return linea;
}
trifuerza(4);