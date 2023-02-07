enum Moves {
    piedra = "🗿", papel = "📄", tijera = "✂️", lagarto = "🦎", spock = "🖖"
}

class Jugada {
    j1: Moves
    j2: Moves

    constructor(j1: Moves, j2: Moves) {
        this.j1 = j1
        this.j2 = j2
    }

    winner(): number {
        // Las tijeras cortan el papel, el papel envuelve la piedra, la piedra aplasta al lagarto,
        // el lagarto envenena a Spock, Spock aplasta las tijeras, las tijeras decapitan al lagarto,
        // el lagarto devora el papel, el papel desaprueba a Spock, Spock desintegra la piedra y,
        // como siempre, la piedra aplasta las tijeras.
        let j1 = this.j1
        let j2 = this.j2
        switch (j1) {
            case Moves.tijera:
                if ([Moves.papel, Moves.lagarto].indexOf(j2) != -1) return 1;
                else if ([Moves.spock, Moves.piedra].indexOf(j2) != -1) return 2;
                return 0;
            case Moves.papel:
                if ([Moves.piedra, Moves.spock].indexOf(j2) != -1) return 1;
                if ([Moves.tijera, Moves.lagarto].indexOf(j2) != -1) return 2;
                return 0;
            case Moves.piedra:
                if ([Moves.tijera, Moves.lagarto].indexOf(j2) != -1) return 1;
                if ([Moves.spock, Moves.papel].indexOf(j2) != -1) return 2;
                return 0;
            case Moves.lagarto:
                if ([Moves.papel, Moves.spock].indexOf(j2) != -1) return 1;
                if ([Moves.piedra, Moves.tijera].indexOf(j2) != -1) return 2;
                return 0
            case Moves.spock:
                if ([Moves.piedra, Moves.tijera].indexOf(j2) != -1) return 1;
                if ([Moves.papel, Moves.lagarto].indexOf(j2) != -1) return 2;
                return 0;
        }
    }
}

const partida = (jugadas: Jugada[]) => {
    let win1 = 0
    let win2 = 0
    for (let j = 0; j < jugadas.length; j++) {
        let w = jugadas[j].winner()
        if (w == 1) {
            win1++;
        } else if (w == 2) {
            win2++;
        }
    }
    if (win1 > win2) {
        console.log("Player 1");
    } else if (win1 < win2) {
        console.log("Player 2");
    } else {
        console.log("Tie");
    }
}

partida([
    new Jugada(Moves.piedra, Moves.tijera),
    new Jugada(Moves.tijera, Moves.piedra),
    new Jugada(Moves.tijera, Moves.tijera)
])