from typing import Protocol, Iterable
import time
import functools
import random
import dataclasses


type Number = float | int


def pause_game(seconds: Number = 3) -> None:
    time.sleep(seconds)


pause_game_by_3_seconds = functools.partial(pause_game, seconds=3)


class MathOperationFn(Protocol[Number]):
    def __call__[T: Number](self, a: T, b: T) -> T:
        ...


def add[T: Number](a: T, b: T) -> T:
    return a + b


def subtract[T: Number](a: T, b: T) -> T:
    return a - b


def multiply[T: Number](a: T, b: T) -> T:
    return a * b


def divide[T: Number](a: T, b: T) -> T:
    try:
        return a / b
    except ZeroDivisionError as err:
        print(f"No se puede dividir por cero: {err}")


@functools.lru_cache
def math_operations() -> list[MathOperationFn]:
    return [add, subtract, multiply, divide]


class MathOPerationSelectorStrategyFn(Protocol):
    def __call__(self, operations: Iterable[MathOperationFn]) -> MathOperationFn:
        ...


def math_operation_random_selector(
    operations: Iterable[MathOperationFn],
) -> MathOperationFn:
    return random.choice(operations)


class IGame(Protocol):
    def play(self) -> None:
        ...


class GameNotRunningExeption(Exception):
    pass


class GameAlreadyRunningExeption(Exception):
    pass


class MathRiddleGame:
    def __init__(self, selector_strategy: MathOPerationSelectorStrategyFn) -> None:
        self.selector_strategy = selector_strategy
        self.__runnning = False
        self.__score = 0

    def __request_answer(self) -> str:
        user_input = input("Ingrese la respuesta: ")

    def __pause_game(self) -> str | None:
        while True:
            user_input = input("Presione enter para continuar")
            if user_input == "":
                break

    def __choice_operation(self) -> MathOperationFn:
        return self.selector_strategy()

    def __stop_game(self) -> None:
        if not self.__runnning:
            raise GameNotRunningExeption("El juego no está corriendo")

        self.__runnning = False
        print("El juego ha finalizado")

    def __show_score(self) -> None:
        print(f"Tu puntuación es: {self.__score} aciertos")

    def __prepare_game(self) -> None:
        while True:
            operation = self.__choice_operation()
            user_input = self.__request_question()
            self.__stop_game()
            self.__show_score()

        self.__show_score()
        self.__stop_game()

    def play(self) -> None:
        if self.__runnning:
            raise GameAlreadyRunningError("El juego ya está corriendo")

        self.__runnning = True
        self.__prepare_game()


def main(game: IGame) -> None:
    try:
        game.play()
    except (GameAlreadyRunningError, GameNotRunningExeption) as err:
        print(err)


if __name__ == "__main__":
    selector_strategy = math_operation_random_selector
    game = MathRiddleGame(selector_strategy=selector_strategy)
    main(game=game)
