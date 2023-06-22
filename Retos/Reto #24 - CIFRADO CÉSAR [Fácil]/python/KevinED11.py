from string import ascii_uppercase
from abc import ABC, abstractmethod


class InvalidCharacterError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class InvalIdCipherError(Exception):
    pass

class InvalidDecrypterError(Exception):
    pass


class ICipher(ABC):
    @property
    @abstractmethod
    def cipher(self) -> str:
        pass
    

class IAlphabet(ABC):
    @abstractmethod
    def get(self) -> str:
        pass


class IDecrypter(ABC):
    @property
    @abstractmethod
    def decrypt(self) -> str:
        pass


class IConversor(ABC):
    @property
    @abstractmethod
    def get(self) -> dict[str, str]:
        pass


class EnglishAlphabet(IAlphabet):
    @staticmethod
    def get() -> str:
        return ascii_uppercase + " "


class SpanishAlphabet(IAlphabet):
    @staticmethod
    def get() -> str:
        return "abcdefghijklmnñopqrstuvwxyz ".upper()


class CesarCipherConversor(IConversor):
    def __init__(self, alphabet: IAlphabet, shift: int) -> None:
        self.__alphabet = alphabet.get()
        self.__shift = shift
    
    @property
    def get(self) -> dict[str, str]:
        letters = self.__alphabet
        cesar = {}
        
        for i, letter in enumerate(letters):
            cesar_position = (i + self.__shift) % len(letters)
            cesar_letter = letters[cesar_position]
            cesar[letter] = cesar_letter
        return cesar



# M

def convert_text(text: str, conversor: dict[str, str]) -> str:
    conversion = ""
    for letter in text:
           if letter not in conversor:
                raise InvalidCharacterError(f"Invalid character: {letter}")
           conversion += conversor[letter]

    return conversion


class CesarCipher(ICipher):
    def __init__(self, text: str, conversor: IConversor) -> None:
        self.__text = text.upper()
        self.__conversor = conversor.get
    
    @property
    def cipher(self) -> str:
        converted_text = convert_text(text=self.__text, conversor=self.__conversor)
        
        return converted_text


class CesarCipherDecrypter(IDecrypter):
    def __init__(self, cesar_text: str, conversor: IConversor) -> None:
        self.__cesar_text = cesar_text.upper()
        self.__conversor = conversor.get
    
    @property
    def decrypt(self) -> str:
        conversor = {v: k for k, v in self.__conversor.items()}
        converted_text = convert_text(text=self.__cesar_text, conversor=conversor)
        
        return converted_text


class Main:
    def __init__(self, cipher: ICipher, decrypter: IDecrypter) -> None:
        self.__cipher = cipher
        self.__decrypter = decrypter
        self.__post_init__()
    
    def __post_init__(self) -> None:
        if not issubclass(type(self.__cipher), ICipher):
            raise InvalidDecrypterError("Invalid cipher")
        if not issubclass(type(self.__decrypter), IDecrypter):
            raise InvalidDecrypterError("Invalid decrypter")

        
    def cipher(self) -> str:
        return self.__cipher.cipher
    
    def decrypt(self) -> str:
        return self.__decrypter.decrypt


if __name__ == "__main__":
    alphabet = EnglishAlphabet()
    conversor = CesarCipherConversor(alphabet, 3)
    try:
        cipher = CesarCipher("kevin duenas perro", conversor)
        decrypter = CesarCipherDecrypter(cipher.cipher, conversor)
        
        program = Main(cipher, decrypter)
        print(program.cipher())
        print(program.decrypt())
    except (InvalidCharacterError,
            InvalIdCipherError,
            InvalidDecrypterError) as err:
        print(err)


