import random, os, webbrowser

#Creado el 19/10/2023 por JuanG3D
print(" Reto #41 - LA CASA ENCANTADA ")
print("""Este es mi primer reto para el canal de Mouredev
El juego trata de caminar por una casa 🏚️ y encontrar unos dulces 🍭.
Empiezas con 4 vidas ❤️, y si fallas alguna pregunta, perderás una vida, así por la cara.
Y hay un 10% de posibilidades de que te encuentres con un
amistoso fantasma 👻 que te quitará una vida y te hará dos preguntas.
Las preguntas son de la misma temática que la del creador del reto, o sea, de programación.
Así que no le pongas este juego a tu abuela de 90 años, porque le va a explotar la cabeza.
Espero que te lo pases bien con el juego.
NOTA: El juego está creado en Python, pero no te fíes mucho del
código porque no soy ningún crack de la programación.""")
input('Dale a cualquier tecla para comenzar el juego, muahaha!\t')
os.system('cls')

# Creando array de la casa encantada
hauntedHouse = []
for x in range(4):
  for y in range(4):
    hauntedHouse.append((x, y))

# Creando una puerta en una de las 4 esquinas de la casa
door = random.choice([(0,0), (0,3), (3,0), (3,3)])

# Creando la habitacion de los dulces en una posición random alejada de la puerta
candyArr = []
op1, op2 = "", ""
x = door[0]
y = 3 if door[1]<1 else 0
op1 = "+" if door[0]<1 else "-"
op2 = "+" if door[1]>1 else "-"
for i in range(4):
  candyArr.append((eval(str(x)+op1+str(i)), y))
for j in range(3):
  candyArr.append((candyArr[3][0], eval(str(y)+op2+str(j)+op2+str(1))))
candy = random.choice(candyArr)
iVidas = 4

# Dibujando la casa encantada
dulces = "⬜️"
puerta = "🚪" 
habitacion = "⬜️"
vidas = "❤️"
cabeza = ["💀", "🤕", "🤒", "🥴", "😀"]

row = ""
posActual = door
for i in range(4):
  for j in range(4):
    if i == door[0] and j == door[1]:
      row += puerta
    elif i == candy[0] and j == candy[1]:
      row += dulces
    elif i == posActual[0] and j == posActual[1]:
      row += cabeza[iVidas]
    else:
      row += habitacion
  row += "\n"
print(vidas * iVidas)
print(row)
questionArr = ["¿Para qué sirve el @ en Python?",
               "¿Con qué lenguaje se está imprimiendo el siguiente Hola Mundo?\n\techo \"Hola Mundo\";",
               "¿Cuál de estos lenguajes es el más antiguo?",
               "¿Cuál de estos lenguajes es el más moderno?",
               "¿Cómo se llama el primer virus informático de la historia?",
               "¿Cómo se imprime Hola Mundo usando Ruby?",
               "¿Qué lenguaje de programación creó Steve Jobs?",
               "¿En qué lenguaje está escrito WhatsApp?",
               "¿Cómo se obtiene la longitud de un array \"miArray\" en Lua?",
               "¿En qué lenguaje está escrito BitTorrent?",
               "¿De qué tipo sería la variable const = 4.5 en JavaScript?",
               "¿Qué resultado se obtendría al hacer Console.WriteLine(\"12\" + \"34\"); en C#?",
               "¿Qué resultado se obtendría en Java al hacer:\n   boolean valor = false;\n   if(valor = true){\n      System.out.println(\"Es true\");\n   }\n   else{\n      System.out.println(\"No es true\");\n}",
               "¿En qué lenguaje está inspirado C#?",
               "¿Cuál de los siguientes lenguajes no es interpretado?",
               "¿Cuál de los siguientes lenguajes no es compilado?",
               "¿Java es un lenguaje compilado o interpretado?",
               "¿Qué pasa si en C# hacemos:\n   for(byte i = 0; i < 300; i++){\n      Console.WriteLine(i);\n   }",
               "¿Qué resultado dará esta instrucción de Kotlin:\n   println(Math.floor(3.1416))",
               "¿Cómo se añade un nuevo item al ArrayList \"miLista\" en C#?",
               "¿Cómo de grande puede ser un número de tipo Int32?",
               "¿Cuántos bits son 1 byte?",
               "Si a una variable le ponemos el nombre MiVariableDeEjemplo, ¿qué caso estamos usando?",
               "¿Cómo podemos insertar en Kotlin una variable \"val edad = 25\" dentro de un string para imprimirlo en pantalla?",
               "¿Cómo se comentan múltiples líneas en Erlang?",
               "¿Qué se imprimirá en pantalla si escribimos ésto en C++?\n   int valor = 5;\n   std::cout << &valor;",
               "¿Cómo se llama esta estructura en TypeScript?\n   personaVIP ? '2.00€' : '10.00€';",
               "¿Qué se imprimirá en pantalla si en Rust hacemos ésto:\n   let numero = 10;\n   numero = 12;\n   println!(\"{}\", numero);",
               "¿Qué significa en Pascal lo siguiente?\n   valor := 1;",
               "¿Cuál fue el primer lenguaje de programación orientado a objetos?"]
posiblesRespuestas = ["A: Sirve para enlazar subatributos\nB: No sirve pa' ná. ¿Acaso has visto un @ en Python alguna vez?\nC: Sirve como prefijo para decorar funciones.\nD: Sirve para calcular la inversa de una matriz adjunta.",
                      "A: PHP\nB: Clojure\nC: C++\nD: Rust",
                      "A: Perl\nB: Python\nC: Erlang\nD: Objective-C",
                      "A: Dart\nB: Zig\nC: Kotlin\nD: Haxe",
                      "A: Melissa\nB: Stoned\nC: Creeper\nD: Lovebug\n",
                      "A: puts Hola Mundo\nB: print('Hola Mundo');\nC: System.out.println(\"Hola Mundo\");\nD: console.log(\"Hola Mundo\");",
                      "A: PostScript\nB: Turbo Pascal\nC: Smalltalk\nD: No creó nunca ningún lenguaje.",
                      "A: C#\nB: Erlang\nC: Scala\nD: ActionScript",
                      "A: miArray->length\nB: miArray.length()\nC: #miArray\nD: len(miArray)",
                      "A: Python\nB: C++\nC: JavaScript\nD: Ruby",
                      "A: bigint\nB: object\nC: float\nD: number",
                      "A: 12 + 34\nB: 1234\nC: 46\nD: Runtime Exception",
                      "A: \"No es true\"\nB: \"error: cannot find symbol\"\nC: \"Es true\"\nD: \"Es más o menos true\"",
                      "A: En JavaScript\nB: En C++\nC: En Java\nD: En Pascal",
                      "A: Go\nB: Python\nC: Lua\nD: PHP",
                      "A: Haskell\nB: Rust\nC: Erlang\nD: JavaScript",
                      "A: Interpretado\nB: Compilado e interpretado\nC: Desfragmentado\nD: Compilado",
                      "A: Que va a ignorar el bucle for y no imprimirá nada.\nB: Que va a imprimir números desde 0 hasta 300.\nC: Que se va a quedar encerrado en el bucle para toda la eternidad.\nD: Que va a imprimir números desde 0 hasta 299.",
                      "A: 3.0\nB: 4\nC: 0.0\nD: 3",
                      "A: miLista.append(\"item\");\nB: miLista.insert(\"item\");\nC: miLista.push(\"item\");\nD: miLista.Add(\"item\");",
                      "A: Entre cinco y diez millones.\nB: Poco más de dos mil millones.\nC: Tropecientos millones.\nD: Un millón y medio, a ojo de buen cubero.",
                      "A: 32\nB: 2\nC: 8\nD: 64",
                      "A: Pascal Case\nB: Snake Case\nC: Kebab Case\nD: Camel Case",
                      "A: print(\"Tengo {edad} años.\")\nB: print(\"Tengo \"..edad..\" años.\")\nC: print(\"Tengo @edad años.\")\nD: print(\"Tengo $edad años.\")",
                      "A: /* Comentario múltiple */\nB: Erlang no tiene comentario múltiple\nC: --[[ Comentario múltiple ]]\nD: {- Comentario múltiple -}",
                      "A: Error: invalid type argument\nB: 5.0\nC: Algo como \"0x7ffe932f5afc\" (dirección de memoria)\nD: 5",
                      "A: Operador ternario\nB: Condicional compuesto\nC: Switch simple\nD: Operador de línea",
                      "A: 10\nB: Error: overwritten before being read\nC: 12\nD: Error: cannot assign twice to immutable variable",
                      "A: A la variable \"valor\" se la divide por 1.\nB: Se crea una variable \"valor\" con valor 1.\nC: Se le suma 1 a la variable \"valor\".\nD: Syntax error.",
                      "A: Pascal\nB: Cobol\nC: Simula 67\nD: Fortran"]
fantasmasList = ["¡OJO! Un amistoso fantasma 👻 te da la bienvenida con un puñetazo en el pecho y con dos preguntas para que te rebanes un poco los sesos:",
                 "¡ATENCIÓN! En la habitación hay un cacho fantasma 👻 que te saluda con una patada en la canilla y con dos preguntas para que te explote un poco el cerebro:",
                 "¡CUIDADO! Un fantasma 👻 te sorprende con un palo en las costillas y con dos preguntas para que sufras un poco:",
                 "¡OJO! Un risueño fantasma 👻 te saluda con un navajazo en la ingle, y quiere aprovechar para preguntarte dos cosas porque mañana tiene examen de informática:",
                 "¡ATENCIÓN! Un fantasma 👻 con crisis nerviosa te encaja un cuchillazo en el riñón y te quiere preguntar dos cositas",
                 "¡CUIDADO! Te encuentras con un fantasma 👻 que te arranca una oreja de un bocado y te hace dos preguntas así, sin venir mucho a cuento.",
                 "¡OJO! Un fantasma 👻 muy divertido te clava un picahielos en la rodilla y te hace dos preguntas sin mucho sentido:",
                 "¡ATENCIÓN! Un fantasma 👻 muy gracioso te quema un ojo con un cigarro, y procede a preguntarte dos dudillas que tiene de programación:",
                 "¡CUIDADO! Te tropiezas con un fantasma 👻 que te sacude un pepinazo en el hígado y te susurra estas dos preguntas:",
                 "¡OJO! Un fantasmita 👻 se presenta con una ensalada de puñetazos y un par de preguntas que no tienen nada que ver con su profesión de fantasma:"]
respuestas = ["C", "A", "D", "B", "C", "A", "D", "B", "C", "A", "D", "B", "C", "C", "A", "D", "B", "C", "A", "D", "B", "C", "A", "D", "B", "C", "A", "D", "B", "C"]
respAcertada = ("Menudo churro te has pegao, reconócelo.", "No sé cómo lo has hecho... pero te estaré vigilando.", "Vaya potra... vaya potra....", "Has tenido suerte... por ahora.", "Anda, tira... que no sé ni cómo has acertado eso.", "Has buscado la respuesta en el ChatGPT, ¿Verdad?", "Tu primo el friki te ha soplado la respuesta, seguro.", "La suerte del principiante... Anda, tira, tira.", "Te has salvado por los pelos, no sé ni cómo.", "Vaya suerte macanuda que me llevas.", "¿Cómo lo has hecho? Anda, sácate la chuleta del bolsillo, que te he visto.")

while True:
  preguntas = 1
  bPregunta= False
  n = input("¿A dónde quieres ir? N S E O  ")
  if n.lower() == "n" and (posActual[0]-1, posActual[1]) in hauntedHouse:
      posActual = (posActual[0]-1, posActual[1])
      continua = True
  elif n.lower() == "s" and (posActual[0]+1, posActual[1]) in hauntedHouse:
      posActual = (posActual[0]+1, posActual[1])
      continua = True
  elif n.lower() == "e" and (posActual[0], posActual[1]+1) in hauntedHouse:
      posActual = (posActual[0], posActual[1]+1)
      continua = True
  elif n.lower() == "o" and (posActual[0], posActual[1]-1) in hauntedHouse:
      posActual = (posActual[0], posActual[1]-1)
      continua = True
  else:
    print("No puedes ir por ahí")
    continua = False

  if continua:
    if posActual == candy:
      print("GANASTE! Encontraste las chuches! 👍\nHala...lárgate a comértelas por ahí, para que te salga caries y se te pudran, muahahaha!\nGracias por jugar al juego de JuanG3D\nSi quieres ver sus diseños 3D superchulos, visita su página web https://sketchfab.com/juang3d 👍\nNos vemos, crack!")
      z = input('Dale a Enter para salir\t')
      break
    elif posActual == door:
      print("Anda! Aquí está la puerta. Pero no pienso salir sin las chuches.")
    else:
      valorRandom = random.randint(0,100)
      if valorRandom <= 10:
        preguntas += 1
        iVidas -= 1
      bPregunta = True

    row = ""
    for i in range(4):
      for j in range(4):
        if i == door[0] and j == door[1]:
          row += puerta
        elif i == candy[0] and j == candy[1]:
          row += dulces
        elif i == posActual[0] and j == posActual[1]:
          row += cabeza[iVidas]
        else:
          row += habitacion
      row += "\n"
    os.system('cls')
    print(vidas * iVidas)
    print(row)
    if iVidas < 1:
      print("MUAHAHAHAHA! Has perdido como vil rata. Ahora vendrá un zombie podrido a absorberte el tuétano.\nMientras, puedes seguir practicando programación, para que no vuelva a pasarte lo mismo la próxima vez.\nHala. Nos vemos.")
      input('Dale a cualquier tecla para salir\t')
      exit(0)
    bFantasma = False
    while preguntas > 0:
      if preguntas > 1:
        print(random.choice(fantasmasList))
        bFantasma = True
      elif bFantasma:
        bFantasma = False
      else:
          print("\n Encuentras una habitación con el siguiente enigma:")
      if bPregunta:
        preguntaNum = random.randint(0, len(questionArr)-1)
        print(questionArr[preguntaNum])
        print(posiblesRespuestas[preguntaNum])
        respuesta = input().upper()
        while respuesta != "A" and respuesta != "B" and respuesta != "C" and respuesta != "D":
          print("¿A qué tecla le has dado? Anda, responde bien")
          respuesta = input().upper()
        if respuesta == respuestas[preguntaNum]:
            print(random.choice(respAcertada))
            questionArr.pop(preguntaNum)
            posiblesRespuestas.pop(preguntaNum)
            respuestas.pop(preguntaNum)
        else:
          iVidas -= 1
          row = ""
          for i in range(4):
            for j in range(4):
              if i == door[0] and j == door[1]:
                row += puerta
              elif i == candy[0] and j == candy[1]:
                row += dulces
              elif i == posActual[0] and j == posActual[1]:
                row += cabeza[iVidas]
              else:
                row += habitacion
            row += "\n"
          print("FALLASTE!! Muahahaha!")
          print(vidas * iVidas)
          print(row)
      preguntas -= 1
    bPregunta = False
