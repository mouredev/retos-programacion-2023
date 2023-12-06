import keyboard
from termcolor import colored

class KonamiDetector:
    def __init__(self):
        self.konami_code = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'b', 'a']
        self.current_keys = []

    def konami_check_decorator(func):
        def wrapper(self, key):
            self.current_keys.append(key.name)
            if self.current_keys[-len(self.konami_code):] == self.konami_code:
                success_msg = colored("¡Código Konami introducido correctamente!", "green")
                print(success_msg)
                self.current_keys = []  # Reinicia la lista de teclas actuales
            elif self.current_keys[-len(self.konami_code):] != self.konami_code[:len(self.current_keys)]:
                error_msg = colored("Código incorrecto. Intenta de nuevo.", "red")
                print(error_msg)
                self.current_keys = []  # Reinicia la lista de teclas actuales
            func(self, key)
        return wrapper

    @konami_check_decorator
    def key_press(self, key):
        pass

    def start_listening(self):
        try:
            keyboard.on_press(self.key_press)
            keyboard.wait()
        except KeyboardInterrupt:
            error_msg = colored("\nSe ha interrumpido la ejecución.", "red")
            print(error_msg)

if __name__ == '__main__':
    try:
        detector = KonamiDetector()
        start_msg = colored("Introduce el Código Konami:", "blue")
        print(start_msg)
        detector.start_listening()
    except Exception as e:
        error_msg = colored(f"\nHa ocurrido un error: {str(e)}", "red")
        print(error_msg)
