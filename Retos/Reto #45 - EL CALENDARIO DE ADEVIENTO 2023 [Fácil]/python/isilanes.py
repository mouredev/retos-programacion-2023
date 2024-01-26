"""
Puntos que el Enunciado no especifica, y como desarrollador asumo:
- Si se introduce una opción inválida el programa avisará de ello,
  y no se lanzará un error.
- La selección de participante (para eliminarlo) sería mucho más
  usable si hubiera un menú de participantes existentes para escoger
  de ella. Dado que no se solicita, se hará aceptando un input (a ciegas).
- Un participante estará totalmente descrito por su nombre (un string).
  No se impondrán limitaciones al string (ni en caracteres especiales
  que puedan introducirse, ni en el uso de lenguaje malsonante, etc.).
- No se especifica que el participante seleccionado en el sorteo deba
  mostrarse por pantalla, pero doy por supuesto que es lo que se desea :)
- Si se intenta efectuar el sorteo estando la lista de participantes
  vacía, entiendo que debería mostrarse un mensaje y no lanzar un error.
"""
import random


ACTIONS = {
    "a": "Añadir",
    "e": "Eliminar",
    "m": "Mostrar",
    "r": "Realizar sorteo",
    "s": "Salir",
}


def main():
    participants = set()
    action_part = ", ".join([f"{v} ({k})" for k, v in ACTIONS.items()])
    main_question = f"Introduce la acción que deseas hacer [{action_part}]: "

    while True:
        action = input(main_question)

        if action == "a":
            participants = add_participant(participants)
            continue

        elif action == "e":
            participants = remove_participant(participants)
            continue

        elif action == "m":
            print_participants(participants)
            continue

        elif action == "r":
            participants = perform_raffle(participants)
            continue

        elif action == "s":
            break

        else:
            msg = f"Lo siento, no reconozco '{action}' como una acción válida. Ignorando..."
            print(msg)
            continue


def add_participant(current_participants: set[str]) -> set[str]:
    """
    Given a set of participants as input, add a new one to it and return
    the updated set. The new participant will be requested to the user.

    Args:
        current_participants (set of strings):
            Set of current participants.

    Returns:
        Updated list of participants, as a set of strings.
    """
    new_participant = input("Nombre del participante que deseas añadir: ")

    if new_participant in current_participants:
        print(f"Lo siento, '{new_participant}' ya es un participante. Ignorando...")
        return current_participants

    current_participants.add(new_participant)

    return current_participants


def remove_participant(current_participants: set[str]) -> set[str]:
    """
    Given a set of participants as input, remove one from it and return
    the updated set. The participant to remove will be requested to the user.

    Args:
        current_participants (set of strings):
            Set of current participants.

    Returns:
        Updated list of participants, as a set of strings.
    """
    participant_to_remove = input("Nombre del participante que deseas eliminar: ")

    if participant_to_remove not in current_participants:
        print(f"Lo siento, '{participant_to_remove}' no está en la lista de participantes. Ignorando...")
        return current_participants

    current_participants.discard(participant_to_remove)
    print(f"Participante '{participant_to_remove}' eliminado con éxito.")

    return current_participants


def print_participants(current_participants: set[str]) -> None:
    """
    Given a set of participants as input, print that set.

    Args:
        current_participants (set of strings):
            Set of current participants.

    Returns:
        Updated list of participants, as a set of strings.
    """
    if not current_participants:
        print("La lista de participantes está vacía.")
        return

    for participant in current_participants:
        print(participant)


def perform_raffle(current_participants: set[str]) -> set[str]:
    """
    Given a set of participants as input, select one at random,
    and print their name. Then, remove it from the set of participants,
    and return the updated set.

    Args:
        current_participants (set of strings):
            Set of current participants.

    Returns:
        Updated list of participants, as a set of strings.
    """
    if not current_participants:
        print("No pudimos realizar el sorteo, porque la lista de participantes está vacía. Ignorando...")
        return current_participants

    selected_participant = random.choice(tuple(current_participants))
    print(f"El participante seleccionado es: {selected_participant}.")

    current_participants.discard(selected_participant)

    return current_participants


if __name__ == "__main__":
    main()
