export function existFridayThirteen(month:number, year: number) {
    let date = new Date(year, month-1, 13)
    console.log(`Para el mes ${month} del año ${year} ${date.getDay() == 5 ? "existe" : "no existe"} viernes 13`)
}

existFridayThirteen(1, 2023)
