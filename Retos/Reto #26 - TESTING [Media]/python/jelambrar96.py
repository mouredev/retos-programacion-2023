#!/usr/bin/python3

"""
# Reto #26: Testing
/*
* Crea tres test sobre el reto 12: "Viernes 13".
* - Puedes copiar una solución ya creada por otro usuario en
*   el lenguaje que estés utilizando.
* - Debes emplear un mecanismo de ejecución de test que posea
*   el lenguaje de programación que hayas seleccionado.
* - Los tres test deben de funcionar y comprobar
*   diferentes situaciones (a tu elección).
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


import unittest


def adridoce_viernes_trece(mes, anio):
    import datetime
    return True if datetime.date(int(anio), int(mes), 13).weekday() == 4 else False


def alberba_viernes_13(year: int, month: int) -> bool:
    # from datetime import datetime
    import datetime
    try:
        return datetime.date(year, month, 13).weekday() == 4
    except:
        return False


def almarro1_friday13(year, month):
    from datetime import date
    return date(year, month, 13).weekday() == 4



class Test (unittest.TestCase):

    LIST_F13 = [
        (2000, 10),
        (2001, 4), 
        (2001, 7),
        (2002, 9),
        (2002, 12),
        (2003, 6),
        (2004, 2),
        (2004, 8),
        (2006, 1),
        (2006, 1),
        (2007, 4),
        (2007, 7),
        (2008, 6),
        (2009, 2),
        (2009, 3),
        (2009, 11),
        (2010, 8),
    ]

    LIST_NF13 = [
        (2000, 11),
        (2001, 5), 
        (2001, 3),
    ]

    def test_adridoce_viernes_trece(self):
        for anio, mes in Test.LIST_F13:
            self.assertTrue(adridoce_viernes_trece(mes, anio), f"{anio}-{mes}")
        for anio, mes in Test.LIST_NF13:
            self.assertFalse(adridoce_viernes_trece(mes, anio), f"{anio}-{mes}")

    def test_alberba_viernes_13(self):
        for anio, mes in Test.LIST_F13:
            self.assertTrue(alberba_viernes_13(anio, mes), f"{anio}-{mes}")
        for anio, mes in Test.LIST_NF13:
            self.assertFalse(alberba_viernes_13(anio, mes), f"{anio}-{mes}")

    def test_almarro1_friday13(self):
        for anio, mes in Test.LIST_F13:
            self.assertTrue(almarro1_friday13(anio, mes), f"{anio}-{mes}")
        for anio, mes in Test.LIST_NF13:
            self.assertFalse(almarro1_friday13(anio, mes), f"{anio}-{mes}")

if __name__ == '__main__':
    unittest.main()

