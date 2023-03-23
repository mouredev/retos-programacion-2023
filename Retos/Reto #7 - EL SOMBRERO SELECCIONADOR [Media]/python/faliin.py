print("🎩:¡Bienvenido al programa del Sombrero Seleccionador de Hogwarts! Para determinar en qué casa de Hogwarts pertenecerás, te haré algunas preguntas.")
print("🎩: 1. ¿Qué cualidad valoras más en ti mismo?")
print("   1) Coraje")
print("   2) Astucia")
print("   3) Lealtad")
print("   4) Inteligencia")
respuesta1 = int(input())

print("🎩: 2. ¿Qué habilidad te gustaría tener?")
print("   1) Volar")
print("   2) Controlar mentes")
print("   3) Cambiar de forma")
print("   4) Leer la mente")
respuesta2 = int(input())

print("🎩: 3. ¿Qué tipo de personas admiras más?")
print("   1) Aquellas que se arriesgan por lo que creen")
print("   2) Aquellas que logran sus objetivos a cualquier costo")
print("   3) Aquellas que se preocupan por los demás")
print("   4) Aquellas que tienen un gran conocimiento y sabiduría")
respuesta3 = int(input())

print("🎩: 4. ¿Qué tipo de animales te gustan más?")
print("   1) Leones")
print("   2) Serpientes")
print("   3) Tejones")
print("   4) Águilas")
respuesta4 = int(input())

print("5. ¿Qué ambiente prefieres?")
print("   1) Aventura y acción")
print("   2) Intriga y secretos")
print("   3) Armonía y compañerismo")
print("   4) Conocimiento y aprendizaje")
respuesta5 = int(input())

print("🎩: ¡Gracias por responder las preguntas! Ahora, basándonos en tus respuestas, el Sombrero Seleccionador ha determinado que tu casa es...  redoble de tambores")

if respuesta1 == 1 and respuesta2 == 1 and respuesta3 == 1:
    print("¡Felicidades! Has sido seleccionado para la casa de Gryffindor🦁.")
elif respuesta1 == 2 and respuesta2 == 2 and respuesta4 == 2:
    print("¡Felicidades! Has sido seleccionado para la casa de Slytherin🐍.")
elif respuesta1 == 3 and respuesta3 == 3 and respuesta5 == 3:
    print("¡Felicidades! Has sido seleccionado para la casa de Hufflepuff🦡.")
else:
    print("¡Felicidades! Has sido seleccionado para la casa de Ravenclaw🦅.")

print("🎩:¡Que tengas un gran año escolar en Hogwarts!")
