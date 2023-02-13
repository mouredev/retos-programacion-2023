'''
/*
 * Escribe un !Hola Mundo! en todos los lenguajes de programación que puedas.
 * Seguro que hay algún lenguaje que te llama la atención y nunca has utilizado,
 * o quizás quieres dar tus primeros pasos... ¡Pues este es el momento!
 *
 * A ver quién se atreve con uno de esos lenguajes que no solemos ver por ahí... 
 */
'''
def reto5(nombre=None):
    if nombre==None or nombre=='':
        nombre='!'
    else:
        nombre=' '+nombre+'!'
    return 'Hola Mundo'+ nombre


if __name__=='__main__':
    myName = input('Escribe tu nombre: \n')
    print(reto5(myName))