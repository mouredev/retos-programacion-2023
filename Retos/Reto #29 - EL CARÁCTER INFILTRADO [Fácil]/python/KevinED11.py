from functools import lru_cache
from typing import Optional

class InvalidLengthError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


@lru_cache()
def difference_between_strings(first_text: str, second_text: str) -> list[Optional[str]]:
    if len(first_text) != len(second_text):
        raise InvalidLengthError("The length of the texts must be equal")
    
    return [b for a, b in zip(first_text, second_text) if a != b]


def main() -> None:
    first_text = "Hola me llamo kevin"
    second_text = "hola Me llamo kevin"

    try:
      diference = difference_between_strings(first_text=first_text, second_text=second_text)
      print(diference)
    except InvalidLengthError as err:
        print(err)

if __name__ == "__main__":
    main()
    
