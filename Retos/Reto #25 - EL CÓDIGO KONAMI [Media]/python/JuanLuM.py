from pynput import keyboard

state=0					#Guarda el estado del AFD

def checkAFD(tecla):
    
    global state
    
    prev_state = state
      
    match state:
        case 0:				#Estado inicial
            if tecla == keyboard.Key.up:
                state=1
        case 1:
            if tecla == keyboard.Key.up:
                state=2
            else: 
                state=0
        case 2:
            if tecla == keyboard.Key.down:
                state=3
            elif tecla != keyboard.Key.up:
                state=0
        case 3:
            if tecla == keyboard.Key.down:
                state=4
            elif tecla == keyboard.Key.up:
                state=1
            else:    
                state=0
        case 4:
            if tecla == keyboard.Key.left:
                state=5
            elif tecla == keyboard.Key.up:
                state=1
            else:   
                state=0
        case 5:
            if tecla == keyboard.Key.right:
                state=6
            elif tecla == keyboard.Key.up:
                state=1
            else:   
                state=0
        case 6:
            if tecla == keyboard.Key.left:
                state=7
            elif tecla == keyboard.Key.up:
                state=1
            else:   
                state=0
        case 7:
            if tecla == keyboard.Key.right:
                state=8
            elif tecla == keyboard.Key.up:
                state=1
            else:   
                state=0
        case 8:
            if tecla == keyboard.KeyCode.from_char('b'):
                state=9
            elif tecla == keyboard.Key.up:
                state=1
            else:   
                state=0
        case 9:
            if tecla == keyboard.KeyCode.from_char('a'):
                state=10
            elif tecla == keyboard.Key.up:
                state=1
            else:   
                state=0
        case 10:			#Estado final
            if tecla == keyboard.Key.enter:
                print("CODIGO KONAMY INTRODUCIDO. MENSAJE DESBLOQUEADO!!!!!!")
                print(" .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.")
                print("| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
                print("| |  ___  ____   | || |     ____     | || | ____  _____  | || |      __      | || | ____    ____ | || |     _____    | |")
                print("| | |_  ||_  _|  | || |   .'    `.   | || ||_   \|_   _| | || |     /  \     | || ||_   \  /   _|| || |    |_   _|   | |")
                print("| |   | |_/ /    | || |  /  .--.  \  | || |  |   \ | |   | || |    / /\ \    | || |  |   \/   |  | || |      | |     | |")
                print("| |   |  __'.    | || |  | |    | |  | || |  | |\ \| |   | || |   / ____ \   | || |  | |\  /| |  | || |      | |     | |")
                print("| |  _| |  \ \_  | || |  \  `--'  /  | || | _| |_\   |_  | || | _/ /    \ \_ | || | _| |_\/_| |_ | || |     _| |_    | |")
                print("| | |____||____| | || |   `.____.'   | || ||_____|\____| | || ||____|  |____|| || ||_____||_____|| || |    |_____|   | |")
                print("| |              | || |              | || |              | || |              | || |              | || |              | |")
                print("| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |")
                print(" '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' ")
                state=0
            elif tecla == keyboard.Key.up:
                state=1
            else:   
                state=0
    print("\u03B4("+str(prev_state)+", "+str(tecla)+") = "+str(state))  #imprime la función de transición
	
def exit(tecla):			
    if tecla == keyboard.KeyCode.from_char('q'):
        return False

with keyboard.Listener(checkAFD, exit) as listener:
	listener.join()
