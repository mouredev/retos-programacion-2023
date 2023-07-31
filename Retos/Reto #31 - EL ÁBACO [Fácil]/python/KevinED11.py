from typing import Protocol


class Counter(Protocol):
    def start(self) -> str:
        ...

class AbacoCounter:
    def __init__(self, secuence: list[str]) -> None:
        self.__secuence = secuence
    
    def __format_result(self, result: str) -> str:
        result = self.__get_result()
        return f"{float(result):,.0f}".replace(",", ".")

    def __choice_number(self, block_numbers: str) -> int:
        if block_numbers[0] == "-":
           return 0
        
        number = 0
        for n in block_numbers:
            if n == "-":
                break
            number += 1
                        
        return number
    
    def __get_result(self) -> str:   
        number = ""
        for block_numbers in self.__secuence:
          number += str(self.__choice_number(block_numbers=block_numbers))

        return number
    
    def start(self) -> str:
        result = self.__get_result()
        output_formatted = self.__format_result(result=result)

        return output_formatted


def main(counter: Counter) -> None:
    result = counter.start()
    print(result)


if __name__ == "__main__":
    secuence = [
        "O---OOOOOOOO",
        "OOO---OOOOOO",
        "---OOOOOOOOO",
        "OO---OOOOOOO",
        "OOOOOOO---OO",
        "OOOOOOOOO---",
        "---OOOOOOOOO",
    ]

    counter = AbacoCounter(secuence=secuence)
    main(counter=counter)