from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from functools import cached_property


class IReader(ABC):
    @abstractmethod
    def read(self) -> str:
        pass


class IWriter(ABC):
    @abstractmethod
    def write(self, text: str, mode: str) -> None:
        pass

    @property
    @abstractmethod
    def output_path(self) -> Path:
        pass


@dataclass
class FileReader(IReader):
    path: Path = Path("./text.txt")

    def read(self) -> str:
        with open(self.path.resolve(), mode="r") as file:
            content = file.read()

        return content


class FileWriter(IWriter):
    def __init__(self, output_path: Path = Path("./text.txt")):
        self.__output_path = output_path

    def write(self, text: str, mode: str = "a") -> None:
        with open(self.output_path, mode=mode) as file:
            file.write(text)

    @property
    def output_path(self) -> Path:
        return self.__output_path.resolve()


@dataclass
class Main:
    reader: IReader
    writer: IWriter

    @cached_property
    def __get_exit_words(self) -> list[str]:
        return ["exit", "adios"]

    def read_input(self) -> None:
        while True:
            user_input = input(
                "Ingresa el contenido a escribir en el archivo: ")

            if user_input in self.__get_exit_words:
                print("\n¡Adiós espero volver a verte pronto!")
                break

            if writer.output_path.exists():
                print(
                    "El archivo ya existe, ¿continuo escribiendo donde esta o inicio desde el principio?")

                while (new_input := input("(1, continuar), (0, iniciar desde el principio): ")) not in ["1", "0"]:
                    print("Por favor selecciona una opción correcta")

                if new_input == "1":
                    self.writer.write(text="\n" + user_input, mode="a")
                    print(self.reader.read())
                    continue

            self.writer.write(text=user_input, mode="w")


if __name__ == "__main__":
    file_path = Path("./text.txt")
    reader = FileReader(path=file_path)
    writer = FileWriter(output_path=file_path)

    program = Main(reader=reader, writer=writer)
    program.read_input()
