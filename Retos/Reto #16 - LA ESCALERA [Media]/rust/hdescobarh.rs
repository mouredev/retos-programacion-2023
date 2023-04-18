// hdescobarh

fn main() {
    println!(
        "Ejemplo escalera de 5 ascendente:\n{}",
        Staircase::new(5).draw_stair()
    );
    println!(
        "Ejemplo escalera de 5 descendente:\n{}",
        Staircase::new(-5).draw_stair()
    );
    println!("Ejemplo escalera de 0:\n{}", Staircase::new(0).draw_stair());
    println!("\nFin.")
}

pub struct Staircase {
    step_number: usize,
    bottom_up_direction: bool,

    // Format characters
    empty_shape: &'static str,
    landing_shape: &'static str,
    riser_shape: &'static str,
    tread_shape: &'static str,
}

impl Staircase {
    pub fn new(step_number: isize) -> Self {
        Self {
            step_number: step_number.unsigned_abs(),
            bottom_up_direction: step_number >= 0,
            empty_shape: "\u{0020}",
            landing_shape: "\u{005F}",
            riser_shape: "\u{007C}",
            tread_shape: "\u{005F}",
        }
    }

    pub fn draw_stair(&self) -> String {
        if self.step_number == 0 {
            return self.landing_shape.repeat(2);
        }

        // Make a grid of step_number*2 + 1 columns and step_number rows. Then fill each row with the corresponding character
        let steps_total_width: usize = self.step_number * 2;
        let mut line_list: Vec<String> = Vec::with_capacity(self.step_number + 1);
        line_list.push(self.empty_shape.repeat(steps_total_width) + self.landing_shape);
        for i in (1..steps_total_width).step_by(2) {
            line_list.push(
                self.empty_shape.repeat(steps_total_width - 1 - i)
                    + self.tread_shape
                    + self.riser_shape
                    + &self.empty_shape.repeat(i),
            )
        }

        // Add new-line characters and reverse lines order if stair is not bottom-up
        for line in line_list.iter_mut() {
            if !self.bottom_up_direction {
                *line = line.chars().rev().collect();
            }
            line.push('\n');
        }

        // return
        line_list.concat()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn draw_correctly_bottom_up_staircase() {
        let testing = Staircase::new(4);
        let e = testing.empty_shape;
        let t = testing.tread_shape;
        let r = testing.riser_shape;

        let correct_draw = vec![
            e.repeat(8) + testing.landing_shape + "\n",
            e.repeat(6) + t + r + e + "\n",
            e.repeat(4) + t + r + &e.repeat(3) + "\n",
            e.repeat(2) + t + r + &e.repeat(5) + "\n",
            e.repeat(0) + t + r + &e.repeat(7) + "\n",
        ]
        .concat();

        assert_eq!(correct_draw, testing.draw_stair())
    }

    #[test]
    fn draw_correctly_top_down_staircase() {
        let testing = Staircase::new(-4);
        let e = testing.empty_shape;
        let t = testing.tread_shape;
        let r = testing.riser_shape;

        let correct_draw = vec![
            "".to_string() + testing.landing_shape + &e.repeat(8) + "\n",
            e.to_string() + r + t + &e.repeat(6) + "\n",
            e.repeat(3) + r + t + &e.repeat(4) + "\n",
            e.repeat(5) + r + t + &e.repeat(2) + "\n",
            e.repeat(7) + r + t + &e.repeat(0) + "\n",
        ]
        .concat();

        assert_eq!(correct_draw, testing.draw_stair())
    }

    #[test]
    fn draw_correctly_zero_steps() {
        let testing = Staircase::new(0);

        assert_eq!(testing.landing_shape.repeat(2), testing.draw_stair())
    }
}
