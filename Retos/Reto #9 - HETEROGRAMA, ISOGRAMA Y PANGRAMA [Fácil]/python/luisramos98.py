#!/usr/bin/env python3

'''
* Crea 3 funciones, cada una encargada de detectar si una cadena de
* texto es un heterograma, un isograma o un pangrama.
* - Debes buscar la definición de cada uno de estos términos.
'''

import string
import re 
from unidecode import unidecode

class HeteroIsoPangrama:

    def __init__(self,cadena):
        self.cadena = re.sub(r'[\d\s]+','',unidecode(cadena.lower()))
        self.tipografias = []
        self.caracteres = {}

    def contar_caracteres(self):
        for i in self.cadena:
            if i in self.caracteres:
                self.caracteres[i] += 1 
            else:
                self.caracteres[i] = 1

    def is_heterograma(self) -> bool: 
        for i in self.caracteres.values():
            if i > 1:
                return False
        return True

    def is_isograma(self) -> bool:
        contador = 0
        for i in self.caracteres.values():
            if contador == 0:
                contador = i 
            if not i == contador:
                return False
        return True

    def is_pangrama(self) -> bool:
        abc = string.ascii_lowercase
        conf_abc = set()
        for i in self.cadena:
            conf_abc.add(i)
        if not abc == ''.join(sorted(conf_abc)):
            return False        
        return True

    def mostrar_tipografias(self):
        print(f'\n[+] La cadena {self.cadena} es:')
        for tipografia in self.tipografias:
            print(f'\t- {tipografia}')

    def detector(self):
        self.contar_caracteres() 
        if self.is_heterograma():
            self.tipografias.append('Heterograma')
        if self.is_isograma():
            self.tipografias.append('Isograma')
        if self.is_pangrama():
            self.tipografias.append('Pangrama')
        if not self.tipografias:
            self.tipografias.append('[!] No soy ni heterograma, ni isograma, ni pangrama')
    
    def start(self):
        self.detector()
        self.mostrar_tipografias()

if __name__ == '__main__':
    detector = HeteroIsoPangrama("Mamá")
#    detector = HeteroIsoPangrama('Ave maria purisima')
    detector.start()

