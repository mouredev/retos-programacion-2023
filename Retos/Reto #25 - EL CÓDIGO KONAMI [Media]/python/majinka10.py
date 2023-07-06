import msvcrt

konami = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'a', 'b', 'enter']
current_sequence = []

while True:
  if msvcrt.kbhit():
    key = msvcrt.getch()
    if key == b'\xe0':
      # Tecla especial, leer siguiente byte
      key = msvcrt.getch()
      if key == b'H':
          current_sequence.append('up')
      elif key == b'P':
          current_sequence.append('down')
      elif key == b'M':
          current_sequence.append('right')
      elif key == b'K':
          current_sequence.append('left')
    elif key in (b'a', b'A'):
        current_sequence.append('a')
    elif key in (b'b', b'B'):
        current_sequence.append('b')
    elif key == b'\r':
        current_sequence.append('enter')
        
    if current_sequence[-len(konami):] == konami:
        print('Código Konami ingresado correctamente!')
        break
