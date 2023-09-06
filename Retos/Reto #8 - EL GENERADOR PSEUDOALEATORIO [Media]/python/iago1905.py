'''
Crea un generador de números pseudoaleatorios entre 0 y 100.
- No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
Es más complicado de lo que parece...

'''
for i in range(101):
    print(id(i)%101)

