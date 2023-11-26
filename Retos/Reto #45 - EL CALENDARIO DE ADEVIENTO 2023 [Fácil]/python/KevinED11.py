from dataclasses import dataclass, field
from typing import Protocol
from random import randint
import time


class ParticipationMecanism(Protocol):
    participants: list[str] = []
    running: bool = False

    def add(self, participant: str) -> None:
        ...

    def delete(self, participant: str) -> None:
        ...

    def show(self) -> None:
        ...

    def run_giveaway(self) -> str:
        ...

    def run(self) -> None:
        ...


def user_input(prompt: str) -> str:
    return input(prompt).lower()


@dataclass
class AdevientoParticipationMecanism:
    participants: list[str] = field(default_factory=list)
    running: bool = field(default=False)

    def add(self, participant: str) -> None:
        if participant in self.participants:
            print(f"El participante '{participant}' ya existe en la lista.")
            return

        self.participants += [participant]
        print(f"El participante '{participant}' ha sido añadido con éxito.")

    def delete(self, participant: str) -> None:
        if participant not in self.participants:
            print(f"El participante '{participant}' no existe en la lista.")
            return

        print(f"El participante '{participant}' ha sido eliminado con éxito.")
        self.participants.remove(participant)

    def show(self) -> None:
        for participant in self.participants:
            print(participant)

    def run_giveaway(self) -> str:
        time.sleep(3)
        giveaway_winner = self.participants[randint(0, len(self.participants) - 1)]

        self.participants.remove(giveaway_winner)
        print(f"El ganador del sorteo es: {giveaway_winner}")
        return giveaway_winner

    def get_options(self) -> dict[str, callable]:
        add_option = lambda: self.add(
            user_input("Introduce el nombre del participante a añadir: ")
        )
        delete_option = lambda: self.delete(
            user_input("Introduce el nombre del participante a eliminar: ")
        )
        return {
            "1": add_option,
            "2": delete_option,
            "3": self.show,
            "4": self.run_giveaway,
            "5": self.exit,
        }

    def run(self) -> None:
        self.running = True
        options = self.get_options()
        while True:
            print(
                "1. Añadir participante, 2. Eliminar participante, 3. Mostrar participantes, 4. Realizar sorteo, 5. Salir"
            )
            option = user_input("Opcion: ")
            if option not in options:
                print("Opcion no valida")
                continue

            result = options[option]()
            if isinstance(result, bool) and result:
                break

    def exit(self) -> bool:
        self.running = False
        print("¡Que tengas un buen dia, hasta luego!")
        return True


@dataclass
class Program:
    participation_mechanism: ParticipationMecanism

    def run(self) -> None:
        self.participation_mechanism.run()


def main(participation_mechanism: ParticipationMecanism) -> None:
    program = Program(participation_mechanism=participation_mechanism)
    program.run()


if __name__ == "__main__":
    participation_mechanism = AdevientoParticipationMecanism()
    main(participation_mechanism=participation_mechanism)
