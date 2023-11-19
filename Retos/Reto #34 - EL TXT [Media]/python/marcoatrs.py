import signal
import sys
from pathlib import Path


def write_line(file_path: Path, line: str):
    with open(file_path, "a") as txt:
        txt.write(f"{line}\n")


def main():
    file_path = Path("text.txt")
    if file_path.exists():
        res = ""
        while res not in ["s", "n"]:
            res = input("El archivo ya existe, borrar contenido (s,n): ").lower()

        if res == "s":
            file_path.unlink()
    file_path.touch(exist_ok=True)
    with open(file_path, "r") as txt:
        print(txt.read())
    while True:
        write_line(file_path, input())


if __name__ == "__main__":
    signal.signal(signal.SIGINT, lambda s, f: sys.exit())
    main()
