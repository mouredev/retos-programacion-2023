import time

# @javierm_p


def metodo_parte_media_del_cuadrado(seed):
    cudrado_seed = seed**2
    _cudrado_seed = str(cudrado_seed)
    if len(_cudrado_seed) < 8:
        _cudrado_seed = ("0" * 9 - len(_cudrado_seed)) + _cudrado_seed
    new_random = int(_cudrado_seed[2:6]) % 101
    return new_random


def rand(seed):
    new_random = (7**5) * seed % (-1 + 2**31)
    new_random = new_random % 101
    return new_random


def randu(seed):
    new_random = (3 + 2**16) * seed % (2**31)
    new_random = new_random % 101
    return new_random


if __name__ == "__main__":
    seed = int(time.time())
    new_random = rand(seed)
    print(new_random)
