import { setScore,render } from "./use-case";


export const gameApp = element => {
    let players = [0, 0];

    if (!Boolean(element) && !document.body.contains(element))
        throw new Error(`HTMLElement ${element} not found.`);

    const btnEL = document.querySelector("#counter");

    render(players, element);


    btnEL.addEventListener('click', () => {
        const winner = Math.trunc(Math.random() * 2); //Número aleatorio entre 0 y 1 donde 0 es jugador 1 y 1 jugador dos
        const [player, finish] = setScore(players, winner);
        render(players, element);

        if (finish) {
            btnEL.disabled = true;
            element.innerHTML +=`<h2>Ha ganado el  P${player + 1}</h2>`;
        }
    });
}