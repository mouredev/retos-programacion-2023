"""
 * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido
 * correctamente desde el teclado. 
 * Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
"""
import keyboard

class konami:
    def __init__(self):
        self.code = [
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
        self.inport_keys = []
    
    def konami_code (self):
        if self.inport_keys == self.code:
            print ("KONAMI: he si sabes esto ya andas viejo")
        
    def keys_press (self, event):
        key = event.key
        self.inport_keys.append(key)
        self.inport_keys = self.inport_keys[-10:]
        self.konami_code()
    
    def star(self):
        keyboard.on_press(self.keys_press)
        keyboard.wait()

if __name__ == "__main__":
    konami_code = konami()
    konami_code.star()
