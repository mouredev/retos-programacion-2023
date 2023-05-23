from statistics import mean

def TextAnalizer(Sentences):

    no_dot=Sentences.replace(".","")
    oraciones = Sentences.split(".")
    palabras =no_dot.split(" ")
    palabros=list(map(len,palabras)) # CountListPalabras = [len(palabra) for palabra in palabras]
    
    countWords=len(palabras)
    countSentences=len(oraciones)
    avgWords=mean(palabros)
    maxstring=max(palabros)

    maxwords=list()
    for index,palabra in enumerate(palabros):
        if maxstring==palabra:
            maxwords.append(palabras[index]) # print(palabras[index])
    print(f'''Numero de palabras : {countWords}\nNumero de Oraciones : {countSentences}\nMedia de palabras : {avgWords}\nMaxWords : {maxwords}''')

def main():
    #texto='''Había una vez un gato llamado Tito que vivía en una casa pequeña. Un día, Tito decidió salir a explorar el mundo. En su aventura, conoció a muchos amigos y vivió muchas experiencias emocionantes.'''
    #texto='''Era una noche oscura y tormentosa. El viento aullaba y las ramas golpeaban las ventanas. Él estaba solo en casa, leyendo un libro de misterio. De repente, escuchó un ruido en el ático. Subió las escaleras con una linterna y abrió la puerta. Lo que vio le heló la sangre: una figura encapuchada con una hoz en la mano le sonreía maliciosamente. Era la muerte, que había venido a buscarlo.'''
    #texto='''Un hombre entra en una tienda de mascotas con la intención de comprar un loro. Se acerca a la jaula donde hay varios ejemplares de diferentes colores y tamaños. El dependiente le dice que el precio varía según la inteligencia y la habilidad del ave para hablar. El hombre señala al loro más grande y hermoso, que tiene un plumaje verde y rojo. El dependiente le dice que ese loro cuesta 500 euros y que sabe decir más de 100 palabras y frases en varios idiomas. El hombre se queda impresionado, pero dice que es demasiado caro para él.'''
    texto='''Era una noche oscura y tormentosa. Un hombre encapuchado corría por las calles vacías, esquivando los relámpagos y el agua que caía a raudales. Llevaba una mochila en la espalda y un objeto brillante en la mano. Era un dispositivo que había robado de un laboratorio secreto, donde trabajaba como científico. El dispositivo era capaz de abrir portales a otras dimensiones, y el hombre quería usarlo para escapar de sus perseguidores.'''        
    TextAnalizer(texto)

if __name__=="__main__":
    main()