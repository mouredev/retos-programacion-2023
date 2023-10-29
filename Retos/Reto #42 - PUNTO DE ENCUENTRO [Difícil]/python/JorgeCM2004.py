class Object():
    position: tuple
    speed: tuple

def ask_position(obj: str) -> tuple:
    coorx = int(input(f"Coordenada x del objeto {obj}: "))
    coory = int(input(f"Coordenada y del objeto {obj}: "))
    return (coorx, coory)

def ask_speed(obj: str) -> tuple:
    speedx = int(input(f"Velocidad en el eje x del objeto {obj}: "))
    speedy = int(input(f"Velocidad en el eje y del objeto {obj}: "))
    return (speedx, speedy)

def main() -> None:
    objA = Object(position = ask_position("A"), speed = ask_speed("A"))
    objB = Object(position = ask_position("B"), speed = ask_speed("B"))
    
if __name__ == "__main__":
    main()