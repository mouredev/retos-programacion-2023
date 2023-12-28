#[repr(u8)]
#[derive(Clone, Copy)]
enum MetaFlags {
    Even = 1,
    Fibonacci = 1 << 1,
    Prime = 1 << 2,
}

impl MetaFlags {
    #[inline(always)]
    fn check(self, flags: u8) -> bool {
        flags & self as u8 == self as u8
    }
}

struct NumberDescriptor {
    pub number: usize,
    pub flags: u8,
}

impl NumberDescriptor {
    fn new(number: usize) -> Self {
        let mut result = Self { number, flags: 0 };
        result.check_prime();
        result.check_fibonacci();
        if number & 1 == 0 {
            result.flags |= MetaFlags::Even as u8;
        }
        result
    }

    // Check if the number is a Fibonacci number using the closed-form expression for the nth Fibonacci number
    fn check_fibonacci(&mut self) {
        const SQRT_5: f64 = 2.23606797749979;
        const PHI: f64 = (1.0 + SQRT_5) / 2.0;
        let x = self.number as f64;
        let a = (PHI.powf(x) - (-PHI).powf(-x)) / SQRT_5;
        if a.round() == a {
            self.flags |= MetaFlags::Fibonacci as u8;
        }
    }

    fn check_prime(&mut self) {
        // Check if the number is even and not equal to 2
        if self.number & 1 == 0 && self.number != 2 {
            return;
        }

        // Check if the number is divisible by any odd number up to its square root
        let sqrt = (self.number as f64).sqrt() as usize;
        for i in (3..=sqrt).step_by(2) {
            if self.number % i == 0 && i != self.number {
                return;
            }
        }

        // If the number is not divisible by any odd number up to its square root, it is prime
        self.flags |= MetaFlags::Prime as u8;
    }
}

impl std::fmt::Display for NumberDescriptor {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{} ", self.number)?;
        if !MetaFlags::Prime.check(self.flags) {
            write!(f, "no ")?;
        }
        write!(f, "es primo ")?;
        if !MetaFlags::Fibonacci.check(self.flags) {
            write!(f, "no ")?;
        }
        write!(f, "es fibonacci y ")?;
        if !MetaFlags::Even.check(self.flags) {
            write!(f, "no ")?;
        }
        write!(f, "es par")?;
        Ok(())
    }
}

pub fn main() -> Result<(), Box<dyn std::error::Error>> {
    let n: usize = input("Por favor introduzca un numero positivo: ")?.parse()?;
    let descriptor = NumberDescriptor::new(n);
    println!("{descriptor}");
    Ok(())
}

// Helper function
fn input(prompt: &str) -> Result<String, Box<dyn std::error::Error>> {
    use std::io::Write;
    print!("{}", prompt);
    std::io::stdout().flush()?;
    let mut input = String::new();
    std::io::stdin().read_line(&mut input)?;
    Ok(input.trim().to_string())
}

#[cfg(test)]
mod test {
    #[test]
    fn n_2() {
        let descriptor = super::NumberDescriptor::new(2);
        assert!(super::MetaFlags::Even.check(descriptor.flags));
        assert!(super::MetaFlags::Fibonacci.check(descriptor.flags));
        assert!(super::MetaFlags::Prime.check(descriptor.flags));
    }

    #[test]
    fn n_3() {
        let descriptor = super::NumberDescriptor::new(3);
        assert!(!super::MetaFlags::Even.check(descriptor.flags));
        assert!(super::MetaFlags::Fibonacci.check(descriptor.flags));
        assert!(super::MetaFlags::Prime.check(descriptor.flags));
    }

    #[test]
    fn n_4() {
        let descriptor = super::NumberDescriptor::new(4);
        assert!(super::MetaFlags::Even.check(descriptor.flags));
        assert!(!super::MetaFlags::Fibonacci.check(descriptor.flags));
        assert!(!super::MetaFlags::Prime.check(descriptor.flags));
    }

    #[test]
    fn n_267914296() {
        let descriptor = super::NumberDescriptor::new(267914296);
        assert!(super::MetaFlags::Even.check(descriptor.flags));
        assert!(super::MetaFlags::Fibonacci.check(descriptor.flags));
        assert!(!super::MetaFlags::Prime.check(descriptor.flags));
    }

    #[test]
    fn n_514229() {
        let descriptor = super::NumberDescriptor::new(514229);
        assert!(!super::MetaFlags::Even.check(descriptor.flags));
        assert!(super::MetaFlags::Fibonacci.check(descriptor.flags));
        assert!(super::MetaFlags::Prime.check(descriptor.flags));
    }
}
