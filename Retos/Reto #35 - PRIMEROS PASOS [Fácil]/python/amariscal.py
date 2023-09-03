# - Haz un "Hola, mundo!"
print ("Hola, mundo!")

# - Crea variables de tipo String, numéricas (enteras y decimales)
name = str()
age = int()
height = float()
is_spanish = bool()

# - Crea una constante.  En python no existen las constante pero se usan variables y "acuerdos"/convención en la nomenclatura
PI = 3.141592

# - Usa un if, else if y else.
age = int (input ("Introduce tu edad: "))

if age <= 3:
    print ("Demasiado pequeño.")
elif age > 3 and age < 13:
    print ("Todavía vas al colegio.")
elif age >= 13 and age < 17:
    print ("Ya vas al instituto, estudias en la ESO.")
else:
    print ("¿A que te dedicas?")

# - Crea estructuras como un array, lista, tupla, set y diccionario.
teams = list ()
teams = ["Betis Betis", "Sevilla FC", "Real Madrid", "Barcelona FC","Atletico de Madrid"]

students = tuple ()
students = ("Alberto Mariscal","José Jaramillo", "Leopoldo Gutierrez", "Jacinto López")

dni = set ()
dni = {"232354344J","656343R","43565434L",}

colegio = dict ()
colegio = {
    "cursos":{1,2,3,4,5,6},
    "nombre":"Colegio El Buen Colegio",
    "profesores":{"José Alonso Gómez","Juan Carlos Calvo","Joaquin Lorenzo Quesadilla","Juan María Bonilla","Fernando Morales Grueso"},
    "Ciudad":"Sevilla",
    "CP":41700,
    "Director":"Francisco León Fernández"
    }

# - Usa un for, foreach y un while.

cities = list ()
cities = ["Sevilla","Cádiz","Huelva","Córdoba","Jaén","Málaga","Granada","Almería"]

# for
for city in cities:
    print ("%s"%(city))

# not foreach in python

# while
i = 0
while i < 10:
    print ("Bucle while con i valor %d"%(i))
    i += 1

# - Crea diferentes funciones (con/sin parámetros y con/sin retorno).

def set_numbers ():
    first_number =float (input("Introduce el primer número: "))
    second_number =float (input("Introduce el segundo número: "))
    return first_number,second_number

def operator_simbol ():
    operator = input ("Selecciona operación + - * / : ")
    while not validate_operation (operator):
        print("No se ha introducido un operador correcto.")
        operator = input ("Selecciona operación + - * / : ")
    return operator

def calculate (numbers,operator):
    match str.lower(operator):
        case "+":
            total = numbers [0] + numbers [1]
            return total
        case "-":
            total = numbers [0] - numbers [1]
            return total
        case "*":
            total = numbers [0] * numbers [1]
            return total
        case "/":
            total = numbers [0] / numbers [1]
            return total

# - Crea una clase.
class Pet:
    def __init__(self,name,identicador,dni_propietario): # def init self == class constructors
        self.name = name
        self.identificador = identicador
        self.__dni_propietario = dni_propietario
        self.fullname = "{} {} ".format(self.name,self.identificador)
    
    # A class may contain functions
    def walk (self):
        print("%s %s is walking now"%(self.name,self.surname))
    
    # A function that return the DNI (private atribute)
    def get_dni_propietario (self):
        return self.__dni_propietario
    
    # A function to modify the DNI value
    def set_dni_propietario (self,dni):
        self.__dni_propietario = dni

first_p = Pet (name="Peluso",identicador="235gsd432f22",dni_propietario="12345678X")
print ("Nombre: %s. Identificador: %s."%(first_p.name,first_p.identificador))
print (first_p.get_dni_propietario()) # 12345678X

# - Muestra el control de excepciones.
try:
    print ("Estos retos molan y le sumo 35" + 35)
except Exception as error_exception:
    print ("it´s a exception. %s" %(error_exception)) 
else:
    print ("¡A por el reto 36!")
finally:
    print ("Finalizamos el reto.")