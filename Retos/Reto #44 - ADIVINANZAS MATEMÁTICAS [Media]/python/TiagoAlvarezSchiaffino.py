import random
import time
from enum import Enum
import threading

class Operation(Enum):
    """Enum representing mathematical operations."""
    ADDITION = "+"
    SUBTRACTION = "-"
    MULTIPLICATION = "*"
    DIVISION = "/"

    def apply(self, a: float, b: float) -> float:
        """
        Apply the operation to the given operands.
        
        Args:
            a (float): The first operand.
            b (float): The second operand.
        
        Returns:
            float: The result of the operation.
        """
        if self == Operation.ADDITION:
            return a + b
        elif self == Operation.SUBTRACTION:
            return a - b
        elif self == Operation.MULTIPLICATION:
            return a * b
        elif self == Operation.DIVISION:
            return a / b if b != 0 else None

def generate_math_question(digits_first: int, digits_second: int) -> tuple:
    """
    Generate a random math question with specified digit limits.
    
    Args:
        digits_first (int): The number of digits for the first operand.
        digits_second (int): The number of digits for the second operand.
    
    Returns:
        tuple: A tuple containing the first operand, second operand, and the chosen operation.
    """
    num1 = random.randint(0, 10**digits_first - 1)
    num2 = random.randint(0, 10**digits_second - 1)
    operation = random.choice(list(Operation))
    return num1, num2, operation

def ask_question(num1: float, num2: float, operation: Operation) -> tuple:
    """
    Ask the user a math question and return the user's answer and the correct result.
    
    Args:
        num1 (float): The first operand.
        num2 (float): The second operand.
        operation (Operation): The chosen operation.
    
    Returns:
        tuple: A tuple containing the user's answer and the correct result.
    """
    result = operation.apply(num1, num2)
    try:
        user_answer = float(input(f"What is the result of {num1} {operation.value} {num2}? "))
    except ValueError:
        user_answer = None
    return user_answer, result

def play_math_game():
    """Play the math quiz game."""
    correct_answers = 0
    num1_digits = 1
    num2_digits = 1
    level_threshold = 5
    tolerance = 1e-6  # adjust tolerance as needed
    question_count = 0

    print("Welcome to the Math Quiz Game!")
    print("You have 3 seconds to answer each question.")
    print("The game ends if you don't answer in time or if you provide an incorrect answer.")
    print("Let's start!\n")

    try:
        while True:
            num1, num2, operation = generate_math_question(num1_digits, num2_digits)
            question_count += 1

            print(f"What is the result of {num1} {operation.value} {num2}? ")

            user_answer = None

            def get_user_answer():
                nonlocal user_answer
                try:
                    user_answer = float(input())
                except ValueError:
                    user_answer = None

            user_input_thread = threading.Thread(target=get_user_answer)
            user_input_thread.start()
            user_input_thread.join(timeout=3)

            if user_answer is not None:
                correct_result = operation.apply(num1, num2)

                if abs(user_answer - correct_result) < tolerance:
                    print("Correct answer!")
                    correct_answers += 1

                    if correct_answers % level_threshold == 0:
                        if num1_digits >= num2_digits:
                            num2_digits += 1
                        else:
                            num1_digits += 1
                else:
                    print("Incorrect answer!")
                    break
            else:
                print("Time's up! You didn't answer in time.")
                break

            if question_count % 5 == 0:
                print(f"\nYou've answered {correct_answers} questions correctly. Moving to the next level.\n")

    except KeyboardInterrupt:
        print("\nGame aborted.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        print(f"\nGame over. You answered {correct_answers} questions correctly.")
        print("Thanks for playing!")

if __name__ == "__main__":
    play_math_game()