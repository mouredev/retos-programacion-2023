# Hello world
print('¡Hola Mundo!')

# Variables
Numeric <- 4
String <- 'Esto es un string' #character
Double <- 3.3
Boolean <- TRUE
Factor <- factor('Hombre')
Date <- as.Date('2023-07-03')

# Constant
CONSTANT <- pi

# Conditionals
if (Numeric < CONSTANT){
    Boolean <- FALSE
} else if (CONSTANT > Double) {
   String <- 'La constante es mayor que el Double'
} else {
   print(paste('El día que hice este programa era', Date))
}

# Structures
Vector <- c(1, 'casa', pi, FALSE)

Tabla <- data.frame(col1 = 1:10, col2 = 11:20)

Lista <- list(value1 = Vector, value2 = Tabla)

Matriz1 <- matrix(Vector, nrow = 2) #Esto se puede volver más complejo

Matriz2 <- matrix(0, nrow = 2, ncol = 3) 

# Loops
for (i in 1:4){
    print(paste('Foreach - Esta es la vuelta', i))
}

i <- 0
while(i < 4){
    print(paste('While - Esta es la vuelta', i))
    i <- i + 1
}

# Functions
saludo <- function() {
    print('Hola, ¿cómo estás?')
}

saludo()

suma <- function(x,y) {
    x + y
}

print(suma(2,2))

# Class S4

    #Definimos la clase student
    setClass("student",
            slots=list(name="character",
                        age="numeric", code="numeric")
            )

    #Definimos una funcion para mostrar los detalles del objeto
    setMethod("show", "student",
            function(object){
                cat(object@name, "\n")
                cat(object@age, "\n")
                cat(object@code, "\n")
            }
            )

    # Definimos una clase que hereda a student (recibe estudiante como atributo)
    setClass("InternationalStudent",
            slots=list(country="character"),
            contains="student"
            )

    # Creamos un estudiante
    student1 <- new("InternationalStudent", name="Adam",
            age=22, code=2210691, country="India")

    show(student1) #LLamamos el metodo del estudiante para mostrar sus datos

# Exceptions
Numeros <- list(1,3,5,'perro',9)

for (i in Numeros) {
   tryCatch({
    print(i**2)
   }, error = function(err) {
    print(paste('Error en la iteracion', i, ':', err$message))
   })
}