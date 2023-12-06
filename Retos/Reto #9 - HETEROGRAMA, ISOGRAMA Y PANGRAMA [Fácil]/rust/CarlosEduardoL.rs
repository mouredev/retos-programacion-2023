use std::collections::HashSet;

/// Returns true if the given word is a heterogram (i.e., contains no repeated letters), false otherwise.
fn is_heterogram(word: &str) -> bool {
    let mut unique_letters = HashSet::new();
    for c in word.chars() {
        if c.is_alphabetic() && !unique_letters.insert(c.to_ascii_lowercase()) {
            return false;
        }
    }
    true
}

/// Returns true if the given word is an isogram (i.e., all letters appear the same number of times), false otherwise.
fn is_isogram(word: &str) -> bool {
    let mut counts = [0; 26];
    for c in word.chars() {
        if c.is_alphabetic() {
            let index = c.to_ascii_lowercase() as usize - 'a' as usize;
            counts[index] += 1;
        }
    }
    let mut first_count = 0;
    for count in counts.iter() {
        if *count != 0 {
            if first_count == 0 {
                first_count = *count;
            } else if *count != first_count {
                return false;
            }
        }
    }
    true
}

/// Returns true if the given word is a pangram (i.e., contains all letters of the alphabet), false otherwise.
fn is_pangram(word: &str) -> bool {
    let mut unique_letters = HashSet::new();
    for c in word.chars() {
        if c.is_alphabetic() {
            unique_letters.insert(c.to_ascii_lowercase());
        }
    }
    unique_letters.len() == 26
}


mod test {
    use super::*;

    #[test]
    fn test_is_heterogram() {
        assert_eq!(is_heterogram("the big dwarf only jumps"), true);
        assert_eq!(is_heterogram("the big dwarf only jumps twice"), false);
    }

    #[test]
    fn test_is_isogram() {
        assert_eq!(is_isogram("isogram isogram"), true);
        assert_eq!(is_isogram("eleven eleven"), false);
    }

    #[test]
    fn test_is_pangram() {
        assert_eq!(is_pangram("The quick brown fox jumps over the lazy dog"), true);
        assert_eq!(is_pangram("The quick brown fox jumps over the dog"), false);
    }

}