"""
/*
 * Escribe un !Hola Mundo! en todos los lenguajes de programación que puedas.
 * Seguro que hay algún lenguaje que te llama la atención y nunca has utilizado,
 * o quizás quieres dar tus primeros pasos... ¡Pues este es el momento!
 *
 * A ver quién se atreve con uno de esos lenguajes que no solemos ver por ahí... 
 */
"""

AMARILLO_I = "\033[3;38;2;243;228;57;49m"
ROSA_B = "\033[1;38;2;241;129;243;49m"
RESET = "\033[0m"


print(f"{ROSA_B}!{RESET}{AMARILLO_I}Hola Mundo{RESET}{ROSA_B}!{RESET}")