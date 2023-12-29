import random

class AdventCalendar:
    """
    Represents the Advent Calendar program for managing participants and conducting raffles.
    """
    def __init__(self):
        """
        Initializes an instance of the AdventCalendar class.
        """
        self.participants = []

    def add_participant(self, name):
        """
        Adds a participant to the list.

        Args:
            name (str): The name of the participant.
        """
        if name in self.participants:
            print(f'The participant "{name}" is already in the list.')
        else:
            self.participants.append(name.capitalize())
            print(f'Participant "{name}" added successfully.')

    def remove_participant(self, name):
        """
        Removes a participant from the list.

        Args:
            name (str): The name of the participant.
        """
        if name in self.participants:
            self.participants.remove(name)
            print(f'Participant "{name}" removed successfully.')
        else:
            print(f'Participant "{name}" is not in the list.')

    def list_participants(self):
        """
        Lists all participants.
        """
        if not self.participants:
            print('No participants are registered.')
        else:
            print('List of participants:')
            for participant in self.participants:
                print(participant)

    def conduct_raffle(self):
        """
        Conducts a raffle, choosing a random winner from the participants.
        """
        if not self.participants:
            print('No participants for the raffle.')
        else:
            winner = random.choice(self.participants)
            print(f'The winner of the raffle is: "{winner}"')
            self.participants.remove(winner)

    def display_menu(self):
        """
        Displays the menu options for the program.
        """
        print("\nAdvent Calendar 2023")
        print("1. Add participant")
        print("2. Remove participant")
        print("3. List participants")
        print("4. Conduct raffle")
        print("5. Exit")

    def start_program(self):
        """
        Starts the Advent Calendar program.
        """
        while True:
            self.display_menu()
            option = input("Select an option (1-5): ")

            if option == "1":
                self.add_participant(input("Enter the participant's name: "))
            elif option == "2":
                self.remove_participant(input("Enter the name of the participant to remove: "))
            elif option == "3":
                self.list_participants()
            elif option == "4":
                self.conduct_raffle()
            elif option == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please enter another option.")

if __name__ == "__main__":
    calendar = AdventCalendar()
    calendar.start_program()
