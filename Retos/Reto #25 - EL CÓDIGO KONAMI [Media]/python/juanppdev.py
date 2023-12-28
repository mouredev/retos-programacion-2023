import keyboard

codigo_konami = ["up", "up", "down", "down", "left", "right", "left", "right", "B", "A"]
progreso = 0

def comprobar_codigo(e):
  global progreso
  
  if e.name == codigo_konami[progreso]:
    progreso += 1
    if progreso == len(codigo_konami):
      print("Codigo Konami introducido correctamente")
      progreso = 0
  else:
      progreso = 0
      
keyboard.on_press(comprobar_codigo)
keyboard.wait('esc')