
class InvalidLengthError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def difference_between_strings(first_text: str, second_text: str) -> list[str]:
    if len(first_text) != len(second_text):
        raise InvalidLengthError("The length of the texts must be equal")
    
    return [second_text[i] for i in range(len(first_text)) if second_text[i] != first_text[i]]


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
    