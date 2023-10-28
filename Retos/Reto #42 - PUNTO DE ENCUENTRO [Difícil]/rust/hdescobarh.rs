// author: Hans D. Escobar H. (hdescobarh)

//! La lógica de la solución es la siguiente. Sí los dos objetos se encuentran, necesariamente
//! existe un tiempo 𝘵 ≥ 0 tal que la distancia euclídea entre las posiciones de los dos objetos es cero.
//! Primero calcula ese tiempo 𝘵, y luego lo usa como parámetro para obtener la posición.
//!
//! # Ejemplo:
//! ```
//! use punto_de_encuentro::*;
//! let object_1 = Object2D::new(&[6.0, 7.0], &[-1.8, -0.6]);
//! let object_2 = Object2D::new(&[2.0, 2.0], &[-1.0, 0.4]);
//! let (collision_point, collision_time) = object_1.ulm_collision(&object_2).unwrap();
//! assert!((collision_time - 5.0).abs() < TOLERANCE);
//! assert!((collision_point.x - -3.0).abs() < TOLERANCE);
//! assert!((collision_point.y - 4.0).abs() < TOLERANCE);
//! ```

#![crate_name = "punto_de_encuentro"]
#![crate_type = "cdylib"]
use std::ops::{Add, Mul, Sub};

/// Parámetro introducido para controlar el impacto de errores de redondeo en valores cercanos al cero [^note].
///
/// [^note]: Para mis información: [Catastrophic cancellation](https://en.wikipedia.org/wiki/Catastrophic_cancellation).
pub const TOLERANCE: f64 = 1E-10_f64;

/// Representa una entidad arbitraria en un espacio vectorial ℝ².
pub struct Object2D {
    /// Vector posición 𝗽.
    location: Vector2D,
    /// Vector velocidad 𝐯. Es decir, desplazamiento (𝗽(𝘵+𝑖) - 𝗽(𝘵)) por unidad de tiempo 𝑖.
    velocity: Vector2D,
}

impl Object2D {
    /// Retorna una entidad en un espacio vectorial ℝ².
    ///
    /// # Argumentos:
    ///
    /// * `location` - La posición actual del objeto (x,y).
    /// * `velocity` - La velocidad (x,y) con la que se mueve el objeto.
    pub fn new(location: &[f64; 2], velocity: &[f64; 2]) -> Self {
        Self {
            location: Vector2D::from(location),
            velocity: Vector2D::from(velocity),
        }
    }
}

impl UniformLinearMotion<Vector2D> for Object2D {
    /// Retorna el tiempo dentro del cual el objeto va a colisionar con otro objeto.
    /// Retorna None sí nunca se encuentran.
    ///
    /// # Argumentos:
    ///
    /// * `other` - El segundo objeto con el que se evaluara la colisión.
    ///
    /// # Ejemplo:
    ///
    /// ```
    /// use punto_de_encuentro::*;
    /// let object_1 = Object2D::new(&[6.0, 7.0], &[-1.8, -0.6]);
    /// let object_2 = Object2D::new(&[2.0, 2.0], &[-1.0, 0.4]);
    /// let time: f64 = object_1.ulm_collision_time(&object_2).unwrap();
    /// assert!((5.0-time).abs() < TOLERANCE);
    /// ```
    ///
    /// # Explicación de la física:
    ///
    /// Sí los dos objetos se encuentran, necesariamente existe un tiempo 𝘵,
    /// tal que la distancia euclídea 𝓓(a,b) = ‖a-b‖ entre las posiciones 𝗽 y 𝗽'
    /// del primer y segundo objeto, respectivamente, es cero; es decir:
    ///
    /// * (1)    ∃𝘵‖𝗽(𝘵)-𝗽'(𝘵)‖ = ‖Δ𝗽(𝘵)‖ = 0
    ///
    /// En movimiento linear uniforme, la velocidad 𝐯 es constante para todo tiempo 𝘵; por lo tanto:
    /// * (2)    𝗽(𝘵) = 𝗽₀ + 𝘵𝐯
    ///
    /// Por (1) y (2), y por propiedades del producto punto ⟨·,·⟩:
    /// * (3)    ⟨Δ𝗽(𝘵), Δ𝗽(𝘵)⟩ = 𝘵² ⟨Δ𝐯,Δ𝐯⟩ + 𝘵 2⟨Δ𝐯,Δ𝗽₀⟩ + ⟨Δ𝗽₀,Δ𝗽₀⟩ = 0
    ///
    fn ulm_collision_time(&self, other: &Self) -> Option<f64> {
        // obtenemos Δ𝗽₀ y Δ𝐯
        let delta_initial_position: Vector2D = self.location - other.location;
        let delta_velocity: Vector2D = self.velocity - other.velocity;
        // Es un polinomio de la forma ax² + bx + c, donde a=⟨Δ𝐯,Δ𝐯⟩, b=2⟨Δ𝐯,Δ𝗽₀⟩, c=⟨Δ𝗽₀,Δ𝗽₀⟩
        let a: f64 = delta_velocity * delta_velocity;
        let b: f64 = delta_velocity * delta_initial_position * 2.0;
        let c: f64 = delta_initial_position * delta_initial_position;
        // sí ambos objetos llevan la misma velocidad, a=0 y b=0. El problema es lineal 0x + c = 0
        if a.abs() < TOLERANCE {
            // sí parten de la misma posición, c=0. Hay infinitas soluciones: ∀x(0x = 0)
            if c.abs() < TOLERANCE {
                return Some(0.0);
            // sí por el contrario, c≠0. No hay solución: ∄x(0x = c)
            } else {
                return None;
            }
        }
        // Cuando a≠0 es un problema cuadrático y aplicamos
        // la formula cuadrática: ( -b +- sqrt(b² - 4 ac) ) / (2a),

        let mut discriminant = (b * b) - (4.0 * a * c);
        // Sí v satisface que -TOLERANCE < v < TOLERANCE, entonces es un cero efectivo
        if discriminant.abs() < TOLERANCE {
            discriminant = 0.0;
        }
        // sí tiene solución en los reales, necesariamente b² - 4ac ≧ 0
        if discriminant < 0.0_f64 {
            return None;
        }
        let sqrt_discriminant = discriminant.sqrt();
        let solution_1 = (-b - sqrt_discriminant) / (2.0 * a);
        let solution_2 = (-b + sqrt_discriminant) / (2.0 * a);
        // es movimiento rectilíneo uniforme en un espacio euclídeo; por lo tanto,
        // a lo sumo existe solo una solución valida (t>=0)
        if solution_1 >= 0.0_f64 {
            Some(solution_1)
        } else if solution_2 > 0.0_f64 {
            Some(solution_2)
        } else {
            None
        }
    }

    /// Calcula la posición del objeto tomando como punto de partida (𝗽₀ = 𝗽(0)) la
    /// ubicación actual del objeto (location). 𝗽(𝘵) = 𝗽₀ + 𝘵𝐯
    ///
    /// # Argumentos:
    ///
    /// * `time` - tiempo 𝘵 transcurrido.
    ///
    /// # Ejemplo:
    ///
    /// ```
    /// use punto_de_encuentro::*;
    /// let object_1 = Object2D::new(&[11.0, 17.0], &[1.64383561643, 3.69863013698]);
    /// let position: Vector2D = object_1.ulm_position_delta_time(&7.3);
    /// assert!((position.x - 23.0).abs() < TOLERANCE
    ///     && (position.y - 44.0).abs() < TOLERANCE);
    /// ```
    fn ulm_position_delta_time(&self, time: &f64) -> Vector2D {
        //  𝗽(𝘵) = 𝗽₀ + 𝘵𝐯
        let delta_position: Vector2D = self.location + (self.velocity * *time);
        delta_position
    }
}

pub trait UniformLinearMotion<T> {
    fn ulm_collision_time(&self, other: &Self) -> Option<f64>;
    fn ulm_position_delta_time(&self, time: &f64) -> T;
    fn ulm_collision(&self, other: &Self) -> Option<(T, f64)> {
        self.ulm_collision_time(other)
            .map(|time| (self.ulm_position_delta_time(&time), time))
    }
}

/// Representa un elemento de un espacio vectorial en ℝ² en coordenadas cartesianas.
/// Tiene definidas las operaciones de suma y resta vectorial, producto punto, y producto escalar.
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Vector2D {
    pub x: f64,
    pub y: f64,
}

/// Construye un Vector desde un Array [f64; 2]
impl From<&[f64; 2]> for Vector2D {
    fn from(value: &[f64; 2]) -> Self {
        Self {
            x: value[0],
            y: value[1],
        }
    }
}

/// Producto punto con otro vector. self * other = ⟨self,other⟩
impl Mul<Vector2D> for Vector2D {
    type Output = f64;
    fn mul(self, rhs: Vector2D) -> Self::Output {
        (self.x * rhs.x) + (self.y * rhs.y)
    }
}

/// Producto escalar. self * scalar
impl Mul<f64> for Vector2D {
    type Output = Vector2D;
    fn mul(self, rhs: f64) -> Self::Output {
        Self {
            x: self.x * rhs,
            y: self.y * rhs,
        }
    }
}

/// Diferencia con otro vector. self - other
impl Sub for Vector2D {
    type Output = Vector2D;

    fn sub(self, rhs: Self) -> Self::Output {
        Vector2D {
            x: self.x - rhs.x,
            y: self.y - rhs.y,
        }
    }
}

/// Suma vectorial. self + other
impl Add for Vector2D {
    type Output = Vector2D;

    fn add(self, rhs: Self) -> Self::Output {
        Vector2D {
            x: self.x + rhs.x,
            y: self.y + rhs.y,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn ulm_collision_time_by_axis() {
        let test_cases = [
            // same origin and velocity
            (
                [[9.0, 0.0], [60.0, 0.0], [9.0, 0.0], [60.0, 0.0]],
                Some(0.0),
            ),
            // same origin, different velocity
            (
                [[15.8, 0.0], [80.3, 0.0], [15.8, 0.0], [-50.0, 0.0]],
                Some(0.0),
            ), // different origin, same velocity
            ([[17.0, 0.0], [123.5, 0.0], [1.8, 0.0], [123.5, 0.0]], None),
            // from here, different origin and velocity
            ([[98.0, 0.0], [30.0, 0.0], [15.0, 0.0], [-42.0, 0.0]], None),
            ([[0.0, 0.0], [0.5, 0.0], [6.0, 0.0], [0.0, 0.0]], Some(12.0)),
            (
                [[-2.5, 0.0], [2.406, 0.0], [4.5, 0.0], [2.1, 0.0]],
                Some(22.8758169934),
            ),
            (
                [[12.0, 0.0], [2.7, 0.0], [179.0, 0.0], [-3.1, 0.0]],
                Some(28.7931031275),
            ),
            (
                [[-10.0, 0.0], [34.0, 0.0], [200.0, 0.0], [-36.0, 0.0]],
                Some(3.0),
            ),
        ];

        // check axis X
        for ([loc1, vel1, loc2, vel2], expected) in &test_cases {
            let object_1 = Object2D::new(loc1, vel1);
            let object_2 = Object2D::new(loc2, vel2);
            let solution = object_1.ulm_collision_time(&object_2);
            if expected.is_some() && solution.is_some() {
                assert!(
                    (expected.unwrap() - solution.unwrap()).abs() < TOLERANCE,
                    "Axis X. Expected {:?}, obtained {:?}",
                    expected,
                    solution
                )
            } else {
                assert_eq!(*expected, solution)
            };
        }

        // now check axis Y
        for ([loc1, vel1, loc2, vel2], expected) in &test_cases {
            let object_1 = Object2D::new(&[loc1[1], loc1[0]], &[vel1[1], vel1[0]]);
            let object_2 = Object2D::new(&[loc2[1], loc2[0]], &[vel2[1], vel2[0]]);
            let solution = object_1.ulm_collision_time(&object_2);
            if expected.is_some() && solution.is_some() {
                assert!(
                    (expected.unwrap() - solution.unwrap()).abs() < TOLERANCE,
                    "Axis Y. Expected {:?}, obtained {:?}",
                    expected,
                    solution
                )
            } else {
                assert_eq!(*expected, solution)
            };
        }
    }

    #[test]
    fn ulm_collision_time_bidimensional() {
        let test_cases = [
            // meet
            (
                [[6.0, 7.0], [-9.0, -3.0], [2.0, 2.0], [-5.0, 2.0]],
                Some(1.0),
            ),
            (
                [[6.0, 7.0], [-1.8, -0.6], [2.0, 2.0], [-1.0, 0.4]],
                Some(5.0),
            ),
            // never meet
            ([[6.0, 7.0], [-1.8, -0.6], [2.0, 2.0], [1.0, 0.4]], None),
        ];

        for ([loc1, vel1, loc2, vel2], expected) in &test_cases {
            let object_1 = Object2D::new(loc1, vel1);
            let object_2 = Object2D::new(loc2, vel2);
            let solution = object_1.ulm_collision_time(&object_2);
            if expected.is_some() && solution.is_some() {
                assert!(
                    (expected.unwrap() - solution.unwrap()).abs() < TOLERANCE,
                    "Expected {:?}, obtained {:?}",
                    expected,
                    solution
                )
            } else {
                assert_eq!(*expected, solution)
            };
        }
    }

    #[test]
    fn ulm_collision_point_bidimensional() {
        let test_cases = [
            // meet
            (
                [[6.0, 7.0], [-1.8, -0.6], [2.0, 2.0], [-1.0, 0.4]],
                Some((Vector2D::from(&[-3.0, 4.0]), 5.0)),
            ),
            // never meet
            ([[6.0, 7.0], [-1.8, -0.6], [2.0, 2.0], [1.0, 0.4]], None),
        ];

        for ([loc1, vel1, loc2, vel2], expected) in &test_cases {
            let object_1 = Object2D::new(loc1, vel1);
            let object_2 = Object2D::new(loc2, vel2);
            let solution = object_1.ulm_collision(&object_2);
            if expected.is_some() && solution.is_some() {
                let (expected_position, expected_time) = expected.unwrap();
                let (solution_position, solution_time) = solution.unwrap();
                let diff_position = expected_position - solution_position;
                let diff_time = expected_time - solution_time;
                assert!(
                    diff_position.x.abs() < TOLERANCE
                        && diff_position.y.abs() < TOLERANCE
                        && diff_time < TOLERANCE,
                    "Expected {:?}, obtained {:?}",
                    expected,
                    solution
                )
            } else {
                assert_eq!(*expected, solution)
            };
        }
    }
}

