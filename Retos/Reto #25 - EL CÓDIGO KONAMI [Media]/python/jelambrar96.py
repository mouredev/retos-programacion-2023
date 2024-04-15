#!/usr/bin/python3

"""
# Reto #25: El Código Konami
/*
 * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente
 * desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
 */
"""

__author__ = "Jorge Lambraño - jelambrar96"
__copyright__ = "Copyright 2024, retos-programacion-2023"
__credits__ = ["Brais Moure - mouredev"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jorge Lambraño"
__email__ = "jelambrar@gmail.com"
__status__ = "Production"


import sys

from enum import Enum
from time import sleep
from pynput.keyboard import Key, KeyCode, Listener

KONAMI_CODE = [ Key.up, Key.up, Key.down, Key.down, Key.left, Key.right,
                Key.left, Key.right, KeyCode.from_char("b"), KeyCode.from_char("a")]


LEN_KONAMI_CODE = len(KONAMI_CODE)


class KonamiKeyboard:

    def __init__(self,):
        self._seq = []

    def check_konami_code(self, key):
        if Key.esc == key:
            sys.exit()
        self._seq.append(key)
        len_seq = len(self._seq)
        if len_seq > LEN_KONAMI_CODE:
            self._seq.pop(0)
        len_seq = len(self._seq)
        if len_seq == LEN_KONAMI_CODE:
            flag = self.compare_seq()
            if flag:
                sleep(0.01)
                print()
                print("KONAMI CODE FOUND")


    def compare_seq(self):
        for i,j in zip(KONAMI_CODE, self._seq):
            if i != j:
                return False
        return True


if __name__ == '__main__':
    kk = KonamiKeyboard()
    print('Type konami code o press ESC to exit ')
    code = Listener(kk.check_konami_code)
    code.start()
    code.join()
