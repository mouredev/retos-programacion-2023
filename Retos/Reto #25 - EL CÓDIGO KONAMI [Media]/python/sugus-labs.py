from pynput import keyboard

# KONAMI CODE
# ['UP, UP, DOWN, DOWN, LEFT, RIGHT, LEFT, RIGHT, B, A, ENTER]

def on_press(key):
    try:
        #print(key.char)
        event_list.append(key.char.upper())
    except AttributeError:
        #print(str(key).lower().replace("key.", ""))
        event_list.append(str(key).upper().replace("KEY.", ""))
    if event_list[-11:] == konami_code:
        print("You WIN!")
        return False
    
def on_release(key):
    #print(f'{key} released')
    if key == keyboard.Key.esc:
        return False

if __name__ == "__main__":
    
    event_list = []
    konami_code = [
        "UP", "UP", "DOWN", "DOWN", 
        "LEFT", "RIGHT", "LEFT", "RIGHT", 
        "B", "A", "ENTER"]
    
    with keyboard.Listener(
        on_press = on_press, 
        on_release = on_release
        ) as listener:
        
        listener.join()
        #print(event_list)
        
