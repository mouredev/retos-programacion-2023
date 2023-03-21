
const reto = (year: number, month: number, day: number = 13): boolean => {
    let f = new Date(year, month - 1, day + 1);
    let name = f.getUTCDay()
    return name == 5
}

console.log(reto(2023, 1))
