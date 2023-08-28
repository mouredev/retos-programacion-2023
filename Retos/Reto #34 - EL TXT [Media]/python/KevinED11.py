from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from functools import cached_property
from enum import StrEnum
from typing import Optional


class InvalidWriteModeError(Exception):
    pass


class ExitWords(StrEnum):
    EXIT = "exit"
    ADIOS = "adios"
    SALIR = "salir"


class FileManipulationModes(StrEnum):
    APPEND = "a"
    WRITE = "w"
    READ = "r"


class UserInteractionFileOptions(StrEnum):
    CONTINUE = "1"
    START_OVER = "0"


class IReader(ABC):
    @abstractmethod
    def read(self) -> str:
        pass


class IWriter(ABC):
    @abstractmethod
    def write(self, text: str) -> None:
        pass


class IFileWriter(IWriter, ABC):
    @property
    @abstractmethod
    def output_path(self) -> Path:
        pass

    @output_path.setter
    @abstractmethod
    def output_path(self, path: Path) -> None:
        pass

    @property
    @abstractmethod
    def write_mode(self) -> FileManipulationModes:
        pass

    @write_mode.setter
    @abstractmethod
    def write_mode(self, mode: FileManipulationModes) -> None:
        pass

    @cached_property
    @abstractmethod
    def supported_writing_modes(self) -> list[FileManipulationModes]:
        pass


@dataclass
class FileReader(IReader):
    path: Path = Path("./text.txt")

    def read(self) -> str:
        with self.path.resolve().open(mode=FileManipulationModes.READ) as file:
            content = file.read()

        return content


class FileWriter(IFileWriter):
    def __init__(self, output_path: Path = Path("./text.txt")):
        self.__output_path: Path = output_path
        self.__write_mode: FileManipulationModes = FileManipulationModes.APPEND
        self.__supported_writing_modes: list[FileManipulationModes] = []

    def write(self, text: str) -> None:
        with self.output_path.open(mode=self.write_mode) as file:
            file.write(text)

    @property
    def output_path(self) -> Path:
        return self.__output_path.resolve()

    @output_path.setter
    def output_path(self, path: Path) -> None:
        self.__output_path = path

    @property
    def write_mode(self) -> FileManipulationModes:
        return self.__write_mode

    @write_mode.setter
    def write_mode(self, mode: FileManipulationModes) -> None:
        if mode not in self.supported_writing_modes:
            raise InvalidWriteModeError(
                f"los modos de escritura soportados son: {self.supported_writing_modes}"
            )

        self.__write_mode = mode

    @cached_property
    def supported_writing_modes(self) -> list[FileManipulationModes]:
        self.__supported_writing_modes += [
            mode for mode in FileManipulationModes if mode != FileManipulationModes.READ
        ]
        return self.__supported_writing_modes


@dataclass
class FileReaderAndWriter:
    reader: IReader
    file_writer: IFileWriter
    
    @cached_property
    def __get_exit_words(self) -> list[ExitWords]:
        return list(ExitWords)

    @cached_property
    def __get_user_interaction_file_options(self) -> list[UserInteractionFileOptions]:
        return list(UserInteractionFileOptions)

    @property
    def __check_file_existence(self) -> bool:
        return self.file_writer.output_path.exists()

    def read_input(self) -> None:
        print(f"Estos son los comandos para salir: {self.__get_exit_words}")

        while (
            user_input := input("Ingresa el contenido a escribir en el archivo: ")
        ) not in self.__get_exit_words:
            if self.__check_file_existence:
                print(
                    "El archivo ya existe, ¿continuo escribiendo donde esta o inicio desde el principio?"
                )

                while (
                    new_input := input(
                        "(1, continuar), (0, iniciar desde el principio): "
                    )
                ) not in self.__get_user_interaction_file_options:
                    print("Por favor selecciona una opción correcta")

                if new_input == UserInteractionFileOptions.CONTINUE:
                    self.file_writer.write_mode = FileManipulationModes.APPEND
                    self.file_writer.write(text="\n" + user_input)
                    print(self.reader.read())
                    continue

            self.file_writer.write_mode = FileManipulationModes.WRITE
            self.file_writer.write(text=user_input)

        print("\n¡Adiós espero volver a verte pronto!")


def main(
    reader: Optional[IReader] = None, file_writer: Optional[IFileWriter] = None
) -> None:
    if reader and file_writer:
        program = FileReaderAndWriter(reader=reader, file_writer=file_writer)
        program.read_input()


if __name__ == "__main__":
    file_path = Path("./text.txt")
    reader = FileReader(path=file_path)
    writer = FileWriter(output_path=file_path)
    main(reader=reader, file_writer=writer)
