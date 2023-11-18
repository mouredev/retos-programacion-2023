type WeatherCondition = {
  temperature: number;
  rainChance: number;
};

const predictNextDayWheater = (
  currentDay: WeatherCondition,
): WeatherCondition => {
  const chance = Math.floor(Math.random() * 10);
  let temperature =
    chance === 1
      ? currentDay.temperature + 2
      : chance === 2
        ? currentDay.temperature - 2
        : currentDay.temperature;

  const rainChance =
    currentDay.rainChance === 100
      ? currentDay.rainChance - 20
      : currentDay.temperature > 25
        ? currentDay.rainChance + 20
        : currentDay.temperature < 5
          ? currentDay.rainChance - 20
          : currentDay.rainChance;

  temperature = currentDay.rainChance === 100 ? temperature - 1 : temperature;

  return { temperature, rainChance };
};

const predictWeather = (
  predictionDays: number,
  initWeatherConditions: WeatherCondition = {
    temperature: 25,
    rainChance: 20,
  },
) => {
  let maxTemp = initWeatherConditions.temperature;
  let minTemp = initWeatherConditions.temperature;
  let rainDaysAmmount = 0;
  const weatherConditions: WeatherCondition[] = [initWeatherConditions];

  for (let day = 0; day <= predictionDays; day++) {
    const nextDayConditions = predictNextDayWheater(weatherConditions[day]);
    weatherConditions.push(nextDayConditions);

    if (nextDayConditions.temperature > maxTemp)
      maxTemp = nextDayConditions.temperature;

    if (nextDayConditions.temperature < minTemp)
      minTemp = nextDayConditions.temperature;

    if (nextDayConditions.rainChance === 100) rainDaysAmmount++;
  }

  console.table(weatherConditions);
  console.log({ maxTemp, minTemp, rainDaysAmmount });
};

predictWeather(50, { temperature: 26, rainChance: 60 });
