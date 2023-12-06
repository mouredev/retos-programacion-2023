const  resultadoJuego = marcador => {
    let points1 = 0;
    let points2 = 0;

    const rules = {
        "🗿": ["✂️", "🦎"],
        "📄": ["🗿", "🖖"],
        "✂️": ["📄", "🦎"],
        "🦎": ["🖖", "📄"],
        "🖖": ["🗿", "✂️"]
    }

    for (let i = 0; i < marcador.length; i++) {
        const [player1, player2] = marcador[i];
        
        if (player1 == player2) continue;
        
        if (rules[player2].find(element => element == player1)) points2 += 1;
        else points1 += 1;
    }
    console.log(points1 == points2 ? "Tie" : points1 > points2 ? "Ganador jugador 1" : "Ganador jugador 2");
}


resultadoJuego([["🗿","✂️"], ["✂️","🗿"], ["✂️","📄"], ["✂️","📄"]]);
