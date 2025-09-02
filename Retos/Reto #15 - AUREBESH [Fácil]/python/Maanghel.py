"""
Crea una función que sea capaz de transformar Español al lenguaje básico
    del universo Star Wars: el "Aurebesh".
- Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
- También tiene que ser capaz de traducir en sentido contrario.

¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.

¡Que la fuerza os acompañe!
"""

class Aurebesh():
    """
    Translator between Spanish text and the Aurebesh alphabet 
    (the written form of Galactic Basic in the Star Wars universe).
    
    Features:
        - Provides bidirectional translation:
            * from Spanish to Aurebesh (`to_aurebesh`)
            * from Aurebesh to Spanish (`to_espanol`)
        - Unknown characters (not present in Aurebesh) are preserved as-is.
        - Handles the special case "ch" as a single Aurebesh token.
    """

    mapping_aurebesh: dict[str, str] = {
        "a": "Aurek", "b": "Besh", "c": "Cresh", "d": "Dorn", "e": "Enth",
        "f": "Forn", "g": "Grek", "h": "Herf", "i": "Isk", "j": "Jenth",
        "k": "Krill", "l": "Leth", "m": "Mern", "n": "Nern", "o": "Osk",
        "p": "Peth", "q": "Qek", "r": "Resh", "s": "Senth", "t": "Trill",
        "u": "Usk", "v": "Vev", "w": "Wesk", "x": "Xesh", "y": "Yirt", "z": "Zerek",
        "ch": "Cherek", ' ': ''
        }

    def to_aurebesh(self, text: str) -> str:
        """
        Convert a Spanish string into Aurebesh.

        Args:
            text (str): Input text in Spanish.

        Returns:
            str: The corresponding text in Aurebesh. Characters not present in the mapping
                will remain unchanged.

        Notes:
            - Multi-character mappings (e.g., "ch") are handled first.
            - Output tokens are separated by spaces.
        """

        self._validate_language(text)
        text_aurebesh: list[str] = []
        text = text.lower()
        count: int = 0
        while count < len(text):
            if count + 1 < len(text) and text[count:count + 2] in self.mapping_aurebesh:
                text_aurebesh.append(self.mapping_aurebesh[text[count:count + 2]])
                count += 2
            elif text[count] in self.mapping_aurebesh:
                text_aurebesh.append(self.mapping_aurebesh[text[count]])
                count += 1
            else:
                text_aurebesh.append(text[count])
                count += 1
        return " ".join(text_aurebesh)

    def _validate_language(self, text: str, aurebesh: bool=False) -> None:
        """
        Validate that the input string is in the expected language format.

        Args:
            text (str): Input text to validate.
            aurebesh (bool): If True, checks that the text only contains valid Aurebesh tokens.
                            If False, performs a basic Spanish validation.

        Raises:
            TypeError: If the input is not a string.
            ValueError: If the string is empty or contains invalid tokens for the given language.
        """
        if not isinstance(text, str):
            raise TypeError("Solo se aceptan cadenas de texto.")
        if not text:
            raise ValueError("El texto no puede estar vacio.")

        if aurebesh:
            words = text.split()
            for word in words:
                if word not in self.mapping_aurebesh.values():
                    raise ValueError("El texto debe estar en aurebesh.")

    def to_espanol(self, text_aurebesh: str) -> str:
        """
        Convert an Aurebesh string back into Spanish.

        Args:
            text_aurebesh (str): Input text in Aurebesh, with tokens separated by spaces.

        Returns:
            str: The corresponding text in Spanish.

        Raises:
            ValueError: If the input is not valid Aurebesh.

        Notes:
            - Unknown Aurebesh tokens are replaced with "?".
            - Empty string validation is enforced.
        """
        self._validate_language(text_aurebesh, aurebesh=True)
        reverse_aurebesh = {v: k for k, v in self.mapping_aurebesh.items()}
        words = text_aurebesh.split(" ")
        text_spanish = [reverse_aurebesh.get(word, "?") for word in words]
        return "".join(text_spanish)


if __name__ == "__main__":
    aurebesh = Aurebesh()
    print(aurebesh.to_aurebesh("Hola mundo!!"))
    print(aurebesh.to_espanol("Herf Osk Leth Aurek  Mern Usk Nern Dorn Osk"))
