import random as rd
import sys
from pytimedinput import timedInput


class Game:

    def __init__(self, lang='en') -> None:
        self.xlevel = 0
        self.ylevel = 0
        self.score = 0
        # User correct hits
        self.uhits = 0
        # Limit time to answer (in seconds)
        self.limit_time = 5
        self.timed_out = False
        self.lang = lang
        self.level = 0
        self.prev = 0

    def generate_random_question(self):
        operations = ['+', '-', '*', '/']
        operation = rd.choice(operations)
        a = rd.randint(10 ** self.xlevel, 10 ** (self.xlevel + 1))
        b = rd.randint(10 ** self.ylevel, 10 ** (self.ylevel + 1))
        c = 0
        if operation == '+':
            c = a + b
        elif operation == '-':
            c = a - b
        elif operation == '*':
            c = a * b
        elif operation == '/':
            c = a // b

        return a, b, c, operation

    def show_game_status(self, current_operation, result_symbol, result_color):
        clear()
        sys.stdout.write(
            f"\033[1;32m🎯 Score {self.score} | ❓ {current_operation} | ⏲️  {self.limit_time}s | 🧮 Level {self.level}\n")
        # sys.stdout.write(f"{result_color}{result_symbol}\033[0m ")
        # sys.stdout.write("→ ")

    def show_stats(self):
        if self.lang == 'es':
            print(f'🎯 Tu puntaje: {self.score}')
            print(f'🔥 Dificultad: {self.xlevel + self.ylevel + 1}')
            print(f'🏆 Respuestas correctas: {self.uhits}')
        else:
          print(f'\n🎯 Your score: {self.score}')
          print(f'🔥 Difficulty: {self.xlevel + self.ylevel + 1}')
          print(f'🏆 Correct hits: {self.uhits}')

    def play(self):
        while True:
            a, b, c, operation = self.generate_random_question()
            self.prev = c

            # Show initial game status
            self.show_game_status(f"{a} {operation} {b}", "", "")

            x, timedOut = timedInput("→ ", timeout=self.limit_time)
            if timedOut:
                self.timed_out = True
                break

            if x == 'exit':
                break

            try:
                x = int(x)

                if x == c:
                    self.uhits += 1
                    self.score += self.xlevel + self.ylevel + 1
                else:
                    break

            except ValueError:
                break

            self.show_game_status("", "", "")
            # time.sleep(0.5)

            if self.uhits != 0:
                # Each 4 levels, give more time to answer
                if self.uhits % 4 == 0:
                    self.limit_time += 1
                if self.uhits % 5 == 0:
                  self.level += 1
                  if self.xlevel > self.ylevel:
                      self.ylevel += 1
                  else:
                      self.xlevel += 1

        clear()
        if self.timed_out:
            if self.lang == 'es':
                print('⌛ Se acabó el tiempo 😭')
            else:
                print('⌛ You ran out of time 😭')
        else:
            if self.lang == 'es':
                print('💀 Respondiste mal 💀')
            else:
                print('💀 You answered wrong 💀')

        print()
        final_message = f'🦃 Respuesta correcta: {self.prev}' if self.lang == 'es' else f'🦃 Correct answer: {self.prev}'
        print(final_message)
        self.show_stats()


def clear():
    sys.stdout.write("\033c")


def show_welcome_message(lang='en'):
    es_welcome_message = '''
    🧮 Bienvenido al juego de preguntas matemáticas! 🧮

    🤓 Tienes que responder tantas preguntas como puedas.
    🧠 Cada 5 respuestas correctas, la dificultad aumentará.
    ❌ Si respondes mal, el juego terminará.
    ⏰ Ten cuidado, tienes tiempo limitado para responder cada pregunta!
    ➗ Para la división, solo escribe el cociente (parte entera).
    '''
    en_welcome_message = '''
    🧮 Welcome to the math quiz game! 🧮

    🤓 You have to answer as many questions as you can.
    🧠 Every 5 correct answers, the difficulty will increase.
    ❌ If you answer wrong, the game will end.
    ⏰ Be careful, you have limited time to answer each question!
    ➗ For division, just write the quotient (integer part).
    '''

    if lang == 'es':
        print(es_welcome_message)
        input('Presiona cualquier tecla para comenzar 🎮\n')
    else:
        print(en_welcome_message)
        input('Press any key to start 🎮\n')

if __name__ == '__main__':
    clear()
    show_welcome_message()
    game = Game()
    game.play()
