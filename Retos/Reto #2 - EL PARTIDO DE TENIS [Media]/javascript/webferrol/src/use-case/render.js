import { turns } from "./types";

export const render = (players, element) => {
    let p1 = players[0],
        p2 = players[1];

    element.innerHTML += `<div>${turns[p1]}-${turns[p2]}</div>`;
}