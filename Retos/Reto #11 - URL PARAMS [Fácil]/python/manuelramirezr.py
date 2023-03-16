import re
import unittest

# Valid url
def validUrl(url):
    pattern = re.compile(r"^https?:\/\/(www\.)?[\w-]+\.[\w-]+(\.[\w-]+)?\/?(\?[\w-]+=[\w-]+(&[\w-]+=[\w-]+)*)?$")
    if pattern.match(url):
        return True
    else:
        return False
# Get parameters from url
def getParameters(url):
    pattern = re.compile(r"[\w-]+=[\w-]+(&[\w-]+=[\w-]+)*")
    if pattern.search(url):
        parameters = pattern.search(url).group()
        return parameters
    else:
        return None
    
# Get values from url
def getValues(url):
    parameters = getParameters(url)
    if parameters:
        values = parameters.split("&")
        for i in values:
            values[values.index(i)] = i.split("=")[1]
        return values
    else:
        return None
    
# Funtion to extract values from url with the requirement
# Dada una URL con parámetros, crea una función que obtenga sus valores.
## * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
##
##  Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
##  los parámetros serían ["2023", "0"]  
   
def extractValues(url):
    if validUrl(url):
        values = getValues(url)
        print(values)
        return values
    else:
        print("Invalid url")
        return None

# Unit test to valid url
class TestValidUrl(unittest.TestCase):
    def test_valid_url(self):
        self.assertTrue(validUrl("https://www.google.com/"))
        self.assertTrue(validUrl("https://retosdeprogramacion.com?year=2023&challenge=0"))
        
    def test_invalid_url(self): 
        self.assertFalse(validUrl("www.google.com"))
        self.assertFalse(validUrl("www.google"))
        self.assertFalse(validUrl("google.com"))
        self.assertFalse(validUrl("google"))
        self.assertFalse(validUrl("https://www.google.com/?"))
        self.assertFalse(validUrl("https://www.google.com/?&"))
        self.assertFalse(validUrl("https://www.google.com/?&="))
        self.assertFalse(validUrl("https://www.google.com/?&=a"))
        self.assertFalse(validUrl("https://www.google.com/?&=a&"))
        self.assertFalse(validUrl("https://www.google.com/?&=a&="))
        self.assertFalse(validUrl("https://www.google.com/?&=a&=b"))
        self.assertFalse(validUrl("https://www.google.com/?&=a&=b&"))
        self.assertFalse(validUrl("https://www.google.com/?&=a&=b&="))
        self.assertFalse(validUrl("https://www.google.com/?&=a&=b&=c"))
        self.assertFalse(validUrl("https://www.google.com/?&=a&=b&=c&"))
        self.assertFalse(validUrl("https://www.google.com/?&=a&=b&=c&="))
    
    def test_get_parameters(self):
        self.assertEqual(getParameters("https://www.google.com/"), None)
        self.assertEqual(getParameters("https://retosdeprogramacion.com?year=2023&challenge=0"), "year=2023&challenge=0")
        self.assertEqual(getParameters("https://retosdeprogramacion.com/search?year=2023"), "year=2023")
    
    def test_get_values(self):
        self.assertEqual(getValues("https://www.google.com/"), None)
        self.assertEqual(getValues("https://retosdeprogramacion.com?year=2023&challenge=0"), ["2023", "0"])
        self.assertEqual(getValues("https://retosdeprogramacion.com/search?year=2023"), ["2023"])

    def test_extract_values(self):
        self.assertEqual(extractValues("https://retosdeprogramacion.com?year=2023&challenge=0"), ["2023", "0"])
        


if __name__ == "__main__":
    unittest.main()


