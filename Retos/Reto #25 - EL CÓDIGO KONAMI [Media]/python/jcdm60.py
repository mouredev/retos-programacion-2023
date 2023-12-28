# Reto #25: El Código Konami
#### Dificultad: Media | Publicación: 19/06/23 | Corrección: 26/06/23

## Enunciado

#
# Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente
# desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
#
import keyboard


class KonamiDetector:
    def __init__(self):
        self.konami_code = [
            "up",
            "up",
            "down",
            "down",
            "left",
            "right",
            "left",
            "right",
            "b",
            "a",
        ]
        self.current_keys = []

    def check_konami_code(self):
        if self.current_keys == self.konami_code:
            print("KONAMI ENCONTRADO!!!!")

    def on_key_press(self, event):
        key = event.name
        self.current_keys.append(key)
        self.current_keys = self.current_keys[-10:]
        self.check_konami_code()

    def start(self):
        keyboard.on_press(self.on_key_press)
        keyboard.wait()


if __name__ == "__main__":
    konami_detector = KonamiDetector()
    konami_detector.start()
