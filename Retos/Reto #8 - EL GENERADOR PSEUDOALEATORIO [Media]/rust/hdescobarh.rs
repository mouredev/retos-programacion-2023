/*
Pseudorandom number generation is a complex subject with a lot of math behind
it (number theory, calculus, and probability theory); then, instead of making
something from scratch, I will make a naive combination of a well known PRNG 
algorithm, the linear congruential generator.
*/

pub struct LinearCongruentialGenerator {
    seed: u64,
    slope: u64,
    cut: u64,
    modulus: u64,
}

impl LinearCongruentialGenerator {
    pub fn new(seed: u64, modulus: u64, slope: u64, cut: u64) -> Self {
        // check assumptions
        if modulus == 0 {
            panic!("Modulus must be bigger than zero.")
        }
        if slope >= modulus || slope == 0 {
            panic!("Slope must be in the interval (0, modulus).")
        }
        if cut > modulus {
            panic!("Cut point must be in the inverval [0, modulus).")
        }
        if seed > modulus {
            panic!("Seed number must be in the interval [0, modulus).")
        }

        Self {
            seed,
            slope,
            cut,
            modulus,
        }
    }

    pub fn generate_number(&mut self) -> u32 {
        // Apply the linear transformation
        let new_number = (self.slope * self.seed + self.cut)
            .checked_rem_euclid(self.modulus)
            .expect("Failed to get modulus.");
        self.seed = new_number;
        // get only the first 31 bits
        let least_k_bits = self.seed & 2u64.pow(31) - 1u64;
        // floor operation to get values in the interval [0, 100)
        let truncate_value = (100.0 * (least_k_bits as f64 / self.modulus as f64)).floor();
        return truncate_value as u32;
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use kolmogorov_smirnov;
    use rand::{thread_rng, Rng};

    #[test]
    fn compare_with_other_rng() {
        // Generate uniform distribution to compare with
        let mut rng = thread_rng();
        let distr = rand::distributions::Uniform::new_inclusive(0, 99);
        let mut uniform_dist: Vec<u32> = Vec::new();
        for _ in 0..1000 {
            uniform_dist.push(rng.sample(distr))
        }

        // Generate data using the Linear Congruential Generator
        let mut lcg = LinearCongruentialGenerator::new(160, 2147483648, 1103515245, 12345);
        let mut lcg_generated_sample: Vec<u32> = Vec::new();
        for _ in 0..1000 {
            lcg_generated_sample.push(lcg.generate_number());
        }

        // Perform Kolmogorov-Smirnof goodness of fit test
        let test_output = kolmogorov_smirnov::test(&uniform_dist, &lcg_generated_sample, 0.95);
        assert_eq!(true, !test_output.is_rejected);
    }
}
