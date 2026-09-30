'use strict';

function simulateWeather(days, initialTemperature, initialRainProbability, random = Math.random) {
  if (!Number.isInteger(days) || days < 1 || !Number.isFinite(initialTemperature) ||
      !Number.isFinite(initialRainProbability) || initialRainProbability < 0 || initialRainProbability > 100) {
    throw new Error('Parámetros no válidos');
  }
  let temperature = initialTemperature;
  let rainProbability = initialRainProbability;
  const forecast = [];

  for (let day = 1; day <= days; day++) {
    if (random() < 0.1) temperature += random() < 0.5 ? -2 : 2;
    const rains = random() * 100 < rainProbability;
    forecast.push({ day, temperature, rainProbability, rains });
    if (temperature > 25) rainProbability = Math.min(100, rainProbability + 20);
    else if (temperature < 5) rainProbability = Math.max(0, rainProbability - 20);
    if (rains) temperature--;
  }

  const temperatures = forecast.map(day => day.temperature);
  return {
    forecast,
    maximum: Math.max(...temperatures),
    minimum: Math.min(...temperatures),
    rainyDays: forecast.filter(day => day.rains).length
  };
}

module.exports = { simulateWeather };

if (require.main === module) console.table(simulateWeather(7, 20, 30).forecast);
