use std::collections::HashMap;

/*
IMPORTANT! Remember that the same alphabet "letter" can have more than one ENCODED CHARACTER.
For example, in Spanish, although 'I', 'i', or 'í' represent the SAME vowel,
all are DIFFERENT Unicode scalar values. In addition, 'í' can be encoded as
a single codepoint (U+00ED) or as two (U+0069 + U+0301), adding more complexity to the task.
Finally, what characters are the same "letter" or grapheme depends on the language; for example,
in Spanish, 'u' and 'ü' are the same vowel, but in German they are two different letters.
 */

// Define the accepted languages
pub enum Language {
    Spanish,
    // English,  Germant, etc.
}

// Make explicit a well defined set of alphabet letters for the current language
pub struct Alphabet {
    pub language: Language,
    base_alphabet: HashMap<String, char>,
    modified_to_base_alphabet_map: HashMap<&'static str, char>,
}

impl Alphabet {
    pub fn new(lang: Language) -> Self {
        // Define the language core charset
        let base_alphabet = match &lang {
            // For Spanish, takes U+00F1 (ñ char) plus all Latin Alphabet Lowercase from Basic Latin Unicode Block
            Language::Spanish => {
                let mut base = (97u8..123u8)
                    .map(|codevalue| (format!("{}", codevalue as char), codevalue as char))
                    .collect::<HashMap<String, char>>();
                base.insert("ñ".to_string(), 'ñ');
                base
            }
        };

        // Define equivalences between diacritic or modified characters an the core set
        let modified_to_base_alphabet_map = match &lang {
            Language::Spanish => HashMap::from([
                // Spanish ACUTE accent (´), combining is U+0301.
                ("á", 'a'), ("a\u{301}", 'a'),
                ("é", 'e'), ("e\u{301}", 'e'),
                ("í", 'i'), ("i\u{301}", 'i'),
                ("ó", 'o'), ("o\u{301}", 'o'),
                ("ú", 'u'), ("u\u{301}", 'u'),
                // Spanish Diaeresis (¨), combining is U+0308.
                ("ü", 'u'), ("u\u{308}", 'u'),
                // Spanish tilde (~), combining is U+0308.
                ("n\u{308}", 'ñ'),
            ]),
        };

        Self {
            language: lang,
            modified_to_base_alphabet_map,
            base_alphabet,
        }
    }

    fn alphabetic_char_belongs_to_language(&self, character: &char) -> bool {
        assert!(
            character.is_alphabetic(),
            "This method checks ONLY alphabetic characters"
        );
        let testing_character = character.to_lowercase().to_string();
        self.base_alphabet.contains_key(&*testing_character)
            || self
                .modified_to_base_alphabet_map
                .contains_key(&*testing_character)
    }

    // Represents all text characters as the base charset
    pub fn get_base_representation(&self, character: &char) -> Option<char> {
        assert!(
            character.is_alphabetic(),
            "This method is intended for alphabetic characters"
        );

        let to_map = character.to_lowercase().to_string();

        match self.base_alphabet.get(&*to_map) {
            Some(mapped) => Some(*mapped),
            None => match self.modified_to_base_alphabet_map.get(&*to_map) {
                Some(mapped) => Some(*mapped),
                None => None,
            },
        }
    }
}

// Stores the text and the methods to check iso, hetero and pangramatic
pub struct Text {
    alphabet: Alphabet,
    content: String,
}

impl Text {
    pub fn new(content: String, lang: Language) -> Self {
        let alphabet = Alphabet::new(lang);
        // Check valid parameters
        if content.is_empty() {
            panic!("The text cannot be empty.")
        }
        for character in content.chars() {
            if !character.is_alphabetic() {
                continue;
            };

            if !alphabet.alphabetic_char_belongs_to_language(&character) {
                panic!("Text contains invalid characters for the chosen language.")
            };
        }

        Self { alphabet, content }
    }

    /*
    Definitions:
    Let Q(x) be the times the letter x appears in an expression X.
        - Isogram: a X that satisfies ∀x∈X, Q(x)=c, such that c is a constant x≥1.
        - Heterogram (or first-order- isogram): an isogram such that c=1.
    Let A(l) be the alphabet of the language l.
        - Pangram: a X that satisfies ∀a∈A(l), Q(a)>= 1
    */

    fn times_base_chars_in_text(&self) -> HashMap<char, usize> {
        let mut counter: HashMap<char, usize> = HashMap::new();
        for character in self.content.chars() {
            // Does not take in account non-alphabetic characters (e.g. format, control or number characters)
            if !character.is_alphabetic() {
                continue;
            }

            let char_to_count = match self.alphabet.get_base_representation(&character) {
                Some(c) => c,
                None => panic!("This should never panic. Constructor must ensure all characters in text are valid alphabet elements."),
            };

            counter
                .entry(char_to_count)
                .and_modify(|count| *count += 1)
                .or_insert(1);
        }

        return counter;
    }

    fn characters_appears_the_same_times(&self) -> Option<usize> {
        let mut counter = self.times_base_chars_in_text().into_values();

        // None if empty
        let reference_value = match counter.next() {
            Some(count) => count,
            None => return None,
        };

        // None if at least one character appears different times
        for other_value in counter {
            if other_value != reference_value {
                return None;
            }
        }
        return Some(reference_value);
    }

    pub fn is_isogram(&self) -> bool {
        match self.characters_appears_the_same_times() {
            Some(_) => true,
            None => false,
        }
    }

    pub fn is_heterogram(&self) -> bool {
        match self.characters_appears_the_same_times() {
            Some(counts) => counts == 1,
            None => false,
        }
    }

    pub fn is_pangram(&self) -> bool {
        let mapped_to_base_characters = self.times_base_chars_in_text();
        for alphabet_char in self.alphabet.base_alphabet.values() {
            match mapped_to_base_characters.contains_key(&*alphabet_char) {
                true => continue,
                false => return false,
            }
        }
        return true;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn spanish_get_correctly_the_repetition_number_in_isogram() {
        let all_lower_non_diacritics = Text::new("racondicidonar".to_string(), Language::Spanish);
        assert_eq!(
            2,
            all_lower_non_diacritics
                .characters_appears_the_same_times()
                .unwrap()
        );

        let mixed_uppercase_non_diacritics =
            Text::new("CentrIfugadLos".to_string(), Language::Spanish);
        assert_eq!(
            1,
            mixed_uppercase_non_diacritics
                .characters_appears_the_same_times()
                .unwrap()
        );

        let mixed_uppercase_with_diacritics =
            Text::new("híperBñAnduzcos".to_string(), Language::Spanish);
        assert_eq!(
            1,
            mixed_uppercase_with_diacritics
                .characters_appears_the_same_times()
                .unwrap()
        );

        let this_is_not_isogram = Text::new("Lavadora".to_string(), Language::Spanish);
        assert_eq!(
            None,
            this_is_not_isogram.characters_appears_the_same_times()
        )
    }

    #[test]
    fn spanish_get_correctly_if_isogram() {
        let this_is_an_isogram = Text::new("Escriba".to_string(), Language::Spanish);
        assert_eq!(true, this_is_an_isogram.is_isogram());

        let this_is_not_isogram = Text::new("Intestinos".to_string(), Language::Spanish);
        assert_eq!(false, this_is_not_isogram.is_isogram())
    }

    #[test]
    fn spanish_get_correctly_if_heterogram() {
        let all_lower_non_diacritics = Text::new("hiperblanduzcos".to_string(), Language::Spanish);
        assert_eq!(true, all_lower_non_diacritics.is_heterogram());

        let mixed_upper_case_non_diacritics =
            Text::new("YuXtAponer".to_string(), Language::Spanish);
        assert_eq!(true, mixed_upper_case_non_diacritics.is_heterogram());

        let mixed_upper_and_diacritic = Text::new("CéntrÍfügAÑos".to_string(), Language::Spanish);
        assert_eq!(true, mixed_upper_and_diacritic.is_heterogram())
    }

    #[test]
    fn spanish_get_correctly_if_pangram() {
        let pangramatic_sentence = "Benjamín pidió una bebida de kiwi y fresa.
        Noé, sin vergüenza, la más exquisita champaña del menú."
            .to_string();
        let this_is_pangram = Text::new(pangramatic_sentence, Language::Spanish);
        assert_eq!(true, this_is_pangram.is_pangram());

        let non_pangramatic_sentence = "Muchos años después, frente al pelotón de fusilamiento,
        el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó
        a conocer el hielo."
            .to_string();
        let this_is_not_pangram = Text::new(non_pangramatic_sentence, Language::Spanish);
        assert_eq!(false, this_is_not_pangram.is_pangram());
    }
}
