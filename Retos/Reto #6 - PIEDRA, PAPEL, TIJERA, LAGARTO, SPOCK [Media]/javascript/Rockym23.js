

var juego = [
{
    objeto:'✂️',
    vence: ['📄', '🦎']
},

{
    objeto:'📄',
    vence: ['🗿', '🖖']
},
{
    objeto:'🗿',
    vence: ['✂️', '🦎']
},
{
    objeto:'🦎',
    vence: ['🖖', '📄']
},
{
    objeto:'🖖',
    vence: ['✂️', '🗿']
},
];

function match(p1, p2){

    //0 for tie, 1 for player 1, 2 for player 2;

    var p1_obj = juego.find(element => element.objeto == p1);
    var p2_obj = juego.find(element => element.objeto == p2);

    if(p1_obj.vence.includes(p2)) return 1;
    if(p2_obj.vence.includes(p1)) return 2;
    return 0;
}

function Juego(juegos){
    
    var resultado = {
        player1 : 0,
        player2 : 0
    };

    juegos.forEach(element => {
        
        let res = match(element[0], element[1]);
        if(res == 1) resultado.player1++;
        else if(res == 2) resultado.player2++;       
    });

    console.log(resultado);

    if(resultado.player1 > resultado.player2){
        return 'Player 1';
    }else if(resultado.player1 < resultado.player2){
        return 'Player 2';
    }else{
        return 'Tie';
    }

}


//🗿 📄 ✂️ 🦎 🖖

console.log(Juego([['🖖', '🦎'], ['🗿', '🦎'], ['📄', '✂️']]));
console.log(Juego([['🖖', '🦎'], ['🗿', '🦎'], ['📄', '✂️'], ['📄', '🖖'], ['🖖', '🗿']]));
console.log(Juego([['🖖', '🖖'], ['🗿', '🦎'], ['📄', '✂️'], ['📄', '🦎'], ['🖖', '🗿']]));
