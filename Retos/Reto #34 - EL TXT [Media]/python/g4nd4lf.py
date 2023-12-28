#Abrir un fichero de texto 
#Leer su contenido
import os
#check if file exists
if os.path.isfile('text.txt'):
    option = input('File exists, do you want to delete it and create a new one or Append to it? [d/A]: ')
    print()
    option = option.lower()
    if option == 'd':
        with open('text.txt', 'w') as f:
            new_text = input('Input text to write to file:\n')
            print()
            f.write(new_text+'\n')
            f.close()
    elif option == 'a' or option =='':
        with open('text.txt', 'r') as f:
            #read file:
            text = f.read()
            f.close()
            print("Texto existente: ")            
            print(text)
        with open('text.txt', 'a') as f:
            new_text = input('Input text to append to file:\n')
            print()
            f.write(new_text+'\n')
            f.close()
else:
    #create file
    print("New file created.\n")
    with open('text.txt', 'w') as f:
        new_text = input('Input text to write to file:\n')
        print()
        f.write(new_text+'\n')
        f.close()

with open('text.txt', 'r') as f:
            text = f.read()
            f.close()
            print("Texto resultante: ")
            print(text)