import random
import string
import secrets

_all = string.ascii_letters + string.digits +  string.punctuation

paswd = "".join(secrets.choice(_all) for _ in range(random.randint(8, 17)))

print(paswd)
