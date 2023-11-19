// Author: Hans D. Escobar H. (hdescobarh)

#![crate_name = "simulador_clima"]
#![crate_type = "cdylib"]

// rand es la biblioteca para generación de números aleatorios
use rand::distributions::{Bernoulli, Standard};
use rand::rngs::StdRng;
use rand::{Rng, SeedableRng};

// Máximo valor permitido en el modelo
const MAX_ALLOWED_TEMPERATURE: f64 = 90.0;
// Mínimo valor permitido en el modelo
const MIN_ALLOWED_TEMPERATURE: f64 = -110.0;

/// Representa una simulación del clima dadas unas condiciones iniciales de temperatura y lluvia
pub struct Simulation {
    /// Número de días de simulación, incluyendo el día inicial
    total_days: usize,
    /// Almacena las predicciones de clima para cada día
    sample: Vec<Forecast>,
    /// Número de días con lluvia
    days_with_rain: Option<usize>,
    /// Máxima temperatura observada
    max_temperature: Option<f64>,
    /// Mínima temperatura observada
    min_temperature: Option<f64>,
}

impl Simulation {
    /// Inicializa y corre la simulación
    ///
    /// # Argumentos:
    /// * `days` - numero de días de simulación
    /// * `init_temperature` - temperatura inicial
    /// * `init_rain_probability` - probabilidad de lluvia inicial
    ///
    /// # Ejemplo:
    /// ```
    /// use simulador_clima::*;
    /// // simulación de 10 días, temperatura inicial de 24.0ºC
    /// // y probabilidad de lluvia inicial del 20%
    /// let simulation = Simulation::run(10, 24.0, 0.20);
    /// let report = simulation.report();
    /// println!("{report}");
    ///
    /// // Ejemplo del output (los valores pueden ser diferentes por le componente aleatorio)
    /// // Day     Temperature     Rain
    /// // 0       24      false
    /// // 1       24      false
    /// // 2       24      true
    /// // 3       23      true
    /// // 4       22      false
    /// // 5       22      false
    /// // 6       22      false
    /// // 7       22      false
    /// // 8       22      false
    /// // 9       22      false
    /// // - Days with rain: 2
    /// // - Max. temperature (ºC): 24
    /// // - Min. temperature (ºC): 22
    /// ```
    pub fn run(days: usize, init_temperature: f64, init_rain_probability: f64) -> Self {
        let mut sample: Vec<Forecast> = Vec::with_capacity(days);
        sample.push(Forecast::new(
            false,
            init_temperature,
            init_rain_probability,
        ));
        let mut simulation = Self {
            total_days: days,
            sample,
            days_with_rain: None,
            max_temperature: None,
            min_temperature: None,
        };
        simulation.sample();
        simulation.fill_stats();
        simulation
    }

    pub fn report(&self) -> String {
        // inicializa la plantilla y extrae la información de cada día
        let mut msg = "Day\tTemperature\tRain\n".to_string();
        for (day, forecast) in self.sample.iter().enumerate() {
            let temperature = forecast.temperature;
            let rained = forecast.rained;
            msg.push_str(&format!("{day}\t{temperature}\t{rained}\n"));
        }
        // Verifica que exista estadísticas
        if self.days_with_rain.is_none()
            || self.max_temperature.is_none()
            || self.min_temperature.is_none()
        {
            return msg;
        }
        msg.push_str(&format!(
            "\
            - Days with rain: {}\n\
            - Max. temperature (ºC): {}\n\
            - Min. temperature (ºC): {}\n",
            self.days_with_rain.unwrap(),
            self.max_temperature.unwrap(),
            self.min_temperature.unwrap()
        ));

        msg
    }

    // simula los demás días a partir del día inicial
    fn sample(&mut self) {
        while self.sample.len() < self.total_days {
            let lastest_forecast = &self.sample[self.sample.len() - 1];
            let next_forecast = lastest_forecast.next_day();
            self.sample.push(next_forecast);
        }
    }

    fn fill_stats(&mut self) {
        // obtiene los dias que llovieron y cuenta su número
        let days_with_rain = self
            .sample
            .iter()
            .filter(|forecast| forecast.rained)
            .count();
        self.days_with_rain = Some(days_with_rain);
        // obtiene la máxima temperatura
        let max_temperature = self
            .sample
            .iter()
            .map(|forecast| forecast.temperature)
            .reduce(f64::max)
            .unwrap();
        self.max_temperature = Some(max_temperature);
        // obtiene la temperatura mínima
        let min_temperature = self
            .sample
            .iter()
            .map(|forecast| forecast.temperature)
            .reduce(f64::min)
            .unwrap();
        self.min_temperature = Some(min_temperature)
    }
}

/// Representa las predicciones de un día
struct Forecast {
    /// Temperatura en Celsius
    temperature: f64,
    /// Probabilidad de lluvia, [0.0, 1.0]
    rain_probability: f64,
    /// Sí efectivamente llovió, es `true`
    rained: bool,
}

impl Forecast {
    fn new(rained: bool, temperature: f64, rain_probability: f64) -> Self {
        if !(0.0..=1.0).contains(&rain_probability) {
            panic!("Probability must be in the close interval [0, 1].")
        }

        if !(MIN_ALLOWED_TEMPERATURE..=MAX_ALLOWED_TEMPERATURE).contains(&temperature) {
            panic!("Temperature out of bounds.")
        }
        Self {
            rained,
            temperature,
            rain_probability,
        }
    }

    // Genera predicciones para el día siguiente
    fn next_day(&self) -> Self {
        // Temperatura
        let next_temperature: f64 = self.temperature_control();
        // Probabilidad de lluvia
        let next_rain_probability: f64 = self.rain_probability_control();
        // Resultado efectivo
        let next_rained: bool = Self::rain_get_random(next_rain_probability);

        Self::new(next_rained, next_temperature, next_rain_probability)
    }

    // Controla como cambia la temperatura del día t+1 según sí llovió en el día t
    fn temperature_control(&self) -> f64 {
        let next_temperature: f64;
        if self.rained {
            next_temperature = self.temperature - 1.0;
        } else {
            // Genera un número aleatorio entre [0, 1) a partir de una distribución uniforme
            let val: f64 = StdRng::from_entropy().sample(Standard);
            // La P(cambio ±2ºC) = 0.1, asumiendo que P(suba 2 | cambió) = P(disminuya 2 | cambió) = 0.5,
            // se tiene que P(suba 2) = P(disminuya 2) = 0.05
            if (0.0..0.05).contains(&val) {
                next_temperature = self.temperature + 2.0;
            } else if (0.05..0.1).contains(&val) {
                next_temperature = self.temperature - 2.0;
            } else if (0.1..1.0).contains(&val) {
                next_temperature = self.temperature;
            } else {
                panic!("Unexpected error. Value out of [0, 1)")
            }
        };
        next_temperature
    }

    // Controla como cambia la probabilidad de lluvia del día t+1 según la temperatura del día t
    fn rain_probability_control(&self) -> f64 {
        let next_rain_probability: f64;

        if self.temperature > 25.0 {
            next_rain_probability = f64::min(self.rain_probability + 0.2, 1.0);
        } else if self.temperature < 5.0 {
            next_rain_probability = f64::max(self.rain_probability - 0.2, 0.0)
        } else {
            next_rain_probability = self.rain_probability
        }
        next_rain_probability
    }

    // Genera un resultado aleatorio de lluvia para el día siguiente
    fn rain_get_random(next_rain_probability: f64) -> bool {
        StdRng::from_entropy().sample(Bernoulli::new(next_rain_probability).unwrap())
    }
}

#[cfg(test)]
mod tests {
    // Solo unas básicas.
    // Testear correctamente un modelo estocástico es dispendioso y
    // creo que va mas allá de los propósitos del ejercicio.
    use crate::*;

    #[should_panic]
    #[test]
    fn invalid_forecast_max_temperature() {
        Forecast::new(false, MAX_ALLOWED_TEMPERATURE + 1.0, 0.1);
    }

    #[should_panic]
    #[test]
    fn invalid_forecast_min_temperature() {
        Forecast::new(false, MIN_ALLOWED_TEMPERATURE - 1.0, 0.1);
    }

    #[should_panic]
    #[test]
    fn higher_than_valid_probability() {
        let temperature = (MAX_ALLOWED_TEMPERATURE + MIN_ALLOWED_TEMPERATURE) / 2.0;
        Forecast::new(false, temperature, 1.1);
    }

    #[should_panic]
    #[test]
    fn lower_than_valid_probability() {
        let temperature = (MAX_ALLOWED_TEMPERATURE + MIN_ALLOWED_TEMPERATURE) / 2.0;
        Forecast::new(false, temperature, -1.0);
    }

    #[test]
    fn initialize_valid_forecast() {
        let temperature = (MAX_ALLOWED_TEMPERATURE + MIN_ALLOWED_TEMPERATURE) / 2.0;
        Forecast::new(false, temperature, 1.0);
        Forecast::new(true, temperature, 1.0);
        Forecast::new(false, temperature, 0.0);
        Forecast::new(true, temperature, 0.0);
    }
}
