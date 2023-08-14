const sleep = (seconds:number) => new Promise(resolve => setTimeout(resolve, seconds*1000));

async function cuenta_regresiva(inicio:number, segundos:number) {
    if (inicio>=0 && segundos>=0) {
        for (let index=inicio; index>=0; index--) {
            console.log(index);
            if (index==0) return;
            await sleep(segundos);
        }
    }
}

cuenta_regresiva(10, 1);