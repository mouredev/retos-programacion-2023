from dataclasses import dataclass


class InvalidText(Exception):
    pass


@dataclass
class AnalyzeText:
    text: str
    _split_words: list[str] = None
    _lenght_words: list[int] = None
    _max_lenght: int = None

    def __post_init__(self):
        if not isinstance(self.text, str) or not self.text:
            raise InvalidText("The content is empty or not a string")

        self._split_words = self.__split_words()
        self._lenght_words = self.__get_lenght_words()
        self._max_lenght = self.__max_lenght()

    def __filter_words(self, text: list[str]) -> list[str]:
        return list(filter(bool, text))

    def __split_words(self) -> list[str]:
        words: list[str] = self.text.split(" ")
        return self.__filter_words(words)

    def __split_characters(self):
        return list(self.text)

    def __get_lenght_words(self) -> list[int]:
        return [len(word) for word in self._split_words]

    def __max_lenght(self) -> int:
        return max(self._lenght_words)

    def lenght_text(self) -> float:
        return float(len(self._split_words))

    def average_characters(self) -> int:
        return sum(self._lenght_words) / self.lenght_text()

    def number_of_sentences(self) -> int:
        return self.__split_characters().count(".")

    def longest_word(self) -> list[str]:
        return [word for word in self._split_words if len(word) == self._max_lenght]

    @property
    def split_words(self) -> list[str]:
        return self._split_words

    @property
    def lenght_words(self) -> list[int]:
        return self._lenght_words

    @property
    def max_lenght(self) -> int:
        return self._max_lenght


if __name__ == "__main__":
    try:
      program = AnalyzeText(text="kevin dueñas musicaaaa. .")
      print(program.lenght_text())

      print(program.average_characters())
      print(program.longest_word())
      print(program.split_words)
      print(program.lenght_words)
      print(program.max_lenght)
      print(program.number_of_sentences())
    except InvalidText as err:
        print(err)
