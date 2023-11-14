# Retos Semanales ‘23
# Reto #26: TESTING
# MEDIA | Publicación: 26/06/23 | Resolución: 03/06/23
#
# Crea tres test sobre el reto 12: "Viernes 13".
# - Puedes copiar una solución ya creada por otro usuario en
#   el lenguaje que estés utilizando.
# - Debes emplear un mecanismo de ejecución de test que posea
#   el lenguaje de programación que hayas seleccionado.
# - Los tres test deben de funcionar y comprobar
#   diferentes situaciones (a tu elección).

# Autor: Clark - @ClarkCodes
# Fecha de Resolución: 31/07/2023

# Imports
import Reto_12_Viernes13 as Viernes13
import unittest
from assertpy import assert_that
from datetime import date, datetime

# Testing class
class TestViernes13( unittest.TestCase ):
    # Tests
    def test_exit_verifying( self ): # Test #1
        false_cases = ( "a", "b", "c", "x", "y", "z", "abc", "xyz", "hola", "prueba", "testing" ) 
        true_cases = ( "q", "Q" )

        for case in false_cases:
            assert_that( Viernes13.exit_verifier( case ) ).is_false()

        for case in true_cases:
            assert_that( Viernes13.exit_verifier( case ) ).is_true()

    def test_is_month_or_year_valid( self ): # Test #2
        false_cases = ( ( -1, Viernes13.ValidatorType.MONTH ),
                        ( 32, Viernes13.ValidatorType.MONTH ) ,
                         ( 35, Viernes13.ValidatorType.MONTH ),
                          ( 40, Viernes13.ValidatorType.MONTH ),
                           ( 150, Viernes13.ValidatorType.MONTH ),
                            ( -5, Viernes13.ValidatorType.MONTH ),
                             ( -10, Viernes13.ValidatorType.MONTH ),
                              ( -20, Viernes13.ValidatorType.MONTH ),
                               ( -1, Viernes13.ValidatorType.YEAR ),
                                ( -5, Viernes13.ValidatorType.YEAR ),
                                 ( -10, Viernes13.ValidatorType.YEAR ),
                                  ( -20, Viernes13.ValidatorType.YEAR ),
                                   ( 1899, Viernes13.ValidatorType.YEAR ),
                                    ( 1898, Viernes13.ValidatorType.YEAR ), 
                                     ( 1895, Viernes13.ValidatorType.YEAR ),
                                      ( 1890, Viernes13.ValidatorType.YEAR ),
                                       ( 1800, Viernes13.ValidatorType.YEAR ),
                                        ( 1700, Viernes13.ValidatorType.YEAR ),
                                         ( 1500, Viernes13.ValidatorType.YEAR ),
                                          ( 1000, Viernes13.ValidatorType.YEAR ) )
        true_cases = (( 1900, Viernes13.ValidatorType.YEAR ),
                      ( 1901, Viernes13.ValidatorType.YEAR ),
                       ( 1902, Viernes13.ValidatorType.YEAR ),
                        ( 1905, Viernes13.ValidatorType.YEAR ),
                         ( 1910, Viernes13.ValidatorType.YEAR ),
                          ( 1920, Viernes13.ValidatorType.YEAR ),
                           ( 1950, Viernes13.ValidatorType.YEAR ),
                            ( 1980, Viernes13.ValidatorType.YEAR ),
                             ( 1995, Viernes13.ValidatorType.YEAR ),
                              ( 2010, Viernes13.ValidatorType.YEAR ),
                               ( 2020, Viernes13.ValidatorType.YEAR ),
                                ( 2022, Viernes13.ValidatorType.YEAR ),
                                 ( 2023, Viernes13.ValidatorType.YEAR ) )

        for case in false_cases:
            assert_that( Viernes13.is_month_year_valid( *case ) ).is_false()

        for case in true_cases:
            assert_that( Viernes13.is_month_year_valid( *case ) ).is_true()

        for month_number in range( 1, 13 ):
            assert_that( Viernes13.is_month_year_valid( month_number, Viernes13.ValidatorType.MONTH ) ).is_true()

    def test_friday_13_verifier( self ): # Test #3
        false_cases = ( ( 7, 2023 ), ( 5, 2023 ), ( 4, 2023 ), ( 3, 2023 ), ( 4, 2022 ), ( 1, 2022 ), ( 8, 2023 ), ( 9, 2023 ) )
        true_cases = ( ( 1, 2023 ), ( 10, 2023 ) )

        for case in false_cases:
            assert_that( Viernes13.friday_13_verifier( *case ) ).is_false()

        for case in true_cases:
            assert_that( Viernes13.friday_13_verifier( *case ) ).is_true()

# Llamada a la Función Principal usando typer
if __name__ == "__main__":
    unittest.main() 
