from typing import Protocol, Iterable
from functools import cached_property

class Counter(Protocol):
    """
    Protocol defining the interface for a counter

    A Counter is an object that provides a method 'start' which returns a string.
    Classes implementing this protocol should define the 'start' method to provide
    a custom implementation for the counter's functionality.

    Example:
        class MyCounter:
            def start(self) -> str:
                # Custom implementation for the counter's start method
                return "Counting has started!"

    """
    def start(self) -> str:
        ...


class AbacusCounter:
    """
    An implementation of the Counter interface
    """
    
    def __init__(self, secuence: Iterable[str]) -> None:
        self.__secuence = secuence
    
    def __post_init__(self) -> None:
        if not isinstance(self.__secuence, (list, tuple, set)):
            raise TypeError("secuence must be a list, set or a tuple of strings")
        
        if not all(isinstance(s, str) for s in self.__secuence):
            raise TypeError("secuence must contain only strings")
    
    def __format_result(self, result: str) -> str:
        return f"{float(result):,.0f}".replace(",", ".")

    def __choice_number(self, block_numbers: str) -> int:
        number = 0
        for n in block_numbers:
            if n == "-":
                break
            number += 1

        return number
    
    @cached_property
    def __get_result(self) -> str:   
        return "".join([str(self.__choice_number(block_numbers=block_numbers)) 
                        for block_numbers in self.__secuence])
            
    def start(self) -> str:
        result = self.__get_result
        output_formatted = self.__format_result(result=result)

        return output_formatted


def main(counter: Counter) -> None:
    """ 
    Entry point of the application
    """
    result = counter.start()
    resul2 = counter.start()
    print(result)
    print(resul2)


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

    counter = AbacusCounter(secuence=secuence)
    main(counter=counter)
    