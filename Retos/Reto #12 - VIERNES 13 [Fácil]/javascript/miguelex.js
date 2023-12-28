const isFridaythe13t = (month, year) => {
    const date = new Date(year, month - 1, 13);
    return date.getDay() === 5;
}

console.log("¿Hay viernes 13 en marzo de 2023? " + isFridaythe13t(3, 2023)); 
console.log("¿Hay viernes 13 en octubre de 2023? " + isFridaythe13t(10, 2023));