aurebesh = {
    "a": "aurek",
    "b": "besh",
    "c": "cresh",
    "d": "dorn",
    "e": "esk",
    "f": "forn",
    "g": "grek",
    "h": "herf",
    "i": "isk",
    "j": "jenth",
    "k": "krill",
    "l": "leth",
    "m": "mern",
    "n": "nern",
    "o": "osk",
    "p": "peth",
    "q": "qek",
    "r": "resh",
    "s": "senth",
    "t": "trill",
    "u": "usk",
    "v": "vev",
    "w": "wesk",
    "x": "xesh",
    "y": "yirt",
    "z": "zerek"
}


def spanish2aurebesh(text: str):
    aurebesh_chars = []
    for t in text:
        aurebesh_chars.append(aurebesh.get(t, t))
    return "".join(aurebesh_chars)


print(spanish2aurebesh("Hola que tal"))
