function Find13Friday(mes , ano){
    const meses = { 1 : 'January', 2: 'February', 3 : 'March',
                4: 'April', 5: 'May', 6: 'June', 7: 'July',
                8: 'August', 9: 'September', 10: 'October',
                11: 'November', 12: 'December'};
    let day = new Date(meses[mes] + '13,'+ano)
    return day.getDay() == 5 ? true : false
}
console.log(Find13Friday(10,2023));