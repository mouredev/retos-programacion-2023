const reto = () => {
    let m = new Date().getTime()
    let numero: number = 0
    let n = new Date().getMilliseconds();

    numero = (m + n) % 100;
    console.log({ numero })
}

reto()
