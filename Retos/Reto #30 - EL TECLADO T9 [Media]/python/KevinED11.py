from functools import lru_cache


T9Keyboard = dict[str, str]


class InvalidT9Key(Exception):
  def __init__(self, message: str) -> None:
     super().__init__(message)


@lru_cache(maxsize=120)
def get_t9_keyboard() -> T9Keyboard:
  return {str(n): (" ", ",.?!", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ")[n] for n in range(10)}


def convert_t9_key_to_character(key: str) -> str:
   if (num_pressed := key[0]) not in get_t9_keyboard():
        raise InvalidT9Key("Enter a valid t9 key")

   return get_t9_keyboard()[num_pressed][len(key) - 1]


@lru_cache(maxsize=120)
def t9_to_text(keys: str) -> str:
  if not isinstance(keys, str) or not keys:
    raise ValueError("Enter a T9 secuence string")
    
  return "".join(convert_t9_key_to_character(key=key) for key in keys.split("-"))


def main() -> None:
    try:
      mouredev = t9_to_text("6-666-88-777-33-3-33-888")
      print(mouredev)
    except (ValueError, InvalidT9Key) as err:
       print(err)


if __name__ == "__main__":
    main()
