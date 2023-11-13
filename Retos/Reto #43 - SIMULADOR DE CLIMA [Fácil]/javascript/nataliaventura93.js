function getRandomIntInclusive(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1) + min);
  }


function climaticConditions (days) {
    let temperature = 20;
    let rain = 10; 
    const temperatureMagicNumber10 = 1;
    const temperatureMagicNumber50 = 2;
    let currentDay = 0;
    let maxTemp = -99;
    let minTemp = 99;
    let rainningDays = 0;
    while (days>0) {
        let randomNumber10 = getRandomIntInclusive(1, 10)
        if (temperatureMagicNumber10 === randomNumber10){
            let ramdonNumber50 = getRandomIntInclusive(1, 2)
            if (temperatureMagicNumber50 === ramdonNumber50) {
                temperature-= 2;
            } else {
                temperature+= 2;  
            }
        }
        if (temperature > 25) {
            rain += 20;
            if (rain > 100) {
                rain = 100;
            }
        }
        if (temperature < 5){
            rain -= 20;
            if (rain < 0) {
                rain = 0;
            }
        }
        if (rain === 100) {
            temperature -= 1;
        }
        currentDay+=1;
        days-=1;
        let messageOfTheDay = "Hoy es día " + currentDay + ", hay una temperatura de " + temperature + "ºC" + " y una probabilidad de lluvia del " + rain + "%";
        if (rain === 100) {
            messageOfTheDay += ". Hoy llueve"
            rainningDays += 1;
        } else {
            messageOfTheDay += ". Hoy no llueve"
        }
        if (temperature > maxTemp) {
            maxTemp = temperature;
        }
        if (temperature < minTemp) {
            minTemp = temperature;
        }


        console.log(messageOfTheDay);
    }
    let messageOfDays = "Estos días tendremos una temperatura máxima de " + maxTemp + "ºC, y una mínima de " + minTemp + "ºC. Lloverá " + rainningDays + " días."
    console.log(messageOfDays);
}

climaticConditions(5);